# ------------------------------------------------------------
# Example code:  Reads each file in swimdata folder,
#               extract data from file-name
#               processes file contents
#  Modules used:
#   os              - OS related to BIF e.g file processing
#   pprint          - print dict in pretty format
#   swimclub_dict   - custom module to process swimmers data
# ------------------------------------------------------------

import os
import pprint

import swimclub_dict #

swimDataFolder="../swimdata"
line_length=80
#

def process_swimm_data():
    print("-" * line_length)
    folder_contents = os.listdir(swimDataFolder)    # list contents of ../swimdata  folder
    for filename in folder_contents:
        file_with_path = os.path.join(swimDataFolder, filename) # combine folder name and filename to get absolute path file_with_path
        print("Processing file:",file_with_path)
        print("-" * line_length)

        swimclub_data = swimclub_dict.process_swim_data_file_dict(file_with_path)
        timing_data = swimclub_data.get("timings")
        swimclub_data.update({"average": swimclub_dict.average_dict(timing_data)})
        pprint.pprint(swimclub_data)
        print("-" * line_length)


process_swimm_data()
