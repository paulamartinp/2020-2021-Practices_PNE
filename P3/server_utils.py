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
    cs.send(response.encode())


def get(cs, list_sequences, argument):
    print_colored("GET", "yellow")
    if 0 <= int(argument) <= 4:
        response = list_sequences[int(argument)]
        print(response)
        cs.send(response.encode())
    else:
        response = "Index out or range. You need to choose a number between 0 and 4"
        print(response)
        cs.send(response.encode())


def info(cs, sequence):
    print_colored("INFO", "green")
    seq = Seq(sequence)
    response = seq.print_percentages()  # -- We have created a new function in Seq1.py to print A: number (percentage)%
    final_response = "Sequence: " + sequence + "\n" + "Total Length: " + str(seq.len()) + "\n" + response
    print(final_response)
    cs.send(str(final_response).encode())


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
    else:
        response = "ERROR. Not available Gene Sequence. Try with ADA, FRAT1, FXN, RNU6_SP, or U5"
        print(response)
        cs.send(response.encode())










