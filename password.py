from tkinter import *
from tkinter.ttk import Combobox
from datetime import datetime
win=Tk()
win.state("zoomed")
win.configure(bg="powder blue")
win.resizable(width=False,height=False)
title=Label(win,text="Banking Automation",font=('arial',60,'bold','underline'),bg="powde")
title.pack()
date=Label(win,text=f"{datetime.now().date()}",font=('arial',15,'bold'),fg='green',bg="p")
date.place(relx=.85,rely=.12)

def mainscreen():
    frm=Frame(win)
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    frm.configure(bg="pink")
def new():
        frm.destroy()
        newscreen()
def fp():
        frm.destroy()
        fpscreen()
def login():
        frm.destroy()
        homescreen()
        lbl_acn=Label(frm,text="ACN",font=('arial',20,'bold'),bg="pink")
        lbl_acn.place(relx=.3,rely=.1)
        e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
        e_acn.place(relx=.4,rely=.1)
        e_acn.focus()
        lbl_pass=Label(frm,text="Pass",font=('arial',20,'bold'),bg="pink")
        lbl_pass.place(relx=.3,rely=.2)
        e_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show="*")
        e_pass.place(relx=.4,rely=.2)
        lgn_btn=Button(frm,command=login,text="login",font=('arial',20,'bold'),bd=5)
        lgn_btn.place(relx=.42,rely=.3)
        reset_btn=Button(frm,text="reset",font=('arial',20,'bold'),bd=5)
        reset_btn.place(relx=.53,rely=.3)
        fp_btn=Button(frm,command=fp,text="forgot password",font=('arial',20,'bold'),bd=5)
        fp_btn.place(relx=.4,rely=.4)

        new_btn=Button(frm,text="create new account",font=('arial',20,'bold'),bd=5,width=19)
        new_btn.place(relx=.38,rely=.5)
def newscreen():
        frm=Frame(win)
        frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
        frm.configure(bg="pink")
def back():
    frm.destroy()
    mainscreen()
    lbl_name=Label(frm,text="Name",font=('arial',20,'bold'),bg="pink")
    lbl_name.place(relx=.3,rely=.1)
    e_name=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_name.place(relx=.4,rely=.1)
    e_name.focus()
    lbl_pass=Label(frm,text="Pass",font=('arial',20,'bold'),bg="pink")
    lbl_pass.place(relx=.3,rely=.2)
    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show="*")
    e_pass.place(relx=.4,rely=.2)
    lbl_email=Label(frm,text="Email",font=('arial',20,'bold'),bg="pink")
    lbl_email.place(relx=.3,rely=.3)
    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=.4,rely=.3)
    lbl_mob=Label(frm,text="Mob",font=('arial',20,'bold'),bg="pink")
    lbl_mob.place(relx=.3,rely=.4)
    e_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mob.place(relx=.4,rely=.4)
    lbl_type=Label(frm,text="Type",font=('arial',20,'bold'),bg="pink")
    lbl_type.place(relx=.3,rely=.5)
    cb_type=Combobox(frm,values=['Saving','Current'],font=('arial',20,'bold'))
    cb_type.current(0)
    cb_type.place(relx=.4,rely=.5)
    open_btn=Button(frm,text="open",font=('arial',20,'bold'),bd=5)
    open_btn.place(relx=.42,rely=.6)
    reset_btn=Button(frm,text="reset",font=('arial',20,'bold'),bd=5)
    reset_btn.place(relx=.53,rely=.6)
    back_btn=Button(frm,text="back",font=('arial',20,'bold'),bd=5,command=back)
    back_btn.place(relx=0,rely=0)
