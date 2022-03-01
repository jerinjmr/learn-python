"""
Learning Python3.

Complete Python Developer in 2022: Zero to Mastery
Udemy Online Course

Advanced Python: Generators
"""
# Excercise 01: Fib series using generators
from time import time


def performance_test(func):
    """Check performance of yield function."""
    def wrapper_func(*args, **kwargs):
        start_time = time()
        print(f'Stating time: {start_time}')
        yield from func(*args, **kwargs)
        stop_time = time()
        print(f'End time: {stop_time}')
        execution_time = stop_time-start_time
        print(f'Execution time: {execution_time}')
    return wrapper_func


@performance_test
def fib_series(fib_length):
    """
    Generate fibonacci series.

    : param fib_length: Length of fib series
    : yield fib_item
    """
    current_num = 0
    next_num = 1
    for _ in range(fib_length):
        yield current_num
        fib_item = current_num+next_num
        current_num, next_num = next_num, fib_item


FIB_LENGTH = 5
fib = fib_series(FIB_LENGTH)
# print(next(fib))
for item in fib:
    print(item)
