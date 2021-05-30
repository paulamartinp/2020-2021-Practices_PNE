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


def listSpecies(arguments):
    ENDPOINT = '/info/species/'
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + PARAMS)
    response = connection.getresponse()
    response_dict = json.loads(response.read().decode())

    species = []
    if arguments == {}:
        limit = len(response_dict['species'])
        for dict in range(0, int(limit)):
            species.append(response_dict['species'][dict]['display_name'])
    else:
        limit = arguments['limit'][0]
        try:
            if 1 <= int(limit) <= len(response_dict['species']):
                for dict in range(0, int(limit)):
                    species.append(response_dict['species'][dict]['display_name'])
            else:
                contents = read_template_html_file("html/errors/exceed_of_limit.html").render()
                return contents
        except ValueError:
            contents = read_template_html_file("html/errors/error.html").render()
            return contents

    context = {
       'species': species,
       'length': len(species),
        'limit': limit
    }
    contents = read_template_html_file('./html/list_species.html').render(context=context)
    return contents

def karyotype(arguments):
    if arguments != {}:
        if len(arguments['specie']) == 1:
            specie = arguments['specie'][0]
            ENDPOINT = '/info/assembly/'
            connection = http.client.HTTPConnection(SERVER)
            connection.request("GET", ENDPOINT + specie + PARAMS)
            response = connection.getresponse()
            response_dict = json.loads(response.read().decode())
            if response.status == 200:
                context = {'karyotype': response_dict['karyotype']}
                contents = read_template_html_file('./html/karyotype.html').render(context=context)
                return contents
            elif response_dict['error']:
                contents = read_template_html_file("html/errors/error.html").render()
                return contents
    else:
        contents = read_template_html_file("html/errors/not_introduced.html").render()
        return contents

def chromosome_length(arguments):
    if arguments != {}:
        if len(arguments) == 2:
            specie = arguments['specie'][0]
            ENDPOINT = '/info/assembly/'
            connection = http.client.HTTPConnection(SERVER)
            connection.request("GET", ENDPOINT + specie + PARAMS)
            response = connection.getresponse()
            response_dict = json.loads(response.read().decode())

            chromo = arguments['chromo'][0]
            if response.status == 200:
                for dict in response_dict['top_level_region']:
                    if dict['name'] == str(chromo):
                        context = {'chromosome_length': dict['length']}
                        contents = read_template_html_file('./html/chromosome_length.html').render(context=context)
                    else:
                        contents = read_template_html_file("html/errors/error.html").render()
                return contents

            else:
                contents = read_template_html_file("html/errors/error.html").render()
                return contents
        else:
            contents = read_template_html_file("html/errors/not_introduced.html").render()
            return contents
    else:
        contents = read_template_html_file("html/errors/not_introduced.html").render()
        return contents










