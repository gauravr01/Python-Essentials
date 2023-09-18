# In Python, a lambda function, also known as an anonymous function, is a 
# way to create small, one-line functions without explicitly defining a function
#  using the def keyword. Lambda functions are typically used when you need a simple
# function for a short-lived purpose and don't want to define a full-fledged function.

# The general syntax of a lambda function is as follows:
#lambda arguement : expression
# Example 1: Basic lambda function
multiply = lambda x, y: x * y
result = multiply(5, 3)
print(result)  # Output: 15

# Example 2: Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Example 3: Sorting a list of tuples using lambda
fruits = [('apple', 10), ('orange', 5), ('banana', 8)]
fruits.sort(key=lambda x: x[1])  # Sort based on the second element of each tuple
print(fruits)  # Output: [('orange', 5), ('banana', 8), ('apple', 10)]
