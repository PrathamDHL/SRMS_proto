#This is the gui for login window, takes input and enters for connection with server of microsoft sql
import mysql.connector as mysqlc

import customtkinter


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
# mydb = None

global connect

def connect(user, passwd):
    global mydb
    mydb = mysqlc.connect(
    host="localhost",
    user= user,
    passwd= passwd
)


class Login( customtkinter.CTk):
    global mydb
    def __init__(self):
        self.name = ""
        self.passwd = ""
        super().__init__()

        self.geometry("550x650")
        self.title("School System Management System")
        self.iconbitmap("MBS.ico")
        self.r = customtkinter.CTkFrame(self, corner_radius=4, border_width=3, width =500, height = 600)

        self.user_text = customtkinter.CTkLabel(self, width=200, height=70, text="Login In", font=("Helvetica Bold", 30) )

        self.login = customtkinter.CTkEntry(self, placeholder_text="Username", width=200, height=40, border_color="Black")
        self.password = customtkinter.CTkEntry(self, placeholder_text="Password", width=200, height=40, border_color="Black", show="*")

        def f_username(self, name): 
            return name 
        
        
        def get_user(self): 
                self.name = str(self.login.get())
            # print (self.name)
            
        def get_pass(self): 
            self.get_pass = str(self.password.get())


        def main(self):
                    print(self.name)
                    print (self.passwd)
                    self.name = str(self.login.get())
                    self.passwd = str(self.password.get())

                    if self.name == "root" and self.passwd == "Toshiba18":
                        connect((self.name), (self.passwd))
                        print("CONNECTED")
                        self.destroy()
                    else: print("Wrong Conditions")
                    


        self.y = customtkinter.CTkEntry(self)
        self.x = customtkinter.CTkButton(self, 100, 45,text= "Connect to Database", corner_radius=10 , text_color="white") 
        self.user_text.pack()
        self.login.place(x = 170, y = 200)
        self.password.place(x = 170, y = 300 + 50)
        self.x.place(x = 225,y = 600)
        self.r.place(x = 25, y =25)
        self.x._command = lambda: main(self)




root= Login()
root.mainloop()
cursor = mydb.cursor()


