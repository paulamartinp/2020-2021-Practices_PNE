from pathlib import Path
filename = "RNU6_269P.txt"
genome = Path(filename).read_text()

first_line = genome.split("\n")
print(first_line[0])