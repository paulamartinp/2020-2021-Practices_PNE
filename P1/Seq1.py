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
            text = "sequence " + str(i) + ":" + " Length" + ":" + str(list_seq[i].len()) + str(list_seq[i])
            termcolor.cprint(text, "yellow")

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