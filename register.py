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
sqlcursor.execute('select*from user')
myrecords=sqlcursor.fetchall()
register = tk.Tk()

style = ttk.Style(register)


register.configure(bg="#202020")
style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)

register.title("Register")

window_width = 1000
window_height = 900
screen_width = register.winfo_screenwidth()
screen_height = register.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

register.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}'
)


register_pic = tk.PhotoImage(file=r"achetz\register.png")

heading = ttk.Label(
    register,
    font=('Poiret One',40),
    text="Register",
    image=register_pic,
    compound='top',
    )
heading.pack(
    pady=30,
   )

userId = tk.StringVar()
userName = tk.StringVar()
email = tk.StringVar()
userpass = tk.StringVar()


IdText = ttk.Label(
    register,
    font=('Lato', 15),
    text='user Id: ',
)

IdText.pack(
    padx=100,
    pady=7,
    anchor=tk.W,
)

IdEntry = tk.Entry(
    register,
    textvariable=userId,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0,
)

IdEntry.focus()
IdEntry.pack(
    padx=100,
    fill=tk.X
)

ttk.Label(register).pack(pady=10)

nameText = ttk.Label(
    register,
    font=('Lato', 15),
    text='user Name: ',
)

nameText.pack(
    padx=100,
    pady=7,
    anchor=tk.W,
)

nameEntry = tk.Entry(
    register,
    textvariable=userName,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0,
   
)

nameEntry.pack(
    padx=100,
    pady=7,
    fill=tk.X
)

ttk.Label(register).pack(pady=10)

userText = ttk.Label(
    register,
    font=('Lato', 15),
    text='password ',
)

userText.pack(
    padx=100,
    anchor=tk.W,
)

userEntry = tk.Entry(
    register,
    textvariable=userpass,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0,
  # show="•",
)

userEntry.pack(
    padx=100,
    pady=7,
    fill=tk.X
)
emailText = ttk.Label(
    register,
    text='Email: ',
    font=('Lato', 15),
)

emailText.pack(
    padx=100,
    pady=7,
    anchor=tk.W
)

emailEntry = tk.Entry(
    register,
    textvariable=email,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0,
)

emailEntry.pack(
    padx=100,
    fill=tk.X
)


def ok():
    for i in myrecords:
        if i[1]==userId.get():
            subprocess.call('python popups/exists_error.py')
            userId.set("")

        
        if userName.get() == "" or userId.get() == "":
            subprocess.call('python popups/blank_error.py')
            userId.set("")
            userName.set("")
        else:
            sqlcursor.execute("insert into user values (userId, userName,userpass,email)")
            sqldatabase.commit()
            
            subprocess.call('python popups/addeduser_info.py')
            subprocess.call('python showuser_page.py')
    
     
submit = tk.Button(
    register,
    text="Register Now!",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=lambda:subprocess.call('python showuser_page.py'),
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

submit.pack(
    pady=15

        


)
quitButton = tk.Button(
    register,
    text="Exit",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=lambda: register.quit(),
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

quitButton.pack(
    padx=100,
    pady=8
  
)

register.mainloop()
