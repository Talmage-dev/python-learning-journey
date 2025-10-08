name = "Bro Code"
phone_number = "021-3456789"

length = len(name) #length method, how long is the string
result1 = name.find("o") #find method, finds something within the string (first one it finds if multiple)
result2 = name.rfind("o") #rfind method, finds something within the string (last one it minds if multiple)
name1 = name.capitalize() #capitalize method, capitalizes the first letter
name2 = name.upper() #upper method, changes all characters to upper case
name3 = name.lower() #lower method, changes all characters to lower case
result3 = name.isdigit() # isdigit method, returns True or Flase if string contains only digits
result4 = name.isalpha() # isalpha method, returns True or False if string contains only alphabetical characters
result5 = phone_number.count("-") #count method, counts how many specified character are in that string
phone_number = phone_number.replace("-", " ") #replace method, replaces specified character with another specified character
# print(help(str)) will bring up a list and explainations of all string methods.

print(length)
print(result1)
print(result2)
print(name1)
print(name2)
print(name3)
print(result3)
print(result4)
print(result5)
print(phone_number)