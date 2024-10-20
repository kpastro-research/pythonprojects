fileName =  "KrishnaMurali-13-100m-Fly.csv"
upperFileName = fileName.upper() # convert file name to upper case KRISHNAMURALI-13-100M-FLY.CSV
print(upperFileName)

lowerFileName = fileName.lower() # convert file name to lower case krishnamurali-13-100m-fly.csv
print(lowerFileName)

fileName.split()    # returns List containing file name ['KrishnaMurali-13-100m-Fly.csv']
print(fileName.split())

fileName.split("-")  # returns List containing  ['KrishnaMurali','13','100m','Fly.csv']
print(fileName.split("-"))

fileName.split("13")  # returns List split by 13  ['KrishnaMurali-','-100m-Fly.csv']
print(fileName.split("13"))

fileName.split("-1")  # returns List split by -1  ['KrishnaMurali','3','00m-Fly.csv']
print(fileName.split("-1"))

fileName.split(".")  # returns List split by .  ['KrishnaMurali-13-100m-Fly','csv']
print(fileName.split("."))

fileName.split("-.")  # returns List split by . ['KrishnaMurali-13-100m-Fly.csv']
print(fileName.split("-."))

print(fileName.split("-").split(".")) # error  AttributeError: 'list' object has no attribute 'split'

print(fileName.split("-").pop(0).split(".")) # error  AttributeError: 'list' object has no attribute 'split'

# ~~~~~~~~~~~~~~~~~~
# LESSONS LEARNT
# ~~~~~~~~~~~~~~~~~~
# split functions
#  if error occurs in middle of script subsequent statement are not executed