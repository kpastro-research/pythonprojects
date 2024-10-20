import statistics
# module swimclub
#100th of second is centisecond 
def convertcentisecond(centiseconds_param):
    minutes_seconds , centiseconds = str(round(centiseconds_param / 100,2)).split('.') # divide by 100 , numbers before decimals are records and after decimal are centiseconds
    minutes = int(int(minutes_seconds) / 60) # assuming centisecond could be more then 60 , here we convert to a minutes
    seconds = int(minutes_seconds) - minutes * 60
    return str(minutes) + ":" + str(seconds) + "." + str(centiseconds) # return average




def process_swim_data(swimmingData):
    centisecondsecondList = list()
    swimmerTimings = {}
    linevalues = swimmingData.strip().split(',')
    for value in linevalues:
        min_second_centisecond = value.strip().split(':')
        min = min_second_centisecond[0]

        second_centi = min_second_centisecond[1].split('.')
        second = second_centi[0]

        centisecond = second_centi[1].split('.').pop(0)

        total_centisecond = int(min) * 60 * 100 + int(second) * 100 + int(centisecond)
        centisecondsecondList.append(total_centisecond)
        swimmerTimings.update({value: total_centisecond})

    # get Ave
    # averagecentisecond = statistics.mean(centisecondsecondList)
    # min_sec_centisecond = convertcentisecond(averagecentisecond)
    # swimmerTimings.append((min_sec_centisecond, "=>", averagecentisecond))
    return swimmerTimings


def get_data_from_file_name(filename):
    swimmerData = {}
    filename_without_extension, file_extension = filename.split('.')
    swimmerName, underAgeGroup, swimDistanceInMeters, swimStroke = filename_without_extension.split('-')
    swimmerData.update({"name":swimmerName})
    swimmerData.update({"agegroup":  underAgeGroup})
    swimmerData.update({"distance": swimDistanceInMeters})
    swimmerData.update({"stroke": swimStroke})
    return swimmerData


def process_swim_data_file(filename):
    swimmerData = get_data_from_file_name(filename)

    with  open(filename, 'r') as file:
        for swimmingData in file.readlines():
            swimmerData.update({"timings":process_swim_data(swimmingData)})

    return swimmerData


def average(timing_data):
    averagedata = {}
    avgcentiseconds = statistics.mean(timing_data.values())
    min_sec_centiseconds = convertcentisecond(avgcentiseconds)
    averagedata.update({min_sec_centiseconds:avgcentiseconds})
    return averagedata

