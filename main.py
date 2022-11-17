import mysql.connector as c
import mysql.connector as c
con=c.connect(host="localhost", user="root", passwd="rahulsehrakv14",port=3306, database="mute")
if con.is_connected():
    print("Done Proced next step..")
    
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql
import os
from happy import mood
from bed_reservation import reservation
from about import web




class covid_management:
    def __init__(self, root):
        self.window = root
        self.window.title("RS Database")
        # Set the window size
        # Here 0,0 represents the starting point of the window 
        self.window.geometry("1366x768+0+0")
        self.window.config(bg = "white")




        self.frame1 = Frame(self.window,  width=2000, height=120)
        self.frame1.place(x=0, y=0)

        label1 = Label(self.frame1, text= "covid management system", font=("times new roman", 40, "bold"), bg="white", fg="black", bd=20).place(x=300,y=10)

        self.frame2=Frame(self.window , bg="pink")
        self.frame2.place(x=0,y=120,width=650,relheight=1)

        self.frame3=Frame(self.window,bg="gold")
        self.frame3.place(x=600,y=120,width=760,relheight=1)


        self.patient_label = Label(self.frame2,text="Patient Name", font=("helvetica",20,"bold"),bg="pink", fg="gray").place(x=20,y=30)
        self.patient_entry = Entry(self.frame2,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.patient_entry.place(x=250, y=40, width=300)


        self.id_label = Label(self.frame2,text="Patient id", font=("helvetica",20,"bold"),bg="pink", fg="gray").place(x=20,y=70)
        self.id_entry = Entry(self.frame2,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.id_entry.place(x=250, y=80, width=300)

        self.age_label = Label(self.frame2,text="age", font=("helvetica",20,"bold"),bg="pink", fg="gray").place(x=20,y=110)
        self.age_entry = Entry(self.frame2,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.age_entry.place(x=250, y=120, width=300)

        self.dob_label = Label(self.frame2,text="D.O.B", font=("helvetica",20,"bold"),bg="pink", fg="gray").place(x=20,y=150)
        self.dob_entry = Entry(self.frame2,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.dob_entry.place(x=250, y=160, width=300)

        self.mail_label = Label(self.frame2,text="email", font=("helvetica",20,"bold"),bg="pink", fg="gray").place(x=20,y=190)
        self.mail_entry = Entry(self.frame2,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.mail_entry.place(x=250, y=200, width=300)

        self.mail_label = Label(self.frame2,text="Be fast, have no regrets... If you need to be right before you move, you will never win", font=("helvetica",10,"bold"),bg="lime",width=80, fg="red").place(x=0,y=580)
      
        self.mail_label = Label(self.frame2,text="It’s going to disappear. One day, it’s like a miracle, it will disappear", font=("helvetica",10,"bold"),bg="lime",width=80, fg="red").place(x=0,y=540)
       
        self.mail_label = Label(self.frame2,text="With COVID-19, we’ve made it to the life raft. Dry land is far away", font=("helvetica",10,"bold"),bg="lime",width=80, fg="red").place(x=0,y=500)



        self.beds_label=Label(self.frame3,text="Dashboard",font=("arial",50,"bold"),bg="yellow",fg="blue").place(x=20,y=30)


        self.insert = Button(self.frame3,text="Personel info",command=self.cold_w,font=("times new roman",18, "bold"),bd=0,cursor="hand2",fg="white",bg="lime").place(x=100,y=200,width=200)
       
       
        self.insert = Button(self.frame3,text="Bed Regestration",command=self.regestration,font=("times new roman",18, "bold"),bd=0,cursor="hand2",fg="white",bg="lime").place(x=100,y=320,width=200)
       
        self.insert = Button(self.frame3,text="About",command=self.web,font=("times new roman",18, "bold"),bd=0,cursor="hand2",fg="white",bg="lime").place(x=100,y=420,width=200)






        self.signup = Button(self.frame2,text="Sign Up",command=self.signup_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=120,y=350,width=250)

    def signup_func(self):
        if self.patient_entry.get=="" or self.id_entry.get=="" or self.age_entry.get=="" or self.dob_entry.get=="" or self.mail_entry.get=="":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
            

    
        else:
            try:
                connection = pymysql.connect(host="localhost", user="root", passwd="rahulsehrakv@14", database="mute")
                cur = connection.cursor()
                cur.execute("select * from gun ")
                row=cur.fetchone()
                cur.execute("insert into gun (patient_name,patient_id,patient_age,patient_dob,mail) values(%s,%s,%s,%s,%s)",
                                    (
                                        self.patient_entry.get(),
                                        self.id_entry.get(),
                                        self.age_entry.get(),
                                        self.dob_entry.get(),
                                        self.mail_entry.get()
                                    
                                    ))
                connection.commit()
                connection.close()
                messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                self.reset_fields()
            except Exception as es:
                messagebox.showerror("Error!",f"Error due to {es}",parent=self.window)

    def reset_fields(self):
        self.patient_entry.delete(0, END)
        self.id_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.dob_entry.delete(0, END)
        self.mail_entry.delete(0, END)

    def cold_w(self):
        self.new_window=Toplevel(self.window)
        self.app=mood(self.new_window)

    def regestration(self):
        self.new_window=Toplevel(self.window)
        self.app=reservation(self.new_window)
   
    def web(self):
        self.new_window=Toplevel(self.window)
        self.app=web(self.new_window)






       
       

if __name__ == "__main__":
    root = Tk()
    obj = covid_management(root)
    root.mainloop()