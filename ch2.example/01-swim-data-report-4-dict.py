# Using swimclub_dict library
# dict is used as

import swimclub_dict #
defaultFileName = "KrishnaMurali-13-100m-Fly.txt"
swimclub_data = swimclub_dict.process_swim_data_file_dict(defaultFileName)

timing_data = swimclub_data.get("timings")
swimclub_data.update({"average": swimclub_dict.average_dict(timing_data)})

print (swimclub_data)
