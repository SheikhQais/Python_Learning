st1 = '''Acha tou kya chal raha ha ajj kal?
ma ne sirf itna kehna tha k
bhanss ki tang life ki lagii pariii ha
aur ma hoon jo serious hi nhi ho raha hoon'''

print(st1[15:]) #String Slicing

print(st1[-33:] +"\"And lenth of string is\"", len(st1)) #len is function to get length of string
print("\n")
print(st1.lower())  #Lower case all characters in string
print("\n")
print(st1.upper())  #upper case all characters in string
print("\n")
print(st1.strip())  #exclude the white spaces in the string from start and last
print("\n")
print(st1.replace("H", "J"))    #method replaces a string with another string
print("\n")
print(st1.split(","))   #method splits the string into substrings if it finds instances of the separator
print("\n")
# Concatenation in Strings
a = "Hello"
b = "Aleena"
c = a+" "+b
print(c)
print("\n")
# format method in string
a = "Hello"
b = "{} Aleena"
print(b.format(a))
print("\n")
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
print("\n")
txt = "We are the so-called \"Vikings\" from the north."
print(txt.casefold())
print("\n")
print(txt.isalpha())