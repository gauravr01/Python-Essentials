# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def start_engine(self):
#         print("Engine started.")

# my_car = Car("Toyota", "Camry")
# print(my_car.make)  # Output: Toyota
# print(my_car.model)  # Output: Camry
# my_car.start_engine()  # Output: Engine started.


#Encapsulaltion
# class BankAccount:
#     def __init__(self):
#         self.balance = 0

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient funds.")

#     def get_balance(self):
#         return self.balance

# my_account = BankAccount()
# my_account.deposit(100)
# my_account.withdraw(50)
# print(my_account.get_balance())  # Output: 50
# In this example, the BankAccount class encapsulates the balance attribute 
# and methods to deposit, withdraw, and get the account balance. The internal 
# implementation details are hidden, and the user interacts with the class
#  through defined methods.



#Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         raise NotImplementedError("Subclass must implement this method.")

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# dog = Dog("Fido")
# cat = Cat("Whiskers")
# print(dog.speak())  # Output: Woof!
# print(cat.speak())  # Output: Meow!


#Abstraction
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# dog = Dog()
# cat = Cat()
# print(dog.speak())  # Output: Woof!
# print(cat.speak())  # Output: Meow!


# ##Composition
# class Engine:
#     def start(self):
#         print("Engine started.")

# class Car:
#     def __init__(self):
#         self.engine = Engine()

#     def start_engine(self):
#         self.engine.start()

# my_car = Car()
# my_car.start_engine()  # Output: Engine started.


#Polymorphism
#overloading
class MathOperations:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

# Create an object
math = MathOperations()

# Method overloading with different parameters
result1 = math.add(2, 3)
result2 = math.add(2, 3, 4)

print(result1)  # Output: 5
print(result2)  # Output: 9

#overriding
class Animal:
    def make_sound(self):
        print("Generic animal sound.")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Create objects
animal = Animal()
dog = Dog()
cat = Cat()

# Method overriding
animal.make_sound()  # Output: Generic animal sound.
dog.make_sound()  # Output: Woof!
cat.make_sound()  # Output: Meow!
