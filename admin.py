from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Admin:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Management System")


        img = Image.open(r"C:\Attendance-Management-System-using-Facial-Recognition\images_for_app\bg_image.png")
        img = img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img= Label(self.root,image = self.photoimg)
        bg_img.place(x=0,y=0,width = 1530 , height=790)


        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=1000,y=0,width=500,height=600)


        img1 = Image.open(r"C:\Attendance-Management-System-using-Facial-Recognition\images_for_app\admin.png")
        img1= img1.resize((200,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img= Label(main_frame,image = self.photoimg1)
        bg_img.place(x=300,y=0,width = 200 , height=200)

        #Admin info

        admin_label = Label(main_frame,text=" Hello I am Admin",font=("times new roman",20,"bold"))
        admin_label.place(x=0,y=5)

        email_label = Label(main_frame,text=" aakritidubey51@gmail.com",font=("times new roman",13,"bold"))
        email_label.place(x=0,y=40)






if __name__== "__main__" :
    root = Tk()
    obj = Admin(root)
    root.mainloop()
