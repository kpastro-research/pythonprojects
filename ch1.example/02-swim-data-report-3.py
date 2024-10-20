#  Very basic method of data processing , not making much use of
# Data Saved in File
#1. FileName Format ( Name-under_age_group-swim_distance_meters-stroke.csv)
    # Example: KrishnaMurali-13-100m-Fly.csv
    #   Read FileName
    #   Split file name seperated by -
    #   store data in variable
        #   SwimmerName,
        #   underAgeGroup,
        #   swimDistanceInMeters,
        #   swimStroke
#2. Recorded Time Format: hrs:min:sec.milliseconds
        # Read line
        # Split line seperated by ,
        # Split each value seperated by ,  int
        #  hrs:min:sec.milliseconds
     # Calculate average sum(values)/number of values
import sys
import statistics
# Task 1 Extract Data from File Name
fileName =  "KrishnaMurali-13-100m-Fly.txt"            # as aas argument to sys.argv[1]
swimmerName, underAgeGroup, swimDistanceInMeters,swimStroke =  fileName.removesuffix(".csv").split('-')
print("----- Method-1- Unpack :Swimmer data from file name ---------")
print("fileName:", fileName)
print("swimmerName:", swimmerName)
print("underAgeGroup:", underAgeGroup)
print("swimDistanceInMeters:", swimDistanceInMeters)
print("swimStroke:", swimStroke)

# Task 2 Extract Data from File Name
fileName =  "KrishnaMurali-13-100m-Fly.txt"
swimmerTimings = list()
millisecondList = list()
with  open(fileName, 'r') as file:
    for line in file.readlines():
        linevalues = line.strip().split(',')
        for value in linevalues:
            min_second_milli = value.strip().split(':')
            min = min_second_milli[0]

            second_milli = min_second_milli[1].split('.')
            second = second_milli[0]

            milli = second_milli[1].split('.').pop(0)

            total_millis = int(min) * 60 * 100 + int(second) * 100 + int(milli)
            millisecondList.append(total_millis)
            swimmerTimings.append((value, "=>", total_millis))

print(swimmerTimings)
print("Mean millisecondList",statistics.mean(millisecondList))

# ~~~~~~~~~~~~~~~~~~
# LESSONS LEARNT
# ~~~~~~~~~~~~~~~~~~
# Everything is object in python
# list can be unpacked into multiple variables
# Default values in list are string
#  mean ~= function in statistics package to calculate average


