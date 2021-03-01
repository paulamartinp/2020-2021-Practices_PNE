import Seq0
FOLDER = "./sequences/"
FILE = "U5"
try:
    if Seq0.correct_directory(FOLDER) == True:
        sequence = Seq0.seq_read_fasta(FOLDER + FILE + ".txt")
        fragment = sequence[0:20]
        reverse_fragment = Seq0.seq_reverse(fragment)
        print("------|Exercise 6|-------")
        print("Frag: " + str(fragment))
        print("Rev : " + str(reverse_fragment))
except FileNotFoundError:
    print("ERROR.INCORRECT FILE")
except ZeroDivisionError:
    print("ERROR. INCORRECT DIRECTORY")
