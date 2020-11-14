from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import home,kasir,menu,history,akun
import config.db
import os

class HistoryWindows:
    def __init__(self):
        self.win = Tk()
        self.canvas = Canvas(self.win, width=600, height=400, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        
        self.win.overrideredirect(True)
        self.win.overrideredirect(False)
        self.win.attributes('-fullscreen',True)

        #x = int(width / 2 - 1000 / 2)
        #y = int(height / 2 - 500 / 2)
        #str1 = "1000x500+"+ str(x) + "+" + str(y)
        #self.win.geometry(str1)
        
        #disable resize
        self.win.resizable(width=False, height=False)
        
        #change the title
        self.win.title('History')

    
    def add_frame(self):
        self.frame = Frame(self.win, height=90, width=1550, bg='#2980B9')
        self.frame.place(x=0, y=0)

        self.labeltitle = Label(self.frame, text="KASIR RESTORAN", bg='#2980B9')
        self.labeltitle.config(font=("Courier", 20, 'bold'))
        self.labeltitle.place(relx=.5, rely=.5, anchor="center")

        self.sidebarf = Frame(self.win, height=70, width=1550)
        self.sidebarf.place(x=0, y=90)

        self.Button1 = Button(self.win, command=self.home)
        self.Button1.place(height=70, width=96, x=0,y=90)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#008080")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='HOME')

        self.Button2 = Button(self.win, command=self.kasir)
        self.Button2.place(height=70, width=96, x=98,y=90)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#008080")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='KASIR')

        self.Button2 = Button(self.win,command=self.menu)
        self.Button2.place(height=70, width=96, x=196,y=90)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#008080")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='MENU')

        self.Button2 = Button(self.win, command=self.history)
        self.Button2.place(height=70, width=96, x=294,y=90)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#008080")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='HISTORY')

        self.Button2 = Button(self.win, command=self.akun)
        self.Button2.place(height=70, width=96, x=392,y=90)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#008080")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='AKUN LOGIN')

        self.Button2 = Button(self.win, command=self.logout)
        self.Button2.place(height=70, width=96, x=1436,y=90)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ff0000")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='LOGOUT')

        self.Frame1 = Frame(self.win)
        self.Frame1.place(relheight=1, relwidth=1, x=0, y=160)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#2980B9")

        self.Canvas1 = Canvas(self.win)
        self.Canvas1.place(relheight=0.8, relwidth=0.99, x = 5, y=170)
        self.Canvas1.configure(background="#2980B9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        
        self.Labelframe1 = LabelFrame(self.win)
        self.Labelframe1.place(relheight=0.7, relwidth=0.47, x=390, y=190)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='TRANSAKSI HARI INI')
        self.Labelframe1.configure(background="#d9d9d9")
        #body




        #text = Text
        self.sframe = Frame(self.win, bg='#d9d9d9')
        self.sframe.place(height=510, relwidth=0.42, x=430, y=240)
        self.scrollbar = Scrollbar(self.sframe, orient=VERTICAL)
        self.box = Listbox(self.win, yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack()
        self.scrollbar.config(command=self.box.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.box.place(height=510, relwidth=0.41, x=430, y=240)
        self.box.config(font=("Arial", 20))
        data = self.tampilkan_hariini()
        for hpr in data:
            self.box.insert(END, hpr)



        self.win.mainloop()
    def cari_hariini(self):
        print('cari')
    def refresh_hariini(self):
        print('refresh')
    def tampilkan_hariini(self):
        getmenu = config.db.history_hariini()
        if getmenu:
            output = []
            for hpr in getmenu:
                self.rupiah = hpr[2]
                output.append('{0} | {1} | {2}'.format(hpr[1],hpr[2],hpr[3]))
            return(output)
        else:
            return('Gagal mengambil data...')
    def home(self):
        self.win.destroy()
        x = home.HomeWindows()
        x.add_frame()

    def kasir(self):
        self.win.destroy()
        x = kasir.KasirWindows()
        x.add_frame()
    def menu(self):
        self.win.destroy()
        x = menu.MenuWindows()
        x.add_frame()
    def history(self):
        self.win.destroy()
        x = history.HistoryWindows()
        x.add_frame()
    def akun(self):
        self.win.destroy()
        x = akun.AkunWindows()
        x.add_frame()
    def logout(self):
        os.remove('session.txt')
        self.win.destroy()