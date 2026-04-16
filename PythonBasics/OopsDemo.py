# classes are user defined blueprint or prototype
# sum, multiplication, addition, constant
# methods, class variables, instance variables, constructor etc.
# objects for you classes.

# self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# constructor name should be __init__
# new keyword is not required when you create object

class Calculator:
    num = 100
    # class variable - constant no matter the number of objects created

    # constructor ---> is a method that is automatically called
    # when you create an object for any class
    # number of variables in object == number of variables in constructor
    # default constructor
    # self is default added in python
    def __init__(self, a, b): #instance variable a, b
        #self == object
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as a method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num



# create an object
obj = Calculator(2, 3) #syntex to create an object in python
# get a method
obj.getData()
print(obj.Summation())

obj1 = Calculator(4,5)
obj1.getData()
print(obj1.Summation())



