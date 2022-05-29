from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime 


class FaceRecognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Management System")


        img = Image.open(r"C:\Attendance-Management-System-using-Facial-Recognition\images_for_app\flat-g1a4c70935_1280.png")
        img = img.resize((650,700),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img= Label(self.root,image = self.photoimg)
        bg_img.place(x=450,y=0,width = 650 , height=700)


         #Button
        b1_1 = Button(bg_img,text = "FACE RECOGNITION",command=self.face_reco,cursor ="hand2",font =("Alegraya sans SC",18,"bold"),fg ="white",bg = "black")
        b1_1.place(x=200,y=600,width = 250 ,height=40)
    

    #attendance+=======


    def mark_attendance(self,d,r,i):
        with open("Attendance_report/atte.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((d not in name_list) and(r not in name_list) and (i not in name_list) ) :
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{d},{r},{i},{dtString},{d1},Present")
                   
        
   


        #+++=====face recognition======++++
    def face_reco(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host ="localhost",username="root",password="aakriti_du001",database="face_reco")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_ID="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
        

                my_cursor.execute("select Roll from student where Student_ID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)


                my_cursor.execute("select department from student where Student_ID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)



                if confidence>77:
                    cv2.putText(img,f"Department:{d}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(d,r,i)                 
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                 
                coord=[x,y,w,y]

            return coord    
        

        def recognize(img,clf,faceCascade):
             coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"face",clf)
             return img
        
       
    
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")


        video_cap=cv2.VideoCapture(0) 
        


 

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)


            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__== "__main__" :
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
