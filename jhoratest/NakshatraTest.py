import datetime
from jhora.panchanga import drik
from jhora import utils, const
from collections import namedtuple as struct
import swisseph as swe

# requires
# pip install geopy
# pip install pytz
# pip install geocoder
# pip install timezonefinder
# pip install pandas
PANCHANGA_DICT = {
    "nakshatras": {"1": "Aśvinī",
                   "2": "Bharaṇī",
                   "3": "Kṛttikā",
                   "4": "Rohiṇī",
                   "5": "Mṛgaśīrā",
                   "6": "Ārdrā",
                   "7": "Punarvasū",
                   "8": "Puṣya",
                   "9": "Āśleṣā",
                   "10": "Maghā",
                   "11": "Pūrvaphalgunī",
                   "12": "Uttaraphalgunī",
                   "13": "Hasta",
                   "14": "Cittā",
                   "15": "Svāti",
                   "16": "Viśākhā",
                   "17": "Anūrādhā",
                   "18": "Jyeṣṭhā",
                   "19": "Mūlā",
                   "20": "Pūrvāṣāḍhā",
                   "21": "Uttarāṣāḍhā",
                   "22": "Śravaṇā",
                   "23": "Dhaniṣṭhā",
                   "24": "Śatabhiṣā",
                   "25": "Pūrvābhādrā",
                   "26": "Uttarābhādrā",
                   "27": "Revatī"
                   }
}
Date = struct('Date', ['year', 'month', 'day'])
Place = struct('Location', ['latitude', 'longitude', 'timezone'])
DEFAULT_AYANAMSA_MODE = "TRUE_PUSHYA"
AVAILABLE_AYANAMSA_MODES = const.available_ayanamsa_modes
DEFAULT_LOCATION=['East Brunswick, United States', 40.42788, -74.41598, -5.0]

def get_current_time():
  now = datetime.datetime.now()
  return now.timetuple()

def get_defaults(date, place , selectedAyanamsha ):

  tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec = (2024, 11, 15, 20,13,37)
  date = Date(tm_year, tm_mon, tm_mday)
  time = str(tm_hour)+":"+str(tm_min) + "." + str(tm_sec)
  time_float = float(str(tm_hour) + "." + str(tm_min) )
  geoLocation, latitude, longitude, timeZone = DEFAULT_LOCATION

  place = drik.Place(geoLocation, latitude, longitude, timeZone)
  ayanmmsa_mode = AVAILABLE_AYANAMSA_MODES[DEFAULT_AYANAMSA_MODE]

  # Setting default , this value needs to come as input

  return date, time, time_float, place ,  ayanmmsa_mode

def get_nakshatra_data(jd, place):
    nakshatra_data = {}
    _nakshatra_data = drik.nakshatra(jd, place)
    [nakshatra_num, nakshatra_starting_time, nakshatra_ending_time, nakshatra_fraction_left,
                 *next_nakshatra] = _nakshatra_data
    nakshatra_data.update({"id": nakshatra_num})
    nakshatra_data.update({"name": PANCHANGA_DICT["nakshatras"][str(nakshatra_num)]})
    nakshatra_data.update({"start_time": utils.to_dms(nakshatra_starting_time)})
    nakshatra_data.update({"end_time": utils.to_dms(nakshatra_ending_time)})
    nakshatra_data.update({"time_left": nakshatra_fraction_left})
    return nakshatra_data

# Get defaults
date, time, time_float , place,  ayanmmsa_mode = get_defaults(None, None, None)
# get jd value
print("Date:",date)
print("Time:",time)
print("Place:",place)

jd = swe.julday(date[0], date[1], date[2], time_float)

print(get_nakshatra_data(jd, place))
