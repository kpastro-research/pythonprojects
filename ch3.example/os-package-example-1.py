import os
from fileinput import filename

import swimclub_dict
curdir = os.curdir
listdir = os.listdir(curdir)

print("os.curdir:",curdir) # print current directory
print("listdir:",listdir) # content of current directory

print("Current working Directory:",os.getcwd())
listdir = os.listdir("../swimdata")
filenameWithPath = "../swimdata/KrishnaMurali-13-100m-Fly.txt"


print("listdir:",listdir)

dirname  = os.path.dirname(filenameWithPath)
print("dirname:",dirname)
basename = os.path.basename(filenameWithPath)
print("basename:",basename)
filenameWithoutPath = "KrishnaMurali-13-100m-Fly.txt"

dirname  = os.path.dirname(filenameWithoutPath)
print("dirname:",dirname)
basename = os.path.basename(filenameWithoutPath)
print("basename:",basename)

# if os.path.dirname(filename) != '':
#     filename_only = os.path.basename(filename)

39.07,37.66,36.13,39.42