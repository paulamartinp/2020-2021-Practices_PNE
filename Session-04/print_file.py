from pathlib import Path
filename = "RNU6_269P.txt"
# -- Open and read file
genome = Path(filename).read_text()
print(genome)




