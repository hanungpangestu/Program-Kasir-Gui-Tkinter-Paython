from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import config.db
import home

class LoginWindows:
    def __init__(self):
        self.win = Tk()

        self.canvas = Canvas(self.win, width=600, height=400, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_vrootheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)
        
        #disable resize
        self.win.resizable(width=False, height=False)
        
        #change the title
        self.win.title('Login')
    
    def add_frame(self):
        self.frame = Frame(self.win, height=400, width=600)
        self.frame.place(x=0, y=0)

        x, y = 70, 20

        img = Image.open('img/sign-in.png')
        img = img.resize((100,100), Image.ANTIALIAS)

        self.img = ImageTk.PhotoImage(img)
        self.label = Label(self.frame, image=self.img)
        self.label.place(x=x+170, y=y+0)

        self.labeltitle = Label(self.frame, text="Silahkan login")
        self.labeltitle.config(font=("Courier", 20, 'bold'))
        self.labeltitle.place(x=180, y=y+110)

        self.emlabel = Label(self.frame, text='Username')
        self.emlabel.config(font=('Courier', 15, 'bold'))
        self.emlabel.place(x=120, y=y+170)

        self.uname = Entry(self.frame, font='Courier 12')
        self.uname.place(x=240, y=y+170)

        self.pslabel = Label(self.frame, text='Password')
        self.pslabel.config(font=('Courier', 15, 'bold'))
        self.pslabel.place(x=120, y=y+200)

        self.passwd = Entry(self.frame, font='Courier 12', show='*')
        self.passwd.place(x=240, y=y+200)

        self.button = Button(self.frame, text='Login', font='Courier 15 bold', command=self.login)
        self.button.place(x=365, y=+260)

        self.win.mainloop()
    
    def login(self):
        data = (
            self.uname.get(),
            config.db.hash_password(self.passwd.get())
        )
        if self.uname.get() == "":
            messagebox.showinfo("Kesalahan", "Harap isi username!")
        elif self.passwd.get() == "":
            messagebox.showinfo("Kesalahan", "Harap isi password!")
        else:
            res = config.db.user_login(data)
            if res:
                messagebox.showinfo("Pesan", "Login Berhasil, Selamat datang {0}!".format(res[3]))
                self.win.destroy()
                with open('session.txt', "a+") as file:
                    file.write("{0}|{1}".format(res[1],res[4]))
                x = home.HomeWindows()
                x.add_frame()
            else:
                messagebox.showinfo("Pesan", "Username/Password Salah!")