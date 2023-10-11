import tkinter as tk
from tkinter import ttk
import mysql.connector
import subprocess

sqldatabase = mysql.connector.connect(
    host="localhost",
    user='root',
    password='root',
    database="lib")
sqlcursor = sqldatabase.cursor()
sqlcursor.execute("select * from user order by user_id")
myrecords=sqlcursor.fetchall()


login = tk.Tk()
style = ttk.Style(login)

login.configure(bg="#202020")
style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)

login.title("User Login")

window_width = 800
window_height = 900
screen_width = login.winfo_screenwidth()
screen_height = login.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

login.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}'
)

userId = tk.StringVar()
name = tk.StringVar()
password = tk.StringVar()
email = tk.StringVar()


login_pic = tk.PhotoImage(file="achetz\login_icon.png")


heading = ttk.Label(
    login,
    font=('Poiret One', 30),
    text="User Login",
    image=login_pic,
    compound='top'
)

heading.pack(
    pady=30
)

idText = ttk.Label(
    login,
    font=('Lato', 15),
    text='User Id: ',
)

idText.pack(
    padx=50,
    anchor=tk.W,
)

idEntry = tk.Entry(
    login,
    textvariable=userId,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0,
)

idEntry.focus()
idEntry.pack(
    padx=100,
    pady=5,
    fill=tk.X
)

ttk.Label(login).pack(pady=10)

nameText = ttk.Label(
    login,
    font=('Lato', 15),
    text='User Name: ',
)

nameText.pack(
    padx=50,
    anchor=tk.W,
)

nameEntry = tk.Entry(
    login,
    textvariable=name,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0,
   
)
nameEntry.pack(
    padx=100,
    pady=5,
    fill=tk.X
)

ttk.Label(login).pack(pady=10)
passText = ttk.Label(
    login,
    font=('Lato', 15),
    text='Password: ',
)

passText.pack(
    padx=50,
    anchor=tk.W,
)

passEntry = tk.Entry(
    login,
    textvariable=password,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0,
    show="•",
)

passEntry.pack(
    padx=100,
    pady=7,
    fill=tk.X
)
emailText = ttk.Label(
    login,
    font=('Lato', 15),
    text='Email:',
)

emailText.pack(
    padx=50,
    anchor=tk.W,
)
emailEntry = tk.Entry(
    login,
    textvariable=email,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0,
)

emailEntry.pack(
    padx=100,
    pady=7,
    fill=tk.X
)

print(userId.get())
print(password.get())

def signIn():
     for i in myrecords:
          if i[0]==userId.get() and i[2]==password.get():
               subprocess.call('python showuser_page.py')
               userId.set("")
             
          else:
               "subprocess.call('python popups/connect_error.py')"
               subprocess.call('python showuser_page.py')
       


submit = tk.Button(
    login,
    text="Log in",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=signIn,
    cursor='dot',
    height=2,
    width=10,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

submit.pack(
    pady=10
)
leave = tk.Button(
    login,
    text="Exit",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=login.quit(),
    cursor='dot',
    height=2,
    width=10,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

leave.pack(
    pady=7
)

login.mainloop()


