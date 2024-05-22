from tkinter import *
root=Tk()
root.title("Registration Form")
root.geometry("600x600")
lable_0=Label(root,text="Registration Form",width=20,font=("bold",20),fg="red")     
lable_0.place(x=90,y=60)
lable_1=Label(root,text=" Full Name:",width=20,font=("bold",10),fg="blue")
lable_1.place(x=80,y=130)
entry_1=Entry(root)
entry_1.place(x=240,y=130)
lable_2=Label(root,text="Email Id:",width=20,font=("bold",10),fg="blue")
lable_2.place(x=68,y=180)
entry_2=Entry(root)
entry_2.place(x=240,y=180)
lable_3=Label(root,text="Gender",width=20,font=("bold",10),fg="blue")
lable_3.place(x=70,y=230)

var=IntVar()
Radiobutton(root,text="Male",padx=7,variable=var,value=1).place(x=235,y=230)
Radiobutton(root,text="Female",padx=25,variable=var,value=2).place(x=290,y=230)




#root.mainloop()

#Regular Expression in python: (REGEX)
'''
import re
re.match()
re.search()
re.findall()
re.compile()
re.split()

#Regular Expression pattern:-
#str1="/^[A-Za-z0-9]$/"
import re
def main():
    phone_no="""9874561245 this  is my phone number please
    my contact number python is multipurpose language ,
    python is interpreter
    """
    num=re.split(",",phone_no)
    print("Phone NO:",num)
main()

'''
'''
import re
def password():
    password=input("Enter the correct password: ")
    flag=0
    while True:
        
        if(len(password)<8):
            flag=-1
            break
        elif not re.search("[a-z]",password):
        
            flag=-1
            break
        elif not re.search("[A-Z]",password):
            flag=-1
            break
        elif not re.search("[0-9]",password):
            flag=-1
            break
        elif not re.search("[_@$]",password):
            flag=-1
            break
        elif not re.search("[\s]",password):
            flag=-1
            break
        else:
            flag=0
            print("valid password")
            break
    if flag ==-1:
    
        print("password not valid")
password()
'''

'''
def my_decorator(func):
    
    def inner(a,b):
        if b>a:
            a,b=b,a
        return func(a,b)
    return inner
@my_decorator
def div(a,b):
    
    print("Div=",a/b)
div(4,2)
div(2,4)
'''
'''
#simple class & object program
class Student():
    def add():
        a=10
        b=20
        c=a+b
        print("Sum of two object=",c)
sum1=Student()
Student.add()
class Student():
    
    def sub():
        a=100
        b=20
        c=a-b
        print("Subtraction=",c)
sum2=Student()
Student.sub()
def decorator(func):
    def inner(a,b):
        if(b>a):
            a,b=b,a
        return func(a,b)
    return inner
@decorator
def div (a,b):
    print ('div=',a/b)
div(4,2)
div(2,4)
'''
class student():
    def get (self):
        self.a=int(input("enter the any num:"))
        self.b=int(input("enter the any num:"))
        self.c=self.a+self.b
    def set (self):
        print("Sum of tow num:",self.c)
obj=student()
obj.get()
obj.set()
obj1=student()
obj1.get()
obj1.set()
#constructor Method
class calc():
    def __init__(self):
        self.x=int(input("Enter the value of a :"))
        self.y=int(input("Enter the vale of b :"))
    def add(self):
        self.c=self.x+ self.y
        print("Add=",self.c)
obj=calc()
obj.add()






















































































