num1 = input("Enter a number:")
num2 = input("Enter another number:")

result = float(num1) + float(num2)
#here the float function will change the string of number into a float number that is it can hold decimal values
#you can also write int but it will only allow integer and not decimal.
#without these function it will treat them like strings 
#if you would input the num1 as 1 and num2 as 9 then result would be 19 without the function

print(result)

#later we will make a much more complicated calculator