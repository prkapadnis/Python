mystring = "My Name is Pratik"
print(mystring)
# Slicing
print(mystring[0:]) # Starting to the End
print(mystring[:5]) #Starting upto specified index 
print(mystring[0:6])  #From specified starting index to specified ending index  
print(mystring[::-1]) # Printitng the reversea a string
print(mystring[0:-1:2]) # printing staring to the end with gap of 2 

#String Function
print(mystring.count('a'))
print(mystring.capitalize())
print(mystring.lower())
print(mystring.upper())
print(mystring.replace("Pratik", "PrKapadnis"))
mystring = mystring.replace("Pratik", "PrKapadnis")
print(mystring)
print(mystring.find("PrKapadnis"))
mystring = "".join(mystring)
print(mystring)
print(f"The length of string is {len(mystring)}")
