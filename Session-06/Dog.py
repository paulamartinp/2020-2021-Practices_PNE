#inside we will have different functions/methods#
#each functions will perform actions on the objects
class Dog:
    def __init__(self, name, age):
        self.name = name   #attributes
        self.age = age

    def set_name(self, name):
        self.name = name
        print("This is {}, and I'm sitting down here".format(self.name))
    def set_age(self, age):
        self.age = age
    def sleep(self):
        pass
    def sitdown(self):
        print("Yes, I will sit down")

ares = Dog("ares", 10)
#print(ares)

toby = Dog("toby", 21)
ares.set_age(20)
#print(toby)

ares.set_name("trueno")
ares.set_age(1)
ares.rollover()
ares.sitdown()


#ares = toby
#black = Dog("toby", 21)
#black.name = "troy"
#print(toby is ares)
# pass


