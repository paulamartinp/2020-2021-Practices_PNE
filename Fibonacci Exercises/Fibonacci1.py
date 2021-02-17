import math
for n in range(0, 11):
    number = (((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n) // math.sqrt(5)
    print(int(number), end=" ")
