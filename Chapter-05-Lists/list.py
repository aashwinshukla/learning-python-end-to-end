#List = [] ordered and changeable . duplicate OK


friends = ["Kevin", "Karen", "Jim"]
#give your list a descriptive name then add your values or item in the []
#you can also put number or True/False

print(friends)


print(friends[0])
#we can also use indexing to call out the values inside list 
#0 will return kevin 
#we can put -1 inside friend[] and we will get Jim

print(friends[1:])
#this will print ['Karen', 'Jim']
#[1:] means 1 onwards 

friends2 = ["Bob", "Mike", "Clair", "Oscar", "Penelope"]
print(friends2[1:3])
# this will start from Mike and end at Clair That is 1 onward till before 3

friends2[1] = "Karen"
print(friends2[1])

# this will change Mike names to Karen 