# This is the MAIN MODULE that has all the modules for the "Home" i.e. MAJOR PART OF THE PROGRAM. 
from tkinter import messagebox
from ctktable_1 import CTkTable
import customtkinter
import os
from PIL import Image
import mysql.connector as mysqlc
mydb = mysqlc.connect(host="localhost",user= "root",passwd= "Password123", database = "maindb")
global student_column_names, rows
cursor = mydb.cursor()
cursor_2 = mydb.cursor()
cursor_3 = mydb.cursor()
cursor_4 = mydb.cursor()
cursor_5_for_student_add = mydb.cursor()
cursor.execute(" SELECT * FROM students where 1=0; ")
while cursor.fetchone() is not None:
    pass
student_column_names = [col[0] for col in cursor.description ]
print("Column Names:", student_column_names)
print (student_column_names[1])
cursor_2.execute("SELECT * FROM students")
rows = cursor_2.fetchall()
rows = [student_column_names] + rows
print(rows)
cursor_3.execute("SELECT * FROM class where 1=0;")
while cursor_3.fetchone() is not None:
    pass
class_column_names = [col[0] for col in cursor_3.description]
print( str(class_column_names))
cursor_4.execute("SELECT * FROM class;")
c_rows = cursor_4.fetchall()
c_rows = [class_column_names]+ c_rows
print(c_rows)
cursor_5 = mydb.cursor()
cursor_5.execute("SET GLOBAL sql_safe_updates = 0;")
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("dark-blue")
Home = customtkinter.CTk()
Home.eval('tk::PlaceWindow . center')
Home.iconbitmap("MBS.ico")
width= Home.winfo_screenwidth()               
height= Home.winfo_screenheight()              
Home.geometry(f'{width}x{height}+{0}+{0}')
Home.state('zoomed')
Home.title("Millsberry School Database")
r = customtkinter.CTkFrame(Home, corner_radius = 4, border_width=2, width=500, height=600)
Main_frame = customtkinter.CTkFrame(Home, width =(255), height=(height), fg_color=("white","black") )
user_text = customtkinter.CTkLabel(Home, width=350, height=150, text="                Millsberry Database", font=customtkinter.CTkFont(size = 38, weight = "bold"), bg_color="transparent", fg_color="transparent")
Main_frame.place (x = 0, y = 0 )
user_text.pack()
count_add = 0 
def textt(n):
    global text 
    text = n 
def Show_Message(Message):
    messagebox.showinfo(Message, "Go to Home")
    Home.destroy()
    os.system('python3.11.exe Home.py')
def Print_error(error):
    messagebox.showerror('Error Message ', f'{error}')
    Home.destroy()
    os.system('python3.11.exe Home.py')
global a 
a = 0
def close_():
    global a
    if a == 1:
        a = 0 
        tabview.destroy()
def Display():  
        global a, tabview, b
        tabview = customtkinter.CTkTabview(Home, width=1150, height= height-300)
        if a == 0:
            a = 1
            tabview.place(x = (width/2)-500, y = 150)
            tabview.add("STUDENTS TABLE") 
            tabview.add("CLASS TABLE")
            scrollable_frame = customtkinter.CTkScrollableFrame(tabview.tab("STUDENTS TABLE"), width=1150, height=height-400, bg_color="transparent")
            scrollable_frame.pack()
            scrollable_frame_switches = []
            table_1 = CTkTable(scrollable_frame, row=len(rows), column=len(student_column_names), values=rows, header_color="Orange", height = 30 , padx=0, pady=1,border_color="Black",  font =('Anaheim', 20),)
            table_1.pack()
            scrollable_frame_2 = customtkinter.CTkScrollableFrame(tabview.tab("CLASS TABLE"), width=1150, height=height-400)
            scrollable_frame_2.pack()
            scrollable_frame_switches = []
            table_2 = CTkTable(scrollable_frame_2, row=len(c_rows), column=len(class_column_names), values=c_rows, header_color="Orange",border_color='black', width = 200, font = ('Anaheim', 20) ,  hover_color="#d0d0d0", height = 40  )
            table_2.pack()
