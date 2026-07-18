print("hello world")
#normal string and print statement

print("hello\"world")
#here \ helped the program to know that what ever comes after the \ it should be printed as well
#hello"world

#otherwise
#print("hello"world")
#here the program thinks string ended after hello because of " and no \"


phrase = "Hello World"
#here variable has a string 
print(phrase)
#this will print the phrase

print(phrase + " nice to meet you ")
#we can do concatenation where variable will be connected with the extra sting we have written inside the print

print(phrase.lower())
#everything will be printed in lower case
print(phrase.upper())
#everything will be printed in upper case

print(phrase.isupper())
#using isupper() will give bool value after checking wether the phrase is completely upper case or not
print(phrase.upper().isupper())
#this will run the first case to make everything upper and then run second case to give true as answer
  