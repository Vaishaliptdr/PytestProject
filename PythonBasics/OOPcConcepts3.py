#Parameterized Constructor

class Calculator:
    num1 = 10  # Class variable
    num2 = 20

    def __init__(self,a,b):
        print("Parameterized Constructor")
        #Here firstNumber and secondNumber are instance variable
        self.firstNumber=a
        self.secondNumber=b


    def add(self):
        print("I will add two numbers")

    def summation(self):
        return self.firstNumber+self.secondNumber+self.num1


obj = Calculator(10,20)
obj1=Calculator(30,70)

print(obj.num1)
print(obj.num2)

obj.add()
print(obj.summation())
print(obj1.summation())