Display()
def  dialog_class_add():
    entry_widgets_student = []
    entry = customtkinter.CTkInputDialog(text=f"Enter the class to append : ", title ="ADD", )
    entry.configure(height = height - 300,width = 1150)
    abc = int(str(entry.get_input()))
    print(abc)
    for i in range(1, len(class_column_names)):
            ad = customtkinter.CTkInputDialog(text=f"Enter value for {class_column_names[i]}", title = "Add to Class Table")
            ad.configure(height = height - 300,width = 1150)
            entry_value = str(ad.get_input())
            if i == 3 : entry_value = int( entry_value )
            entry_widgets_student.append(entry_value)
    print(entry_widgets_student)    
    cursor_add_c = mydb.cursor()
    entered  = entry_widgets_student
    try:
            i = 1
            j = 0
            q = f"INERT INTO class  ({class_column_names[i]} ,{class_column_names[i+1]},{student_column_names[i+2]} ,{class_column_names[i+3]},{class_column_names[i+4]}) VALUES ({entered[j]}, {entered[j+1]}, {entered[j+2]}, '{entered[j+3]}`, '{entered[j+4]}');"
            cursor_add_c.execute(q)
            mydb.commit()
            Show_Message("Succesfully Added But Make sure to Add the data as the value of No. of Students has increased !")
    except mysqlc.Error as err:
        Print_error(err) 
def dialog_students_add():
    entry_add = []
    for i in range(1, len(student_column_names)):
            ad = customtkinter.CTkInputDialog(text=f"Enter value for {student_column_names[i]}", title = "Add to Student Table")
            ad.configure(height = height - 300,width = 1150)
            entry_value = str(ad.get_input())
            if i == 1 : entry_value = int( entry_value )
            entry_add.append(entry_value)
    print(entry_add)
    r = 'Cursor_add'
    locals()[r] = mydb.cursor()
    try: 
        i = 1 
        j = 0 
        locals()[r].execute(f"INSERT INTO students (Class,first_name,last_name,Dob,Section,UniqueID,Address) VALUES (  {entry_add[j]}, '{entry_add[j+1]}', '{entry_add[j+2]}', '{entry_add[j+3]}', '{entry_add[j+4]}', '{entry_add[j+5]}', '{entry_add[j+6]}');",multi=True)
        mydb.commit()
        locals()[r].close()
        cursor_sd = mydb.cursor()
        cursor_sd.execute("SET SQL_SAFE_UPDATES=0;  UPDATE class AS c SET c.`No. of Students` = ( SELECT COUNT(*) FROM students WHERE students.Class = c.Class);",multi=True)
        mydb.commit()
        Show_Message("Succesfully Added")
    except mysqlc.Error as err: Print_error(err)
def Add():
    close_()
    global count_add 
    text = customtkinter.CTkLabel(Home, width=350, height=150, text=" Choose Table to add: ", font=(("Anaheim"), 38), text_color="White" )
    Button_Class = customtkinter.CTkButton(Home, width=220, height=100,font=(("Anaheim"), 25),text="Class Table", command=lambda: dialog_class_add())
    Button_Student = customtkinter.CTkButton(Home, width=220, height=100,font=(("Anaheim"), 25),  text="Student Table", command= lambda: dialog_students_add())
    if count_add == 0 : 
        count_add = 1
        text.place(x = 650, y =100)
        Button_Student.place( x = 700, y = 350  )
        Button_Class.place( x = 700, y = 550  )
    else: 
        count_add = 0 
        Button_Student.place_forget()
        Button_Class.place_forget()
