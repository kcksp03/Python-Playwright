str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"

print(str[1]) #a
print(str[0:5]) #Rahul ---> get substring in python

print(str+str1) #concatenation
print(str3 in str) #substring check

var = str.split(".") #list created
print(var)
print(var[0])

str4 = "  great   "
print(str4.strip()) #to remove space
print(str4.lstrip()) # to remove space on the left
print(str4.rstrip()) # to remove space on the right
