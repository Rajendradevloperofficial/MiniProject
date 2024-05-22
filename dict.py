'''

def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
f1=fibonacci()
    
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))

'''
#sort A list without using a sort keyword
'''

list1=[12,6,5,13,40,1,4,2,3]
n= len(list1)
for i in range(n):
    for j in range(i+1,n):
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
print(list1)
print(n)
'''
# write A Code To Check Whether A String is PALINDROME Or not?

"""
a='nitin'
if a==a[::-1]:
    print("Yes the is palindrom ")
else:
    print("No")


# alternative way
s="nitin"
n=len(s)
x=0
for i in range(n):
    if s[i]!= s[n-i-1]:
        x=1
        break
if x==0:
    print("yes is palindrom")
else:
    print("no")

"""
# sort a dictionary /by using dict comprehension
'''
dict1={575:"Apple",876:"Mango",132:"Grapes",782:"Banana"}
d=sorted(dict1.keys())
dict2={}
for i in d:
    dict2[i]=dict1[i]
print(dict2)

 #values 

dict1={575:"Apple",876:"Mango",132:"Grapes",782:"Banana"}
dict2={key:value for key,value in sorted(dict1.items(),key=lambda x: x[1])}
print(dict2)

#Print all pairs with given sum
list1=[8,7,2,5,3,1]
n=len(list1)
k=10
for i in range(n):
    for j in range(i+1,n):
        if(list1[i]+list1[j])==k:
            print(list1[i],list1[j])
            
  
#Fibonacci Using Recursion
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
nterms=int(input("How many terms?"))
if nterms <=0:
    print("Plese enter a postive integer")
else:
    for i in range(nterms):
        print(recur_fibo(i))
 
#find the output
#input: "the sky is blue"
#output: "bule is sky the"
s="the sky is blue"
l=s.split()
l=l[::-1]
l=" ".join(l)
print(l)
 

# find max repeated charcter in a string  time Complexity should be lessar than 0(n2)
s="iitinytnnhhn"
ch={}
for i in s:
    if i in ch:
        ch[i]+=1
    else:
        ch[i]=1
#print(ch)
max_char=max(ch,key=ch.get)
print(max_char)
        
   '''
list1=[10,50,20,56,100]
maximum=list1[0]
minimum=list1[0]
for i in list1:
    if i > maximum:
        maximum=i
    if i < minimum:
        minimum=1
print("maximum",maximum)
print("minimum",minimum)



question = how to given string  statment  in reverse without useing revesre method and slicing
soulution
d="I'm Rajendra Kumar Gupta Now I'm Training in Python Devloper in ducat "
b=d.split()
c=""

for i in b:
          c=i+" "+c
          print(c)