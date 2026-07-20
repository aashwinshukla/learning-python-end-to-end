# class methods = allow operations related to the class itself
#                 take (cls) as the first parameter, which represents the class itself

class Student:
    
    count = 0  # class method to deal with this 
    total_gpa = 0
    
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    #INSTANCE METHOD
    def get_info(self): 
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls): 
        return f"total no. of students {cls.count}"

    @classmethod
    def get_average_gpa(cls): 
        if cls.count == 0: 
            return 0
        else: 
            return f"{cls.total_gpa/ cls.count}"
        
    
student1 = Student("Steve", 3.2)
student2 = Student("Mark", 2.0)
student3 = Student("Luna", 4.0)

print(Student.get_count())
print(Student.get_average_gpa())

