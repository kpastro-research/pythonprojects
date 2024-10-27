# ------------------------------------------------------------
# Example code:  Reads each file in swimdata folder,
#               extract data from file-name
#               processes file contents
#               generate html from swimmer_data and save to charts folders
#               Reads charts folder and generates index all links all html files in
#
#  Modules used:
#   swimclub_dict   - custom module to process swimmers data
# ------------------------------------------------------------
from pprint import pprint
import os
import webbrowser
import swimclub_dict #

SWIM_DATA_FOLDER="../swimdata"
CHARTS_FOLDER= "../charts/"
CHARTS_FOLDER_PATH=os.path.realpath(CHARTS_FOLDER)
line_length=80
log = False
#
all_swimclub_data=swimclub_dict.get_swim_data_dict(SWIM_DATA_FOLDER, 0,400,SWIM_DATA_FOLDER)
for swimmer in all_swimclub_data:
    if log:
        print(swimmer)
    swimmer_data_node = all_swimclub_data.get(swimmer)
    all_swimmer_data = {swimmer:swimmer_data_node}
    if log:
        pprint(all_swimmer_data)
    # Generate html with swimmer data and graph
    swimclub_dict.gen_html_page(all_swimmer_data, swimmer, CHARTS_FOLDER)

# Create index html and open in browser
# link all html into index

folder_contents = os.listdir(CHARTS_FOLDER)    # list contents of ../swimdata  folder
index_html="index-sorted.html"
html_header = (f"<!DOCTYPE html>"
               f"<html lang='en'>"
               f" <head>"
               f"      <meta charset='UTF-8'>"
               f"      <title>Example Swim Club Report </title>"
               f"</head>")
html_body = (f"<body>"
             f"<table border='1'>"
             f"   <tr>"
             f"       <td colspan=2>Ordered alphabetically Swimmer Report Index </td>"
             f"   </tr>")
html_body_content = ""
for counter, filename in enumerate(sorted(folder_contents)):
    file_with_path = os.path.join(CHARTS_FOLDER, filename) # combine folder name and filename to get absolute path file_with_path
    if log:
        print("Processing file:"+file_with_path  )
        print("-" * line_length )

    filename_only = swimclub_dict.get_file_name_only(filename)
    swimmer_data = swimclub_dict.get_data_from_file_name_dict(filename)
    html_body_content = (html_body_content
                         + ( f"   <tr>"
                             f"       <td align='middle'>{counter}</td>"
                             f"       <td><a href='{CHARTS_FOLDER_PATH+"/"+filename_only}' target='_blank'>{swimmer_data.get('name')} Under age {swimmer_data.get('agegroup')} {swimmer_data.get('distance')} {swimmer_data.get('stroke')}</a></td>"
                             f"   </tr>"))
# for loop
html_footer = ( f"</table>"
                f"</body>"
                f"</html>")
final_html_page = html_header + html_body + html_body_content + html_footer
# write to html file
with open("../"+index_html, "w") as sf:
    print(final_html_page, file=sf)

# open file in browser
webbrowser.open("file://"+os.path.realpath("../"+index_html))

