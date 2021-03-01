def sumn(n):
    res = 0
    for i in range(1, n + 1):
        res += 1
    return res

#Main program:
print("Sum of the first 20 intg: ", sumn(20))
print("sum of the first 10 elements:", sumn(10))