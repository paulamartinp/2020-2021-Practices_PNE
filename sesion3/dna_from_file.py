def count_nucleotides(seq):
    a = 0
    c = 0
    t = 0
    g = 0
    for n in seq:
        if n == "A":
            a += 1
        elif n == "C":
            c += 1
        elif n == "T":
            t += 1
        elif n == "G":
            g += 1
        else:
            print("ERROR")
    return a, c, g, t

def read_from_file(filename):
    with open(filename, 'r') as f:
        seq = f.read()
        seq = seq.replace('\n', '')
        return seq

def correct_dna(seq):
    incorrect = 0
    for n in seq:
        if n != 'A' and n != 'C' and n != 'G' and n != 'T':
            incorrect += 1
        else:
            incorrect += 0

    if incorrect == 0:
        correct = True
    else:
        correct = False
    return correct

#Main program
seq = read_from_file("dna.txt")
correct = correct_dna(seq)

if correct == True:
    print("Total lenght", len(seq))
    a, c, g, t = count_nucleotides(seq)
    print(count_nucleotides(seq))
    print("A:" + str(a) + "\n" + "C:" + str(c) + "\n" + "G:" + str(g) + "\n" + "T:" + str(g))


