from tester import modulos
class Parent():
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        z = self.num1 + self.num2
        print(z)
    
    def sub(self):
        z = self.num1 - self.num2
        print(z)
        
    def mul(self):
        z = self.num1 * self.num2
        print(z)

class Child(Parent):
    pass


#To run any method, first declare an instance of a class
#Then use that instance to call a method


test = Parent(45,5) #creating an instance for the parent class
#test1 = Child(23,3) #creating an instance for the child class

#test1.add()
#test.add()
#test.sub()
#test.mul()

test.modulos()
