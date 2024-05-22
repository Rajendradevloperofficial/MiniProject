#Question
'''
a = int(input("Enter first number : "))
b = int(input("Enter Second number : "))
c = int(input("Enter Third number : "))

m = a 
 if a < b :
    m = b
    if b < c :
        m = c
    
print("greatest : ", m)

'''
a=int(input("Enter the num of a"))
b=int(input("enter the num of b"))
c=int(input("Enter the num of c"))
m=a
if(m<b):
    m=b
if(m<c):
    m=c
print(m,"the largest num:")
print()
s1=int(input("Enter the num of s1:"))
s2=int(input("enter the num of s2:"))
s3=int(input("Enter the num of s3:"))
if(s1==s2 and s2==s3 and s3==s1):
    print("The tringle is Equilaterals")
if(s1==s2 and s2!=s3)or(s2==s3 and s3!=s1)or(s3==s1 and s1!=s2):
    print("The tringle is isoselese")
if(s1!=s2)and(s2!=s3)and(s3!=s1):
    print("The tringle is scalen")
