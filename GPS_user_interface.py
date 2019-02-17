#Jonathan Navarro 83144130
#GPS_user_interface
import urllib.parse
import urllib.request
import json
from GPS_functions import *
from GPS_outputs import *
"""
Implements the GPS system user interface in which ones specifies the number of locations first,
then the locations themselves, then specifies the number of outputs, then the outputs themselves whether
they are steps (for directions), totaldistance (for total distance), total time (for total time), and
LatLong (for Latitude and Longitude).  
"""


def GPS_system():
    '''
Runs the GPS system 
    '''
    ingredients = request_response(gps_url(tuples_param(locations_param(num_locations()))))
    final_results(output_param(), ingredients)
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')


if __name__ == '__main__':
    GPS_system()
    
