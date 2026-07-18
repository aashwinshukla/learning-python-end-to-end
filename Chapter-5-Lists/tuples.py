# tuple is similar to list but once declared cannot be changed
# tuple are with () and list are with []


coordinates = (4, 5)

print(coordinates[1])
# we will get 5

coordinates[1]= 10
# we try to change index 1 

print(coordinates[1])
#code will throw an error since tuple cant be changed

coordinates = [(4, 5), (6, 7), (67, 69)]
# you can make list of tuples as shown above 

