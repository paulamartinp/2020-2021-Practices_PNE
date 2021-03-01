from pathlib import Path
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





