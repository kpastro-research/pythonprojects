# ------------------------------------------------------------
# module: swimclub_dict
# contains functions to process suimmer data
# ------------------------------------------------------------
import os
import statistics
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
    avgcentiseconds = statistics.mean(timing_data.values())
    min_sec_centiseconds = convertcentisecond_dict(avgcentiseconds)
    averagedata.update({min_sec_centiseconds:avgcentiseconds})
    return averagedata

