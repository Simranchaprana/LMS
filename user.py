
import tkinter as tk
from tkinter import ttk
import mysql.connector  
import subprocess

user = tk.Tk()
style = ttk.Style(user)
user.columnconfigure(0, weight=2)

user.configure(bg="#202020")
style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)
user.title("Home Page")
window_width = 900
window_height = 800
screen_width = user.winfo_screenwidth()
screen_height = user.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
user.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}'
)
###
user_pic = tk.PhotoImage(file="achetz\stack_book.png")
heading = ttk.Label(
    user,
    font=('Poiret One', 40),
    text="WELCOME " + "!",
    image=user_pic,
    compound='top',
)
heading.grid(
    row=0,
    column=0,
    columnspan=3,
    pady=30
)



ttk.Label(user).grid(row=2, column=0, pady=20)
roleTitle = ttk.Label(
    user,
    text="Please Resister youself if not registered yet!!",
    foreground="#EC9657",
    font=('Montserrat Bold', 25),
    justify=tk.CENTER
)

roleTitle.grid(
    row=1,
    column=0,
)

ttk.Label(user).grid(row=1, column=1, pady=20)
def open_register():
    subprocess.call('python register.py')


registerButton = tk.Button(
    user,
    text="Register Now!!",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=open_register,
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)
registerButton.grid(
    row= 3,
    column=0,
)


ttk.Label(user).grid(row=4, column=0, pady=30)
def open_login_user():
    subprocess.call('python user_login.py')
admButton = tk.Button(
    user,
    text="Login",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=open_login_user,
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)
admButton.grid(
    row=4,
    column=0,
)
quitButton = tk.Button(
    user,
    text="Exit",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=lambda: user.quit(),
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)
quitButton.grid(

    row=10,
    column=0,
)

user.mainloop()
    
