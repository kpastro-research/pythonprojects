# Using swimclub_dict library
# dict is used as
import sys
from fileinput import filename

import swimclub_dict #
defaultFileName = "KrishnaMurali-13-100m-Fly.txt"
swimclub_data = swimclub_dict.process_swim_data_file(defaultFileName)

timing_data = swimclub_data.get("timings")
swimclub_data.update({"average":swimclub_dict.average(timing_data)})

print (swimclub_data)
