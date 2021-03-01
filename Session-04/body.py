from pathlib import Path
filename = "RNU6_269P.txt"
genome = Path(filename).read_text()

sequence = genome[genome.find("\n") + 1:]
print(sequence)
