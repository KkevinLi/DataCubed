'''
	Helper functions not associated directly with Django
'''
import googlemaps
import json

#The key should be placed somewhere more secure such as your env path
client = googlemaps.Client(key = 'AIzaSyAvSVDnhX1ZXH5maxh8BT90sdj7kC36KXw')

def writeToFile(text):
	f = open('test.txt','w')
	f.write(str(results))
	f.close()


def formatTspJson(distance,time,path,origin,destination):
	s = {"distanceInMeters":distance,
			"timeInMinutes":time,
			"path":
			{
				"origin" : origin,
				"destination" : destination,
				"pathTaken" : path
			}}
	return json.dumps(s)
'''
	Using the directions api this function will output the 
	optimal route from start to destination while passing through input cities
	returns json string in the format {distanceInMeters:X,timeInMinutes:Y,pathTraveled:[Z]}
'''
def directionApi(origin, destination, cities):

	if origin == None or destination == None:
		return -1;
	totalDistance = 0
	totalTime = 0;
	pathTraveled = []
	cities = ["Barossa+Valley,SA","Clare,SA","Connawarra,SA","McLaren+Vale,SA"]
	results = client.directions(origin,origin,waypoints = cities, optimize_waypoints = True)

	if(len(results) > 0):
		for route in results[0]["legs"][:-1]:
			totalDistance += route["distance"]['value']
			totalTime += route["duration"]['value']
			pathTraveled.append(route["end_address"])
	print( formatTspJson(totalDistance,totalTime,pathTraveled,origin,destination) )
	#	print ((results[0]["waypoint_order"]))



