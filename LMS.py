import tkinter as tk
from tkinter import ttk

import mysql.connector  
import subprocess
import random


details = {}
with open("credentials.txt") as file:
    x= file.read()
    lis=x.split(" -|- ")
    details['username'] = lis[0]
    details['password'] = lis[1]
    details['nickname'] = lis[2]

sqldatabase = mysql.connector.connect(host="localhost",user=details['username'],password=details['password'])
sqlcursor = sqldatabase.cursor()
sqlcursor.execute("create database if not exists lib")
sqlcursor.execute("use lib")

sqlcursor.execute('create table if not exists all_books (id int not null primary key, name varchar(500), author varchar(500),genre varchar(400))engine=InnoDB')
sqlcursor.execute('create table if not exists available_books (id int unique references all_books(id), name varchar(600), author varchar(600),genre varchar(400))engine=InnoDB')
        
sqlcursor.execute('create table if not exists issued_books (id int references all_books(id),name varchar(900),author varchar(600),genre varchar(400),due_date varchar(700), email varchar(700))engine=InnoDB')
"""
sqlcursor.execute("insert into available_books select * from all_books")
"""
bookList = [
    (1, 'A Better India: A Better World', 'Narayana Murthy','Realism'),
    (2, "The Pilgrim's Progress", 'John Bunyan','Symbolism'),
    (3, 'Robinson Crusoe', 'Daniel Defoe','Adventure'),
    (4, "Gulliver's Travels", 'Jonathan Swift','Fantasy'),
    (5, 'Clarissa', 'Samuel Richardson','Epistolary'),
    (6, 'Tom Jones ', 'Henry Fielding','Fiction'),
    (7, 'The Life and Opinions of Tristram Shandy, Gentleman', 'Laurence Sterne','Fiction'),
    (8, 'Emma', 'Jane Austen','Romance'),
    (9, 'Frankenstein ', 'Mary Shelley','Horror'),
    (10, 'Nightmare Abbey', 'Thomas Love Peacock','Fiction'),
    (11, 'The Narrative of Arthur Gordon Pym of Nantucket', 'Edgar Allan Poe','Adventure'),
    (12, 'Sybil', 'Benjamin Disraeli','Socialism'),
    (13, 'Jane Eyre', 'Charlotte Brontë','Romance'),
    (14, 'Wuthering Heights', 'Emily Brontë','Gothic'),
    (15, 'Vanity Fair', 'William Thackeray','Humor'),
    (16, 'David Copperfield', 'Charles Dickens','Coming of age'),
    (17, 'The Scarlet Letter ', 'Nathaniel Hawthorne','Romance'),
    (18, 'Moby-Dick', 'Herman Melville','Adventure'),
    (19, "Alice's Adventures in Wonderland", 'Lewis Carroll','Fiction'),
    (20, 'The Moonstone', 'Wilkie Collins','Mystery'),
    (21, 'Little Women', 'Louisa May Alcott','Coming of age'),
    (22, 'Middlemarch', 'George Eliot','Social'),
    (23, 'The Way We Live Now', 'Anthony Trollope','Humor'),
    (24, 'The Adventures of Huckleberry Finn', 'Mark Twain','Adventure'),
    (25, 'Kidnapped', 'Robert Louis Stevenson','Historical'),
    (26, 'Three Men in a Boat', 'Jerome K Jerome','Humor'),
    (27, 'The Sign of Four', 'Arthur Conan Doyle','Mystery'),
    (28, 'The Picture of Dorian Gray', 'Oscar Wilde','Gothic'),
    (29, 'New Grub Street', 'George Gissing','Realism'),
    (30, 'Jude the Obscure', 'Thomas Hardy','Realism'),
    (31, 'The Red Badge of Courage', 'Stephen Crane','War'),
    (32, 'Dracula', 'Bram Stoker','Horror'),
    (33, 'Heart of Darkness', 'Joseph Conrad','Adventure'),
    (34, 'Sister Carrie', 'Theodore Dreiser','Realism'),
    (35, 'Kim', 'Rudyard Kipling','Adventure'),
    (36, 'The Golden Bowl', 'Henry James','Drama'),
    (37, 'Hadrian the Seventh', 'Frederick Rolfe','Humor'),
    (38, 'The Wind in the Willows', 'Kenneth Grahame','Fantasy'),
    (39, 'The History of Mr Polly', 'HG Wells','Humour'),
    (40, 'Zuleika Dobson', 'Max Beerbohm','Humor'),
    (41, 'The Good Soldier', 'Ford Madox Ford','Romance'),
    (42, 'The Thirty-Nine Steps', 'John Buchan','Adventure'),
    (43, 'The Rainbow', 'DH Lawrence','Social'),
    (44, 'Of Human Bondage', 'W Somerset Maugham','Coming of age'),
    (45, 'The Age of Innocence','Edith Wharton','Social'),
    (46, 'Ulysses', 'James Joyce','Fiction'),
    (47, 'Babbitt', 'Sinclair Lewis','Social'),
    (48, 'A Passage to India', 'EM Forster','Historical'),
    (49, 'Gentlemen Prefer Blondes', 'Anita Loos','Humor'),
    (50, 'Mrs Dalloway', 'Virginia Woolf','Fiction'),
    (51, 'The Great Gatsby', 'F Scott Fitzgerald','Social'),
    (52, 'Lolly Willowes', 'Sylvia Townsend Warner','Coming of age'),
    (53, 'The Sun Also Rises', 'Ernest Hemingway','War'),
    (54, 'The Maltese Falcon', 'Dashiell Hammett','Fiction'),
    (55, 'As I Lay Dying', 'William Faulkner','Gothic'),
    (56, 'Brave New World', 'Aldous Huxley','Fiction'),
    (57, 'Cold Comfort Farm', 'Stella Gibbons','Humor'),
    (58, 'Nineteen Nineteen', 'John Dos Passos','Historical'),
    (59, 'Tropic of Cancer', 'Henry Miller','Autobiography'),
    (60, 'Scoop', 'Evelyn Waugh','Drama'),
    (61, 'Murphy', 'Samuel Beckett','Fiction'),
    (62, 'The Big Sleep', 'Raymond Chandler','Adventure'),
    (63, 'Party Going', 'Henry Green','Mystery'),
    (64, 'At Swim-Two-Birds', 'Flann O Brien','Fiction'),
    (65, 'The Grapes of Wrath', 'John Steinbeck','Realism'),
    (66, 'Joy in the Morning', 'PG Wodehouse','Adventure'),
    (67, "All the King's Men", 'Robert Penn Warren','Fiction'),
    (68, 'Under the Volcano', 'Malcolm Lowry','Fiction'),
    (69,  "It Ends With Us ", 'Colleen Hoover','Romance'),
    (70, "It Start With Us", 'Colleen Hoover','Romance')
    
]
"""
for i in bookList:
    sqlcursor.execute(f"insert ignore into all_books values {i}")
    sqlcursor.execute(f"insert ignore into available_books values {i}")
   """ 

