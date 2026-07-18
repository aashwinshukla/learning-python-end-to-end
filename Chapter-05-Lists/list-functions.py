lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "JIm", "Oscar", "Toby"]

friends.extend(lucky_numbers)
#this will extend the friends list and add the lucky_number list to it as well

friends.append(creed)
# this will add creed at the end of the list friends 

friends.insert(1, "Kelly")
#this will add Kelly at index 1 moving other to right

friends.remove("Jim")
# this will remove jim from the list

friends.clear()
#this will empty the list

friends.pop()
#this will randomly pop a element off the list

friends.index("Kevin")
# this helps find if an element is on the list or not

friends.count("Jim")
#this will count the number of time Jim element came in the list

friends.sort()
#this will sort all the element in alphabetical order 
#if there are numbers then ascending order

friends.reverse()
#this will reverse the list

friends2 = friends.copy()
#copies the list

print(friends)


