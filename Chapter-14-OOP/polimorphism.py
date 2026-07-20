# Polymorphism = Greek word that means to "have many forms on faces"
#               TWO WAYS TO ACHIEVE POLYMORPHISM
#               1. Inheritance = An object could be treated of the same type as a parent class
#               2. "Duck typing" = Object must have necessary attributes/method


from abc import abstractmethod

class Shape:
    @abstractmethod 
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius 
        
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2
    
class Pizza(Circle): 
    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.toppings = toppings

shapes = [Circle(4), Square(5), Pizza("pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()} cm square")
    
# now here our pizza is also a pizza, circle and a shape

# now "Duck typing"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self): 
        print("woof")
        
class Cat(Animal):
    def speak(self):
        print("meow")
        
class Car:
    alive = False
    
    def speak(self):
        print("honk")
    
        
animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

# we will get a error because car doesnt  have the speak attribute 

# but we can change .horn to .speak in the class Car 
#and then the code will run 