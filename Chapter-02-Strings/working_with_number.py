print(2)
#normal print statement taking integer
print(2.3547648)
#normal print statement taking decimal number
print(-12389.455)
#normal print statement taking negative number


print(2*3.14)
#can do basic arithmetics 

print(3*4+5)
#will do from left to right

print(3*(4+5))
#will solve parenthesis first

print(10%4)
#can you modulus function

my_num = 5
print(str(my_num))
#will change number into string...even though when code will run you will not be able to differentiate since it will still return 5

#print(my_num + "my favorite number")
#here we didnt changed to string thats why the code will not run 
#therefore in above cases str() is used


my_num=-5
print(abs(my_num))
#taking absolute value 

print(pow(4, 6))
#giving answer to 4 power 6 or 4^6

print(max(4, 6))
print(min(4, 6))
#above will give max min value from the set they have that is 6 and 4 respectively
 
print(round(3.2))
#round to 3
print(round(3.7))
#round to 4


from math import *
#math module
#will give more function to use

print(floor(3.7))
#no matter whats the value it will give lowermost value that is here 3

print(ceil(3.1))
#no matter whats the value it will give uppermost value that is here 4

print(sqrt(36))
#will give square root of 36 that is 6

#etc.....

#another thing you can do with imported math file is
import math
print(math.pi)
print(math.e)
# and get value of pi and e 
# when used import math 
# always write math.sqrt(), math.ceil(), math.floor(), etc
# you cant just write ceil() like we did using from math import


import math 
radius = float(input("Enter radius of the circle"))
circumference = 2 * math.pi * radius 

print(f"the circumference of the circle is {round(circumference, 2)}cm")

# above is a small use of maths 