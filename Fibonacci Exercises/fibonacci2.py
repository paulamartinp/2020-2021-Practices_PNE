#Function to print the nth Fibonacci term
import math
def fibon(n):
    number = int((((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n) // math.sqrt(5))
    return str(n) + "th Fibonacci term: " + str(number)

print(fibon(5))
print(fibon(10))
print(fibon(15))