from pathlib import Path
import termcolor

def seq_ping():
    print("OK")

def take_out_first_line(seq):
    return seq[seq.find('\n') + 1:].replace('\n', '')

def seq_read_fasta(filename):
    sequence = take_out_first_line(Path(filename).read_text())
    return sequence

def seq_len(sequence):
    return len(sequence)

def seq_count_bases(seq, base):
    return seq.count(base)

def create_dict(seq):
    gene_dict = {"A": 0, "T": 0, "C": 0, "G": 0}
    for gene in seq:
        gene_dict[gene] += 1
    return gene_dict

def seq_reverse(seq):
    position = -1
    reverse_sequence = ""
    first_gene = False
    while not first_gene:
        gene = seq[position]
        reverse_sequence += gene
        position = position - 1
        if position == -(len(seq) + 1):
            return reverse_sequence
            first_gene = True


def seq_complement(seq):
    new_seq = ""
    position = 0
    last_gene = False
    while not last_gene:
        gene = seq[position]
        position += 1
        if gene == "A":
            new_seq += "T"
        elif gene == "T":
            new_seq += "A"
        elif gene == "C":
            new_seq += "G"
        elif gene == "G":
            new_seq += "C"

        if position == len(seq):
            return new_seq
            last_gene = True


def correct_directory(directory):
    if directory == "./sequences/" or directory == "../P0/sequences/" or directory == "../Session-04/":
        return True
    else:
        raise ZeroDivisionError


def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases
        if self.is_valid_sequence():
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "Error"
            print("INCORRECT sequence detected")

    @staticmethod
    def print_seqs(list_seq):
        for i in range(0, len(list_seq)):
            text = "sequence " + str(i) + ":" + " Length" + ":" + str(list_seq[i].len()) + str(list_seq[i])
            termcolor.cprint(text, "yellow")
    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True

    # If we want to create a function , not a method, we use @staticmethod
    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)





