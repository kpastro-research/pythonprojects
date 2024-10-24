# ------------------------------------------------------------
# module: swimclub_dict
# contains functions to process suimmer data
# Version:3.0
# ------------------------------------------------------------
import os
import pprint
import statistics
import hfpy_utils
# ------------------------------------------------------------
# function: process_time
# extract min, second and centisecond from given time
# ------------------------------------------------------------
def process_time(value):
    if ":" in value:
        min, second_centi = value.split(":")
        if "." in second_centi:
            second, centi = second_centi.split(".")
        else:
            second = second_centi
            centi = "0"
    else:
        min = 0
        if "." in value:
            second, centi = value.split(".")
        else:
            second = value
            centi = "0"
    return min, second, centi
# ------------------------------------------------------------
# function: convertcentisecond_dict
# converts centiseconds to  min, second and centisecond
# ------------------------------------------------------------
def convertcentisecond_dict(centiseconds_param):
    minutes_seconds , centiseconds = str(round(centiseconds_param / 100,2)).split('.') # divide by 100 , numbers before decimals are records and after decimal are centiseconds
    minutes = int(int(minutes_seconds) / 60) # assuming centisecond could be more then 60 , here we convert to a minutes
    seconds = int(minutes_seconds) - minutes * 60
    return str(minutes) + ":" + str(seconds) + "." + str(centiseconds) # return average

# ------------------------------------------------------------
# function: process_swim_data_dict
# process all swim-times seperated by ,
# ------------------------------------------------------------
def process_swim_data_dict(swimmingData):
    centisecondsecondList = list()
    swimmerTimings = {}
    linevalues = swimmingData.strip().split(',')
    for value in linevalues:
        min, second, centiseconds = process_time(value) # process time and get min, seconds and centi seconds

        total_centisecond = int(min) * 60 * 100 + int(second) * 100 + int(centiseconds)
        centisecondsecondList.append(total_centisecond)
        swimmerTimings.update({value: total_centisecond})
    return swimmerTimings
# ------------------------------------------------------------
# function: get_file_name_only
# extract filename with extension is file-name is prefixed with absolute path
# ------------------------------------------------------------
def get_file_name_only(filename):
    return os.path.basename(filename)   # exclude the path and get file name only

# ------------------------------------------------------------
# function: get_data_from_file_name_dict
# extracts swimmer data from file-name
# ------------------------------------------------------------
def get_data_from_file_name_dict(filename):
    swimmerData = {}
    filename_without_extension, file_extension = get_file_name_only(filename).split('.')    # split file-name and extensiob
    swimmerName, underAgeGroup, swimDistanceInMeters, swimStroke = filename_without_extension.split('-')    # split file name and get data from file-name
    swimmerData.update({"name":swimmerName})
    swimmerData.update({"agegroup":  underAgeGroup})
    swimmerData.update({"distance": swimDistanceInMeters})
    swimmerData.update({"stroke": swimStroke})
    return swimmerData

# ------------------------------------------------------------
# function: get_data_from_file_name_dict
# process swimmer data in file-name and also processes content of file
# ------------------------------------------------------------
def process_swim_data_file_dict(filename):
    swimmerData = get_data_from_file_name_dict(filename)

    with  open(filename, 'r') as file:
        for swimmingData in file.readlines():
            swimmerData.update({"timings":process_swim_data_dict(swimmingData)})

    return swimmerData

# ------------------------------------------------------------
# function: average_dict
# - calculates average of centisecond
# - converts average centsecond to min:second.second format
# ------------------------------------------------------------
def average_dict(timing_data):
    averagedata = {}
    avgcentiseconds = int(statistics.mean(timing_data.values()))
    min_sec_centiseconds = convertcentisecond_dict(avgcentiseconds)
    averagedata.update({min_sec_centiseconds:avgcentiseconds})
    return averagedata

# ------------------------------------------------------------
# function: get_range_from_timing
# - calculates range value from based on set of centiseconds
# - parameters
#       timing_data - dict of timing dict ({min:sec.centisecond: centiseconds})
#       t_min - minimum range values default 0
#       t_max -  maximum range values default 0
#       log - boolean if print statement to be executed
#  return time_range dict  ({min:sec.centisecond: range value })
# ------------------------------------------------------------
def get_range_from_timing(timing_data, t_min, t_max, log):
    time_range ={}
    for timing in timing_data:

        value = timing_data.get(timing)
        range = int(hfpy_utils.convert2range(value, 0, max(timing_data.values()),t_min,t_max))
        time_range.update({timing:range})
        if log:
            print (timing, "->", timing_data.get(timing), "->" , range)

    return time_range

# ------------------------------------------------------------
# function: get_swim_data_dict
# - iterators over all files and generates a dictionary
# - converts average centsecond to min:second.second format
# ------------------------------------------------------------
def get_swim_data_dict(swimDataFolder, t_min, t_max, log):

    # all_swimclub_data = {'':{}}
    all_swimclub_data={}
    line_length=80
    if log:
        print("-" * line_length)
    folder_contents = os.listdir(swimDataFolder)    # list contents of ../swimdata  folder
    for filename in folder_contents:
        file_with_path = os.path.join(swimDataFolder, filename) # combine folder name and filename to get absolute path file_with_path
        if log:
            print("Processing file:"+file_with_path  )
            print("-" * line_length )

        swimclub_data = process_swim_data_file_dict(file_with_path)
        timing_data = swimclub_data.get("timings")
        swimclub_data.update({"average": average_dict(timing_data)})
        swimclub_data.update({"timings_range": get_range_from_timing(timing_data, t_min, t_max, log)})
        if log:
            pprint.pprint(swimclub_data )
            print("-" * line_length  )
        all_swimclub_data.update({filename: swimclub_data})

    return all_swimclub_data
# ------------------------------------------------------------
# function: get_simple_text_graph_data
# - Demonstrate
#   - processing dictionary
#   - use of f-string
#   - get first element from dictionary
# ------------------------------------------------------------
def get_simple_text_graph_data(swimmer_data_node):

    border_line = "-" * 60
    user_data = (f"{border_line}"
                 f"\nName:{swimmer_data_node.get('name')}"
                 f"\nAge Group:{swimmer_data_node.get('agegroup')}"
                 f"\nDistance:{swimmer_data_node.get('distance')}"
                 f"\nStroke:{swimmer_data_node.get('stroke')}"
                 f"\n{border_line}")
    timings_data_range = swimmer_data_node.get('timings_range')
    user_graph_data = f""
    counter = len(timings_data_range)
    max_range = 440

    for timing in timings_data_range:
        range = timings_data_range.get(timing)
        user_graph_data = user_graph_data + f"\n{counter} |{'*' * int(range / 10)} {' ' * int(((max_range) - range) / 10)}{timing}"
        counter = counter - 1


    user_graph_data = user_graph_data + (f"\n{border_line}"
                                         f"\nAverage time: {next(iter(swimmer_data_node.get("average")))}"
                                         f"\n{border_line}")
    return user_data , user_graph_data