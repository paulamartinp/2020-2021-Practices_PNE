import Seq0
from Seq0 import Seq

seq_list1 = Seq0.generate_seqs("A", 3)
seq_list2 = Seq0.generate_seqs("AC", 5)

print("List 1:")
Seq.print_seqs(seq_list1)
print()
print("List 2:")
Seq.print_seqs(seq_list2)