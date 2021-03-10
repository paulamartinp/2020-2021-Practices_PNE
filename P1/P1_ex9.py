from Seq1 import Seq

def print_result(sequence):
    print("Sequence: " + " Length:" + str(sequence.len()) + " " + str(sequence))
    print("Bases:", sequence.count())
    print("Rev:", sequence.reverse())
    print("Comp:", sequence.complement())

print("-----|Practice 1, Exercise 9|----")
PATH = "./projects/"
s1 = Seq()
s1.seq_read_fasta(PATH + "U5" + ".txt")
print_result(s1)
