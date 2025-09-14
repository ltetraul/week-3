import seaborn as sns
import pandas as pd

#exercise 1
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print(fib(10))

#exercise 2
def to_binary(n):
    if n < 2:
        return str(n)
    else:
        return to_binary(n // 2) + str(n % 2)
print(to_binary(2))
print(to_binary(15))
