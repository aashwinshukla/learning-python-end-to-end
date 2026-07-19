# match case statement = similar to switch case in c 

def day_of_week(day): 
    match day:
        case 1:
            return "it is monday"
        case 2: 
            return "it is tuesday "
        case 3: 
            return " it is wednesday "
        case 4: 
            return "it is thursday"
        case 5: 
            return "it is friday"
        case 6: 
            return "it is saturday"
        case 7:
            return "it is sunday"
        case _:
            return "not valid input"
    


day = int(input("enter the number between 1-7 "))
print(day_of_week(day))