from tkinter import *
import re
import pandas as pd
import openpyxl as op
a=[]
b=[]
def reg():
    count=0
    d=0
    count1=0
    special="""!@#$%^&*()-+?_'"=,<>/"""
    u= username.get()
    p= password.get()
    if u.count('@')>=1 and u.count('.')>=1:
        if u.index('@')>u.index('.') or u[0]=='@':
            count=1
        if (u.index('@')+1)==u.index('.'):
            count=1
        if u[0].isnumeric() or any(c in special for c in u[0]) :
            count=1
        if len(p)<5 or len(p)>16:
            count1=1
        regex=("^(?=.*[a-z])(?=."+"*[A-Z])(?=.*\\d)"+"(?=.*[-+_!@#$%^&*., ?]).+$")
        t=re.compile(regex)
        if p==None:
            count1=1
        if  re.search(t,p):
            d=1
        if d!=1:
            count1=1
        if count==1:
            print("invalid username")
        if count1==1:
            print("invalid password")
        if count==0 and count1==0:
            a.append(u)
            b.append(p)
            df=pd.DataFrame({"Username":a,"Passwords":b})
            # df.to_excel("D:\Python files\Bootcamp_codes\Registration_project.xlsx")
            with pd.ExcelWriter("D:\Python files\Bootcamp_codes\Registration_project.xlsx", mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
                df.to_excel(writer, sheet_name="Sheet1", header=None, startrow=writer.sheets["Sheet1"].max_row,index=False)
            print("Welcome Aboard")
    else:
        print("Invalid username, Username must contain @ and .")
    return

def login():
    u= username.get()
    p= password.get()
    df= pd.read_excel("D:\Python files\Bootcamp_codes\Registration_project.xlsx")
    df.columns=['Username','Password']
    if u in df['Username'].unique():
        df1=df[df['Username']==str(u)]
        val= df1['Password'].iloc[0]
        if str(val)==str(p):
            print(f"Welcome {u}")
        else:
            print("Invalid Password")
    else:
        print("Username not found Please register")


def fpass():
    u= username.get()
    p= password.get()
    df = pd.read_excel("D:\Python files\Bootcamp_codes\Registration_project.xlsx")
    df.columns = ['Username', 'Password']
    if u in df['Username'].unique():
        df1=df[df['Username']==str(u)]
        val= df1['Password'].iloc[0]
        print(val)
    else:
        print('Username Not found please register')

root= Tk()
root.title("Registration")
root.geometry("400x200")
Label(root,text="WELCOME!!",font="ar 15 bold").grid(row=0,column=1)
Label(root,text="Username/Email",font="ar 10").grid(row=1,column=0)
Label(root,text="Password",font="ar 10").grid(row=2,column=0)
username = StringVar()
password = StringVar()
uname_value= Entry(root,textvariable=username)
pvalue=Entry(root,textvariable=password)
uname_value.grid(row=1,column=1)
pvalue.grid(row=2,column=1)
Button(text="Register",command= reg).grid(row=5,column=1)
Button(text="Login",command= login).grid(row=5,column=2)
Button(text="Forgot Password",command= fpass).grid(row=5,column=3)
root.mainloop()
