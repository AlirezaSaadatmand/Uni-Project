import sqlite3
from tkinter import *
from tkinter import messagebox

con = sqlite3.connect("data/database.db")
cursor = con.cursor()

init1 = """
        CREATE TABLE IF NOT EXISTS tblUser(
            id integer primary key,
            username text,
            password text
        )
        """

init2 = """
        CREATE TABLE IF NOT EXISTS tblContacts(
        id integer primary key,
        name text,
        lastname text,
        phonenumber integer,
        cellnumber integer,
        address text    
        )
        """

def  connect():
    cursor.execute(init1)
    con.commit()
    
    cursor.execute(init2)
    con.commit()
        
# New User Function
def check_newuser(name , pas , lb , top):
    check = True
    for i in cursor.execute("SELECT username FROM tblUser").fetchall():
        if list(i)[0] == name.get():
            check = False

    if name.get() == "":
        lb.config(text="Enter the Username")
        return
    
    if pas.get() != "" and len(pas.get()) >= 8:
        if check:
            cursor.execute(f"INSERT INTO tblUser (username , password) values ('{name.get()}' , '{pas.get()}')")
            con.commit()
            top.destroy()
        else:
            lb.config(text = "Username already exists")
            name.delete(0 , END)
            pas.delete(0 , END)
    else:
        lb.config(text="Password must be 8 characters")

# Log In Function
def check_login(name , pas , lb):
    foundusername = False
    lst = []
    for i in cursor.execute("SELECT username FROM tblUser").fetchall():
        lst.append(list(i)[0])
            
    if name.get() in lst:
        foundusername = True
        
    if name.get() == "":
        lb.config(text="Enter the username")
        return False
    
    if pas.get() == "":
        lb.config(text="Enter the password")
        return False
    else:
        if not foundusername:
            lb.config(text="Username not found")
            return False
        else:
            passwords = []
            for i in cursor.execute("SELECT password FROM tblUser").fetchall():
                passwords.append(list(i)[0])
            
            if passwords[lst.index(name.get())] == pas.get():
                lb.config(text="Log in successful")
                return True
            else:
                lb.config(text="Wrong password")
                return False
            
