# Typecasting = process of converting a variable from one data type to another 
# str() int() bool() float()

name = "Maxwell"
age = 25
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# this will tell the type of variable

gpa = int(gpa)
print(gpa)

# now here gpa converts to int and return 3 instead of 3.2
#this applies to all variable 

#if you turn 

age = str(age)
print(age)
# the answer will be still the same but 
print(type(age))
# when you check type you will see that age has become string will 
# if a num is converted into string then it can cause problem when solving maths

