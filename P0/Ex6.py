import Seq0

FOLDER = "./sequences/"
FILE = "U5"
sequence = Seq0.seq_read_fasta(FOLDER + FILE + ".txt")
fragment = sequence[0:20]

reverse_fragment = Seq0.seq_reverse(fragment)

print("------|Exercise 6|-------")
print("Fragment: " + str(fragment))
print("Reverse fragment: " + str(reverse_fragment))
