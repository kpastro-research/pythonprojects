# ------------------------------------------------------------
# Example code:  Reads each file in swimdata folder,
#               extract data from file-name
#               processes file contents
#               prints swimmer details and text graph
#  Modules used:
#   swimclub_dict   - custom module to process swimmers data
# ------------------------------------------------------------


import swimclub_dict #

swimDataFolder="../swimdata"
line_length=80
#
all_swimclub_data=swimclub_dict.get_swim_data_dict(swimDataFolder, 0,400,False)
for swimmer in all_swimclub_data:
    swimmer_data_node = all_swimclub_data.get(swimmer)
    user_data, user_graph_data =swimclub_dict.get_simple_text_graph_data(swimmer_data_node)
    print(user_data)
    print(user_graph_data)