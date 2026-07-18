def say_hi():
    print("hello User ")
    
# def gives program idea that we want to use function
# after writing function name everything under it will be part of the function
# we added print("Hello User") inside the function , if you run the code nothing will happen 
#because you need to call the function first 

say_hi()

# we can also add parameter inside the ( ) of the function 

def user(name):
    print("hello "+name)

user("Mike")
user("Steve")

#now here this will print mike and steve name while running the code
#if you know c it is pretty similar 
# you can add as many parameters you want
