import Seq0
FOLDER = "./sequences/"
FILE = "U5"
try:
    if Seq0.correct_directory(FOLDER) == True:
        sequence = Seq0.seq_read_fasta(FOLDER + FILE + ".txt")
        print("---------|Exercise 2|----------")
        print("DNA file: " + FILE + ".txt" + ":")
        print("The first 20 nucleotides are:")
        print(sequence[0:20])
except FileNotFoundError:
    print("ERROR. INCORRECT FILE")
except ZeroDivisionError:
    print("ERROR. INCORRECT DIRECTORY")



