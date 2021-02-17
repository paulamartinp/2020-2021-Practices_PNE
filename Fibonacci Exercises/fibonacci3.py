#Function to sum the nth Fibonacci term
import math
def fibosum(n):
    addition = 0
    for i in range(0, n + 1):
        number = (((1 + math.sqrt(5)) / 2) ** i - ((1 - math.sqrt(5)) / 2) ** i) // math.sqrt(5)
        addition = addition + int(number)
    return "Sum of the first" + str(n) + " terms of the Fibonacci series: " + str(addition)

print(fibosum(5))
print(fibosum(10))