from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Management System")

        title_lbl = Label(self.root, text = "Train Data Set",font =("Alegraya sans SC",35,"bold"),fg ="white",bg = "blue")
        title_lbl.place(x=0,y=0,width=1530,height = 45)

        #Button
        b1_1 = Button(self.root,text = "TRAIN DATA",command=self.train_classifier,cursor ="hand2",font =("Alegraya sans SC",30,"bold"),fg ="white",bg = "black")
        b1_1.place(x=0,y=380,width = 1530 ,height=60)


    def train_classifier(self):
       data_dir=("Data")   #Accessing Directory
       path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
    
       faces=[]
       ids=[]


       for image in path:
           img=Image.open(image).convert('L')  #Image converted to Gray scale 
           imageNp=np.array(img,'uint8')       #Histogram Grid
           id=int(os.path.split(image)[1].split('.')[1]) #indexing and positioning
        
           faces.append(imageNp)
           ids.append(id)
           cv2.imshow("Training..",imageNp)
           cv2.waitKey(1)==13
       ids=np.array(ids)


    #============training the classifier===========

       clf=cv2.face.LBPHFaceRecognizer_create()
       clf.train(faces,ids)
       clf.write("classifier.xml")   #faces and ids binary coded and saved here
       cv2.destroyAllWindows()
       messagebox.showinfo("Result","Training datasets completed!!")







if __name__== "__main__" :
    root = Tk()
    obj = Train(root)
    root.mainloop()
