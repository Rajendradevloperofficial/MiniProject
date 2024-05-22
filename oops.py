class demo():
    x=int(input("Enter the num of x:"))
    y=int(input("Enter the num of y:"))
    @classmethod
    def add(cls):
        print("Add=",cls.x+cls.y)
    @classmethod
    def sub(cls):
        print("Sub=",cls.x-cls.y)
obj=demo()
obj.add()
obj.sub()
    
#simple class & object program
class calc():
    x=int(input("Enter the value of x:"))
    y=int(input("Enter the value of y:"))
    @classmethod
    def add(cls):
            print("Add=",cls.x+cls.y)
    @classmethod    
    def sub(cls):
        print("Sub=",cls.x-cls.y)
obj=calc()
calc.add()
calc.sub()
        
#simple static method
class calc():
    @staticmethod
    def add():
        a=int(input("Enter the value of a:"))
        b=int(input("Enter the value of b:"))
        print("Add=",a+b)
    @staticmethod
    def sub():
        a=int(input("Enter the value of a:"))
        b=int(input("Enter the value of b:"))
        print("Sub=",a-b)
obj=calc()
obj.add()
obj.sub()
