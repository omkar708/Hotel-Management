#Importing Libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import pymysql


#                                   ************************************FRONTEND******************************************


#=======================Design of Window
class customer():
    def __init__(self, root):
        mf_c = "lightgoldenrod"
        self.root=root
        self.root.title("Hotel Management System")
        self.root.configure(bg = "skyblue")
        self.root.geometry('1700x750+0+0')
        title = Label(self.root, text = "Hotel Management System", bd = 9, relief = GROOVE , font = ("Algerian", 40, 'bold'), bg = "black", fg = "white")
        title.pack(side=TOP,fill=X)

        self.rn =StringVar()
        self.n = StringVar()
        self.mn = StringVar()
        self.an = StringVar()
        self.ci = StringVar()
        self.co = StringVar()
        self.ng = StringVar()
        self.b1 = StringVar()
        self.tt = StringVar()
        self.upd = StringVar()
        sr = StringVar()

        
        #SHOW BUTTON FUNCTION
        def show():
            conn = mysql.connector.connect(host = 'localhost', user = "root", passwd = "112233", database = "omdata")
            mycur=conn.cursor()
            mycur.execute("select * from hms")
            result = mycur.fetchall()
            for res in result:
                treev.insert("",'end',values=(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7]))
        
        #SEARCH BUTTON FUNCTION
        def search():
            if sr.get()== "":
                messagebox.showerror("Customer Info", "Customer Room Number Require to fill")
            else:
                conn = mysql.connector.connect(host = 'localhost', user = "root", passwd = "112233", database = "omdata")
                mycur=conn.cursor()
                mycur.execute("select * from hms where Room_No LIKE '%"+sr.get()+"%'")
                serch=mycur.fetchall()
                for res in serch:
                    treev.insert("",'end',values=(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7]))
                
        #CLEAR BUTTON FUNCTION
        def clearb():
            treev.delete(*treev.get_children())

        #DELETE BUTTON FUNCTION 
        def delete():
            rs=self.tt.get()
            if rs=="":
                messagebox.showerror("Customer Info", "Customer Room Number Require to fill")
            else:
                conn = pymysql.connect(host = 'localhost', user = "root", passwd = "112233", database = "omdata")
                quer1="DELETE FROM hms WHERE Room_No='%s'"%(rs)
                mycur=conn.cursor()
                mycur.execute(quer1)
                conn.commit()
                mycur.close()
                conn.close()
                messagebox.showinfo("Customer Info ","Record Deleted Successfully")
                self.tt.set('')


#======================TO MANAGE FRAME
        Manage_Frame = Frame(self.root, bd = 10, relief=RIDGE, bg = mf_c)
        Manage_Frame.place(x=20,y=100, width = 550, height = 640)
        m_title = Label(Manage_Frame,text = "   Manage Customers", bg = mf_c, fg = "blue",  font = ("Arial black", 30, 'bold'))
        m_title.grid(row=0,column=0)


