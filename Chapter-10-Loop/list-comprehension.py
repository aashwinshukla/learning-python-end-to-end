#list comprehension = a concise way to create lists in python 
#                     compact and easier to read than traditional loops 

# traditional 

double = []
for x in range(1, 11): 
    double.append(x*2)
    
print(double)

# list comprehension 
# [expression for value in iterable if condition]

doubles = [x * 2 for x in range(1, 11)]

print(doubles)

# can also be used in string 

fruits = ["apple", "orange", "coconut", "pineapple"]
fruits = [fruit.upper() for fruit in fruits ]
print(fruits)

#OR simpler 

fruits = [fruit.upper() for fruit in ["apple", "orange", "coconut", "pineapple"] ]
print(fruits)


# we are yet to see conditions so lets get to them 

number = [1, -2, 3, -4, 5, -6]
posi_num = [num for num in number if num>=0]
neg_num = [num for num in number if num<0]


print(posi_num)
print(neg_num)
#result = [1, 3, 5]
#         [-2, -4, -6]
