from Seq1 import Seq
def print_colored(message, color):
    import termcolor
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def ping(cs):
    print_colored("PING command!", "green")
    response = "OK!"  # -- Send a response message to the client
    print(response)
    cs.send(str(response).encode())  # -- The message has to be encoded into bytes

def get(cs, list_sequences, argument):
    print_colored("GET", "yellow")
    if 0 <= int(argument) <= 4:
        response = list_sequences[int(argument)]
        print(response)
        cs.send(response.encode())

def info(cs, argument):
    print_colored("INFO", "green")
    seq = Seq(argument)
    print("Sequence: " + argument)
    print("Total Length: " + str(seq.len()))
    nucleotides = seq.count()
    for k, v in nucleotides.items():
        percentage = round((100 * (v / len(argument))), 1)
        print(k + ": " + str(v) + " (" + str(percentage) + "%)")

def comp(cs, argument):
    print_colored("COMP", "green")
    seq = Seq(argument)
    print(seq.complement())

def rev(cs, argument):
    print_colored("REV", "green")
    seq = Seq(argument)
    print(seq.reverse())

def gene(cs, argument, gene_list, GENE_FOLDER):
    print_colored("GENE", "green")
    if argument in gene_list:
        sequence = Seq()
        sequence.seq_read_fasta(GENE_FOLDER + argument + ".txt")
        print(sequence)










