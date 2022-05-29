from time import strftime
from datetime import datetime
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import FaceRecognition
from attendance import Attendance
from admin import Admin


class Attendance_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Management System")

        img = Image.open(r"C:\Attendance-Management-System-using-Facial-Recognition\images_for_app\bg_image.png")
        img = img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img= Label(self.root,image = self.photoimg)
        bg_img.place(x=0,y=0,width = 1530 , height=790)


        #+++++++++++time+++++++++++
        def time():
             string=strftime('%H:%M:%S %p')
             lbl.config(text=string)
             lbl.after(1000,time)
        
        lbl = Label(bg_img,text="Search By:",font=("times new roman",13,"bold"),bg="white",fg="black")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        



       
        #student button
        img2 = Image.open(r"C:\Attendance-Management-System-using-Facial-Recognition\images_for_app\login.png")
        img2= img2.resize ((220,220),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(bg_img,image=self.photoimg2,command=self.student_details,cursor = "hand2")
        b1.place(x=200,y=100,width = 220 ,height=220)

        b1_1 = Button(bg_img,text = "Details",cursor ="hand2",command=self.student_details,font =("Alegraya sans SC",15,"bold"),fg ="white",bg = "black")
        b1_1.place(x=200,y=300,width = 220 ,height=40)

        
        #detect face button
        img3 = Image.open(r"C:\Attendance-Management-System-using-Facial-Recognition\images_for_app\flat-g1a4c70935_1280.png")
        img3= img3.resize ((220,220),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg_img,image=self.photoimg3,cursor = "hand2",command=self.face_data)
        b1.place(x=500,y=100,width = 220 ,height=220)

        b1_1 = Button(bg_img,text = "Face Recognition",cursor ="hand2",command=self.face_data,font =("Alegraya sans SC",15,"bold"),fg ="white",bg = "black")
        b1_1.place(x=500,y=300,width = 220 ,height=40)
        

        #Attendance face button
        img4 = Image.open(r"C:\Attendance-Management-System-using-Facial-Recognition\images_for_app\atte.png")
        img4= img4.resize ((220,220),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image=self.photoimg4,cursor = "hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width = 220 ,height=220)

        b1_1 = Button(bg_img,text = "Attendance",cursor ="hand2",command=self.attendance_data,font =("Alegraya sans SC",15,"bold"),fg ="white",bg = "black")
        b1_1.place(x=800,y=300,width = 220 ,height=40)




         #Train  button
        img5 = Image.open(r"C:\Attendance-Management-System-using-Facial-Recognition\images_for_app\train.jpeg")
        img5= img5.resize ((220,220),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,cursor = "hand2",command=self.train_data)
        b1.place(x=1100,y=100,width = 220 ,height=220)

        b1_1 = Button(bg_img,text = "Train data",cursor ="hand2",command=self.train_data,font =("Alegraya sans SC",15,"bold"),fg ="white",bg = "black")
        b1_1.place(x=1100,y=300,width = 220 ,height=40)




         #Images button
        img6 = Image.open(r"C:\Attendance-Management-System-using-Facial-Recognition\images_for_app\folder.png")
        img6= img6.resize ((220,220),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image=self.photoimg6,cursor = "hand2",command=self.open_img)
        b1.place(x=400,y=380,width = 220 ,height=220)

        b1_1 = Button(bg_img,text = "Images",cursor ="hand2",command=self.open_img,font =("Alegraya sans SC",15,"bold"),fg ="white",bg = "black")
        b1_1.place(x=400,y=580,width = 220 ,height=40)




        #Admin button
        img7 = Image.open(r"C:\Attendance-Management-System-using-Facial-Recognition\images_for_app\admin.png")
        img7= img7.resize ((220,220),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image=self.photoimg7,cursor = "hand2",command=self.admin_data)
        b1.place(x=710,y=380,width = 220 ,height=220)

        b1_1 = Button(bg_img,text = "Admin",cursor ="hand2",command=self.admin_data,font =("Alegraya sans SC",15,"bold"),fg ="white",bg = "black")
        b1_1.place(x=710,y=580,width = 220 ,height=40)



        #Exit button
        img8 = Image.open(r"C:\Attendance-Management-System-using-Facial-Recognition\images_for_app\exit.png")
        img8= img8.resize ((220,220),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image=self.photoimg8,cursor = "hand2",command=self.iExit)
        b1.place(x=1000,y=380,width = 220 ,height=220)

        b1_1 = Button(bg_img,text = "Exit",cursor ="hand2",command=self.iExit,font =("Alegraya sans SC",15,"bold"),fg ="white",bg = "black")
        b1_1.place(x=1000,y=580,width = 220 ,height=40)
    def open_img(self):
        os.startfile("Data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to Exit this System",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
              return    

     #==================Function buttons=============

    def student_details(self):
         self.new_window=Toplevel(self.root)
         self.app=Student(self.new_window)
    
    def train_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Train(self.new_window)
    
    

    def face_data(self):
         self.new_window=Toplevel(self.root)
         self.app=FaceRecognition(self.new_window)

    def attendance_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Attendance(self.new_window)     
     

    def admin_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Admin(self.new_window)






        






if __name__== "__main__" :
    root = Tk()
    obj = Attendance_System(root)
    root.mainloop()
