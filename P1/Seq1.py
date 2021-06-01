import termcolor
from pathlib import Path

class Seq:
    """A class for representing sequences"""
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"
    def __init__(self, strbases=NULL_SEQUENCE):
        if strbases == "NULL":
            print("NULL seq created!")
            self.strbases = strbases
        else:
            if Seq.is_valid_sequence(strbases):  #Because is_valid_sequence() is an static method we use Seq.
                print("New sequence created!")
                self.strbases = strbases
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print("INCORRECT sequence detected")

    @staticmethod  # --- We are creating a function inside a class, not a method
    def print_seqs(list_seq, color):
        for i in range(0, len(list_seq)):
            text = "sequence " + str(i) + ":" + " Length:" + str(list_seq[i].len()) + " " + str(list_seq[i])
            termcolor.cprint(text, color)

    @staticmethod
    def is_valid_sequence(bases):
        for c in bases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True

    # If we want to create a function , not a method, we use @staticmethod
    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == Seq.INVALID_SEQUENCE or self.strbases == Seq.NULL_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return a, c, g, t
        else:
            for ch in self.strbases:
                if ch == "A":
                    a += 1
                elif ch == "C":
                    c += 1
                elif ch == "G":
                    g += 1
                elif ch == "T":
                    t += 1

            return a, c, g, t

    def count(self):
        a, c, g, t = self.count_bases()
        return {"A": a, "C": c, "T": t, "G": g}

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            complement = ""
            for ch in self.strbases:
                if ch == "A":
                    complement += "T"
                elif ch == "C":
                    complement += "G"
                elif ch == "G":
                    complement += "C"
                elif ch == "T":
                    complement += "A"
            return complement

    @staticmethod
    def take_out_first_line(seq):
        return seq[seq.find('\n') + 1:].replace('\n', '')

    def seq_read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())

    def higher_base(self):
        self.strbases = self.count()
        nucleotide = list(self.strbases.keys())
        value = list(self.strbases.values())
        higher_nucleotide = nucleotide[value.index(max(value))]
        return higher_nucleotide

def test_sequences():
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid sequence")
    return s1, s2, s3

class Gene(Seq):
    """This class is derived from the Seq Class
    All the objects of class Gene will inherit the methods
    from the Seq Class"""
    # --When inherit, we obtain the objects and the methods from parent class
    def __init__(self, strbases, name=""):
        # --Initialize the sequence with the value
        # --Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the Gene name along w/ the sequence"""
        return self.name + "-" + self.strabses

    # def len(self):
    #    if len(self.strbases) < 10:
    #        return "Sequence" + self.strbases + "is not long"

    # YOU DON'T NEED TO DO THIS because we are inheriting, we can use
    # the one of the parent class --> g = Gene("ACG", "FRAT") --> g.len()



