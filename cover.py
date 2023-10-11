import tkinter as tk
from tkinter import ttk

import mysql.connector  
import subprocess


cover = tk.Tk()
style = ttk.Style(cover)
cover.columnconfigure(0, weight=2)

cover.configure(bg="#202020")
style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)
cover.title("Home Page")
window_width = 900
window_height = 900
screen_width = cover.winfo_screenwidth()
screen_height = cover.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
cover.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}'
)
###
cover_pic = tk.PhotoImage(file="achetz\cover.png")
heading = ttk.Label(
    cover,
    font=('Poiret One', 40),
    text="Role " + "?",
    image=cover_pic,
    compound='top',
)
heading.grid(
    row=0,
    column=0,
    pady=30
)



ttk.Label(cover).grid(row=1, column=0, pady=20)
roleTitle = ttk.Label(
    cover,
    text="Please Chosse your role!!",
    foreground="#45B39D",
    font=('Montserrat Bold', 25),
    justify=tk.CENTER
)

roleTitle.grid(
    row=1,
    column=0,
)

ttk.Label(cover).grid(row=1, column=1, pady=20)
def open_user():
    subprocess.call('python user.py')


userButton = tk.Button(
    cover,
    text="User",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=open_user,
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)
userButton.grid(
    row= 2,
    column=0,
)
ttk.Label(cover).grid(row=4, column=0, pady=30)
def open_add():
    subprocess.call('python showadm_page.py')


guestButton = tk.Button(
    cover,
    text="Guest",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=open_add,
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)
guestButton.grid(
    row= 4,
    column=0,
)


ttk.Label(cover).grid(row=4, column=0, pady=30)
def open_adm():
    subprocess.call('python login.py')
admButton = tk.Button(
    cover,
    text="Admin",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=open_adm,
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)
admButton.grid(
    row=7,
    column=0,
)


cover.mainloop()
    
