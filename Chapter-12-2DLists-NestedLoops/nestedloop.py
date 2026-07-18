number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8 ,9],
    [0]
    
]
#a normal list 

for row in number_grid:
    for col in number_grid:
        print(col)
        
#this is a nested loop where we are accessing all the element separetly 
#if we remove inside for loop all we get is number_grid back in our terminal
#but we want is each element thats where nested loop help us 
