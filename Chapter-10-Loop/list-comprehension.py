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

