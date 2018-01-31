from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from libs import googlemap_util
import json

'''
	Csrf_exempt in order to curl. Unit Test is already provided which bypasses csrf
	On post request one part takes in json input 
	Else if we had a front end we would take form input 
'''
@csrf_exempt
def index(request):
	optimalPath = ""
	if request.method == 'POST':
		if 'application/json' in request.META['CONTENT_TYPE']:
			data = json.loads(request.body)
			origin = data["origin"]
			destination = data["destination"]
			locations = data["locations"]
		else:
		#	print ("Not Json input")
			origin = request.POST.get("origin",None)
			destination = request.POST.get("destination",None)
			locations = ','.join(map(str,request.POST.getlist("locations")))
		optimalPath = googlemap_util.directionApi(origin,destination,locations) + "\n"
	return HttpResponse(optimalPath, content_type = 'application/json')

