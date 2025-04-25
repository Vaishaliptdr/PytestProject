#Default Constructor

class Calculator:

    num1=10                #Class variable
    num2=20

    def __init__(self):
        print("Default Constructor")


    def add(self):
        print("I will add two numbers")

obj=Calculator()

print(obj.num1)
print(obj.num2)

obj.add()