def dialog_class_A():
        text_window = str("Type in the Class to delete")
        dialog_c = customtkinter.CTkInputDialog(text= text_window , title="Add")
        dialog_c.configure(height = height - 300,width = 1150)
        To_delete_A = str(dialog_c.get_input()) 
        if To_delete_A not in str(c_rows): messagebox.showinfo(" No Record Found", "No Such Record Found ")
        else:
            try:
                cursor_d = mydb.cursor()
                cursor_d.execute(f"DELETE FROM grades where Class = {To_delete_A} ;  ") 
                mydb.commit()
                Show_Message("Succesfully Deleted")
            except mysqlc.Error as err: Print_error(err)
def dialog_students_A():    
        text_window = str("Type in the first_name to delete")
        dialog_c = customtkinter.CTkInputDialog(text= text_window , title="Add")
        dialog_c.configure(height = height - 300,width = 1150)
        To_delete = str(dialog_c.get_input()) 
        if To_delete not in str(rows):messagebox.showinfo("No Record Found", "No Such Record Found")
        else:
            try:
                cursor_d = mydb.cursor()
                cursor_d.execute(f"DELETE FROM students where `first_name` LIKE '{To_delete}' ;") 
                mydb.commit()
                Show_Message("Succesfully Deleted !")
            except mysqlc.Error as err:
                Print_error(err)
global count_add_D
count_add_D = 0 
def Delete():
    close_()
    global count_add_D
    textt("D")
    global count_add 
    text = customtkinter.CTkLabel(Home, width=350, height=150, text=" Choose Table to add: ", font=(("Anaheim"), 38), text_color="White" )
    Button_Class_A = customtkinter.CTkButton(Home, width=220, height=100,font=(("Anaheim"), 25),text="Delete in Class Table", command=lambda: dialog_class_A())
    Button_Student_A = customtkinter.CTkButton(Home, width=220, height=100,font=(("Anaheim"), 25),  text="Delete in Student Table", command= lambda: dialog_students_A())
    if count_add_D == 0 : 
        count_add_D = 1
        text.place(x = 650, y =100)
        Button_Student_A.place( x = 700, y = 350  )
        Button_Class_A.place( x = 700, y = 550  )
    else: 
        count_add_D = 0 
        Button_Student_A.place_forget()
        Button_Class_A.place_forget()
count_MOD = 0
def Modify_student():
    entry_widgets_student = []
    entry = customtkinter.CTkInputDialog(text=f"Enter the first name to append : ", title ="Modify")
    entry.configure(height = height - 300,width = 1150)
    ab = f"{entry.get_input()}"
    print(ab)
    if ab in str(c_rows) or ( ab in str(rows)): 
        for i in range(1, len(student_column_names)):
            ad = customtkinter.CTkInputDialog(text=f"Enter value for {student_column_names[i]}")
            ad.configure(height = height - 300,width = 1150)
            entry_value = str(ad.get_input())
            if i == 1 : entry_value = int( entry_value )
            entry_widgets_student.append(entry_value)
        print(entry_widgets_student)    
        cursor_mod = mydb.cursor()
        i = 1AA
        j = i -1
        try: 
            cursor_mod.execute(f"UPDATE students SET {student_column_names[i]} = {entry_widgets_student[j]}, {student_column_names[i+1]} = '{entry_widgets_student[j+1]}', {student_column_names[i+2]} = '{entry_widgets_student[j+2]}', {student_column_names[i+3]} = '{entry_widgets_student[j+3]}', {student_column_names[i+4]} = '{entry_widgets_student[j+4]}', {student_column_names[i+5]} = '{entry_widgets_student[j+5]}', {student_column_names[i+6]} = '{entry_widgets_student[j+6]}'  WHERE first_name = '{ab}';")
            mydb.commit()
            Show_Message("Succesfully Edited")
        except mysqlc.Error as err: Print_error(err)
    else:   
        Print_error("Error : No such first name found")
