# ------------------------------------------------------------
# Example code:  Reads each file in swimdata folder,
#               extract data from file-name
#               processes file contents
#  Modules used:
#   os              - OS related to BIF e.g file processing
#   pprint          - print dict in pretty format
#   swimclub_dict   - custom module to process swimmers data
# ------------------------------------------------------------
from pprint import pprint

import swimclub_dict #

swimDataFolder="../swimdata"
line_length=80
#
all_swimclub_data=swimclub_dict.get_swim_data_dict(swimDataFolder, 0,400,False)
pprint(all_swimclub_data.get("Darius-13-100m-Breast.txt"))
