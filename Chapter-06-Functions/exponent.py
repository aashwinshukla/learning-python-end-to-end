print(2**3)
#this means 2^3

def raise_to_power(base_num, pow_num): 
    result = 1
    for index in range (pow_num): 
        result *= base_num
    return result

print(raise_to_power(2, 3))

#the above loop will loop the multiplication pow_num times creating a exponent formula

# another basic way of writing exponents is 

friends = 5
friends **= 2 # or
friends = friends ** 2
# this means friends raise to power 2