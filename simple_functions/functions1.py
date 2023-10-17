from functools import cache

#To make functions visible to the package
__all__ = ['my_sum','factorial']

def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    return n * factorial(n-1) if n else 1
