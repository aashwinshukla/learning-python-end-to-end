# variable scope is where a variable is visible and accessible 
# scope resolution = (LEGB) local -> Enclosed -> Global -> Build-in

def func1(): 
    x = 1
    print(x)

def func2(): 
    x = 2
    print(x)
    
func1()
func2()

#here we have x variable inside the function and both function ignores each others x
# this is local 

#now for enclosed

def func1(): 
    x = 1
    
    
    def func2(): 
        print(x)
    func2()
    
func1()

# we removed the x = 2 from func2 therefore it will check enclosed variable that is x = 1
# and print that 

# now in the global 

def func1():
    print(x)

def func2():
    print(x)
    
x = 3
    
func1()
func2()

# both function take x = 3 which is outside of both the functions 

# now for build-in

from math import e

def func1(): 
    print(e)
    
func1()
    
#here it will print 2.71 and so on but if we add

from math import e

def func1(): 
    print(e)
    
e = 3

func1()

#now the python will prioritize x = 3 because it is a global variable 

# scope resolution = (LEGB) local -> Enclosed -> Global -> Build-in