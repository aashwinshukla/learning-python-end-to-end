# class variable = shared among all instances of a class
#                  defined outside the construct
#                  allow you to share data among all objects created from that class

class Student:   #class
    
    class_year = 2024  # this is class variable which is accepted by the objects inside the object that is below and does not need to be declared in it 
    num_student = 0
    
    
    def __init__(self, name, age):      # }
        self.name = name                # }  object and the variable in it are called instance variable  
        self.age = age                  # }
        Student.num_student += 1
        
        
student1 = Student("Steve", 22)
student2 = Student("Luna", 20)
student3 = Student("Mark", 24)

print(student1.name)
print(student1.age)
print(Student.class_year)
# now even though the class_year is not in the object it still works
# best practice is to write Student.class_year rather than student1.class_year or any name on object.class_year 
# its because it do not care what object it is, if its inside main class it will print it

# now here we will add another class variable that is num_student = 0
# i also added Student.num_student += 1 instance inside the object to count number of student 

print(Student.num_student)
# it prints 3

print(f"My graduating class of {Student.class_year} has {Student.num_student} students in the class")