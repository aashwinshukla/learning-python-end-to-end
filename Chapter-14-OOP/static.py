# Static methods = A method that belongs to a class rather than any object from that class(instance)
#                  usually used for general utility functions

#Instance method = Best for operations on instances of the class (object)
#Static method = Best for utility function that do not need access to class data 

class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def getinfo(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position): 
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position
    
employee1 = Employee("Steve", "Manager")
employee2 = Employee("Mark", "Cook")
employee3 = Employee("Joe", "Cashier")

print(Employee.is_valid_position("Cook"))  #static method only have to access class and no need to access any object    
print(employee1.getinfo())  #}
print(employee2.getinfo())  #}  instance method 
print(employee3.getinfo())  #}

