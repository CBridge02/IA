from tkinter import *
from tkinter import ttk
from .FitnessMainPage import*
from .FitnessLogin import *
from .Database import*

newLogin = Login()
newMainPage = MainPage()
newDatabase = Database()

root = TK()
root.title('Tabs')
root.geometry("500x500")

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady = 15)

def hide():
    my_notebook.hide(1)

def show():
    my_notebook.add(my_frame1, text="Red Tab")

def select():
    my_notebook.select(1)

my_frame1 = Frame(my_notebook, width=500, height=500, bg="blue")
my_frame1 = Frame(my_notebook, width=500, height=500, bg="red")
my_frame3 = Frame(my_notebook, width=500, height=500, bg="green")

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)
my_frame3.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="Login")
my_notebook.add(my_frame2, text="Main Page")
my_notebook.add(my_frame3, text="Database")

my_button = Button(my_frame1, text = "Hide Tab 2", command=hide).pack(pady=10)

my_button2 = Button(my_frame1, text = "Show Tab 2", command=show).pack(pady=10)

my_button3 = Button(my_frame1, text = "Navigate To Tab 2", command=select).pack(pady=10)

root.mainloop()
