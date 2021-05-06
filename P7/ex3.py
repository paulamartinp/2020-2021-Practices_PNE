import http.client
import json

DICT_GENES = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362'
}

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
ID = DICT_GENES['MIR633']
PARAMS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)  # --We are connecting to the server
connection.request("GET", ENDPOINT + ID + PARAMS)
response = connection.getresponse() # -- HTTP response
print("Response received:", response.status, response.reason)
# -- Useful for dicts -->print(json.dumps(response, indent=4, sort_keys=True))

if response.status == 200:  # This means there are nor errors
    response = json.loads(response.read().decode())
    print(json.dumps(response, indent=4, sort_keys=True))
    print("Gene:", ID)
    print("Description:", response["desc"])
    print("Bases:", response["seq"])
elif response.status == 404:
    print("Check if the END POINT is correctly written!!!")

