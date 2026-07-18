# so lets make our own language 
# in our language all vowels turn into z 
# ie dog ---> dzg

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "z"
        else :
            translation = translation + letter 
    return translation
            
print(translate(input("Enter a phrase:")))