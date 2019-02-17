#Jonathan Navarro 83144130
#GPS_outputs

import json

class journey_steps:
    '''
is the generator class for the directions
    '''
    def directions(self,x):
        for items in x['route']['legs']:
            for item2 in items ['maneuvers']:
                print(item2['narrative'])

class deltaX:
    '''
is the generator class for the total distance
    '''
    def displacement(self,x:''):
        print(x['route']['distance'])

class elapsedT:
    '''
is the generator class for the total time
    '''
    def deltaT(self,x:''):
        print((x['route']['time'])/60,'mins')

class LATLONG:
    '''
is the generator class for the latitude and longitude 
    '''
    def position(self,x:''):
        for items in x['route']['locations']:
            lat_long = (items['latLng']['lat'])
            if str(lat_long).startswith('-'):
                print(lat_long[1:-1], 's')
            else:
                print(lat_long,'n')
            latlngEW = (items['latLng']['lng'])
            if str(latlngEW).startswith('-'):
                print(str(latlngEW)[1:-1],'w')
            else:
                print(latlngEW,'e')

def output_param():
    '''
generates the output parameters 
    '''
    output_list = []
    in_for_out = input()
    if int(in_for_out) >= 1:
        if int(in_for_out) <= 4:
            for x in range(int(in_for_out)):
                in_for_param = input()
                output_list.append(in_for_param)
        else:
            print('try again')
            output_param()
    else:
        print('try again')
        output_param()
    return output_list
    
def final_results(out_param:'',json_result:'loaded json'):
    '''
returns the final readable results
    '''
    for items in out_param:
        inputs = str(items.lower())
        if inputs == 'steps':
            journey_steps.directions(1,json_result)
        elif inputs == 'totaldistance':
            deltaX.displacement(1,json_result)
        elif inputs == 'total time':
            elapsedT.deltaT(1,json_result)
        elif inputs == 'latlong':
            LATLONG.position(1,json_result)
        else:
            print('theres an error here')
            
    