def Modify_class():
    entry_widgets_student = []
    entry = customtkinter.CTkInputDialog(text=f"Enter the class to append : ", title ="Modify")
    entry.configure(height = height - 300,width = 1150)
    abc = int(str(entry.get_input()))
    print(abc)
    if str(abc) in str(c_rows) or ( str(abc) in str(rows)): 
        for i in range(1, len(class_column_names)):
            ad = customtkinter.CTkInputDialog(text=f"Enter value for {class_column_names[i]}")
            ad.configure(height = height - 300,width = 1150)
            entry_value = str(ad.get_input())
            if i == 3 : entry_value = int( entry_value )
            entry_widgets_student.append(entry_value)
        print(entry_widgets_student)    
        cursor_mod = mydb.cursor()
        try:
            i = 1
            j = 0
            cursor_mod.execute(f"UPDATE students SET {class_column_names[i]} = {entry_widgets_student[j]}, {class_column_names[i+1]} = {class_column_names[j+1]}, {student_column_names[i+2]} = {entry_widgets_student[j+2]}, {class_column_names[i+3]} = '{entry_widgets_student[j+3]}', {class_column_names[i+4]} = '{entry_widgets_student[j+4]}'  WHERE class = {abc};")
            Show_Message("Succesfully Edited")
            
        except mysqlc.Error as error : Print_error(error)
    else:
        Print_error("Error No such first name found")
count_add_mod = 0 
def Modify():
    close_()
    global count_add_mod
    text = customtkinter.CTkLabel(Home, width=350, height=150, text=" Choose Table to add: ", font=(("Anaheim"), 38), text_color="White" )
    Button_Class = customtkinter.CTkButton(Home, width=220, height=100,font=(("Anaheim"), 25),text="Student Table", command=lambda: Modify_student())
    Button_Student = customtkinter.CTkButton(Home, width=220, height=100,font=(("Anaheim"), 25),  text="Class Table",command= lambda: Modify_class())
    if count_add_mod == 0 : 
        count_add_mod = 1
        text.place(x = 650, y =100)
        Button_Student.place( x = 700, y = 350  )
        Button_Class.place( x = 700, y = 550  )
    else: 
        count_add_mod = 0 
        Button_Student.place_forget()
        Button_Class.place_forget()
def convert_to_int(abcd):
            try:  
                integer = int(abcd)
                return integer
            except ValueError: 
                return str(f'"{abcd}"')
def get_column_names(table):
    cursor_a = mydb.cursor()
    cursor = mydb.cursor()
    sql_query = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}'"
    cursor.execute(sql_query)
    column_names = tuple((column[0],) for column in cursor_a.fetchall())
    return column_names
