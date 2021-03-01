import Seq0
GENE_FOLDER = "./sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]
base_list = ["A", "C", "G", "T"]
print("-------|Exercise 8|-------")
try:
    if Seq0.correct_directory(GENE_FOLDER) == True:
        for gene in gene_list:
            sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
            gene_dict = Seq0.create_dict(sequence)
            keys = list(gene_dict.keys())
            values = list(gene_dict.values())
            higher_nucleotide = keys[values.index(max(values))]
            print("Gene " + gene + ":" + " Most frequent Base: " + str(higher_nucleotide))
except FileNotFoundError:
    print("ERROR.INCORRECT FILE")
except ZeroDivisionError:
    print("ERROR. INCORRECT DIRECTORY")