def fpscreen():
    frm=Frame(win)
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    frm.configure(bg="pink")
def back():
    frm.destroy()
    mainscreen()
    back_btn=Button(frm,text="back",font=('arial',20,'bold'),bd=5,command=back)

    back_btn.place(relx=0,rely=0)
    lbl_acn=Label(frm,text="ACN",font=('arial',20,'bold'),bg="pink")
    lbl_acn.place(relx=.3,rely=.2)
    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=.4,rely=.2)
    e_acn.focus()
    lbl_email=Label(frm,text="Email",font=('arial',20,'bold'),bg="pink")
    lbl_email.place(relx=.3,rely=.3)
    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=.4,rely=.3)
    lbl_mob=Label(frm,text="Mob",font=('arial',20,'bold'),bg="pink")
    lbl_mob.place(relx=.3,rely=.4)
    e_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mob.place(relx=.4,rely=.4)
    rec_btn=Button(frm,text="recover",font=('arial',20,'bold'),bd=5)
    rec_btn.place(relx=.42,rely=.6)
    reset_btn=Button(frm,text="reset",font=('arial',20,'bold'),bd=5)
    reset_btn.place(relx=.53,rely=.6)
def homescreen():
    frm=Frame(win)
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    frm.configure(bg="pink")
def logout():
    frm.destroy()
    mainscreen()
def detailsscreen():
    ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
    ifrm.place(relx=.25,rely=.15,relwidth=.6,relheight=.6)
    ifrm.configure(bg="white")
    lbl=Label(ifrm,text="This is Account Details Screen",font=('arial',25,'bold'),bg="pink")
lbl.pack()
def depositscreen():

ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
ifrm.place(relx=.25,rely=.15,relwidth=.6,relheight=.6)
ifrm.configure(bg="white")
lbl=Label(ifrm,text="This is Deposit Screen",font=('arial',25,'bold'),bg="white")
lbl.pack()
def withdrawscreen():
ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
ifrm.place(relx=.25,rely=.15,relwidth=.6,relheight=.6)
ifrm.configure(bg="white")
lbl=Label(ifrm,text="This is withdraw Screen",font=('arial',25,'bold'),bg="white")
lbl.pack()
def historyscreen():
ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
ifrm.place(relx=.25,rely=.15,relwidth=.6,relheight=.6)
ifrm.configure(bg="white")

lbl=Label(ifrm,text="This is History Screen",font=('arial',25,'bold'),bg="white")
lbl.pack()
def transferscreen():
    ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
    ifrm.place(relx=.25,rely=.15,relwidth=.6,relheight=.6)
    ifrm.configure(bg="white")
    lbl=Label(ifrm,text="This is Transfer Screen",font=('arial',25,'bold'),bg="white")
    lbl.pack()
def updatescreen():
    ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
    ifrm.place(relx=.25,rely=.15,relwidth=.6,relheight=.6)
    ifrm.configure(bg="white")
    lbl=Label(ifrm,text="This is Update Profile Screen",font=('arial',25,'bold'),bg="pink")
    lbl.pack()
    lbl_wel=Label(frm,text="Welcome,",font=('arial',15,'bold'),bg="pink")
    lbl_wel.place(relx=0,rely=0)
    logout_btn=Button(frm,text="logout",font=('arial',15,'bold'),command=logout)
    logout_btn.place(relx=.93,rely=0)
    details_btn=Button(frm,text="Details",font=('arial',20,'bold'),width=12,command=deta)
    details_btn.place(relx=0,rely=.1)
    deposit_btn=Button(frm,command=depositscreen,text="Deposit",font=('arial',20,'bold'))
    deposit_btn.place(relx=0,rely=.2)
    withdraw_btn=Button(frm,command=withdrawscreen,text="Withdraw",font=('arial',20,'bol'))
    withdraw_btn.place(relx=0,rely=.3)
    profile_btn=Button(frm,command=updatescreen,text="Update profile",font=('arial',20,'b'))
    profile_btn.place(relx=0,rely=.4)
    history_btn=Button(frm,command=historyscreen,text="History",font=('arial',20,'bold'))
    history_btn.place(relx=0,rely=.5)
    trans_btn=Button(frm,command=transferscreen,text="Transfer",font=('arial',20,'bold'))
    trans_btn.place(relx=0,rely=.6)
mainscreen()
win.mainloop()
































