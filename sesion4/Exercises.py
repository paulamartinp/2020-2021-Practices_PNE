#Exercise 1
from pathlib import Path
filename = "../P0/sequences/RNU6_2P.txt"
#Open and read file
contents = Path(filename).read_text()
#print(contents)

#Exercise 2
first_line = contents.split("\n")
print(first_line[0])

#Exercise 3
sequence = first_line[1:]
for n in sequence:
    print(n)
