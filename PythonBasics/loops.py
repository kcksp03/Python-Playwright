
greeting = "Good Morning"

a=4

if greeting == "Morning": # if condition:
    print("Condition matches")
    print("second line")
else:
    print("Condition does not match")

print("if else condition code is completed")

if greeting == "Good Morning": # if condition:
    print("Condition matches")
    print("second line")
else:
    print("Condition does not match")

print("if else condition code is completed")

if a>2: # if condition:
    print("Condition matches")
    print("second line")
else:
    print("Condition does not match")

print("if else condition code is completed")

# for loop

obj= [2, 3, 5, 7, 9]

for i in obj:
    print(i*2)

# sum of First 5 Natural numbers 1+2+3+4+5 = 15
# for (i=0;i<5;i++) ---> increment by 1
summation = 0
for j in range(1,6): # range(i,j) -> i to j+1
    summation = summation + j

print(summation)

# increment by 2 ??
print("****************************")
# k starts with 1
# print till 10
# increment by 2
for k in range(1,10,2):
    print(k)

print("************SKIPPING FIRST INDEX****************")
# if initial index is not given it will start iteration from 0 (default)
for m in range(10):
    print(m)
