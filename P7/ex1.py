import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)  # --We are connecting to the server
connection.request("GET", ENDPOINT + PARAMS)
response = connection.getresponse() # -- HTTP response
answer_decoded = response.read().decode()
print(type(answer_decoded), answer_decoded)

dict_response = json.loads(answer_decoded)
print(type(dict_response), dict_response)

if dict_response['ping'] == 1:
    print('PING OK!! The database is running')
else:
    print('The database is not running...')
