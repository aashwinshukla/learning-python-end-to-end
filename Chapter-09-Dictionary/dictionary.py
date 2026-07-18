monthConversion = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
        }

# we have created different keys representing different value in our dictionary 

print(monthConversion["Nov"])
#here we can print value of key by writing the key in the []

#other ways are
print(monthConversion.get("Dec", "not a valid key "))
#here we have also declared a default as well 
#key can be number as well 

