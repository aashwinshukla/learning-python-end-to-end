#looping or repeating a code till the condition is true 

i=1
while i<=10:
    print(i)
    i += 1
    
print("done with loop")


# below code shows how we can use loop to force someone to give input 
name = input("Enter your name")
while name == "":
    print("You did not enter your name ")
    name = input("Enter your name")

print(f"Hello {name}!")
