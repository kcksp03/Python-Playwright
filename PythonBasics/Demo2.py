
# List


# list isa data type and should have []
# it can contain variables with different data types

values = [1, 2,"rahul", 4, 5]

print(values[0]) # first value in the list

print(values[3]) # 4th value in the list

print(values[-1]) # last value in the list

print(values[1:3])
# 2nd value till the 4th value in the list except the 4th
# it will print "2 rahul"

# insert is add a variable in the middle of the list
values.insert(3, "shetty")
print (values)

# append is to add a variable to the end of the list
values.append("End")
print (values)

# update 3rd variable in the list
values[2] = "RAHUL"
print (values)

# delete variable in the list
del values[0]
print (values)

# Tuple
# immutable

val = (1, 2,"rahul", 4, 5)

print (val)

# val[2] = "RAHUL" --- this throws an error as a tuple in immutable

# Dictionary

dic = {"a":2, 4:"bcd", "c":"Hello world"}

print(dic[4])
print(dic["c"])

#

dict = {}

dict["firstname"] = "Rahul"

dict["lastname"] = "shetty"

dict["gender"] = "Male"

print(dict)
print(dict["lastname"])