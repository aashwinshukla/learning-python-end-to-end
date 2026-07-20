# Inheritance = Allows a class to inherit attributes and methods from another class
#               helps with code reusability and extensibility
#               class Child(Parent)

class Animal: 
    def __init__ (self, name): 
        self.name = name
        self.is_alive = True
        
    def eat(self): 
        print(f"{self.name} is eating")
    
    def sleep(self): 
        print(f"{self.name} is sleeping")
        
class Dog(Animal):      #taking from Animal
    pass

class Cat(Animal):      #taking from Animal
    pass

class Mouse(Animal):    #taking from Animal
    pass

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.sleep()
dog.eat()


# now here to our advantage we dont have to write the complete object inside the Animal class
# into all the new class we made called Dog , Cat , Mouse 
# all we typed was pass and it still worked because it inherited the Animal class

 