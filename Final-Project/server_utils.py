import pathlib
import jinja2
import http.client
import json

SERVER = 'rest.ensembl.org'
PARAMS = "?content-type=application/json"

def read_html_file(filename):
    contents = pathlib.Path(filename).read_text()
    return contents

def read_template_html_file(filename):
    contents = jinja2.Template(pathlib.Path(filename).read_text())
    return contents

def print_colored(message, color):
    import termcolor
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")


def listSpecies(limit):
    ENDPOINT = '/info/species/'
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + PARAMS)
    response = connection.getresponse()
    response_dict = json.loads(response.read().decode())

    species = []
    if 0<= int(limit) <= 310:
        for dict in range(0, int(limit)):
            species.append(response_dict['species'][dict]['display_name'])
    elif limit == None:
        for dict in response_dict['species']:
            species.append(dict['display_name'])

    context = {
       'species': species,
        'length': len(species)
    }
    contents = read_template_html_file('./html/list_species.html').render(context=context)
    return contents

def karyotype(id):
    ENDPOINT = '/info/assembly/'
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + id + PARAMS)
    response = connection.getresponse()

    if response.status == 200:
        context = json.loads(response.read().decode())
        contents = read_template_html_file('./html/karyotype.html').render(context=context)
        return contents







