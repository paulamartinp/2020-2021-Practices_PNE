import Seq0

GENE_FOLDER = "./sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN" ]
base_list = ["A", "C", "G", "T"]
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    print("Gene " + str(gene) + ": " + str(Seq0.create_dict(sequence)))


