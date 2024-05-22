'''Method Overloading & Method Overriding in Python :-
Method Overloading:-

(1) Method Overloading is one concept of Polymorphism.
(2) It comes under the elements of OOPs.
(3) It is worked in the same method names and different arguments.
(4) Arguments different will be based on a number of arguments & types 
of arguments.
'''
class Area():
    def find_area(self,a=None,b=None):
        if(a!=None and b!=None):
            print("Area of Rectangle=",a*b)
        elif(a!=None):
            print("Area of Square=",a*a)
        else:
            print("Nothing to find")
obj=Area()
obj.find_area()
obj.find_area(2)
obj.find_area(2,4)


'''
Method Overriding:-

(1) Method Overriding is also one concept of Polymorphism.
(2) It comes under the elements of OOPs.
(3) Method Overriding is the method having the same name with the         same arguments.
(4) It is implemented with inheritance.
(4) It is mostly used for memory reducing processes.
'''
class A():
    def showData(self):
        print("I'm in A() Class..")

class B(A):
    def showData(self):
        print("I'm in B() Class..")




obj1=A()
obj1.showData()

obj2=B()
obj2.showData()


















                  
