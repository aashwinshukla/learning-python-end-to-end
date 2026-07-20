import random 
import string 

chars = " " + string.punctuation + string.digits + string.ascii_letters
#above char will give us a random string 
# print(chars)
# result = 
#!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

chars = list(chars)
key = chars.copy()
# now we will have list of the element from that string

random.shuffle(key)


print(f"chars : {chars}")
print(f"key   : {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    
print(f"original message : {plain_text}")
print(f"encrypted message: {cipher_text}")

#DECRYPTION
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    
print(f"original message : {plain_text}")
print(f"encrypted message: {cipher_text}")

