#Created by: Jonathan Navarro 
#GPS_user_interface
from GPS_inputs import *
from GPS_outputs import *
"""
Implements the GPS system user interface in which ones specifies 
the number of locations first,then the locations themselves, 
then specifies the number of outputs, then the outputs themselves whether
they are steps (for directions), totaldistance (for total distance), 
total time (for total time), and LatLong (for Latitude and Longitude).  
"""


def GPS_system():
    '''
Runs the GPS system 
    '''
    print("Welcome to the MapQuest API!")
    input = GPS_inputs()
    input.number_of_locations()
    input.locations_parameters()
    input.gps_url()
    input.request_response()
   
    output = GPS_outputs()
    output.output_parameters()
    output.final_results(input.response)

    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')


if __name__ == '__main__':
    GPS_system()
    
