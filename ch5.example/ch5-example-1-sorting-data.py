# Example code to read and process json files
import json


# Open the JSON file
with open('../jsondata/all_swim_club_data.json', 'r') as jd:
    json_data = json.load(jd)

print(sorted(json_data))



# JSON