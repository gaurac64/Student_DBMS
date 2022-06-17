from tkinter import  *
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Managament System")

        self.root.geometry("1980x1080+0+0")
        self.root.configure(bg="White")

        title=Label(self.root,text="Student Mgmt System",bd=10, relief=GROOVE ,font=("times new roman",30,"bold"),bg="#FAC213",fg="White")
        title.pack(side=TOP,fill=X)


# ********************************Manage Frame***********************************
        self.Roll_No_var=StringVar()
        self.Name_var=StringVar()
        self.Email_var=StringVar()
        self.Gender_var=StringVar()
        self.Contact_var=StringVar()
        self.DoB_var=StringVar()

        self.Search_by=StringVar()
        self.Search_txt=StringVar()


# ********************************Manage Frame***********************************


        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#7FB5FF")
        Manage_Frame.place(x=20,y=100,width=550,height=670)


        m_title=Label(Manage_Frame,text="Manage Frame",bg="#7FB5FF",fg="White",font=("times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20,padx=10)


        lbl_roll=Label(Manage_Frame,text="Roll No",bg="#7FB5FF",fg="White",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("",16),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=40,sticky="w")


        lbl_name=Label(Manage_Frame,text="Name",bg="#7FB5FF",fg="White",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.Name_var,font=("",16),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=40,sticky="w")


        lbl_email=Label(Manage_Frame,text="E-mail",bg="#7FB5FF",fg="White",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(Manage_Frame,textvariable=self.Email_var,font=("",16),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=40,sticky="w")


        lbl_Gender=Label(Manage_Frame,text="Gender",bg="#7FB5FF",fg="White",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("",16),state='readonly')
        combo_gender['values'] = ("Male","Female","Other")
        combo_gender.grid(row=4,column=1,pady=10,padx=40,sticky="w")


        lbl_Contact=Label(Manage_Frame,text="Contact",bg="#7FB5FF",fg="White",font=("times new roman",20,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_Contact=Entry(Manage_Frame,textvariable=self.Contact_var,font=("",16),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=40,sticky="w")


        lbl_DOB=Label(Manage_Frame,text="D.O.B",bg="#7FB5FF",fg="White",font=("times new roman",20,"bold"))
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_DOB=Entry(Manage_Frame,textvariable=self.DoB_var,font=("",16),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=40,sticky="w")


        lbl_Address=Label(Manage_Frame,text="Address",bg="#7FB5FF",fg="White",font=("times new roman",20,"bold"))
        lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_Address=Text(Manage_Frame,width=25,height=5,font=('',16))
        self.txt_Address.grid(row=7,column=1,pady=10,padx=40,sticky='w')

# ********************************Button Frame***********************************


        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg='#FAC213')
        btn_Frame.place(x=55,y=600,width=430)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
        

# ********************************Detail Frame***********************************
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#7FB5FF")
        Detail_Frame.place(x=600,y=100,width=920,height=670)
        

        lbl_Search=Label(Detail_Frame,text="Search",bg="#7FB5FF",fg="White",font=("times new roman",25,"bold"))
        lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.Search_by,width=10,font=("",20),state='readonly')
        combo_search['values'] = ("RollNo","Name","Contact")
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        txt_Search=Entry(Detail_Frame,width=15,textvariable=self.Search_txt,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        Searchbtn=Button(Detail_Frame,text="Search",command=self.Search_data,width=15,height=2,bd=4).grid(row=0,column=3,padx=10,pady=10)
        Showallbtn=Button(Detail_Frame,text="Show All",command=self.fetch_data,width=15,height=2,bd=4).grid(row=0,column=4,padx=10,pady=10)

# ********************************Table Frame***********************************
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#FF85B3")
        Table_Frame.place(x=10,y=70,width=890,height=580)

        Scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        Scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("RollNo","Name","E-mail","Gender","Contact","D.O.B","Address"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.Student_table.xview)
        Scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("RollNo",text="RollNo")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("E-mail",text="E-mail")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Contact",text="Contact")
        self.Student_table.heading("D.O.B",text="D.O.B")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("RollNo",width=100)
        self.Student_table.column("Name",width=200)
        self.Student_table.column("E-mail",width=200)
        self.Student_table.column("Gender",width=200)
        self.Student_table.column("Contact",width=200)
        self.Student_table.column("D.O.B",width=200)
        self.Student_table.column("Address",width=250)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_students(self):
        if self.Roll_No_var.get()=="" or self.Name_var.get()=="" or self.Email_var.get()=="" or self.Contact_var.get()=="" or self.Gender_var.get()=="" or self.DoB_var.get()=="" :
                messagebox.showerror("Error","All Fields are required!!!")
        elif self.Roll_No_var.get().isnumeric()==False:
                messagebox.showerror("Error","RollNo Field should be Numeric!!!")
        else:
                con=pymysql.connect(host="localhost",user="root",password="",database="sdms")
                cur=con.cursor()
                cur.execute("INSERT INTO students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                                self.Name_var.get(),
                                                                                self.Email_var.get(),
                                                                                self.Gender_var.get(),
                                                                                self.Contact_var.get(),
                                                                                self.DoB_var.get(),
                                                                                self.txt_Address.get('1.0',END)
                                                                                ))
                con.commit()
                self.fetch_data()
                messagebox.showinfo("Success","Record has been inserted.")
                self.clear()
                con.close()

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sdms")
        cur=con.cursor()
        cur.execute("SELECT * FROM students")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows :
                        self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.DoB_var.set("")
        self.txt_Address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.DoB_var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])
    
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sdms")
        cur=con.cursor()
        cur.execute("UPDATE students SET RollNo=%s,Name=%s,Email=%s,Gender=%s,Contact=%s,DoB=%s,Address=%s",(self.Roll_No_var.get(),
                                                                        self.Name_var.get(),
                                                                        self.Email_var.get(),
                                                                        self.Gender_var.get(),
                                                                        self.Contact_var.get(),
                                                                        self.DoB_var.get(),
                                                                        self.txt_Address.get('1.0',END)
                                                                        # self.Roll_No_var.get()
                                                                        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sdms")
        cur=con.cursor()
        cur.execute("DELETE FROM students WHERE RollNo=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


    def Search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sdms")
        cur=con.cursor()

        cur.execute("SELECT * FROM students WHERE "+str(self.Search_by.get())+" LIKE '%"+str(self.Search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows :
                        self.Student_table.insert('',END,values=row)
                con.commit() 
        con.close()




root=Tk()
ob = Student(root)
root.state('zoomed')
root.mainloop()