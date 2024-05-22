from tkinter import*
cal=Tk()
cal.title("Calculator")
operator=" "
text_input=StringVar()
txt_display=Entry(cal,font=("arial",20,"bold"),textvariable=text_input,bd=30,insertwidth=3,bg="green",justify="right").grid(columnspan=4)

button7=Button(cal,padx="16",pady="16",bd=8,fg="black",font=("arial",20,"bold"),text="7",command=lambda:btnclik(7))
button7.grid(row=1,column=0)
button8=Button(cal,padx="16",pady="16",bd=8,fg="black",font=("arial",20,"bold"),text="8",command=lambda:btnclik(8))
button8.grid(row=1,column=1)
button9=Button(cal,padx="16",pady="16",bd=8,fg="black",font=("arial",20,"bold"),text="9",command=lambda:btnclik(9))
button9.grid(row=1,column=2)
button_add=Button(cal,padx="16",pady="16",bd=8,fg="black",font=("arial",20,"bold"),text="+",command=lambda:btnclik("+"))
button_add.grid(row=1,column=3)

button4= Button(cal,padx="16",pady="16",bd=8,fg="black",font=("arial",20,"bold"),text="4",command=lambda:btnclik(4))
button4.grid(row=2,column=0)
button5=Button(cal,padx="16",pady="16",bd=8,fg="black",font=("arial",20,"bold"),text="5",command=lambda:btnclik(5))
button5.grid(row=2,column=1)
button6=Button(cal,padx="16",pady="16",bd=8,fg="black",font=("arial",20,"bold"),text="6",command=lambda:btnclik(6))
button6.grid(row=2,column=2)
button_sub=Button(cal,padx="16",pady="16",bd=8,fg="black",font=("arial",20,"bold"),text="-",command=lambda:btnclik("-"))
button_sub.grid(row=2,column=3)

button1=Button(cal,padx="16",pady="16",bd=8,fg="black",font=("arial",20,"bold"),text="1",command=lambda:btnclik(1))
button1.grid(row=3,column=0)
button2=Button(cal,padx="16",pady="16",bd=8,fg="black",font=("arial",20,"bold"),text="2",command=lambda:btnclik(2))
button2.grid(row=3,column=1)
button3=Button(cal,padx="16",pady="16",bd=8,fg="black",font=("arial",20,"bold"),text="3",command=lambda:btnclik(3))
button3.grid(row=3,column=2)
button_div=Button(cal,padx="16",pady="16",bd=8,fg="black",font=("arial",20,"bold"),text="/",command=lambda:btnclik("/"))
button_div.grid(row=3,column=3)






button0=Button(cal,padx="16",pady="16",bd=8,fg="black",font=("arial",20,"bold"),text="0",command=lambda:btnclik(0))
button0.grid(row=4,column=0)
buttonclr=Button(cal,padx="16",pady="16",bd=8,fg="black",font=("arial",20,"bold"),text="C",command=lambda:clr())
buttonclr.grid(row=4,column=1)
buttonEqul=Button(cal,padx="16",pady="16",bd=8,fg="black",font=("arial",20,"bold"),text="=",command=lambda:Equl())
buttonEqul.grid(row=4,column=2)
button_mul=Button(cal,padx="16",pady="16",bd=8,fg="black",font=("arial",20,"bold"),text="*",command=lambda:btnclik("*"))
button_mul.grid(row=4,column=3)



def btnclik(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
    
def clr():
    global operator
    operator=" "
    text_input.set(" ")

def Equl():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=" "
