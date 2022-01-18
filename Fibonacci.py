import unittest
num = int(input()) #parsing
def fibonacci(n):
    if n <= 1:
        return n
    else:
        #recurssion
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(num):
    print(fibonacci(i))

