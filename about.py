from cProfile import label
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import pymysql

class web:
    def __init__(self, root):
        self.window = root
        self.window.title("RS Database")
        # Set the window size
        # Here 0,0 represents the starting point of the window 
        self.window.geometry("1366x768+0+0")
        self.window.config(bg = "white")


        self.frame1 = Frame(self.window,bg="white", width=9000, height=750)
        self.frame1.place(x=0, y=0)


        self.detail4_label = Label(self.frame1,text="Coronavirus disease (COVID-19) is an infectious disease \n caused by the SARS-CoV-2 virus.\nMost people infected with the virus will experience\n  mild to moderate respiratory illness and recover without \n  requiring special treatment. However, some will become seriously ill\n and require medical attention. Older people and those with underlying medical conditions \n like cardiovascular disease, diabetes, chronic respiratory disease,\n  or cancer are more likely to develop serious illness. Anyone can get sick with COVID-19 and become seriously \n ill or die at any age. The best way to prevent and slow down\n  transmission is to be well informed about the disease and how\n the virus spreads. Protect yourself and others from infection \nby staying at least 1 metre apart from others, wearing a properly\n fitted mask, and washing your hands or using an alcohol-based\n rub frequently. Get vaccinated when it’s your \nturn and follow local guidance.The virus \ncan spread from an infected person’s mouth \nor nose in small liquid particles when they \ncough, sneeze, speak, sing or \nbreathe. These particles range from larger respiratory\n droplets to smaller aerosols. It is important to practice respiratory etiquette,\n for example by coughing into a flexed elbow, and to stay home and \nself-isolate until you recover if you feel unwell.", font=("helvetica",20,"bold"),bg="white", fg="black").place(x=0,y=0)




if __name__ == "__main__":
    root = Tk()
    obj = web(root)
    root.mainloop()