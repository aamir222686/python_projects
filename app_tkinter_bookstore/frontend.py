"""
--> A program which stores the below information.
>Title
>Author
>Year
>ISBN

--> User can:
>View All Records
>Search an entry
>add entry
>update entry
>Delete
>Close The GUI

--> Sqlite3 used to store the information.

@author: Aamir
"""
from tkinter import *
from backend import *

#App functions here
def get_selected_row(event):
    try:
        global selected_tuple
        index=lb.curselection()[0]
        selected_tuple=lb.get(index)
        e1.delete(0, END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    lb.delete(0, END)
    for row in view_all():
        lb.insert(END, row)
        
def search_command():
    lb.delete(0, END)
    for row in search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        lb.insert(END, row)

def add_command():
    insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    lb.delete(0, END)
    lb.insert(END, "Below Entry Added!")
    lb.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    
def delete_command():
    delete(selected_tuple[0])
    lb.delete(0, END)
    lb.insert(END, "Entry Deleted!")
    
def update_command():
    update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    lb.delete(0, END)
    lb.insert(END, "Below Entry Updated!")
    lb.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    

window = Tk()
window.wm_title("Bookstore")

#Create stacked entry columns and rows with Title, Author, Year, ISBN
#Title Entry
e1_l = Label(window, text='Title')
e1_l.grid(row=0, column=1)
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=2, padx=10, pady=10)

#Author Entry
e2_l = Label(window, text='Author')
e2_l.grid(row=0, column=3)
author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=4, padx=10, pady=10)

#Year Entry
e3_l = Label(window, text='Year')
e3_l.grid(row=1, column=1)
year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=2, padx=10, pady=10)

#ISBN Entry
e4_l = Label(window, text='ISBN')
e4_l.grid(row=1, column=3)
isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=4, padx=10, pady=10)

#Create a listbox
lb = Listbox(window)
lb.grid(row=2, column=1, rowspan=7, columnspan=2, ipadx=15)

#Create a scroller
sc = Scrollbar(window)
sc.grid(row=2, column=3, rowspan=6, columnspan=1, ipady=40)

#Configure Scroll Bar with the listbox
lb.configure(yscrollcommand=sc.set)
sc.configure(command=lb.yview)

#Bind the listbox to get the data on the list item clicked on
lb.bind('<<ListboxSelect>>', get_selected_row)

#Now abuttons for View ALl, Search entry, Add Entry, Update, Delete, Close
#View All
b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=4, pady=3)

#Search Entry
b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=4, pady=3)

#Add Entry
b3 = Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=4, pady=3)

#Update
b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=4, pady=3)

#Delete
b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=4, pady=3)

#Close
def close_window():
    window.destroy()

b6 = Button(window, text="Close", width=12, command=close_window)
b6.grid(row=7, column=4, pady=3)

window.mainloop()

