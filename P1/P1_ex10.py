from Seq1 import Seq

def print_result(sequence):
    print("Gene " + str(gene) + ": " + "Most frequent base: " + str(sequence.higher_base()))

GENE_FOLDER = "./projects/"
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_2P"]

print("----|Practice 1, Exercise 10|-----")
for gene in gene_list:
     genome = Seq()
     genome.seq_read_fasta(GENE_FOLDER + gene + ".txt")
     print_result(genome)

