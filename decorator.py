import time
import functools


def measure_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper



@measure_execution_time
def compute_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


n = int(input())
result = compute_factorial(n)
print(f"The factorial of {n} is: {result}")
