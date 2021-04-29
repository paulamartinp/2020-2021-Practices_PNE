from Seq1 import Seq
import pathlib
import jinja2

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


def ping(cs):
    print_colored("PING command!", "green")
    response = "OK!"
    print(response)
    cs.send(response.encode())


def get(list_sequences, seq_number):
   context = {
       'number': seq_number,
       'sequence': list_sequences[int(seq_number)]
   }
   contents = read_template_html_file('./html/get.html').render(context=context)
   return contents




def info(sequence):
    seq = Seq(sequence)
    percentages = seq.print_percentages()  # -- We have created a new function in Seq1.py to print A: number (percentage)%
    seq_info = "Total Length: " + str(seq.len())
    context = {
        'gene_information': seq_info,
        'gene_name': sequence,
        'gene_percentages': percentages
    }
    contents = read_template_html_file('./html/info.html').render(context=context)
    return contents


def comp(argument):
    seq = Seq(argument)
    context = {
        'gene_name': seq,
        'gene_comp': seq.complement()
    }
    contents = read_template_html_file('./html/comp.html').render(context=context)
    return contents



def rev(argument):
    seq = Seq(argument)
    context = {
        'seq_name': argument,
        'seq_reverse': seq.reverse()
    }
    contents = read_template_html_file('./html/rev.html').render(context=context)
    return contents


def gene(seq_name):
    PATH = "./projects/" + seq_name + ".txt"
    s1 = Seq()
    s1.seq_read_fasta(PATH)
    context = {
        'gene_name': seq_name,
        'gene_contents': s1.strbases
    }
    contents = read_template_html_file('./html/gene.html').render(context=context)
    return contents








