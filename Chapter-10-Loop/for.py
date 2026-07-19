for letter in "Python":
    print(letter)
    
# here for loop is printing out all the letters of Python on different line 

friends = ["jim", "luna", "steve"]
for friend in friends:
    print(friend)
    
#here each name of friend is getting printed on different lines

for index in range(10):
    print(index)
    
# here 0 to 9 all number get printed
# if you put range(3, 10) you will get 
# 3
# 4
# 5
# 6
# 7
# 8 
# 9 
# you can also write starting and ending point 
#for index in range(1,11):
#for index in range(1, 11, 2):
# 2 means it will jump by 2 like the code will return 1 3 5.....
#we can use reverse instead of range and we will have reverse countdown
 

for index in range(len(friends)):
    print(friends[index])
    
# all the above are mostly looping in an array

# you can add if function or other inside of for function or vice versa make things work better

# we can use continue keyword to skip a value return 
# we can also use break keyword to finish the loop 

#we can do something with this 

import time

my_time = int(input("Enter the time in seconds "))

for x in range(0, my_time):
    time.sleep(1)
print("TIMES UPP")

#lets say my input is 5 sec then after 5 sec i will get times up 

