#Generators are a way to create iterators in Python. They allow you to generate
#  values one at a time, saving memory
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()

for _ in range(10):
    print(next(fib_gen))



# class CustomMeta(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['custom_attribute'] = 'Custom Value'
#         return super().__new__(cls, name, bases, attrs)

# class MyClass(metaclass=CustomMeta):
#     pass

# print(MyClass.custom_attribute)
