import time

#Decorators allow you to modify the behavior of functions or classes. 
# Here's an example of a decorator that logs the execution time of a function:
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result
    return wrapper

@measure_time #decorators
def greet(name):
    print(f"Hello, {name}!")
    print("Gaurav Is Here" , name)

greet("John")


