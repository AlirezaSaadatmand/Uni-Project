from tkinter import *
from tkinter import ttk
from sys import exit
from BackEnd import * 

class Project:
    def __init__(self , root):
        connect()
        self.root = root
        self.root.config(bg = "white")
        self.root.title("PhoneBook")
        self.root.geometry("450x450")
        
        self.img = PhotoImage(file="assets/User-Authentication.png")

        self.image_lb = Label(self.root)
        self.image_lb.config(image=self.img)
        self.image_lb.pack(pady=(40, 20))
        
        self.wellcome_lb = Label(self.root , text="Wellcome to Phonebook")
        self.wellcome_lb.config(font=("Yahoma",14 , "bold") , bg="white" , fg="blue")
        self.wellcome_lb.pack(pady=10)
        
        #User name frame
        self.username_f = Frame(self.root , width=500 , height=50)
        self.username_f.config(bg="white")
        self.username_f.pack(pady=10)
        
        self.username_lb = Label(self.username_f , text="Username :")
        self.username_lb.config(bg="white")
        self.username_lb.pack(side=LEFT)
        
        self.username_e = ttk.Entry(self.username_f)
        self.username_e.config(justify=CENTER)
        self.username_e.pack(side=LEFT , padx=20 , ipadx=50)
        
        #Password frame
        self.password_f = Frame(self.root , width=500 , height=50)
        self.password_f.config(bg="white")
        self.password_f.pack()
        
        self.password_lb = Label(self.password_f , text="Password : ")
        self.password_lb.config(bg="white")
        self.password_lb.pack(side=LEFT )
        
        self.password_e = ttk.Entry(self.password_f)
        self.password_e.config(justify=CENTER)
        self.password_e.pack(side=LEFT, padx=20 , ipadx=50)
        
        self.LogIn_btn = ttk.Button(self.root , text="Login" , command=self.dis)
        self.LogIn_btn.pack(pady=15)
        
        #New User Button
        self.new_user_btn = Button(self.root , text="New User? Sign Up" , command=self.newuser)
        self.new_user_btn.config(font=("Yamoha" , 10 , "italic") , fg="blue" , bg="white" , border=0)
        self.new_user_btn.pack()
        
    def newuser(self):
        self.top = Toplevel(self.root)
        self.top.config(bg="white")
        self.top.title("Sign Up")
        self.top.geometry("450x450")
        
        self.img2 = PhotoImage(file="assets/New-User.png")
        
        self.image2_lb = Label(self.top)
        self.image2_lb.config(image=self.img2)
        self.image2_lb.pack(pady=(30, 30))
        
        self.wellcome_lb2 = Label(self.top , text="Username and Password")
        self.wellcome_lb2.config(font=("Yahoma",14 , "bold") , bg="white" , fg="blue")
        self.wellcome_lb2.pack(pady=10)
        
        self.new_user_frame = Frame(self.top)
        self.new_user_frame.config(bg="white")
        self.new_user_frame.pack()
        
        #User name frame
        self.username_f2 = Frame(self.new_user_frame , width=500 , height=50)
        self.username_f2.config(bg="white")
        self.username_f2.pack(pady=10)
        
        self.username_lb2 = Label(self.username_f2 , text="New Username :")
        self.username_lb2.config(bg="white")
        self.username_lb2.pack(side=LEFT)
        
        self.username_e2 = ttk.Entry(self.username_f2)
        self.username_e2.config(justify=CENTER)
        self.username_e2.pack(side=LEFT , padx=20 , ipadx=50)
        
        #Password frame
        self.password_f2 = Frame(self.new_user_frame , width=500 , height=50)
        self.password_f2.config(bg="white")
        self.password_f2.pack(pady=10)
        
        self.password_lb2 = Label(self.password_f2 , text="New Password : ")
        self.password_lb2.config(bg="white")
        self.password_lb2.pack(side=LEFT )
        
        self.password_e2 = ttk.Entry(self.password_f2)
        self.password_e2.config(justify=CENTER)
        self.password_e2.pack(side=LEFT, padx=20 , ipadx=50)
        
        self.Submit_btn = ttk.Button(self.new_user_frame , text="Submit" , command=lambda : check_newuser(self.username_e2 , self.password_e2 , self.wellcome_lb2 , self.top))
        self.Submit_btn.pack(pady=15 )
    
    def dis(self):
        if check_login(self.username_e , self.password_e , self.wellcome_lb):    
            self.image_lb.destroy()
            self.wellcome_lb.destroy()
            self.username_f.destroy()
            self.password_f.destroy()
            self.LogIn_btn.destroy()
            self.new_user_btn.destroy()
            self.user()
         
    def user(self):        
        self.img3 = PhotoImage(file="assets/phonebook.png")
        
        self.image3_lb = Label(self.root)
        self.image3_lb.config(image=self.img3)
        self.image3_lb.pack(side=TOP , pady=(5 , 0))

        #left Frame
        self.left_frame = Frame(self.root , width=300)
        self.left_frame.config(bg="white")
        self.left_frame.pack(side=LEFT)
        
        self.left_top_frame = LabelFrame(self.left_frame , text="Contacts information" , width=300 , height=150)
        self.left_top_frame.config(bg="white")
        self.left_top_frame.pack(side=TOP , padx=10 , pady=(10 , 21))
        
        self.left_left_top_frame = Frame(self.left_top_frame , width=150 , height=300)
        self.left_left_top_frame.config(bg="white")
        self.left_left_top_frame.pack(side=LEFT)
        
        self.lid = Label(self.left_left_top_frame , text="ID:")
        self.lid.config(bg="white")
        self.lid.pack(pady=5)
        
        self.lname = Label(self.left_left_top_frame , text="Name:")
        self.lname.config(bg="white")
        self.lname.pack(pady=5)
        
        self.llastname = Label(self.left_left_top_frame , text="Last Name:")
        self.llastname.config(bg="white")
        self.llastname.pack(pady=5)
        
        self.lphonenumber = Label(self.left_left_top_frame , text="Phone Number:")
        self.lphonenumber.config(bg="white")
        self.lphonenumber.pack(pady=5)
        
        self.lcellnumber = Label(self.left_left_top_frame , text="Cell Number:")
        self.lcellnumber.config(bg="white")
        self.lcellnumber.pack(pady=5)
        
        self.laddress = Label(self.left_left_top_frame , text="Address:")
        self.laddress.config(bg="white")
        self.laddress.pack(pady=5)
        
        
        self.left_right_frame = Frame(self.left_top_frame , width=150 , height=300)
        self.left_right_frame.config(bg="white")
        self.left_right_frame.pack(side=RIGHT)
        
        self.eid = ttk.Entry(self.left_right_frame)
        self.eid.config(justify=CENTER)
        self.eid.pack(pady=5, padx=10 , ipadx=30)
        
        self.ename = ttk.Entry(self.left_right_frame)
        self.ename.config(justify=CENTER)
        self.ename.pack(pady=5, padx=10 , ipadx=30)
        
        self.elastname = ttk.Entry(self.left_right_frame)
        self.elastname.config(justify=CENTER)
        self.elastname.pack(pady=5, padx=10 , ipadx=30)
        
        self.ephonenumber = ttk.Entry(self.left_right_frame)
        self.ephonenumber.config(justify=CENTER)
        self.ephonenumber.pack(pady=5, padx=10 , ipadx=30)
        
        self.ecellnumber = ttk.Entry(self.left_right_frame)
        self.ecellnumber.config(justify=CENTER)
        self.ecellnumber.pack(pady=5, padx=10 , ipadx=30)
        
        self.eaddress = ttk.Entry(self.left_right_frame)
        self.eaddress.config(justify=CENTER)
        self.eaddress.pack(pady=5 , padx=10 , ipadx=30)
        
        self.left_bottom = Frame(self.left_frame)
        self.left_bottom.config(bg="white")
        self.left_bottom.pack(side=BOTTOM)
        
        self.first_btn = ttk.Button(self.left_bottom , text="First" , command=lambda : show_data("first" , self.eid , self.ename , self.elastname , self.ephonenumber , self.ecellnumber , self.eaddress))
        self.first_btn.pack(side=LEFT)
        
        self.prev_btn = ttk.Button(self.left_bottom , text="Prev" , command=lambda : show_data("prev" , self.eid , self.ename , self.elastname , self.ephonenumber , self.ecellnumber , self.eaddress))
        self.prev_btn.pack(side=LEFT)
        
        self.next_btn = ttk.Button(self.left_bottom , text="Next" , command=lambda : show_data("next" , self.eid , self.ename , self.elastname , self.ephonenumber , self.ecellnumber , self.eaddress))
        self.next_btn.pack(side=LEFT)
        
        self.last_btn = ttk.Button(self.left_bottom , text="Last" , command=lambda : show_data("last" , self.eid , self.ename , self.elastname , self.ephonenumber , self.ecellnumber , self.eaddress))
        self.last_btn.pack(side=LEFT)
        
        #Right Frame
        self.right_frame = Frame(self.root , width=170 )
        self.right_frame.config(bg="white")
        self.right_frame.pack(pady=(10 , 20) , ipady=25)
        
               
        self.new_btn = ttk.Button(self.right_frame , text="New", command=lambda : show_data("new" , self.eid , self.ename , self.elastname , self.ephonenumber , self.ecellnumber , self.eaddress))
        self.new_btn.pack(padx=10 , pady=(0 , 5), ipadx=50)
        
        self.edit_btn = ttk.Button(self.right_frame , text="Edit" , command=lambda : show_data("edit" , self.eid , self.ename , self.elastname , self.ephonenumber , self.ecellnumber , self.eaddress))
        self.edit_btn.pack(padx=10 , pady=(0 , 5), ipadx=50)
        
        self.delete_btn = ttk.Button(self.right_frame , text="Delete" , command=lambda : show_data("delete" , self.eid , self.ename , self.elastname , self.ephonenumber , self.ecellnumber , self.eaddress))
        self.delete_btn.pack(padx=10 , pady=(0 , 5), ipadx=50)
        
        self.submit_btn = ttk.Button(self.right_frame , text="Submit" , command=lambda : show_data("submit" , self.eid , self.ename , self.elastname , self.ephonenumber , self.ecellnumber , self.eaddress))
        self.submit_btn.pack(padx=10 , pady=(0 , 5), ipadx=50)
        
        self.cancel_btn = ttk.Button(self.right_frame , text="Cancel" , command=lambda : show_data("cancel" , self.eid , self.ename , self.elastname , self.ephonenumber , self.ecellnumber , self.eaddress))
        self.cancel_btn.pack(padx=10 , pady=(0 , 15) , ipadx=50)
    
        self.search_lb = Label(self.right_frame , text="search by : ")
        self.search_lb.config(bg="white")
        self.search_lb.pack(pady=(0 , 5))  

        self.menu= StringVar()

        self.drop= ttk.OptionMenu(self.right_frame, self.menu, "ID","ID", "Name","Lastname","Phonenumber","Cellnumber","Address")
        self.drop.pack(pady=(0 , 5))
        
        self.search_e = ttk.Entry(self.right_frame , width=20)
        self.search_e.config(justify=CENTER)
        self.search_e.pack(ipadx=10 , pady=(0 , 5))
        
        self.search_btn = ttk.Button(self.right_frame , text="Search" , command=lambda : search(self.menu.get() , self.search_e , self.eid , self.ename , self.elastname , self.ephonenumber , self.ecellnumber , self.eaddress))
        self.search_btn.pack(ipadx=50 , padx=10  , side=BOTTOM)
        
        show_data("init" , self.eid , self.ename , self.elastname , self.ephonenumber , self.ecellnumber , self.eaddress)
        
            
def main():
    root = Tk()
    app = Project(root)
    root.mainloop()

if __name__ == '__main__':
    main()
