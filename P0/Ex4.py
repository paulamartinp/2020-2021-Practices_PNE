import Seq0
GENE_FOLDER = "./sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]
base_list = ["A", "C", "G", "T"]
try:
    if Seq0.correct_directory(GENE_FOLDER) == True:
        print("\n" + "------|Exercise 5|------")
        for gene in gene_list:
            sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
            print("\n" + "Gene" + gene)
            for base in base_list:
                print(base + ":" + str(Seq0.seq_count_bases(sequence, base)))
except FileNotFoundError:
    print("ERROR. INCORRECT FILE")
except ZeroDivisionError:
    print("Error. INCORRECT DIRECTORY")