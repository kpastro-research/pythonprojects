# Using _swimclub_ library
import sys
from fileinput import filename

import swimclub #
defaultFileName = "KrishnaMurali-13-100m-Fly.txt"
print (swimclub.process_swim_data_file(defaultFileName))
