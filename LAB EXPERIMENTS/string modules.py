import string
 
print("Lowercase letters:", string.ascii_lowercase)
print("Uppercase letters:", string.ascii_uppercase)
print("Digits           :", string.digits)
print("Punctuation      :", string.punctuation)
 
s = "welcome to python programming"
print("Capitalize :", s.capitalize())
print("Title      :", string.capwords(s))
print("Upper      :", s.upper())
print("Replace    :", s.replace("python", "Python"))
print("Split      :", s.split())
print("Count of o :", s.count("o"))
print("Find 'to'  :", s.find("to"))
