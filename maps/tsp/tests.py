from django.test import TestCase
from django.test import Client

# Create your tests here.
class  TspTest(TestCase):
	"""docstring for  TspTest"""

	def SetUp(self):
		self.client = Client()

	def test_sendLocationAsPost(self):
		origin = "Adelaide,SA"
		destination = "Adelaide,SA"
		cities = ["Barossa+Valley,SA","Clare,SA","Connawarra,SA","McLaren+Vale,SA"]

		response = self.client.post('/tsp/',{'origin':origin,'destination':destination, 'locations':cities})
		self.assertEqual(response.status_code,200)
