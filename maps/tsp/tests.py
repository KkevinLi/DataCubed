from django.test import TestCase
from django.test import Client
import json

# Create your tests here.
class  TspTest(TestCase):
	"""docstring for  TspTest"""

	def SetUp(self):
		self.client = Client()

	def test_sendLocationAsPost(self):
		origin = "Adelaide,SA"
		destination = "Adelaide,SA"
		cities = ["Barossa+Valley,SA","Clare,SA","Connawarra,SA","McLaren+Vale,SA"]
		pythonDict = {
				"origin":origin,
				"destination":destination, 
				"locations":cities
			}
		print (pythonDict)
		response = self.client.post('/tsp/',json.dumps(pythonDict),content_type = "application/json")
	#	response = self.client.post('/tsp/',(pythonDict))
		
		self.assertEqual(response.status_code,200)
