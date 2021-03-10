from Seq1 import Seq, test_sequences

def print_result(i, sequence):
    print("sequence " + str(i) + " Length:" + str(sequence.len()) + " " + str(sequence))
    print("Bases:", sequence.count())
    print("Rev:", sequence.reverse())

print("----|Practice 1, Exercise 7|-----")
#-- We create the test sequence
list_sequences = list(test_sequences())
for i in range(0, len(list_sequences)):
    print_result(i, list_sequences[i])

