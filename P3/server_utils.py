from Seq1 import Seq
def print_colored(message, color):
    import termcolor
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def ping(cs):
    print_colored("PING command!", "green")
    response = "OK!"
    print(response)
    cs.send(str(response).encode())  # -- Send a response message to the client encoded into bytes

def get(cs, list_sequences, argument):
    print_colored("GET", "yellow")
    if 0 <= int(argument) <= 4:
        response = list_sequences[int(argument)]
        print(response)
        cs.send(response.encode())

def info(cs, sequence):
    print_colored("INFO", "green")
    seq = Seq(sequence)
    print("Sequence: " + sequence)
    print("Total Length: " + str(seq.len()))
    nucleotides = seq.count()
    for keys, values in nucleotides.items():  # -- seq.count() returns a dictionary
        percentage = round((100 * (values / len(sequence))), 1)
        data = keys + ": " + str(values) + " (" + str(percentage) + "%) "
        print(data)
        response = "Sequence: " + sequence + "\n" + "Total length: " + str(seq.len()) + "\n" + str(data)
        cs.send(response.encode())


def comp(cs, argument):
    print_colored("COMP", "green")
    seq = Seq(argument)
    complement = seq.complement()
    print(complement)
    cs.send(complement.encode())

def rev(cs, argument):
    print_colored("REV", "green")
    seq = Seq(argument)
    reverse = seq.reverse()
    print(reverse)
    cs.send(reverse.encode())

def gene(cs, argument, gene_list, GENE_FOLDER):
    print_colored("GENE", "green")
    if argument in gene_list:
        sequence = Seq()
        sequence.seq_read_fasta(GENE_FOLDER + argument + ".txt")
        print(sequence)
        cs.send(str(sequence).encode())











