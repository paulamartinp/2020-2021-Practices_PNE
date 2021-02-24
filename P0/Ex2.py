import Seq0
FOLDER = "./sequences/"
FILE = "U5"
sequence = Seq0.seq_read_fasta(FOLDER + FILE + ".txt")
print("---------|Exercise 2|----------")
print("The first 20 nucleotides are:")
print(sequence[0:20])


