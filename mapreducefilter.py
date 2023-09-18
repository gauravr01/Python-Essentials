# Map, reduce, and filter are three commonly used higher-order
#  functions in Python that operate on sequences such as lists, tuples
# , or sets. These functions allow you to perform transformations and computations 
# on the elements of a sequence in a concise and efficient way. Here's an 
# explanation
#  of each function:

# Map:
# The map() function applies a given function to each item in an iterable 
# (e.g., a list) and returns a new iterable with the results. It takes 
# two arguments: the function to be applied and the iterable. The function
#  is applied to each element of the iterable, and the results are collected 
# into a new iterable.
#-------------------------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]

# Square each number using map()
squared_numbers = map(lambda x: x**2, numbers)

# Print the squared numbers
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
#-------------------------------------------------------------------------------------------
# Reduce:
# The reduce() function applies a binary function (a function that takes two 
# arguments) cumulatively to the items of an iterable, from left to right, to reduce 
# the iterable to a single value. It requires the functools module to be imported.
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Calculate the sum of numbers using reduce()
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

# Print the sum
print(sum_of_numbers)  # Output: 15
#-------------------------------------------------------------------------------------------
# The filter() function constructs an iterator from elements of an iterable for 
# which a given condition (a function that returns a boolean) is true. It returns 
# a new iterable that contains only the elements for which the condition is true.
numbers = [1, 2, 3, 4, 5]

# Filter even numbers using filter()
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Print the even numbers
print(list(even_numbers))  # Output: [2, 4]