#========================FOR MANAGE CUSTOMERS     
        #FOR ROOM NO
        l_Room_No = Label(Manage_Frame,text="Room Number : ",bg = mf_c, fg = "Black", font=("times new roman", 16, "bold"))
        l_Room_No.place(x = 10, y = 62)
        txt_Room_No = Entry(Manage_Frame, font=("times new roman", 16, "bold"),textvariable=self.rn, bd = 5, relief=GROOVE,width=25)
        txt_Room_No.place(x=200, y = 60)
        
        #FOR NAME 
        l_Name = Label(Manage_Frame,text="Customer Name : ",bg = mf_c, fg = "Black", font=("times new roman", 16, "bold"))
        l_Name.place(x = 10, y = 124)
        txt_Name = Entry(Manage_Frame, font=("times new roman", 16, "bold"),textvariable=self.n, bd = 5, relief=GROOVE,width=25)
        txt_Name.place(x=200, y = 120)
        
        #FOR MOBILE NO
        l_Mobile_No = Label(Manage_Frame,text="Mobile Number : ",bg = mf_c, fg = "Black", font=("times new roman", 16, "bold"))
        l_Mobile_No.place(x = 10, y = 185)
        txt_Mobile_No = Entry(Manage_Frame, font=("times new roman", 16, "bold"),textvariable=self.mn, bd = 5, relief=GROOVE,width=25)
        txt_Mobile_No.place(x=200, y = 180)

        #FOR IDENTITY
        l_Adhar_No = Label(Manage_Frame,text="Adhar Number : ",bg = mf_c, fg = "Black", font=("times new roman", 16, "bold"))
        l_Adhar_No.place(x = 10, y = 245)
        txt_Adhar_No = Entry(Manage_Frame, font=("times new roman", 16, "bold"),textvariable=self.an, bd = 5, relief=GROOVE,width=25)
        txt_Adhar_No.place(x=200, y = 240)

        #FOR CHECKIN
        l_Check_in = Label(Manage_Frame,text="Check In : ",bg = mf_c, fg = "Black", font=("times new roman", 16, "bold"))
        l_Check_in.place(x = 10, y = 305)
        txt_Check_in = Entry(Manage_Frame, font=("times new roman", 16, "bold"),textvariable=self.ci, bd = 5, relief=GROOVE,width=25)
        txt_Check_in.place(x=200, y = 300)

        #FOR CHECKOUT
        l_Check_out = Label(Manage_Frame,text="Check Out : ",bg = mf_c, fg = "Black", font=("times new roman", 16, "bold"))
        l_Check_out.place(x = 10, y = 365)
        txt_Check_out = Entry(Manage_Frame, font=("times new roman", 16, "bold"),textvariable=self.co, bd = 5, relief=GROOVE,width=25)
        txt_Check_out.place(x=200, y = 360)
        
        #FOR NUMBER OF GUEST
        l_No_Guest = Label(Manage_Frame,text="Number of Guests : ",bg = mf_c, fg = "Black", font=("times new roman", 16, "bold"))
        l_No_Guest.place(x = 10, y = 425)
        txt_No_Guest=ttk.Combobox(Manage_Frame,textvariable=self.ng,font=("times new roman",15,'bold'),state='readonly',width=26)
        txt_No_Guest['values']=("1","2","3","4")
        txt_No_Guest.place(x=200,y=420)

        #FOR BILL
        l_Bill = Label(Manage_Frame,text="Bill : ",bg = mf_c, fg = "Black", font=("times new roman", 16, "bold"))
        l_Bill.place(x = 10, y = 490)
        txt_Bill = Entry(Manage_Frame, font=("times new roman", 16, "bold"),textvariable=self.b1, bd = 5, relief=GROOVE,width=25)
        txt_Bill.place(x=200, y = 480)

        #FOR DELETE BY ROOM NUMBER
        l_delete = Label(self.root,text="Delete by Room No. : ",bg ="skyblue",  fg = "Black", font=("times new roman", 16, "bold"))
        l_delete.place(x = 650, y = 550)
        txt_delete = Entry(self.root, font=("times new roman", 16, "bold"),textvariable=self.tt, bd = 5, relief=GROOVE,width=40)
        txt_delete.place(x=900, y = 550)

        #SEARCH BY ROOM NUMBER
        l_search = Label(self.root,text="Search by Room No. : ",bg ="skyblue",  fg = "Black", font=("times new roman", 16, "bold"))
        l_search.place(x = 650, y = 605)
        txt_search = Entry(self.root, font=("times new roman", 16, "bold"),textvariable=sr, bd = 5, relief=GROOVE,width=40)
        txt_search.place(x=900, y = 605)

        #FOR UPDATE BY ROOM NUMBER
        l_update = Label(self.root,text="Update by Room No. : ",bg = "skyblue", fg = "Black", font=("times new roman", 16, "bold"))
        l_update.place(x = 650, y = 660)
        txt_update = Entry(self.root, font=("times new roman", 16, "bold"), bd = 5, relief=GROOVE,width=40,textvariable=self.upd)
        txt_update.place(x=900, y = 660)


#================================FOR BUTTONS
        #FOR ADD BUTTON
        add_btn = Button(Manage_Frame,text="ADD",bg="green3",font=("times new roman", 13, "bold"),width=10,command=self.add)
        add_btn.place(x = 20, y=540)
        
        #FOR SHOW BUTTON
        show_btn = Button(Manage_Frame,text="SHOW",bg="green3",font=("times new roman", 13, "bold"),width=10,command=show)
        show_btn.place(x = 150, y=540)

        # FOR SEARCH BUTTON
        search_btn = Button(Manage_Frame,text="SEARCH",bg="green3",font=("times new roman", 13, "bold"),width=10,command=search)
        search_btn.place(x = 270, y=540)

        #FOR UPDATE BUTTON
        update_btn = Button(Manage_Frame,text="UPDATE",bg = "green3",font=("times new roman", 13, "bold"),width=10, command=self.update_data)
        update_btn.place(x = 395, y=540)

        #FOR CLEAR BUTTON
        clear_btn = Button(Manage_Frame,text="CLEAR", bg = "red",font=("times new roman", 13, "bold"),width=10,command=clearb)
        clear_btn.place(x = 80, y=585)

        #FOR EXIT BUTTON
        exit_btn = Button(Manage_Frame,text="EXIT", bg="red",height=1,width=10,font=("times new roman", 13, "bold"),command=self.root.destroy)
        exit_btn.place(x = 320, y=585)

        #FOR DELETE BUTTON
        delete_btn = Button(Manage_Frame,text="DELETE", bg = "red",font=("times new roman", 13, "bold"),width=10,command=delete)
        delete_btn.place(x = 200, y=585)


