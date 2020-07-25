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
from backend import Database

database = Database("bookstore.db")

class Window(object):
    
    def __init__(self, window):
        self.window = window
        self.window.wm_title("Bookstore")
        
        #Create stacked entry columns and rows with Title, Author, Year, ISBN
        #Title Entry
        e1_l = Label(window, text='Title')
        e1_l.grid(row=0, column=1)
        self.title_text = StringVar()
        self.e1 = Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=2, padx=10, pady=10)
        
        #Author Entry
        e2_l = Label(window, text='Author')
        e2_l.grid(row=0, column=3)
        self.author_text = StringVar()
        self.e2 = Entry(window, textvariable=self.author_text)
        self.e2.grid(row=0, column=4, padx=10, pady=10)
        
        #Year Entry
        e3_l = Label(window, text='Year')
        e3_l.grid(row=1, column=1)
        self.year_text = StringVar()
        self.e3 = Entry(window, textvariable=self.year_text)
        self.e3.grid(row=1, column=2, padx=10, pady=10)
        
        #ISBN Entry
        e4_l = Label(window, text='ISBN')
        e4_l.grid(row=1, column=3)
        self.isbn_text = StringVar()
        self.e4 = Entry(window, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=4, padx=10, pady=10)
        
        #Create a listbox
        self.lb = Listbox(window)
        self.lb.grid(row=2, column=1, rowspan=7, columnspan=2, ipadx=15)
        
        #Create a scroller
        sc = Scrollbar(window)
        sc.grid(row=2, column=3, rowspan=6, columnspan=1, ipady=40)
        
        #Configure Scroll Bar with the listbox
        self.lb.configure(yscrollcommand=sc.set)
        sc.configure(command=self.lb.yview)
        
        #Bind the listbox to get the data on the list item clicked on
        self.lb.bind('<<ListboxSelect>>', self.get_selected_row)
        
        #Now abuttons for View ALl, Search entry, Add Entry, Update, Delete, Close
        #View All
        b1 = Button(window, text="View All", width=12, command=self.view_command)
        b1.grid(row=2, column=4, pady=3)
        
        #Search Entry
        b2 = Button(window, text="Search Entry", width=12, command=self.search_command)
        b2.grid(row=3, column=4, pady=3)
        
        #Add Entry
        b3 = Button(window, text="Add Entry", width=12, command=self.add_command)
        b3.grid(row=4, column=4, pady=3)
        
        #Update
        b4 = Button(window, text="Update", width=12, command=self.update_command)
        b4.grid(row=5, column=4, pady=3)
        
        #Delete
        b5 = Button(window, text="Delete", width=12, command=self.delete_command)
        b5.grid(row=6, column=4, pady=3)
        
        #Close
        b6 = Button(window, text="Close", width=12, command=self.close_window)
        b6.grid(row=7, column=4, pady=3)
        
    def get_selected_row(self, event):
        try:
            index=self.lb.curselection()[0]
            self.selected_tuple=self.lb.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END,self.selected_tuple[4])
        except IndexError:
            pass
     
    def view_command(self):
        self.lb.delete(0, END)
        for row in database.view_all():
            self.lb.insert(END, row)
            
    def search_command(self):
        self.lb.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.lb.insert(END, row)
    
    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.lb.delete(0, END)
        self.lb.insert(END, "Below Entry Added!")
        self.lb.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))
        
    def delete_command(self):
        database.delete(self.selected_tuple[0])
        self.lb.delete(0, END)
        self.lb.insert(END, "Entry Deleted!")
        
    def update_command(self):
        database.update(self.selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.lb.delete(0, END)
        self.lb.insert(END, "Below Entry Updated!")
        self.lb.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))
    
    def close_window(self):
        database.close_conn()
        self.window.destroy()  

window = Tk()
Window(window)
window.mainloop()