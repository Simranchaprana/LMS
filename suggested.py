import tkinter as tk
from tkinter import ttk
import mysql.connector

details = {}
with open("credentials.txt") as file:
    lis = file.read().split(" -|- ")
    details['username'] = 'root'
    details['password'] = 'root'
    details['nickname'] = lis[1]


sqldatabase = mysql.connector.connect(
    host="localhost",
    user=details['username'],
    password=details['password'],
    database="lib"
)
sqlcursor = sqldatabase.cursor()

suggested = tk.Tk()
style = ttk.Style(suggested)

style.theme_use('clam')

theme = style.theme_use()
style.theme_create("dummy", parent=theme)
style.theme_use("dummy")

suggested.configure(bg="#202020")

style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)
style.configure(
    'Treeview',
    font=('Manrope Bold', 12),
    background="#202020",
    foreground="#fafafa",
    rowheight=40
)

style.configure(
    'Treeview.Heading',
    font=('Montserrat', 20),
    background="#202020",
    foreground="#fafafa",
)

style.configure(
    "Vertical.TScrollbar",
    background="#202020",
    borderwidth=1,
    arrowcolor="#fafafa"
)

suggested.title("Suggested Books")

window_width = 1000
window_height = 800
screen_width = suggested.winfo_screenwidth()
screen_height = suggested.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

suggested.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}'
)

suggested_book = tk.PhotoImage(file=r"achetz\added_icon.png")

heading = ttk.Label(
    suggested,
    font=('Poiret One', 40),
    text="Suggested Books",
    image=suggested_book,
    compound='top',
    justify=tk.CENTER
)

heading.grid(
    pady=30,
    padx=10,
    row=0,
    column=0,
)


sqlcursor.execute("select * from suggested_book")

books = []
for i in sqlcursor:
    books += [i]

columns = ('book_id', 'book_name', 'author')

tree = ttk.Treeview(
    suggested,
    columns=columns,
    show='headings',
    height=10,
    padding=0,
)

tree.column(
    'book_id',
    width=100,
    anchor=tk.CENTER
)

tree.column(
    'book_name',
    width=500,
    anchor=tk.W
)

tree.column(
    'author',
    width=300,
    anchor=tk.W
)

tree.heading(
    'book_id',
    text='ID',
)

tree.heading(
    'book_name',
    text='Name',
)

tree.heading(
    'author',
    text='Author',
)

tree.tag_configure(
    'available',
    background="#252525",
    foreground="#fafafa",
)

tree.tag_configure(
    'issued',
    background="#252525",
    foreground="#fafafa",
)

av = []
sqlcursor.execute("select * from available_books")
for book in sqlcursor:
    av += [book]

for details in books:
    if details in av:
        tree.insert(
            '',
            tk.END,
            values=details,
            tags='available'
        )
    else:
        tree.insert(
            '',
            tk.END,
            values=details,
            tags='issued'
)

tree.grid(
    row=2,
    column=0,
    sticky='nsew',
    rowspan=5,
    padx=32.5,
    pady=20
)

scrollbar = ttk.Scrollbar(
    suggested,
    orient=tk.VERTICAL,
    command=tree.yview
)

tree.configure(
    yscroll=scrollbar.set
)

scrollbar.grid(
    row=0,
    column=1,
    sticky='ns',
    rowspan=10
)


quitButton = tk.Button(
    suggested,
    text="Exit",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=lambda: suggested.quit(),
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
    columnspan=2
)


suggested.mainloop()

 
