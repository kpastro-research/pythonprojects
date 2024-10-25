#------------------------------------------------------------
# Example: Includes following
#   - processing  dictionary object
#   - get element from dictionary  by key
#   - get First element from list of values 2 methods
#   - use of len BIF
#   - use of f-strings to generate html
#   - use of enumeration BIF  in loop
#   - saving html to file
#------------------------------------------------------------


CHARTS="../charts/"
all_data= {"Darius-13-100m-Breast.txt": {'agegroup': '13',
                                         'average': {'1:31.89': 9189},
                                         'distance': '100m',
                                         'name': 'Darius',
                                         'stroke': 'Breast',
                                         'timings': {'1:30.24': 9024,
                                                     '1:30.81': 9081,
                                                     '1:31.53': 9153,
                                                     '1:31.74': 9174,
                                                     '1:32.73': 9273,
                                                     '1:33.05': 9305,
                                                     '1:33.18': 9318},
                                         'timings_range': {'1:30.24': 387,
                                                           '1:30.81': 389,
                                                           '1:31.53': 392,
                                                           '1:31.74': 393,
                                                           '1:32.73': 398,
                                                           '1:33.05': 399,
                                                           '1:33.18': 400}}}

fname="Darius-13-100m-Breast.txt"
fname_ext_excluded=fname.split('.')[0]
html_header=(f"<!DOCTYPE html>"
            f"<html lang='en'>"
            f" <head>"
            f"      <meta charset='UTF-8'>"
            f"      <title>{fname_ext_excluded}</title>"
            f"</head>")

swimmer_data = all_data.get(fname)
timings_data_range = swimmer_data.get('timings_range')
html_body=(f"<body>"
           f"<table border='1'>"
           f"   <tr>"
           f"       <td colspan=2>{fname_ext_excluded}</td>"
           f"   </tr>"
           f"   <tr>"
           f"       <td>Name:</td>"
           f"       <td>{swimmer_data.get('name')}</td>"
           f"   </tr>"
           f"   <tr>"
           f"       <td>Age Group:</td>"
           f"       <td>Under {swimmer_data.get('agegroup')}</td>"
           f"   </tr>"
           f"   <tr>"
           f"       <td>Distance:</td>"
           f"       <td>{swimmer_data.get('distance')}</td>"
           f"   </tr>"
           f"   <tr>"
           f"       <td>Stroke:</td>"
           f"       <td>{swimmer_data.get('stroke')}</td>"
           f"   </tr>")


svg_chart=(f"   <tr>"
           f"       <td colspan=2 align='middle'>{fname_ext_excluded}</td>"
           f"   </tr>")
timings_data_range_length = len(timings_data_range)
for counter, timing in enumerate(timings_data_range):
    range = timings_data_range.get(timing)
    if counter%2 == 0:
        rgb="75,150,250"
    else:
        rgb="250,150,75"

    svg_chart = svg_chart + (f"   <tr>"
    f"       <td align='right'>{timings_data_range_length - counter}</td>"
    f"       <td>"
    f"             <svg height='15' width='400'>"
    f"                 <rect height='15' width='{range}' style='fill:rgb({rgb})'/>"
    f"             </svg>{'&nbsp;' *5} {timing}"
    f"         </td>"         
    f"   </tr>")

svg_chart = svg_chart + (
    f"   <tr>"
    f"       <td align='right'>Average:</td>"
    f"       <td>{next(iter(swimmer_data.get("average")))}</td>"
    f"   </tr>"
    f"</table>"
    f"</body>"
    f"</html>")
final_html_page = html_header + html_body +svg_chart

with open(CHARTS+fname_ext_excluded+".html", "w") as sf:
    print(final_html_page, file=sf)
                                      
           
           
                                      






