# if you write a code like below

number = int(input("Enter a number : "))
#this converts input into number as we already learned
print(number)
#this prints out the input 
#the problem is if someone input alphabets the program will throw error and we dont want that

try: 
    number = int(input("Enter a number : "))
    print(number)
except:
    print("invalid Input")
          

# the code above will try something and if doesnt make any sense then it will do what is in except 
