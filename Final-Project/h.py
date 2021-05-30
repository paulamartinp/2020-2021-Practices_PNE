SERVER = 'rest.ensembl.org'
PARAMS = "?content-type=application/json"
import json
import http.client
ENDPOINT = '/sequence/id/'
connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + "ENSG00000165879" + PARAMS)
response = connection.getresponse()
response_dict = json.loads(response.read().decode())
print(response_dict)