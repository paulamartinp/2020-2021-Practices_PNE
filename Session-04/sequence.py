from pathlib import Path
filename = "ADA.txt"
genome = Path(filename).read_text()

sequence = genome[genome.find("\n") + 1:].replace("\n", "")
print(sequence)