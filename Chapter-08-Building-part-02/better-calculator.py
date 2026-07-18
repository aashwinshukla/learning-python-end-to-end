def calculator(num1, op, num2):
    
    if op == "+":
        result = num1 + num2
        print(result)
    elif op =="-":
        result = num1- num2
        print(result)
    elif op == "*":
        result = num1 * num2
        print(result)
    elif op == "/":
        result = num1 / num2
        print(result)
    else:
        print("operator is wrong, try again! ")
        
    return result



num1 = float(input("enter first number:"))
op = input("enter an operator:")
num2 = float(input("enter second number:"))

calculator(num1, op, num2)


