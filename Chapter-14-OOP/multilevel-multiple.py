# Multiple Inheritance = inheritance from more than one parent class C(A, B)
# Multilevel inheritance = inherit from a parent which inherits from another parent C(B) <- B(A) <- A

class Prey: 
    def flee(self): 
        print("this animal is fleeing")

class Predator:
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