#=====================FOR TREE VIEW
        treev = ttk.Treeview(self.root,selectmode='browse',height=20)
        treev.place(x = 600, y = 100, width = 900)
        treev['column']=("1","2","3","4","5","6","7","8")
        treev['show'] = 'headings'
        
        treev.column("1", width= 10, anchor='c')
        treev.column("2", width= 30, anchor='se')
        treev.column("3", width= 50, anchor='se')
        treev.column("4", width= 60, anchor='se')
        treev.column("5", width= 40, anchor='se')
        treev.column("6", width= 40, anchor='se')
        treev.column("7", width= 10, anchor='se')
        treev.column("8", width= 10, anchor='se')


        treev.heading("1",text="Room No.")
        treev.heading("2",text="Customer Name")
        treev.heading("3",text="Mobile No.")
        treev.heading("4",text="Adhar No.")
        treev.heading("5",text="Check In")
        treev.heading("6",text="Check Out")
        treev.heading("7",text="Guests")
        treev.heading("8",text="Bill")

        #===============SCROLLBAR
        verscroll=ttk.Scrollbar(self.root,orient='vertical',command=treev.yview) 
        verscroll.pack(side='right',fill='x')
        treev.configure(xscrollcommand=verscroll.set)
              

#==================DEFINATIONS OF BUTTONS
    #ADD BUTTON FUNCTION
    def add(self): 
        if (self.rn.get() == "" or self.n.get() == "" or self.mn.get() == "" or self.an.get() == "" or self.ci.get() == "" or self.co.get() == "" or self.ng.get() == "" or self.b1.get() == ""):
            messagebox.showerror("All fields must required to fill")
        else:      
            conn=pymysql.connect(host="localhost",user="root",password='112233',db='omdata')
            cur=conn.cursor()
            cur.execute("insert into hms values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.rn.get(),
                                                                            self.n.get(),
                                                                            self.mn.get(),
                                                                            self.an.get(),
                                                                            self.ci.get(),
                                                                            self.co.get(),
                                                                            self.ng.get(),
                                                                            self.b1.get() 
            ))
            conn.commit()
            self.clear()
            conn.close()
            messagebox.showinfo("Customer Info", "Customer Information Submitted Successfully")

    #CLEAR BUTTON FUNCTION
    def clear(self):
        self.rn.set('')
        self.n.set('')
        self.mn.set('')
        self.an.set('')
        self.ci.set('')
        self.co.set('')
        self.ng.set('')
        self.b1.set('')

   
        


    #UPDATE BUTTON FUNCTION
    def update_data(self):
        if (self.n.get() == "" or self.mn.get() == "" or self.an.get() == "" or self.ci.get() == "" or self.co.get() == "" or self.ng.get() == "" or self.b1.get() == ""):
            messagebox.showerror("All fields must required to fill")
        else:
            conn=pymysql.connect(host="localhost",user="root",password='112233',db='omdata')
            cur=conn.cursor()
            cur.execute("update hms set Name=%s,Mobile_No=%s,Adhar_No=%s,Check_in=%s,Check_out=%s,No_Guest=%s, Bill=%s where Room_No=%s",(
                                                                                self.n.get(),
                                                                                self.mn.get(),
                                                                                self.an.get(),
                                                                                self.ci.get(),
                                                                                self.co.get(),
                                                                                self.ng.get(),
                                                                                self.b1.get(),
                                                                                self.upd.get()

        ))
        conn.commit()
        self.clear()
        conn.close()
        messagebox.showinfo("Customer Info", "Customer Information Updated Successfully")
        self.upd.set('')
        

root = Tk()
obj = customer(root)
root.mainloop()


#               ************************* MYSQL ***************************
#====================To create table
# db = mysql.connector.connect(host = 'localhost', user = "root", passwd = "112233", database = "omdata")
# cursor = db.cursor()
# sql = "create table hms(Room_No varchar(25), Name varchar(25),Mobile_No varchar(25),Adhar_No varchar(25),Check_in varchar(25), Check_out varchar(25), No_Guest varchar(25),Bill varchar(25), primary key(Mobile_No));"
# cursor.execute(sql)
# db.close()