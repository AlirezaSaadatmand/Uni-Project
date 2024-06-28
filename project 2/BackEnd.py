import sqlite3
from tkinter import *
from tkinter import messagebox
from sys import exit

con = sqlite3.connect("data/database.db")
cursor = con.cursor()

state = "normal"

query = """
    CREATE TABLE IF NOT EXISTS tbllibrary(
    id integer primary key,
    title text,
    author text,
    year integer,
    subject text        
)
        """
def connect(tree):
    cursor.execute(query)
    con.commit()
    
    content = cursor.execute("SELECT * FROM tbllibrary").fetchall()
    if content:
        for i in content:
            tree.insert("",'end',id=list(i)[0] , values=(i))

def exit_app():
    if messagebox.askokcancel("Exit" , "Are you sure you want to close the app ?"):
        con.close()
        exit()
      
def show_all(title , year , author , subject , tree):
    lst = [title , author , year , subject]
    for item in tree.get_children():
        tree.delete(item)
    content = cursor.execute("SELECT * FROM tbllibrary").fetchall()
    if content:
        for i in content:
            tree.insert("",'end',id=list(i)[0] , values=(i))
        for i in lst:
            i.config(state=NORMAL)
            i.delete(0 , END)
            i.config(state=DISABLED)
            

def delete_btn(title , year , author , subject , tree):
    if tree.selection(): 
        if messagebox.askokcancel("Delete" , f"Do you want to delete this item ?"):
            cursor.execute(f"DELETE FROM tbllibrary WHERE id={tree.focus()}")
            tree.delete(tree.focus())
            show_all(title , year , author , subject , tree)
            
def change(btn , title , year , author , subject , tree):
    lst = [title , author , year , subject]
    global state
    
    if btn == "selected":
        for index , i in enumerate(lst):
            i.config(state=NORMAL)
            i.delete(0 , END)
            i.insert(END , tree.item(tree.focus())["values"][index + 1])
            i.config(state=DISABLED)
            
    if btn == "new":
        state = "new"
        for i in lst:
                i.config(state=NORMAL)
                i.delete(0 , END)
    if btn == "submit":
        if state == "new":
            cursor.execute(f"INSERT INTO tbllibrary (title , author , year , subject) VALUES ('{title.get()}' , '{author.get()}' , '{year.get()}' , '{subject.get()}')")
            con.commit()
            for i in lst:
                i.delete(0 , END)
                i.config(state=DISABLED)
            state = "normal"
            show_all(title , year , author , subject , tree)

            
        if "edit" in state and title.get() and year.get() and author.get() and subject.get():
            cursor.execute(f"UPDATE tbllibrary SET title='{title.get()}' , author='{author.get()}' , year='{year.get()}' , subject='{subject.get()}' WHERE id={state[-1]}")
            con.commit()
            for i in lst:
                i.delete(0 , END)
                i.config(state=DISABLED)
            state="normal"
            show_all(title , year , author , subject , tree)

            
    if btn == "edit":
        if tree.selection():
            for i in range(len(lst)):
                lst[i].config(state=NORMAL)
                lst[i].delete(0 , END)
                lst[i].insert(END , tree.item(tree.focus())["values"][i+1])
        state = "edit" + str(tree.focus())
    if btn == "cancel":
        if "edit" in state:
            for i in lst:
                i.config(state=DISABLED)
                
        if state == "new":
            if tree.item(tree.focus())["values"]:
                for index , i in enumerate(lst):
                    i.config(state=NORMAL)
                    i.delete(0 , END)
                    i.insert(END , tree.item(tree.focus())["values"][index + 1])
                    i.config(state=DISABLED)
            else:
                for i in lst:
                    i.config(state=DISABLED)
def search(tree , selected , searched):

    content = cursor.execute(f"SELECT * FROM tbllibrary WHERE {selected.get()}='{searched.get()}'").fetchall()
    if content:
        for item in tree.get_children():
            tree.delete(item)
        for i in content:
            tree.insert("",'end',id=list(i)[0] , values=(i))
        searched.delete(0 , END)
        