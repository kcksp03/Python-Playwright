file = open('test.txt')

# print(file.read()) #read all the contents of the file
# print(file.read(2)) #reads only 2 characters

# read one single line at a time readLine()
#print(file.readline())
#print(file.readline())

# interview question
# print line by line using readLine method
#line = file.readline()
#while line!="":
#    print (line)
#    line = file.readline()

for line in file.readlines():
    print(line)

file.close()