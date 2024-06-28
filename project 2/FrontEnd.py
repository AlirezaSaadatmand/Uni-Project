from tkinter import *
from tkinter import ttk
from BackEnd import *

class Project:
    def __init__(self , root):
        self.root = root
        self.root.title("Library Management")
        self.root.geometry("660x450")

        # TOP FRAME
        self.top_frame = Frame(self.root , width=550 ,height=100)
        self.top_frame.pack(side=TOP)
        
        # TOP RIGHT FRAME
        self.top_right_frame = Frame(self.top_frame , width=100 , height=100)
        self.top_right_frame.pack(side=RIGHT)
        
        self.img = PhotoImage(file="assets/library.png")
        
        self.img_lb = Label(self.top_right_frame)
        self.img_lb.config(image=self.img)
        self.img_lb.pack(side=RIGHT , padx=(10 , 0))
        
        # TOP LEFT FRAME
        self.top_left_frame = Frame(self.top_frame , width=550 , height=100)
        self.top_left_frame.pack(side=LEFT , padx=5)
        
        # TOP LEFT TOP FRAME
        self.top_left_top_frame = Frame(self.top_left_frame , width=550 , height=50)
        self.top_left_top_frame.pack(side=TOP , pady=(0 , 10))
        
        Label(self.top_left_top_frame , text="Book Title :").pack(side=LEFT , padx=5)
        
        self.book_title_entry = ttk.Entry(self.top_left_top_frame , justify=CENTER , state=DISABLED)
        self.book_title_entry.pack(side=LEFT, padx=5 , ipady=7 , ipadx=15)
        
        Label(self.top_left_top_frame , text="Publish Year :").pack(side=LEFT, padx=5)

        self.publish_year_entry = ttk.Entry(self.top_left_top_frame , justify=CENTER , state=DISABLED)
        self.publish_year_entry.pack(side=LEFT, padx=5 , ipady=7 , ipadx=15)
        
        # TOP LEFT BOTTOM FRAME
        self.top_left_bottom_frame = Frame(self.top_left_frame , width=550 , height=50)
        self.top_left_bottom_frame.pack(side=BOTTOM)
        
        Label(self.top_left_bottom_frame , text="Author :").pack(side=LEFT , padx=(16 , 0))

        self.author_entry = ttk.Entry(self.top_left_bottom_frame , justify=CENTER , state=DISABLED)
        self.author_entry.pack(side=LEFT , padx=(9 , 1) , ipady=7 , ipadx=15)
        
        Label(self.top_left_bottom_frame , text="Subject :").pack(side=LEFT , padx=(35 , 0))
        
        self.subject_entry = ttk.Entry(self.top_left_bottom_frame , justify=CENTER , state=DISABLED)
        self.subject_entry.pack(side=LEFT ,padx=(10 , 0) , ipady=7 , ipadx=15)
        
        # MIDDLE FRAME
        self.middle_frame = Frame(self.root , width=550 , height=400)
        self.middle_frame.pack()
        
        # MIDDLE LEFT FRAME
        self.middle_left_frame = Frame(self.middle_frame , width=400 , height=400)
        self.middle_left_frame.pack(side=LEFT)
        
        self.treeview = ttk.Treeview(self.middle_left_frame , columns=("id" , "title" , "author" , "year" , "subject") , show="headings" )
        self.treeview.column("id",anchor=CENTER, stretch=NO, width=80)
        self.treeview.heading("id" , text="Book ID")
        self.treeview.column("title",anchor=CENTER, stretch=NO, width=140)
        self.treeview.heading("title" , text="Title")
        self.treeview.column("author",anchor=CENTER, stretch=NO, width=120)
        self.treeview.heading("author" , text="Author")
        self.treeview.column("year",anchor=CENTER, stretch=NO, width=80)
        self.treeview.heading("year" , text="Year")
        self.treeview.column("subject",anchor=CENTER, stretch=NO, width=100)
        self.treeview.heading("subject" , text="Subject")
        
        self.treeview.pack(side=LEFT , padx=(5 , 0) , ipady=19)
        self.treeview.bind('<ButtonRelease-1>', lambda x : change("selected" , self.book_title_entry , self.publish_year_entry , self.author_entry , self.subject_entry , self.treeview))
        
        self.scrollbar = ttk.Scrollbar(self.middle_left_frame, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side="right", fill="y")
        
        # MIDDLE RIGHT FRAME
        self.middle_right_frame = Frame(self.middle_frame , width=300 , height=400)
        self.middle_right_frame.pack(side=RIGHT)
        
        ttk.Button(self.middle_right_frame , text="Show All" , command=lambda : show_all(self.book_title_entry , self.publish_year_entry , self.author_entry , self.subject_entry , self.treeview)).pack(ipadx=15 , ipady=3 , pady=4)
        ttk.Button(self.middle_right_frame , text="New" , command=lambda : change("new" , self.book_title_entry , self.publish_year_entry , self.author_entry , self.subject_entry , self.treeview)).pack(ipadx=15 , ipady=3 , pady=4)
        ttk.Button(self.middle_right_frame , text="Edit" , command=lambda : change("edit" , self.book_title_entry , self.publish_year_entry , self.author_entry , self.subject_entry , self.treeview)).pack(ipadx=15 , ipady=3 , pady=4)
        ttk.Button(self.middle_right_frame , text="Submit" , command=lambda : change("submit" , self.book_title_entry , self.publish_year_entry , self.author_entry , self.subject_entry , self.treeview)).pack(ipadx=15 , ipady=3 , pady=4)
        ttk.Button(self.middle_right_frame , text="Cancel" , command=lambda : change("cancel" , self.book_title_entry , self.publish_year_entry , self.author_entry , self.subject_entry , self.treeview)).pack(ipadx=15 , ipady=3 , pady=4)
        ttk.Button(self.middle_right_frame , text="Delete" , command=lambda : delete_btn(self.book_title_entry , self.publish_year_entry , self.author_entry , self.subject_entry , self.treeview)).pack(ipadx=15 , ipady=3 , pady=4)
        ttk.Button(self.middle_right_frame , text="Exit" , command=exit_app).pack(ipadx=15 , ipady=3 , pady=4)
        
        # BOTTOM FRAME        
        self.bottom_frame = Frame(self.root , width=550 , height=100)
        self.bottom_frame.config(bg="blue")
        self.bottom_frame.pack(side=BOTTOM , pady=(1 , 10))
        
        self.footer = LabelFrame(self.bottom_frame , text="Search Books")
        self.footer.config(font=("Tahoma" , 14 , "italic") , fg="blue")
        self.footer.pack(side=LEFT , padx=(0 , 0) , ipadx=18 , ipady=20)
        
        self.radio_var = StringVar()
        
        self.title_radio = ttk.Radiobutton(self.footer , variable=self.radio_var , value="title")
        self.title_radio.pack(side=LEFT , padx=(5 , 0))
        
        self.title_label = Label(self.footer , text="Title")
        self.title_label.config(fg="blue")
        self.title_label.pack(side=LEFT , padx=(0 , 5))
        
        self.author_radio = ttk.Radiobutton(self.footer , variable=self.radio_var , value="author")
        self.author_radio.pack(side=LEFT)
        
        self.author_label = Label(self.footer , text="Author")
        self.author_label.config(fg="blue")
        self.author_label.pack(side=LEFT , padx=(0 , 5))
        
        self.year_radio = ttk.Radiobutton(self.footer  , variable=self.radio_var , value="year")
        self.year_radio.pack(side=LEFT)
        
        self.year_label = Label(self.footer , text="Year")
        self.year_label.config(fg="blue")
        self.year_label.pack(side=LEFT , padx=(0 , 5))
        
        self.subject_radio = ttk.Radiobutton(self.footer , variable=self.radio_var , value="subject")
        self.subject_radio.pack(side=LEFT)
        
        self.subject_label = Label(self.footer , text="Subject")
        self.subject_label.config(fg="blue")
        self.subject_label.pack(side=LEFT , padx=(0 , 5))
        
        self.search_entry = ttk.Entry(self.footer)
        self.search_entry.config(justify=CENTER)
        self.search_entry.pack(side=LEFT , padx=5 , ipadx=40 , ipady=1)
        
        ttk.Button(self.footer , text="Search" , command=lambda : search(self.treeview , self.radio_var , self.search_entry)).pack(side=LEFT , padx=(5 , 0) , ipadx=20 , ipady=1)

        
        # INITIAL DATA BASE CONNECTION
        connect(self.treeview)

def main():
    root = Tk()
    app = Project(root)
    root.mainloop()

if __name__ == '__main__':
    main()
