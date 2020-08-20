import pickle
import csv
def reader():
    global l
    l=[]
    with open("username.dat","rb") as f1:
        try:
            while True:
                l.extend(pickle.load(f1))
        except EOFError:
            pass

                
def loginfn():
    a=1
    while a:
        c=0
        x=input("Enter username")
        for i in l:
            if i[0]==x:
                print("Username not available")
                c=1
        if not(c):
            d=1
            while d:
                y=input("Enter password")
                if len(y)>=8 and y.isalnum() and not(y.isspace()):
                    print("Registered")
                    l.append([x,y])
                    with open("username.dat","wb") as f1:
                        pickle.dump(l,f1)
                    d=0;a=0
                else:
                    print("Password does not meet the requirements")
def opener(a=1):
    if a:
        while True:
            try:
                x=int(input("Are you a new user? press 1 if yes and 2 if no"))
                if x==1:
                    loginfn()
                    break
                if x==2:
                    divider()
                    break
            except ValueError:
                print("You need to type 1 for yes 2 for no")
    else:
        while True:
            try:
                x=int(input("Do you want to create a new account 1 if yes 2 if no"))
                if x==1:
                    loginfn()
                    break
                if x==2:
                    divider()
                    break
            except ValueError:
                print("You need to type 1 for yes 2 for no")

def divider():
    x=int(input("Do you already have an account Press 1 if yes and 2 if no"))
    if x==1:
        oldaccount()
    if x==2:
        opener(0)
def oldaccount():
    h=1
    while h:
        a=0
        try:
            x=input("Enter your username if you already have an account")
            for i in l:
                if i[0]==x:
                    y=i[1]
                    a=1
            if not(a):
                print("Account doesnt exist")
                print(opener(0))
            else:
                g=5
                while g>0:
                    y1=input("Enter your password")
                    if y1==y:
                        print("Login successful")
                        g=0
                        h=0
                    else:
                        print("Incorrect password")
                        g-=1
                        print(g,"more attempt(s) remaining. This username will be deleted otherwise")
        except ValueError:
            pass
#main
reader()
opener()

