# formate for print()

price = 3.14243

print(f"price is {price:.2f}")
# :.2f this will round decimal to 2 places

print(f"price is {price:10}")
# :10 this will add 10 spaces in the print including the price 
#result = price is 3.14
#         price is    3.14243

print(f"price is {price:010}")
# :010 we added 0 before 10 that will make all the spaces in previous result to show as zero 

print(f"price is {price:<10}")
# when used < the price will be left justified 
print(f"price is {price:>10}")
# when used > the price will be right justified or default as :10
print(f"price is {price:^10}")
#when used ^ the price is centered 

print(f"price is {price:+}")
# when used + the positive number will have a + infront of them 
print(f"price is {price: }")
# when left empty after : the price will have a single gap infront 
print(f"price is {price:,}")
# using ,  we can create a thousand place comma 
#we can also add
print(f"price is {price:,.2f}")
#this we will do two things at the sme time ie thousand place comma and two decimal place round off

