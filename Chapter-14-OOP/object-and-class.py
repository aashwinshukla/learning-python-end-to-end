# object = a "bundle" of related attributes (variable) and methods (functions)
#          ex. phone, cup, book
#          you need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object 

from carClass import Car


# class Car: 
#    def __init__(self, model, year, color, for_sale):
#        self.model = model 
#        self.year = year 
#        self.color = color
#        self.for_sale = for_sale
        
car1 = Car("mustang", 2024, "red", False)
car2 = Car("Ferrari", 2004, "red", True)
car3 = Car("Charger", 2026, "yellow", True)

print(car1)
# this will give us memory address of the Car object but we want to get specific attribute from it 

print(car1.model)
# the period ( . ) known as attribute access operator 
print(car2.year)
print(car3.color)
print(car1.for_sale)

# now if change car1 to car 2 or 3 in print statement is will print their specific attributes 

# now we have commented the Car class and made a new file called carClass.py
# and we will import the file at top 
# now we can still run the program even though the class is in the other file 

car1.drive()
car1.stop()

#we created methods in carClass.py  which are def drive(self) and def stop(self)
#and thats what we printed using above statement 

car1.describe()
car2.describe()
cae3,describe()
# we created another method called def describe(self)
# when we print here we get all knowledge about the car

