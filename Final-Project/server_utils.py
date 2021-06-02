import pathlib
import jinja2
import http.client
import json
from Seq1 import Seq

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
        if len(limit.split(' ')) == 1:
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
        else:
            contents = read_template_html_file("html/errors/no_blank_spaces.html").render()
            return contents

    context = {
       'species': species,
       'length': len(species),
       'limit': limit
    }
    contents = read_template_html_file('./html/list_species.html').render(context=context)
    return contents

def karyotype(arguments, path_name):
    if arguments != {}:
        try:
            specie = arguments['specie'][0]
            if len(specie.split(' ')) == 1:
                ENDPOINT = '/info/assembly/'
                connection = http.client.HTTPConnection(SERVER)
                connection.request("GET", ENDPOINT + specie + PARAMS)
                response = connection.getresponse()
                response_dict = json.loads(response.read().decode())
                if path_name == "/karyotype":
                    if response.status == 200:
                        context = {'karyotype': response_dict['karyotype']}
                        contents = read_template_html_file('./html/karyotype.html').render(context=context)
                        return contents
                    elif response_dict['error']:
                        contents = read_template_html_file("html/errors/error.html").render()
                        return contents
                elif path_name == "/chromosomeLength":
                    if response.status == 200:
                        chromo = arguments['chromo'][0]
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
                contents = read_template_html_file("html/errors/no_blank_spaces.html").render()
                return contents

        except KeyError:
            contents = read_template_html_file("html/errors/not_introduced.html").render()
            return contents
    else:
        contents = read_template_html_file("html/errors/not_introduced.html").render()
        return contents


def gene_seq(arguments,path_name,HUMAN_GENES):
    if arguments != {}:
        gene = arguments['gene'][0]
        ENDPOINT = "/sequence/id/"
        id = HUMAN_GENES[gene]
        connection = http.client.HTTPConnection(SERVER)
        connection.request("GET", ENDPOINT + id + PARAMS)
        response = connection.getresponse()
        response_dict = json.loads(response.read().decode())
        if path_name == "/geneSeq" and response.status == 200:
            context = {'sequence': response_dict['seq'], 'gene': gene}
            contents = read_template_html_file('./html/gene_sequence.html').render(context=context)
            return contents
        elif path_name == "/geneInfo" and response.status == 200:
            sequence = Seq(response_dict['seq'])
            chromo_info_list = response_dict['desc'].split(":")
            context = {'length': sequence.len(),
                       'start': chromo_info_list[3],
                       'end': chromo_info_list[4],
                       'chromo_name': chromo_info_list[1],
                       'id': response_dict['id'],
                       'gene': gene
                       }
            contents = read_template_html_file('./html/gene_sequence_info.html').render(context=context)
            return contents
        elif path_name == "/geneCalc" and response.status == 200:
            sequence = Seq(response_dict['seq'])
            context = {'length': sequence.len(),
                       'percentages': sequence.print_percentages(),
                       'gene': gene
                       }
            contents = read_template_html_file('./html/gene_percentages.html').render(context=context)
            return contents
        else:
            contents = read_template_html_file("html/errors/error.html").render()
            return contents
    else:
        contents = read_template_html_file("html/errors/not_introduced.html").render()
        return contents











