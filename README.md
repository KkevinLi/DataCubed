# Shortest Path For Travelling Multiple Locations

Django webserver which takes a list of addresses and outputs the total distance, time and route to go through all locations.

Utilizes Google DIrections API.  Logic implementation is in maps/libs/googlemap_util.py and maps/tsp/views.py

An Api Key is already provided in project. Swap it out for your own if neccesary.

## Prerequisites
pip install -r requirements.txt  (Virtualenv is already in repo. Do : source venv/bin/activate)

## Running Test
-python manage.py test (Can modify the origin, destination and locations inside maps/tsp/tests.py)

-python manage.py runserver

curl -H "Content-Type: application/json" -X POST -d '{"origin" : "Adelaide,SA", "destination": "Adelaide,SA", "locations": ["Barossa+Valley,SA", "Clare,SA", "Connawarra,SA", "McLaren+Vale,SA"]}' http://localhost:8000/tsp/
