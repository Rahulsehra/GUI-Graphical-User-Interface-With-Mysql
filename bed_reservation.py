import mysql.connector as c
con=c.connect(host="localhost", user="root", passwd="rahulsehrakv14", database="reg")
if con.is_connected():
    print("Done Proced next step..")
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import pymysql


class reservation:
    def __init__(self, root):
        self.window = root
        self.window.title("RS Database")
        # Set the window size
        # Here 0,0 represents the starting point of the window 
        self.window.geometry("1366x768+0+0")
        self.window.config(bg = "white")

        
        self.frame1 = Frame(self.window,bg="gold", width=9000, height=750)
        self.frame1.place(x=0, y=0)

        label1 = Label(self.frame1, text= "Beds Booked/left", font=("times new roman", 40, "bold"), bg="gold", fg="red",width=30, bd=30).place(x=180,y=10)



        self.detail_label = Label(self.frame1,text=" Patient Name", font=("helvetica",20,"bold"),bg="gold", fg="white").place(x=30,y=195)
        self.my_entry = Entry(self.frame1,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.my_entry.place(x=250, y=200, width=300) 
      
        self.detail_label = Label(self.frame1,text=" Bed ID", font=("helvetica",20,"bold"),bg="gold", fg="white").place(x=800,y=185)
        self.b_entry = Entry(self.frame1,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.b_entry.place(x=950, y=190, width=300) 


        self.detail_label = Label(self.frame1,text=" Bed Reg No", font=("helvetica",20,"bold"),bg="gold", fg="white").place(x=30,y=270)
        self.c_entry = Entry(self.frame1,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.c_entry.place(x=250, y=278, width=300) 


        self.detail_label = Label(self.frame1,text="Date", font=("helvetica",20,"bold"),bg="gold", fg="white").place(x=800,y=270)
        self.d_entry = Entry(self.frame1,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.d_entry.place(x=950, y=278, width=300) 



        
        self.detail_label = Label(self.frame1,text="Room No", font=("helvetica",20,"bold"),bg="gold", fg="white").place(x=30,y=355)
        self.e_entry = Entry(self.frame1,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.e_entry.place(x=250, y=357, width=300) 


        self.detail_label = Label(self.frame1,text="Category", font=("helvetica",20,"bold"),bg="gold", fg="white").place(x=800,y=350)
        self.cat = ttk.Combobox(self.frame1,font=("helvetica",13),state='readonly',justify=CENTER)
        self.cat.place(x=950, y=352,width=300)
        self.cat['values'] = ("Select","Defence","Private","VIP")
        self.cat.current(0)
        
    


        self.detail_label = Label(self.frame1,text=" Bed Type", font=("helvetica",20,"bold"),bg="gold", fg="white").place(x=30,y=430)
        self.type = ttk.Combobox(self.frame1,font=("helvetica",13),state='readonly',justify=CENTER)
        self.type.place(x=250,y=439,width=300)
        self.type['values'] = ("Select","Covid Bed","General Bed","Emergency Bed")
        self.type.current(0)
       
        self.detail_label = Label(self.frame1,text="Purpose/", font=("helvetica",20,"bold"),bg="gold", fg="white").place(x=800,y=430)
        self.detail_label = Label(self.frame1,text="Condition", font=("helvetica",20,"bold"),bg="gold", fg="white").place(x=800,y=465)
        self.f_entry = Entry(self.frame1,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.f_entry.place(x=950,y=436, width=300,height=250)

        self.Register = Button(self.frame1,text="Register",command=self.bistar,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="red",fg="white").place(x=250,y=550,width=250)




    def bistar(self):
        if self.my_entry.get()=="" or self.b_entry.get=="" or self.c_entry.get=="" or self.d_entry.get=="" or self.e_entry.get=="" or self.f_entry.get=="" or self.cat.get() == "Select" or self.type.get()=="Select" :
 
                messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
 
        else:
                try:
                    connection = pymysql.connect(host="localhost", user="root", passwd="rahulsehrakv@14", database="reg")
                    cur = connection.cursor()
                    cur.execute("select * from bed")
                    row=cur.fetchone()
                    cur.execute("insert into bed (patient_name,ben_id,bed_reg_no,date_,room_no,category,bed_type,purpose) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                    (
                                        self.my_entry.get(),
                                        self.b_entry.get(),
                                        self.c_entry.get(),
                                        self.d_entry.get(),
                                        self.e_entry.get(),
                                        self.f_entry.get(),
                                        self.cat.get(),
                                        self.type.get()
                                    
                                    ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                    self.reset_fields()
                except Exception as es:
                     messagebox.showerror("Error!",f"Error due to {es}",parent=self.window)



    def reset_fields(self):
        self.my_entry.delete(0,END)
        self.b_entry.delete(0,END)
        self.c_entry.delete(0,END)
        self.d_entry.delete(0,END)
        self.e_entry.delete(0,END)
        self.f_entry.delete(0,END)
        self.cat.delete(0,END)
        self.type.delete(0,END)
   






       







        



if __name__ == "__main__":
    root = Tk()
    obj = reservation(root)
    root.mainloop()












