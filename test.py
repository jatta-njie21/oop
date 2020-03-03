class Oop():
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        z = self.num1 + self.num2
        print(z)
    
    def sub(self):
        z = self.num1 - self.num2
        print(z)


test = Oop(45,5)

test.add()
test.sub()