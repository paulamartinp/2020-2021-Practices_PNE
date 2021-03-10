import termcolor

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):
        if strbases == "NULL":
            print("NULL seq created!")
            self.strbases = strbases
        else:
            if Seq.is_valid_sequence(strbases):
                print("New sequence created!")
                self.strbases = strbases
            else:
                self.strbases = "ERROR"
                print("INCORRECT sequence detected")

    @staticmethod
    def print_seqs(list_seq):
        for i in range(0, len(list_seq)):
            text = "sequence " + str(i) + ":" + " Length:" + str(list_seq[i].len()) + " " + str(list_seq[i])
            print(text)

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
        if self.strbases == "NULL" or self.strbases == "Error":
            return 0
        else:
            return len(self.strbases)

    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        for ch in self.strbases:
            if ch == "A":
                a += 1
            elif ch == "C":
                c += 1
            elif ch == "G":
                g += 1
            elif ch == "T":
                t += 1



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

    #def len(self):
    #    if len(self.strbases) < 10:
    #        return "Sequence" + self.strbases + "is not long"

    # YOU DON'T NEED TO DO THIS because we are inheriting, we can use
    # the one of the parent class --> g = Gene("ACG", "FRAT") --> g.len()


