from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Management System")

        #==========variables=============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_sec=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()         
        
        


        img = Image.open(r"C:\Attendance-Management-System-using-Facial-Recognition\images_for_app\bg_image.png")
        img = img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img= Label(self.root,image = self.photoimg)
        bg_img.place(x=0,y=0,width = 1530 , height=790)


        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=55,width=1500,height=600)

        #left side label frame

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Detail",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height = 580)


        #current course info
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information ",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=10,width=720,height = 150)


        #Department
        dep_label = Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CSE","IT","CE","ME","ECE","CHE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)



        #course
        

        course_label = Label(current_course_frame,text="Course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","TE","BE","SE","B.tech")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label = Label(current_course_frame,text="Year",font=("times new roman",13,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2021","2022","2023","2024","2025","2026")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester

        semester_label = Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Even","Odd")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)



         #Class Student info
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information ",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=200,width=720,height = 320)

        #Student id
        studentId_label = Label(class_student_frame,text="Student ID",font=("times new roman",13,"bold"))
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label = Label(class_student_frame,text="Student Name",font=("times new roman",13,"bold"))
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Section
        section_label = Label(class_student_frame,text="Section",font=("times new roman",13,"bold"))
        section_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

       

        section_combo=ttk.Combobox(class_student_frame,textvariable=self.var_sec,font=("times new roman",13,"bold"),state="readonly",width=20)
        section_combo["values"]=("A","B")
        section_combo.current(0)
        section_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        

        #RollNo
        rollno_label = Label(class_student_frame,text="Roll No",font=("times new roman",13,"bold"))
        rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


       #Gender
        gender_label = Label(class_student_frame,text="Gender",font=("times new roman",13,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)



        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=20)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)


        #DOB
        dob_label = Label(class_student_frame,text="Date of Birth",font=("times new roman",13,"bold"))
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        

        #Email
        email_label = Label(class_student_frame,text="Email",font=("times new roman",13,"bold"))
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone No
        phone_label = Label(class_student_frame,text="Phone No.",font=("times new roman",13,"bold"))
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        address_label = Label(class_student_frame,text="Address",font=("times new roman",13,"bold"))
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take a Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        #button frame

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=210,width=700,height=40)


        save_btn=Button(btn_frame,text="Submit",command=self.add_data,width = 17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width = 17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width = 17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command= self.reset_data,width = 17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=235,width=700,height=30)


        take_a_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take a Photo",width = 35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_a_photo_btn.grid(row=0,column=0)



        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width = 35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


        
        

        


        










         #right side label frame

        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Detail",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=660,height = 580)


        #======================search system==================
        Search_student_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System ",font=("times new roman",12,"bold"))
        Search_student_frame.place(x=5,y=125,width=650,height = 100)


        search_label = Label(Search_student_frame,text="Search By:",font=("times new roman",13,"bold"),bg="green")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_student_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select ","Roll No.","Phone No.","Student ID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry=ttk.Entry(Search_student_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)




        search_btn=Button(Search_student_frame,text="Search",width = 10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_student_frame,text="Show all",width = 10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=650,height = 350)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","sec","roll","gender","dob","email","phone","address","photo"),
        xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side= BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("dob",text="Date of Birth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone no")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #============Function Declaration===============
    def add_data(self):
        if self.var_dep.get()=="Select Dpartment" or self.var_std_name.get()=="" or self.var_std_id.get=="":
            messagebox.showerror("Error","All Feilds are required!",parent=self.root)
        else:
            try:
        
                conn=mysql.connector.connect(host ="localhost",username="root",password="aakriti_du001",database="face_reco")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_sec.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_radio1.get()
                                                                                                            ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Details added successfully!",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)   



    #========fetch data============
    def fetch_data(self):
        conn=mysql.connector.connect(host ="localhost",user="root",password="aakriti_du001",database="face_reco")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()


        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()        


    #========get cursor===========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_sec.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_email.set(data[9]),
        self.var_dob.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_radio1.set(data[13])


    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Dpartment" or self.var_std_name.get()=="" or self.var_std_id.get=="":
            messagebox.showerror("Error","All Feilds are required!",parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update this student detail",parent=self.root)
                if Update >0:
                   conn=mysql.connector.connect(host ="localhost",username="root",password="aakriti_du001",database="face_reco")
                   my_cursor=conn.cursor()
                   my_cursor.execute("update student set department=%s,Year=%s,course=%s,Semester=%s,Section=%s,Roll=%s,Name=%s,Gender=%s,dob=%s,Email=%s,phone=%s,Address=%s,photoSample=%s where Student_ID=%s",(
                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                self.var_sec.get(),
                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.var_std_id.get()
                                                                                                                                                                              ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student DTails successfully updated",parent =self.root)
                conn.commit()
                self.fetch_data()
                conn.close()        
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent= self.root)



    #delete function

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Student Id is required",parent= self.root) 
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","DO you want to delete ",parent = self.root)
                if delete>0:
                   conn=mysql.connector.connect(host ="localhost",username="root",password="aakriti_du001",database="face_reco")
                   my_cursor=conn.cursor()
                   sql="delete from student where Student_ID = %s"
                   val = (self.var_std_id.get(),)
                   my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Deleted!!",parent = self.root)           
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_sec.set("Select Section")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")

    #Generate data set or take photo samples   
    def generate_dataset(self):
        if self.var_dep.get()=="Select Dpartment" or self.var_std_name.get()=="" or self.var_std_id.get=="":
            messagebox.showerror("Error","All Feilds are required!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host ="localhost",username="root",password="aakriti_du001",database="face_reco")
                my_cursor=conn.cursor() 
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set department=%s,Year=%s,course=%s,Semester=%s,Section=%s,Roll=%s,Name=%s,Gender=%s,dob=%s,Email=%s,phone=%s,Address=%s,photoSample=%s where Student_ID=%s",(
                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                self.var_sec.get(),
                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.var_std_id.get()==id+1
                                                                                                                                                                            )) 
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #============load predefined data on frontal face=======
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces= face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor =1.3
                    #Minimum Neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame)is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)   
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set !!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    





if __name__== "__main__" :
    root = Tk()
    obj = Student(root)
    root.mainloop()
