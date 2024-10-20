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
from pprint import pprint
# Task 1 Extract Data from File Name
fileName =  "KrishnaMurali-13-100m-Fly.csv"            # as aas argument to sys.argv[1]
fileNameAttributeList = fileName.split('-')
swimmerName = fileNameAttributeList[0] # Swimmers Name
underAgeGroup = fileNameAttributeList[1] # Age Group
swimDistanceInMeters = fileNameAttributeList[2]
swimStroke = fileNameAttributeList[3].split('.').pop(0)
swmimmerDataMethod1 = (fileName, swimmerName, underAgeGroup, swimDistanceInMeters,swimStroke)
# pprint(dir(fileName))
print("----- Method-1:Swimmer data from file name ---------")
print("fileName:", fileName)
print("swimmerName:", swimmerName)
print("underAgeGroup:", underAgeGroup)
print("swimDistanceInMeters:", swimDistanceInMeters)
print("swimStroke:", swimStroke)

fileNameAttributeList = fileName.split('.').pop(0).split('-')
swimmerName = fileNameAttributeList[0] # Swimmers Name
underAgeGroup = fileNameAttributeList[1] # Age Group
swimDistanceInMeters = fileNameAttributeList[2]
swimStroke = fileNameAttributeList[3]
swmimmerDataMethod2 = (fileName, swimmerName, underAgeGroup, swimDistanceInMeters,swimStroke)
# pprint(dir(fileName))
print("----- Method-2:Swimmer data from file name ---------")
print("fileName:", fileName)
print("swimmerName:", swimmerName)
print("underAgeGroup:", underAgeGroup)
print("swimDistanceInMeters:", swimDistanceInMeters)
print("swimStroke:", swimStroke)
print("----- Swimmer data ---------")
print("swmimmerDataMethod1 == swmimmerDataMethod2:", swmimmerDataMethod1 == swmimmerDataMethod2)
fileNameAttributeList = fileName.removesuffix(".csv").split('-')
swimmerName = fileNameAttributeList[0] # Swimmers Name
underAgeGroup = fileNameAttributeList[1] # Age Group
swimDistanceInMeters = fileNameAttributeList[2]
swimStroke = fileNameAttributeList[3]
swmimmerDataMethod3 = (fileName, swimmerName, underAgeGroup, swimDistanceInMeters,swimStroke)
print("----- Method-3:Swimmer data from file name ---------")
print("fileName:", fileName)
print("swimmerName:", swimmerName)
print("underAgeGroup:", underAgeGroup)
print("swimDistanceInMeters:", swimDistanceInMeters)
print("swimStroke:", swimStroke)
print("----- Swimmer data ---------")
print("swmimmerDataMethod2 == swmimmerDataMethod3:", swmimmerDataMethod2 == swmimmerDataMethod3)

# Task 2 Extract Data from File Name

lineInFile= "1:27.95,1:21.07,1:30.96,1:23.22,1:27.95,1:28.30"        #open(fileName,'r') function to open file
valuesInLine = lineInFile.split(',')
swimmerTimings = list()
for values in valuesInLine:

    min_second_milli = values.split(':')
    min = min_second_milli[0]

    second_milli = min_second_milli[1].split('.')
    second = second_milli[0]

    milli = second_milli[1].split('.').pop(0)
    swimmerTimings.append((min,second, milli))

print(swimmerTimings)





# ~~~~~~~~~~~~~~~~~~
# LESSONS LEARNT
# ~~~~~~~~~~~~~~~~~~
# Everything is object in python
