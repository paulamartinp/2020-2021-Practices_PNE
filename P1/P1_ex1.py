from Seq1 import Seq, Gene

print("----Exercise 1----")
seq = Seq("ACTGA")
print("Sequence " + str(1) + ": (Length: " + str(seq.len()) + " ) " + str(seq))
gene = Gene("AACG", "hola")
print(gene.len())