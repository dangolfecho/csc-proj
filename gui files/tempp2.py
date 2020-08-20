from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as tkkr
import time
from gtts import gTTS
from playsound import playsound
import pygame
from pygame import mixer
pygame.init()
def convert():
    my_audio=gTTS('')
    my_audio.save("hello1.mp3")
def register_user():
    username_info=username.get()
    password_info=password.get()
    with open(username_info+".txt","w")as file:
        file.write(username_info+"\n")
        file.write(password_info)
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    playsound("hello1.mp3")
    
    '''Label(login_frame1,text="Registration Success",fg="green",font=('calibri',11)).grid(row=4,column=1,padx=20,pady=10)
    Label(login_frame1,text="")'''
    screen1.destroy()
def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("700x900")
    global username
    global password
    global username_entry
    global password_entry
    global login_frame1
    username=StringVar()
    password=StringVar()
    Label(screen1,text="PLEASE ENTER THE FOLLOWING DETAILS",background="purple",foreground="pink",width="300",bd=10,height="2",font= ("calibri",30),relief=GROOVE).pack()
    bg_icon=ImageTk.PhotoImage(file="sky.jpg")
    bg_lbl=Label(screen1,image=bg_icon).pack()
    username_icon=ImageTk.PhotoImage(file="username2.png")
    pass_icon=ImageTk.PhotoImage(file="password2.png")
    user_icon=ImageTk.PhotoImage(file="usericon3.png")
    login_frame1=Frame(screen1,bg="pink")
    login_frame1.place(x=500,y=325)
    logolbl=Label(login_frame1,image=user_icon).grid(row=0,column=0,pady=20)
    lbluser=Label(login_frame1,text="username",image=username_icon,compound=LEFT,font=("times new roman","20","bold")).grid(row=1,column=0,padx=20,pady=10)
    lblpass=Label(login_frame1,text="password",image=pass_icon,compound=LEFT,font=("times new roman","20","bold")).grid(row=2,column=0,padx=20,pady=10)
    username_entry=Entry(login_frame1,textvariable=username)
    username_entry.grid(row=1,column=1,padx=20,pady=10)
    password_entry=Entry(login_frame1,textvariable=password)
    password_entry.grid(row=2,column=1,padx=20,pady=10)
    Button(login_frame1,text="Register",width="10",height="1",command=register_user).grid(row=3,column=1,padx=20,pady=10)
    login_frame1.mainloop()
    screen1.mainloop()  
def login():
    tkkr.showinfo("Login","You are logged in")
def main_screen():
    global screen
    screen=Tk()
    screen.geometry('700x900')
    screen.title("SIGN IN REQUIRED")
    Label(text="VIRAT KOHLI AIRLINES RESERVATION-SIGN UP",background="purple",foreground="pink",width="300",bd=10,height="2",font= ("calibri",30),relief=GROOVE).pack()
    mixer.music.load("hello.mp3")
    mixer.music.play()
    bg_icon=ImageTk.PhotoImage(file="sky.jpg")
    bg_lbl=Label(image=bg_icon).pack()
    Label(text="").pack()
    login_frame=Frame(screen,bg="pink")
    login_frame.place(x=500,y=325)
    Label(login_frame,text="PLEASE SIGN IN TO CONTINUE",background="pink",height="2",width="30",font=("times new",20,"bold")).grid(row=1,column=0,padx=20,pady=10)
    Button(login_frame,text="Log In",height="2",width="30",command=login).grid(row=4,column=0,padx=20,pady=10)
    Button(login_frame,text="Register",height="2",width="30",command=register).grid(row=7,column=0,padx=20,pady=10)    
    screen.mainloop()
main_screen()


