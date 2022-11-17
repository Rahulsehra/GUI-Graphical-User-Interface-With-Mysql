import mysql.connector as c
con=c.connect(host="localhost", user="root", passwd="rahulsehrakv14", database="happy")
if con.is_connected():
    print("Done Proced next step..")

from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import pymysql


class mood:
    def __init__(self, root):
        self.window = root
        self.window.title("RS Database")
        # Set the window size
        # Here 0,0 represents the starting point of the window 
        self.window.geometry("1366x768+0+0")
        self.window.config(bg = "white")


#################frame #############
        self.frame1 = Frame(self.window, width=800,bg="silver", height=750)
        self.frame1.place(x=0, y=0)
      
      ################frame 2 ##############################
        self.frame2 = Frame(self.window, width=800,bg="gold", height=750)
        self.frame2.place(x=800, y=0)

       

        label1 = Label(self.frame1, text= "Personel Details", font=("times new roman", 40, "bold"), bg="white", fg="black", bd=20).place(x=180,y=10)




        
        self.detail_label = Label(self.frame1,text=" First Name", font=("helvetica",20,"bold"),bg="silver", fg="black").place(x=20,y=135)
        self.a_entry = Entry(self.frame1,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.a_entry.place(x=200, y=140, width=300) 
 
        self.detail_label = Label(self.frame1,text=" last Name", font=("helvetica",20,"bold"),bg="silver", fg="black").place(x=20,y=175)
        self.b_entry = Entry(self.frame1,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.b_entry.place(x=200, y=180, width=300)
       
       
        self.detail2_label = Label(self.frame1,text=" Phone No ", font=("helvetica",20,"bold"),bg="silver", fg="black").place(x=20,y=215)
        self.c_entry = Entry(self.frame1,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.c_entry.place(x=200, y=220, width=300)
       
       
        self.detail3_label = Label(self.frame1,text=" Address ", font=("helvetica",20,"bold"),bg="silver", fg="black").place(x=20,y=255)
        self.d_entry = Entry(self.frame1,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.d_entry.place(x=200, y=260,height=50, width=400)
       
       
        self.detail4_label = Label(self.frame1,text=" Father name", font=("helvetica",20,"bold"),bg="silver", fg="black").place(x=20,y=345)
        self.e_entry = Entry(self.frame1,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.e_entry.place(x=200, y=350, width=400)
       
        self.detail5_label = Label(self.frame1,text=" Blood group", font=("helvetica",20,"bold"),bg="silver", fg="black").place(x=20,y=380)
        self.f_entry = Entry(self.frame1,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.f_entry.place(x=200, y=390, width=400)

        self.Register = Button(self.frame1,text="Register",command=self.winter,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="red",fg="white").place(x=150,y=470,width=250)
##########################add +++++25 ++++ in y ##################################################
        self.intro=Label(self.frame2,text="Tips for creating an information form ", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=10)
        self.intro=Label(self.frame2,text="Here are some tips to help you create an effective information form for employees: ", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=30)
        self.intro=Label(self.frame2,text="\fClarity: Keep the info form & instructions straightforward and easy to understand. ", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=55)
        self.intro=Label(self.frame2,text="\fStandard format: Create a common form for all employees.ensure complete form  ", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=105)
        self.intro=Label(self.frame2,text=" \n  ", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=130)
        self.intro=Label(self.frame2,text="\fLogical order: Ensure the form follows a logical order that most people are ", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=155)
        self.intro=Label(self.frame2,text="used to completing", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=180)
        self.intro=Label(self.frame2,text=" \n ", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=205)
        self.intro=Label(self.frame2,text="\fData accessibility: Ensure that the appropriate parties, such as your HR team", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=230)
        self.intro=Label(self.frame2,text="and the employee's manager, can access data.", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=255)
        self.intro=Label(self.frame2,text="\n", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=280)
        self.intro=Label(self.frame2,text="\fSafe storage: Use cloud-based HR software and work with your information techno ", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=305)
        self.intro=Label(self.frame2,text="logy (IT) or data privacy professional to ensure you follow safe data practices ", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=330)
        self.intro=Label(self.frame2,text="for storing sensitive personal information. Ensure you learn all local ", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=355)
        self.intro=Label(self.frame2,text="and international laws, if applicable, regarding personal information. ", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=380)
        self.intro=Label(self.frame2,text="\n ", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=405)
        self.intro=Label(self.frame2,text="\fBe transparent: Only ask for information that the business requires.", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=430)
        self.intro=Label(self.frame2,text="Let employees know the organisation would not disclose their information  ", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=455)
        self.intro=Label(self.frame2,text="to unauthorised company members.", font=("helvetica",10,"bold"),bg="gold", fg="black").place(x=20,y=480)


    def winter(self):
            if self.a_entry.get()=="" or self.b_entry.get=="" or self.c_entry.get=="" or self.d_entry.get=="" or self.e_entry.get=="" or self.f_entry.get==""  :
                messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
 
            else:
                try:
                    connection = pymysql.connect(host="localhost", user="root", passwd="rahulsehrakv@14", database="happy")
                    cur = connection.cursor()
                    cur.execute("select * from mood ")
                    row=cur.fetchone()
                    cur.execute("insert into mood (first_name,last_name,phone_no,address,father_name,blood_group) values(%s,%s,%s,%s,%s,%s)",
                                    (
                                        self.a_entry.get(),
                                        self.b_entry.get(),
                                        self.c_entry.get(),
                                        self.d_entry.get(),
                                        self.e_entry.get(),
                                        self.f_entry.get()
                                    
                                    ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                    self.reset_fields()
                except Exception as es:
                     messagebox.showerror("Error!",f"Error due to {es}",parent=self.window)



    def reset_fields(self):
        self.a_entry.delete(0,END)
        self.b_entry.delete(0,END)
        self.c_entry.delete(0,END)
        self.d_entry.delete(0,END)
        self.e_entry.delete(0,END)
        self.f_entry.delete(0,END)
    



if __name__ == "__main__":
    root = Tk()
    obj = mood(root)
    root.mainloop()
        