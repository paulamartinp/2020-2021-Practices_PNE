import Seq0

FOLDER = "./sequences/"
FILE = "U5"
sequence = Seq0.seq_read_fasta(FOLDER + FILE + ".txt")
fragment = sequence[0:20]
complement = Seq0.seq_complement(fragment)

print("------|Exercise 6|-------")
print("Frag: " + str(fragment))
print("Comp: " + str(complement))