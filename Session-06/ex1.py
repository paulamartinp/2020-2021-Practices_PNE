class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):

        self.strbases = strbases
        if self.is_valid_sequence():
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("INCORRECT sequence detected")

    def is_valid_sequence(self):
        for c in self.strbases:
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
        return len(self.strbases)

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherite
       the methods from the Seq class
    """
    pass

# --- Main program
s1 = Seq("AGTACACTGGT")
g = Gene("Am I a valid sequence?")

# -- Printing the objects
print("sequence: " + str(s1))
print("sequence: " + str(g))