from tkinter import *
from PIL import Image
from PIL import ImageTk
import login

class WelcomeWindows:
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
        self.win.title('Welcome')
       
    def add_frame(self):
        self.frame = Frame(self.win, height=400, width=600)
        self.frame.place(x=0, y=0)

        x, y = 70, 20

        img = Image.open('img/cart.png')
        img = img.resize((150,150), Image.ANTIALIAS)

        self.img = ImageTk.PhotoImage(img)
        self.label = Label(self.frame, image=self.img)
        self.label.place(x=x+140, y=y+0)

        self.labeltitle = Label(self.frame, text="Salamat Datang")
        self.labeltitle.config(font=("Courier", 20, 'bold'))
        self.labeltitle.place(x=180, y=y+160)

        self.button = Button(self.frame, text="Lanjutkan", font=('helvetica', 20, 'underline italic'), bg='dark green', fg='white', command=self.login)
        self.button.place(x=x+155, y=y+230)
        self.win.mainloop()

    def login(self):
        self.win.destroy()
        log = login.LoginWindows()
        log.add_frame()
        

if __name__ == "__main__":
    x = WelcomeWindows()
    x.add_frame()