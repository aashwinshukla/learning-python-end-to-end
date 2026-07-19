#anything in python saved in "" are called strings
#when storing numbers there is no need to use quotation mark


character_name = "mark" 
#character_name is the variable here which hold the value in ""

character_age = "26"  #or just 26 
#character_age in the variable here which hold the value in ""
#you can store any kind of number, from decimal to extremely big number easily in the variable


print("there was once a man name "+ character_name +".")
print("he was "+ character_age +" years old") 
#adding +variable+ inside the print will add the value of the variable automatically

character_name = "joe"
#you can write the same variable again in the code and give it a new value and it will print the same from down here

print("there was a man named "+character_name+".")  

#result
#there was once a man name mark.
#he was 26 years old
#there was a man named joe.

is_male = False
#this is a bool values which can also declared but True or False initial should be capital 

#three main data type 
#1. string
#2. number 
#3. bool


# modern or correct way of writing would be 

name = "Mike"
print(f"hello {name}!")

#here we used f string and {} to print the variable.