sqldatabase.commit()
home = tk.Tk()
style = ttk.Style(home)
home.columnconfigure(0, weight=2)
home.columnconfigure(1, weight=1)
home.columnconfigure(2, weight=1)
home.configure(bg="#202020")
style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)
home.title("DeCyphers Library MS")
window_width = 1500
window_height = 800
screen_width = home.winfo_screenwidth()
screen_height = home.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
home.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}'
)
home_pic = tk.PhotoImage(file="achetz\home_book.png")
heading = ttk.Label(
    home,
    font=('Poiret One', 40),
    text="BOOKMATE" + "!",
    image=home_pic,
    compound='top',
)
heading.grid(
    row=0,
    column=0,
    columnspan=3,
    pady=30
)
noticeTitle = ttk.Label(
    home,
    text="SALE",
    foreground="#EC9657",
    font=('Montserrat Bold', 30),
)
noticeTitle.grid(
    row=1,
    column=0,
)
noticeText = ttk.Label(
    home,
    text="Flat " + str(random.randint(50, 100)) + "% off on selected books, hurry!" +
    "\n" + "Offer only for " + str(random.randint(2, 10)) + " days!",
    foreground="#505050",
    font=('Manrope', 20),
    justify=tk.CENTER
)
noticeText.grid(
    row=2,
    column=0
)

ttk.Label(home).grid(row=3, column=0, columnspan=3, pady=20)
infoTitle = ttk.Label(
    home,
    text="HURRY UP!!",
    foreground="#45B39D",
    font=('Montserrat Bold', 30),
)

infoTitle.grid(
    row=4,
    column=0,
)
infoText = ttk.Label(
    home,
    text="The site will undergo maintenance shortly, and \nwill be down for " +
    str(random.randint(5, 40)) + " minutes.",
    foreground="#505050",
    font=('Manrope', 20),
    justify=tk.CENTER
)
infoText.grid(
    row=5,
    column=0
)

ttk.Label(home).grid(row=1, column=1, columnspan=2, pady=20)
def openShow():
    subprocess.call('python showadm_page.py')
showButton = tk.Button(
    home,
    text="Show books",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=openShow,
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
    )
showButton.grid(
    row=2,
    column=1,
)
def openAdd():
    subprocess.call('python add_page.py')
addButton = tk.Button(
    home,
    text="Add books",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=openAdd,
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)
addButton.grid(
    row=2,
    column=2,
)
def openIssue():
    subprocess.call('python issue_page.py')


issueButton = tk.Button(
    home,
    text="Issue books",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=openIssue,
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)
issueButton.grid(
    row=4,
    column=1,
)
def openReturn():
    subprocess.call('python return_book.py')
returnButton = tk.Button(
    home,
    text="Return books",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=openReturn,
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)
returnButton.grid(
    row=4,
    column=2,
)
"""
impButton = tk.Button(
    home,
    text="Important",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)
impButton.grid(
    row=6,
    column=1,
)

def rickroll(e):
    webbrowser.open_new(
        r"https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    )
    impButton["text"] = "lol rickrolld"
    impButton["background"] = "#459DB3"
impButton.bind(
    "<Button-1>",
    rickroll
)"""
quitButton = tk.Button(
    home,
    text="Exit",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=lambda: home.quit(),
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)
quitButton.grid(

    row=6,
    column=2,
)
home.mainloop()
    