def change_appearance_mode_event( new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
r = 0 
def Search():
    global r, test
    test = 1
    if r == 0: 
        r = 1
        textt("S")
        text_window = str("Type the keyword")
        dialog = customtkinter.CTkInputDialog(text= text_window , title="SEARCH WINDOW")
        dialog.configure(height = height - 300,width = 1150)
        Value_entered = str(dialog.get_input())
        global a,  b, c
        cursor_s = mydb.cursor()
        cursor_c = mydb.cursor()
        cursor_c.execute(f" SELECT * FROM class WHERE `S.No.`= {convert_to_int(Value_entered)} OR Class = {convert_to_int(Value_entered)} OR `No. of Students` = {convert_to_int(Value_entered)} OR `No. of Sections` = {convert_to_int(Value_entered)} OR INCHARGE = '{Value_entered}' OR Building = '{Value_entered}';")
        searched_c = cursor_c.fetchall()
        cursor_s.execute(f'SELECT * FROM students WHERE `S,No.` = {convert_to_int(Value_entered)} OR Class = {convert_to_int(Value_entered)} OR first_name = "{Value_entered}" OR last_name = "{Value_entered}" OR Dob = "{Value_entered}" OR Section = "{Value_entered}" OR UniqueID = "{Value_entered}" OR Address = "{Value_entered}";')  
        searched = cursor_s.fetchall()
        if searched == [] and  searched_c == []: Print_error("No such Record Found")
        searched = [student_column_names]+ searched
        searched_c = [class_column_names ] +searched_c
        print (searched)
        print(searched_c) 
        student_column = str(f'{[tuple(student_column_names)]}')
        student_column = list(student_column)
        class_column = str(f'{[tuple(class_column_names)]}')
        class_column = list(class_column)
        tabview = customtkinter.CTkTabview(Home, width=1150, height= height-300)
        tabview.place(x = (width/2)-500, y = 150)
        tabview.add("SEARCH IN STUDENTS TABLE")
        tabview.add("SEARCH IN CLASS TABLE")
        scrollable_frame = customtkinter.CTkScrollableFrame(tabview.tab("SEARCH IN STUDENTS TABLE"), width=1150, height=height-400)
        scrollable_frame.pack()
        scrollable_frame_switches = []
        table = CTkTable(scrollable_frame, row=len(rows), column=len(student_column_names), values=searched, header_color="Orange", height = 30 , padx=1, pady=1,border_color="Black",  font =('Anaheim', 20))
        table.pack()
        scrollable_frame_2 = customtkinter.CTkScrollableFrame(tabview.tab("SEARCH IN CLASS TABLE"), width=1150, height=height-400, fg_color= "transparent")
        scrollable_frame_2.pack()
        scrollable_frame_switches = []
        table_2 = CTkTable(scrollable_frame_2, row=len(c_rows), column=len(class_column_names), values=searched_c, header_color="Orange",border_color='black', width = 200, font = ('Anaheim', 20) ,  hover_color="#d0d0d0", height = 40  )
        table_2.pack()     
def Close():
    Home.destroy()
def Reload():
    Show_Message("Do you want to Reload ? ")

appearance_mode_menu = customtkinter.CTkOptionMenu(Home, values=["Light", "Dark", "System"], command= change_appearance_mode_event, bg_color = ("transparent"))
Button_Close = customtkinter.CTkButton(Home, width=220, height=80,fg_color="transparent", corner_radius=0, font=(("Anaheim"), 25), command= lambda: Reload(), text = "Reload", text_color=("Black", "White"),  hover_color=("Black", "White"))
Button_Close.pack(pady = 6,  anchor = 'w', padx = 20 )
Button_2 = customtkinter.CTkButton(Home, width=220, height=100,font=(("Anaheim"), 25), command= lambda:  Modify(), text = "📝 Modify" , text_color=("Black", "White"),fg_color="transparent") #(Light Mode, DarkMode)
Button_2.pack(pady = 6, anchor = 'w', padx = 20)
Button_3 = customtkinter.CTkButton(Home, width=220, height=100,font=(("Anaheim"), 25), command= lambda: Search(), text = "🔎 Search" ,text_color=("Black", "White"),fg_color="transparent")
Button_3.pack(pady = 6, anchor = 'w', padx = 20 )
Button_4 = customtkinter.CTkButton(Home, width=220, height=100,font=(("Anaheim"), 25), command= lambda: Add(), text = "➕ Add ",text_color=("Black", "White"),fg_color="transparent")
Button_4.pack(pady = 6, anchor = 'w', padx = 20 )
Button_5 = customtkinter.CTkButton(Home, width=220, height=100,font=(("Anaheim"), 25), command= lambda: Delete(), text = "❌ Delete",text_color=("Black", "White"),fg_color="transparent")
Button_5.pack(pady = 6, anchor = 'w', padx = 20 )
appearance_mode_label = customtkinter.CTkLabel(Home ,text="Appearance Mode:", anchor="w", fg_color=("White", "Black"))
appearance_mode_label.pack(padx = 20, anchor='w', pady = 6)
appearance_mode_menu.pack(pady = 6, anchor = 'w', padx = 20)
Home.mainloop()
mydb.close()
