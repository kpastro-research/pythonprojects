

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

# Example 1:  get an element by key
swimmer_data = all_data.get("Darius-13-100m-Breast.txt")
print("swimmer_data:",swimmer_data)
#  get 1st element from swimmer_data > average attribute dict
print("First Element-1:", list(swimmer_data.get("average"))[0])
print("First Element-2:", next(iter(swimmer_data.get("average"))))

# Example 2:  get an element by key
timings_data = swimmer_data.get('timings')
# ordered_timings_data = collections.OrderedDict(timings_data)
pprint(timings_data)
timings_data_min_sec_centi = timings_data.keys()
timings_data_centiseconds = list(timings_data.values())
print("List:",timings_data_centiseconds)

# Example 3: use of sorting
print("Sort:",sorted(timings_data_centiseconds))

timings_data_range = swimclub_dict.get_range_from_timing(timings_data, 0, 400, False)
# pprint(timings_data_range)
timings_data_range = swimmer_data.get('timings_range')
# Example 4: character multiplier
border_line = "-" * 60
# Example 5: use of f-string
user_data = (f"{border_line}"
             f"\nName:{swimmer_data.get('name')}"
             f"\nAge Group:{swimmer_data.get('agegroup')}"
             f"\nDistance:{swimmer_data.get('distance')}"
             f"\nStroke:{swimmer_data.get('stroke')}"
             f"\n{border_line}")
user_graph_data = f""
# Example 6: use of len function with dictionary
counter = len(timings_data_range)
max_range = 440
# Example 7: iterating dictionary with for loop
for timing in timings_data_range:
    key = timing
    range = timings_data_range.get(timing)
    # Example 8: aggregating text graph
    user_graph_data = user_graph_data + f"\n{counter} |{'~' * int(range / 10)} {' ' * int(((max_range) - range) / 10)}{timing}"
    counter = counter - 1


user_graph_data = user_graph_data + (f"\n{border_line}"
                                     f"\nAverage time: {next(iter(swimmer_data.get("average")))}"
                                     f"\n{border_line}")


print(user_data, user_graph_data)

                                      
           
           
                                      






