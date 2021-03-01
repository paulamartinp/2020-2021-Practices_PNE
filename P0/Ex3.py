import Seq0
GENE_FOLDER = "./sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]
try:
    if Seq0.correct_directory(GENE_FOLDER) == True:
        print("------- |Exercise 3|-------")
        for gene in gene_list:
            sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
            print("Gene " + str(gene) + " ---->" + " Length: "+ str(Seq0.seq_len(sequence)))
except FileNotFoundError:
    print("ERROR. INCORRECT FILE")
except ZeroDivisionError:
    print("ERROR. INCORRECT DIRECTORY")

