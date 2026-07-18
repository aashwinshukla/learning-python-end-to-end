#if statement

is_male = True

if is_male:
    print("you are a male")
else:
    print("you are not a male")
    
# this is the most basic example for if statement where we used bool values
#anything under if or else will be part of their function and if condition fulfill it will do as directed 

is_tall = True

if is_male or is_tall:
    printf("you are either male or tall or both")
else: 
    print("you are neither tall nor male")
    
#this is another any of using if statement by comparing and using more that one factors

#lets make it better 

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(in_tall):
    print("You are a short male ")
elif not(is_male) and is_tall:
    print("you are not a male and tall")
else:
    print("You are not a male and not tall ")
    
#this makes more cases possible
# we used elif that is else if to check other cases before going to default that is else


