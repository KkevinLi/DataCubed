from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from libs import googlemap_util
import json


# Create your views here.
@csrf_exempt
def index(request):
	if request.method == 'POST':
		origin = request.POST.get("origin",None)
		destination = request.POST.get("destination",None)
		locations = ','.join(map(str,request.POST.getlist("locations")))
		googlemap_util.directionApi(origin,destination,locations)
		print ("hi")
	return HttpResponse("Hello world")
