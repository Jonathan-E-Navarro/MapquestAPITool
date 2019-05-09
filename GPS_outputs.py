#Created by: Jonathan Navarro 
#GPS_outputs

class GPS_outputs(object):
    def __init__(self):
        self.parameters = None

    """docstring for GPS_outputs"""
    def directions(self,x):
        print("Directions: ")
        for items in x['route']['legs']:
            print("\n")
            for item2 in items ['maneuvers']:
                print(item2['narrative'])
        print("\n")

    def displacement(self,x:''):
        print("Total Distance: ")
        print(x['route']['distance'])
        print("\n")

    def deltaT(self,x:''):
        print("Total Estimated Time: ")
        print((x['route']['time'])/60,'mins')
        print("\n")


    def position(self,x:''):
        print("Latitude and Longitude: ")
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
        print("\n")

    def output_parameters(self):
        '''
    generates the output parameters 
        '''
        output_list = []
        in_for_out = input("Enter amount of Parameters: ")
        if int(in_for_out) >= 1:
            if int(in_for_out) <= 4:
                for x in range(int(in_for_out)):
                    in_for_param = input("Enter Parameter: ")
                    output_list.append(in_for_param)
            else:
                print('try again')
                output_param()
        else:
            print('try again')
            output_param()
        self.parameters = output_list
        return 


    def final_results(self,json_result:'loaded json'):
        '''
        returns the final readable results
        '''
        print("RESULTS: ")
        print("\n")
        for items in self.parameters:
            inputs = str(items.lower())
            if inputs == 'directions':
                GPS_outputs.directions(1,json_result)
            elif inputs == 'distance':
                GPS_outputs.displacement(1,json_result)
            elif inputs == 'time':
                GPS_outputs.deltaT(1,json_result)
            elif inputs == 'latlong':
                GPS_outputs.position(1,json_result)
            else:
                print('theres an error here')
    
        
        
            
    
