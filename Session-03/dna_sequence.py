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


seq = input("Introduce a seq:")
print("Total lenght", len(seq))
a, c, g, t = count_nucleotides(seq)
print(count_nucleotides(seq))
print("A:" + str(a) + "\n" + "C:" + str(c) + "\n" + "G:" + str(g) + "\n" + "T:" + str(g))



