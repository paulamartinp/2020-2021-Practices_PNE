import Seq0
FOLDER = "./sequences/"
FILE = "U5"
try:
    if Seq0.correct_directory(FOLDER) == True:
        sequence = Seq0.seq_read_fasta(FOLDER + FILE + ".txt")
        fragment = sequence[0:20]
        complement = Seq0.seq_complement(fragment)
        print("------|Exercise 6|-------")
        print("Frag: " + str(fragment))
        print("Comp: " + str(complement))
except FileNotFoundError:
    print("ERROR.INCORRECT FILE")
except ZeroDivisionError:
    print("ERROR. INCORRECT DIRECTORY")