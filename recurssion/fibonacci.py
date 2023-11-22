# to show the fibonacci series using reccursion

# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# n = input("Enter the number: ")
# m = int(n)
# print(fibonacci(m))

from functools import lru_cache


import sys

sys.setrecursionlimit(10000)

@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(500))

