#Inheritance

from PythonBasics.OOPcConcepts3 import Calculator


class ChildClass(Calculator):

    x=6
    def __init__(self):
        Calculator.__init__(self,5,4)

    def total(self):
        return self.x+self.num1+self.summation()

Obj=ChildClass()
print(Obj.total())