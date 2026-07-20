# Multiple Inheritance = inheritance from more than one parent class C(A, B)
# Multilevel inheritance = inherit from a parent which inherits from another parent C(B) <- B(A) <- A


class Animal: 
    def eat(self): 
        print(" this animal  is eating")
        
        
class Prey(Animal): 
    def flee(self): 
        print("this animal is fleeing")

class Predator(Animal):
    def hunt(self): 
        print("this animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey ,Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()


# here is we put .flee with hawk and .hunt with rabbit it will not work since those attributes do not belong to them whereas fish can do both 
# this is multiple inheritance

# now to show multi level i added animal class with def eat(self)
# and gave it to prey and predator 
# now the following code should work because of multilevel inheritance

rabbit.eat()
hawk.eat()
fish.eat()

#this is like getting inheritance from parents that belonged to grandparents 

