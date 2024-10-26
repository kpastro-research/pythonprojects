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
import swimclub_dict

CHARTS="../charts/"
all_swimmer_data= {"Darius-13-100m-Breast.txt": {'agegroup': '13',
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

swimmer="Darius-13-100m-Breast.txt"
swimclub_dict.gen_html_page(all_swimmer_data, swimmer, CHARTS)


                                      
           
           
                                      






