

import swimclub_dict
from pprint import pprint

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


swimmer_data=all_data.get("Darius-13-100m-Breast.txt")
timings_data = swimmer_data.get('timings')
# ordered_timings_data = collections.OrderedDict(timings_data)
pprint(timings_data)
timings_data_min_sec_centi = timings_data.keys()
timings_data_centiseconds = list(timings_data.values())

# print("List:",timings_data_centiseconds)
# print("Sort:",sorted(timings_data_centiseconds))
# pprint(sorted(timings_data))
# ordered_centiseconds=timings_data_centiseconds.sort()
# # timings_data_ordered_centiseconds=timings_data_centiseconds.sort()
# print("timings_data_ordered_centiseconds",ordered_centiseconds)
# print("timings_data_centiseconds:",timings_data_centiseconds)
timings_data_range = swimclub_dict.get_range_from_timing(timings_data, 0, 400, False)
# pprint(timings_data_range)
timings_data_range = swimmer_data.get('timings_range')
border_line = "-" * 60
user_data=(f"{border_line}"
           f"\nName:{swimmer_data.get('name')}"
           f"\nAge Group:{swimmer_data.get('agegroup')}"
           f"\nDistance:{swimmer_data.get('distance')}"
           f"\nStroke:{swimmer_data.get('stroke')}"
           f"\n{border_line}")

user_graph_data=f""
counter = len(timings_data_range)
max_range = 440
for timing in timings_data_range:
    key = timing
    range = timings_data_range.get(timing)
    user_graph_data = user_graph_data + f"\n{counter} |{'~' * int(range/10)} {' ' * int(((max_range) - range)/10)}{timing}"
    counter = counter - 1
# avg_time_list = swimmer_data.get('average').keys()
# avg_time_list.mapping.get()
# print(avg_time_list)

user_graph_data = user_graph_data +  (f"\n{border_line}"
                                      f"\nAverage time: {swimmer_data.get('average').keys()}"
                                      f"\n{border_line}")

print(user_data)
print(user_graph_data)
                                      
           
           
                                      






