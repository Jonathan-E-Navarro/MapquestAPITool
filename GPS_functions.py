#Jonathan Navarro 83144130
#GPS_functions

import urllib.parse
import urllib.request
from itertools import*
import json 

base_URL = 'http://open.mapquestapi.com/directions/v2/route?'
app_key = urllib.parse.unquote('Fmjtd%7Cluu82161l9%2Cb5%3Do5-942au6', encoding='utf-8')

##def pairwise(iterable):
##    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
##    a, b = tee(iterable)
##    next(b, None)
##    return list(zip(a, b))


def num_locations()-> list:
    '''
    Creates the amount of locations
    '''
    location_list = []
    while True:
        try:
            number_of_locations = int(input())
            if isinstance(number_of_locations, int)== True:
                for x in range(number_of_locations):
                    location_list.append('location')
                return location_list
            else:
                print('Error not an integer')
        except ValueError:
            print('Error not an integer')


def locations_param(location_list: [str]) -> str:
    '''
    Creates the search location URL
    '''
    location_type = ['from','to']
    new_locations = []
    order_of_loc = 0
    for location in location_list:
        locs = input() 
        #order_of_loc += 1
        #for x in location_type:
        new_locations.append(locs)
        #new_locations.append((('from',input(), ('to', input())))
        #new_locations.append((('from',location), ('to', location)))
        #new_locations.append(location + str(order_of_loc))
    #fart = new_locations[::3]
    #butt = new_locations[2::2+1]
    #return fart+butt
    return new_locations #[::3]
            

def tuples_param(location_list: [str]) -> str:
    '''
    Creates the search location URL
    '''
    #location_type = ['to']
    loclist= location_list
    new_locations = []
    new_locations.append(('from',loclist[0]))
    #order_of_loc = 0
    
    for location in loclist[1:]:
        #locs = input()
        new_locations.append(('to',location))
        #order_of_loc += 1
    
        #new_locations.append((('from',input(), ('to', input())))
        #new_locations.append((('from',location), ('to', location)))
        #new_locations.append(location + str(order_of_loc))
    #fart = new_locations[::3]
    #butt = new_locations[2::2+1]
    #return fart+butt
    return new_locations #[::3]


def gps_url(new_locations:[str])-> str:
    '''
    creates directions search URL
    '''
    locations_direc = ('from','to') 
    locations_to_use = new_locations
    num_locations_to_use = 0
    gps_param = [('key', app_key),('ambiguities','ignore')]

    for x in locations_to_use:
        gps_param.append(x)
        #gps_param.append((x,input()))
    return base_URL + urllib.parse.urlencode(gps_param) 

def stuff(x:'list'):
    '''
assigns the from and too but is not used because I found a better way so disregard
    '''
    newlist= []
    loopcounter= 0
    newlist.append('from '+ x[0])
    for items in x:
        y = len(x)
        if loopcounter == y-1:
            break
        else:
            newlist.append('to '+x[loopcounter+1])
            loopcounter +=1
    return newlist

def request_response(url:'url'):
    '''
opens the URl and returns a loaded json response
    '''
    try:
        request = urllib.request.urlopen(url)
        json_response = request.read().decode(encoding = 'utf-8')
        return json.loads(json_response)
    finally:
        if request != None:
            request.close()
    
    


    