state = None
def show_data(command , id , name , last , phone , cell , add):
    global state
    lst = [id , name , last , phone , cell  , add]

    id.config(state=NORMAL)
    idd = id.get()
    id.config(state=DISABLED)

    # INITIAL command
    if command == "init":
        id.config(state=NORMAL)
        if not cursor.execute("SELECT id FROM tblContacts").fetchall():
            for i in lst:
                i.delete(0 , END)
                i.insert(END , "NO DATA")
                i.config(state=DISABLED)
                
        else:
            for i in cursor.execute("SELECT * FROM tblcontacts WHERE id=1").fetchall():
                for j in lst:
                    j.config(state=NORMAL)
                    j.delete(0 , END)
                    j.insert(END , str(list(i)[lst.index(j)]))
                    j.config(state=DISABLED)
    
    # NEW btn
    if command == "new":
        state = "new"
        for i in lst:
            if i == id:
                idnumber = len(cursor.execute("SELECT id FROM tblcontacts").fetchall()) + 1
                i.config(state=NORMAL)
                i.delete(0 , END)
                i.insert(END , str(idnumber))
                i.config(state=DISABLED)

            else:
                i.config(state=NORMAL)
                i.delete(0 , END)
    
    # EDIT btn
    if command == "edit" and cursor.execute("SELECT * FROM tblContacts").fetchall() and state != "new":
        state = "edit"
        for i in lst:
            if i != id:
                i.config(state=NORMAL)
            
    # DELETE btn
    if command == "delete":
        id.config(state=NORMAL)
        idd = id.get()
        id.config(state=DISABLED)
        if messagebox.askokcancel("Delete" , f"Do you want to delete the contact with id : {idd}"):
            if idd != "NO DATA":
                cursor.execute(f"DELETE FROM tblcontacts WHERE id={idd}")
                con.commit()
                
                for i in range(int(idd) , len(cursor.execute("SELECT * FROM tblcontacts").fetchall()) + 1):
                    cursor.execute(f"UPDATE tblcontacts SET id = {i} WHERE id = {i + 1}")         
                    con.commit()   
                
                if not cursor.execute("SELECT id FROM tblContacts").fetchall():
                    for i in lst:
                        i.config(state=NORMAL)
                        i.delete(0 , END)
                        i.insert(END , "NO DATA")
                        i.config(state=DISABLED)
                    
                else:
                    for i in cursor.execute("SELECT * FROM tblcontacts WHERE id=1").fetchall():
                        for j in lst:
                            j.config(state=NORMAL)
                            j.delete(0 , END)
                            j.insert(END , str(list(i)[lst.index(j)]))
                            j.config(state=DISABLED)
    
    # SUBMIT btn            
    if command == "submit":
        if state == "new":
            check = True
            for i in lst:
                if i.get() == "" :
                    check = False
            if check:
                cursor.execute(f"""INSERT INTO tblContacts (id , name , lastname , phonenumber , cellnumber , address)
                               values ('{id.get()}' , '{name.get()}' , '{last.get()}' , '{phone.get()}' , '{cell.get()}' , '{add.get()}')""")
                con.commit()
                for i in cursor.execute("SELECT * FROM tblcontacts WHERE id=1").fetchall():
                    for j in lst:
                        j.config(state=NORMAL)
                        j.delete(0 , END)
                        j.insert(END , str(list(i)[lst.index(j)]))
                        j.config(state=DISABLED)
        
        if state == "edit":
            id.config(state=NORMAL)
            idd = id.get()
            id.config(state=DISABLED)
            cursor.execute(f"UPDATE tblcontacts SET name = '{name.get()}' , lastname = '{last.get()}' , phonenumber = '{phone.get()}' ,cellnumber = '{cell.get()}' , address = '{add.get()}' WHERE id='{idd}'")    
            con.commit()
            for i in lst:
                i.config(state=DISABLED)

    # CANCEL btn
    if command == "cancel":
        state = None
        if cursor.execute("SELECT * FROM tblContacts").fetchall():
            for i in cursor.execute(f"SELECT * FROM tblcontacts WHERE id={idd}").fetchall():
                for j in lst:
                    j.config(state=NORMAL)
                    j.delete(0 , END)
                    j.insert(END , str(list(i)[lst.index(j)]))
                    j.config(state=DISABLED)
        else:
            id.config(state=NORMAL)
            for i in lst:
                i.delete(0 , END)
                i.insert(END , "NO DATA")
                i.config(state=DISABLED)

    # FIRST btn
    if command == "first" and idd != "NO DATA":
        for i in cursor.execute("SELECT * FROM tblcontacts WHERE id=1").fetchall():
            for j in lst:
                j.config(state=NORMAL)
                j.delete(0 , END)
                j.insert(END , str(list(i)[lst.index(j)]))
                j.config(state=DISABLED)
    
    # PREV btn
    if command == "prev" and idd != "NO DATA":
        for i in cursor.execute(f"SELECT * FROM tblcontacts WHERE id={int(idd) - 1}").fetchall():
            for j in lst:
                j.config(state=NORMAL)
                j.delete(0 , END)
                j.insert(END , str(list(i)[lst.index(j)]))
                j.config(state=DISABLED)

    # NEXT btn
    if command == "next" and idd != "NO DATA":
        for i in cursor.execute(f"SELECT * FROM tblcontacts WHERE id={int(idd) + 1}").fetchall():
            for j in lst:
                j.config(state=NORMAL)
                j.delete(0 , END)
                j.insert(END , str(list(i)[lst.index(j)]))
                j.config(state=DISABLED)
                
    # LAST btn
    if command == "last" and idd != "NO DATA":
        count = len(cursor.execute("SELECT * FROM tblcontacts").fetchall())
        for i in cursor.execute(f"SELECT * FROM tblcontacts WHERE id={count}").fetchall():
            for j in lst:
                j.config(state=NORMAL)
                j.delete(0 , END)
                j.insert(END , str(list(i)[lst.index(j)]))
                j.config(state=DISABLED)
              
# SEAECH section  
def search(selected , searched , id , name , last , phone , cell , add):
    if searched.get() != "":
        lst = [id , name , last , phone , cell  , add]
        lst2 = []
        value = None
        for i in list(cursor.execute(f"SELECT {selected.lower()} FROM tblContacts").fetchall()):
            lst2.append(str(i[0]))
            
        if selected == "ID":
            value = int(searched.get())
            val = str(selected.lower())
            if searched.get() in lst2:
                for i in cursor.execute(f"SELECT * FROM tblContacts WHERE {val} = {value}").fetchall():
                    for j in lst:
                        j.config(state=NORMAL)
                        j.delete(0 , END)
                        j.insert(END , str(list(i)[lst.index(j)]))
                        j.config(state=DISABLED)
        else:
            value = searched.get()
            val = str(selected.lower())
            if searched.get() in lst2:
                for i in cursor.execute(f"SELECT * FROM tblContacts WHERE {val} = '{value}'").fetchall():
                    for j in lst:
                        j.config(state=NORMAL)
                        j.delete(0 , END)
                        j.insert(END , str(list(i)[lst.index(j)]))
                        j.config(state=DISABLED)
                        
                        