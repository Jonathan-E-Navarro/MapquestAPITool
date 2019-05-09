#Created by: Jonathan Navarro
#GPS_functions

import urllib.parse
import urllib.request
from itertools import*
import json 


class GPS_inputs(object):
    """docstring for GPS_inputs"""
    def __init__(self):
        self.base_URL = 'http://open.mapquestapi.com/directions/v2/route?'
        self.app_key = urllib.parse.unquote('Fmjtd%7Cluu82161l9%2Cb5%3Do5-942au6', encoding='utf-8')
        self.location_count = None
        self.locations = None
        self.url = None
        self.response = None

    def number_of_locations(self)-> int:
        '''
        Creates the amount of locations
        '''
        location_list = []
        location_counter = 0 
        while True:
            try:
                number_of_locations = int(input("Enter the number of Locations: "))
                if isinstance(number_of_locations, int)== True:
                    location_counter = number_of_locations
                    self.location_count = number_of_locations
                    return 
                else:
                    print('Error not an integer')
            except ValueError:
                print('Error not an integer')


    def locations_parameters(self) -> str:
        '''
        Creates the search location URL
        '''
        locations = []
        for i in range(self.location_count):
            location = input("Enter Location: ") 
            locations.append(location)
                
        new_locations = []
        new_locations.append(('from',locations[0]))
        
        for location in locations[1:]:
            new_locations.append(('to',location))

        self.locations = new_locations
        return 


    def gps_url(self)-> str:
        '''
        creates directions search URL
        '''
        gps_param = [('key', self.app_key),('ambiguities','ignore')]
        gps_param+=self.locations
        self.url = self.base_URL + urllib.parse.urlencode(gps_param)
        return 


    def request_response(self):
        '''
        opens the URl and returns a loaded json response
        '''
        try:
            request = urllib.request.urlopen(self.url)
            json_response = request.read().decode(encoding = 'utf-8')
            self.response = json.loads(json_response)
            return 

        finally:
            if request != None:
                request.close()
        
    


    




        
    
    


    
