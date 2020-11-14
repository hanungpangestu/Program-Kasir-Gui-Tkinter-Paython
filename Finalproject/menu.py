from tkinter import *
from tkinter import messagebox
import home,kasir,menu,history,akun
import config.db
import os

class MenuWindows:
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
        self.win.title('Menu')

    
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
        self.Labelframe1.place(relheight=0.75, relwidth=0.97, x=18, y=190)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='DAFTAR MENU')
        self.Labelframe1.configure(background="#d9d9d9")
        #body

        self.Buttona = Button(self.win, command=self.tambah)
        self.Buttona.place(height=40, width=60, x=50, y=230)
        self.Buttona.configure(activebackground="#ececec")
        self.Buttona.configure(activeforeground="#000000")
        self.Buttona.configure(background="#008080")
        self.Buttona.configure(disabledforeground="#a3a3a3")
        self.Buttona.configure(foreground="#000000")
        self.Buttona.configure(highlightbackground="#d9d9d9")
        self.Buttona.configure(highlightcolor="black")
        self.Buttona.configure(pady="0")
        self.Buttona.configure(text='TAMBAH')

        self.Buttona = Button(self.win, command=self.edit)
        self.Buttona.place(height=40, width=60, x=120, y=230)
        self.Buttona.configure(activebackground="#ececec")
        self.Buttona.configure(activeforeground="#000000")
        self.Buttona.configure(background="#2980B9")
        self.Buttona.configure(disabledforeground="#a3a3a3")
        self.Buttona.configure(foreground="#000000")
        self.Buttona.configure(highlightbackground="#d9d9d9")
        self.Buttona.configure(highlightcolor="black")
        self.Buttona.configure(pady="0")
        self.Buttona.configure(text='EDIT')

        self.Buttona = Button(self.win, command=self.hapus)
        self.Buttona.place(height=40, width=60, x=190, y=230)
        self.Buttona.configure(activebackground="#ececec")
        self.Buttona.configure(activeforeground="#000000")
        self.Buttona.configure(background="#ff0000")
        self.Buttona.configure(disabledforeground="#a3a3a3")
        self.Buttona.configure(foreground="#000000")
        self.Buttona.configure(highlightbackground="#d9d9d9")
        self.Buttona.configure(highlightcolor="black")
        self.Buttona.configure(pady="0")
        self.Buttona.configure(text='HAPUS')

        self.slabel = Label(self.win, text='Cari dengan nama : ')
        self.slabel.place(height=40, width=150, x=840, y=230)
        self.slabel.config(font=("Arial", 12), bg='#d9d9d9')

        self.sbox = Entry(self.win)
        self.sbox.place(height=40, width=240, x=1000, y=230)
        self.sbox.config(font=("Arial", 15))

        self.search = Button(self.win, command=self.cari)
        self.search.place(height=40, width=60, x=1250, y=230)
        self.search.configure(activebackground="#ececec")
        self.search.configure(activeforeground="#000000")
        self.search.configure(background="#008080")
        self.search.configure(disabledforeground="#a3a3a3")
        self.search.configure(foreground="#000000")
        self.search.configure(highlightbackground="#d9d9d9")
        self.search.configure(highlightcolor="black")
        self.search.configure(pady="0")
        self.search.configure(text='CARI')

        self.Buttona = Button(self.win, command=self.refresh)
        self.Buttona.place(height=40, width=80, x=1320, y=230)
        self.Buttona.configure(activebackground="#ececec")
        self.Buttona.configure(activeforeground="#000000")
        self.Buttona.configure(background="#008080")
        self.Buttona.configure(disabledforeground="#a3a3a3")
        self.Buttona.configure(foreground="#000000")
        self.Buttona.configure(highlightbackground="#d9d9d9")
        self.Buttona.configure(highlightcolor="black")
        self.Buttona.configure(pady="0")
        self.Buttona.configure(text='SELESAI')

        #text = Text
        self.sframe = Frame(self.win, bg='#d9d9d9')
        self.sframe.place(height=510, relwidth=0.930, x=50, y=290)
        self.scrollbar = Scrollbar(self.sframe, orient=VERTICAL)
        self.box = Listbox(self.win, yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack()
        self.scrollbar.config(command=self.box.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.box.place(height=510, relwidth=0.917, x=50, y=290)
        self.box.config(font=("Arial", 20))
        data = self.tampilkan()
        for hpr in data:
            self.box.insert(END, hpr)


        


        self.win.mainloop()
    def edit(self):
        datam = self.box.get(ANCHOR)
        if datam == "":
            messagebox.showinfo("Kesalahan", "Harap pilih Menu terlebih dahulu!")
        else:
            info = datam.split(" | ")
            harga = info[1].replace("Rp ", "")
            harga = harga.replace(".", "")
            if info[2] == "Minuman":
                jenis = 1
            elif info[2] == "Makanan":
                jenis = 2
            else:
                jenis = 0
            self.tambah = Tk()
            self.tambah.title('Edit Menu')
            self.tambah.geometry('300x200')
            self.tambah.resizable(width=False, height=False)
            
            judul = Label(self.tambah, text='Edit Menu', font=('Helvetica',16))
            judul.grid(row=0,column=0,columnspan=2, pady="10")
            
            self.nama = Label(self.tambah, text="Nama Menu", font=('Arial',12))
            self.nama.grid(row=1,column=0, sticky=W, padx=10)
            self.harga = Label(self.tambah, text="Harga Menu", font=('Arial',12))
            self.harga.grid(row=2,column=0, sticky=W, padx=10)
            self.jenis = Label(self.tambah, text="Jenis Menu", font=('Arial',12))
            self.jenis.grid(row=3,column=0, sticky=W, padx=10)
            
            self.nbox = Entry(self.tambah)
            self.nbox.insert(0, info[0])
            self.nbox.configure(state='readonly')
            self.nbox.grid(row=1,column=1)
            self.hbox = Entry(self.tambah)
            self.hbox.insert(0, harga)
            self.hbox.grid(row=2,column=1)
            OPTIONS = [
                "Pilih Jenis",
                "Minuman",
                "Makanan"
                ]
            self.variable = StringVar(self.tambah)
            self.variable.set(OPTIONS[jenis]) # default value
            self.w = OptionMenu(self.tambah, self.variable, *OPTIONS)
            self.w.grid(row=3,column=1)
            
            self.tmbh = Button(self.tambah, text="Edit",command=self.edit_menu).grid(row=5,column=0,padx=10,pady=10)
    def edit_menu(self):
        nmenu = self.nbox.get()
        hmenu = self.hbox.get()
        jmenu = self.variable.get()
        data = [
            hmenu,
            jmenu,
            nmenu
        ]
        edit = config.db.edit_menu(data)
        self.tambah.destroy()
        self.box.delete('0', 'end')
        #self.box.delete(0, END)
        data = self.tampilkan()
        for hpr in data:
            self.box.insert(END, hpr)
        messagebox.showinfo("Info", "Menu {0} berhasil diedit!".format(nmenu))
    def cari(self):
        nama = self.sbox.get()
        self.sbox.delete('0', 'end')
        if nama == "":
            messagebox.showinfo("Kesalahan", "Harap isi kolom nama menu!")
        else:
            getnmenu = config.db.cari_menu(nama)
            self.box.delete('0', 'end')
            if getnmenu:
                output = []
                for hpr in getnmenu:
                    output.append('{0} | {1} | {2}'.format(hpr[1],hpr[2],hpr[3]))
                for nmenu in output:
                    self.box.insert(END, nmenu)
            else:
                self.box.insert(END, 'Menu tidak ditemukan...')

    def refresh(self):
        self.box.delete('0', 'end')
        #self.box.delete(0, END)
        data = self.tampilkan()
        for hpr in data:
            self.box.insert(END, hpr)
    def rupiah_format(self):
        str_value = str(self.rupiah)
        after_decimal = str_value
        
        reverse = after_decimal[::-1]
        temp_reverse_value = ""
        
        for index, val in enumerate(reverse):
            if (index + 1) % 3 == 0 and index + 1 != len(reverse):
                temp_reverse_value = temp_reverse_value + val + "."
            else:
                temp_reverse_value = temp_reverse_value + val
                
        temp_result = temp_reverse_value[::-1]
        
        return "Rp " + temp_result + ""
    def tampilkan(self):
        getmenu = config.db.data_menu()
        if getmenu:
            output = []
            for hpr in getmenu:
                self.rupiah = hpr[2]
                output.append('{0} | {1} | {2}'.format(hpr[1],self.rupiah_format(),hpr[3]))
            return(output)
        else:
            return('Gagal mengambil data...')
    def tambah(self):
        self.tambah = Tk()
        self.tambah.title('Tambah Menu')
        self.tambah.geometry('300x200')
        self.tambah.resizable(width=False, height=False)

        judul = Label(self.tambah, text='Tambah Menu', font=('Helvetica',16))
        judul.grid(row=0,column=0,columnspan=2, pady="10")

        self.nama = Label(self.tambah, text="Nama Menu", font=('Arial',12))
        self.nama.grid(row=1,column=0, sticky=W, padx=10)
        self.harga = Label(self.tambah, text="Harga Menu", font=('Arial',12))
        self.harga.grid(row=2,column=0, sticky=W, padx=10)
        self.jenis = Label(self.tambah, text="Jenis Menu", font=('Arial',12))
        self.jenis.grid(row=3,column=0, sticky=W, padx=10)

        self.nbox = Entry(self.tambah)
        self.nbox.grid(row=1,column=1)
        self.hbox = Entry(self.tambah)
        self.hbox.grid(row=2,column=1)
        OPTIONS = [
            "Pilih Jenis",
            "Minuman",
            "Makanan"
            ]
        self.variable = StringVar(self.tambah)
        self.variable.set(OPTIONS[0]) # default value
        self.w = OptionMenu(self.tambah, self.variable, *OPTIONS)
        self.w.grid(row=3,column=1)

        self.tmbh = Button(self.tambah, text="Tambah",command=self.tambah_menu).grid(row=5,column=0,padx=10,pady=10)
    
    def tambah_menu(self):
        if self.nbox.get() == "":
            self.tambah.destroy()
            messagebox.showinfo("Kesalahan", "Harap isi nama menu!")
        elif self.hbox.get() == "":
            self.tambah.destroy()
            messagebox.showinfo("Kesalahan", "Harap isi harga menu!")
        elif self.variable.get() == "Pilih Jenis":
            self.tambah.destroy()
            messagebox.showinfo("Kesalahan", "Harap pilih jenis menu!")
        else:
            data = (
                self.nbox.get(),
                self.hbox.get(),
                self.variable.get()
            )
            nama = self.nbox.get()
            tambah = config.db.tambah_menu(data)
            self.tambah.destroy()
            self.box.delete('0', 'end')
            #self.box.delete(0, END)
            data = self.tampilkan()
            for hpr in data:
                self.box.insert(END, hpr)
            messagebox.showinfo("Info", "Menu {0} berhasil diinput!".format(nama))
            
    def hapus(self):
        datam = self.box.get(ANCHOR)
        if datam == "":
            messagebox.showinfo("Kesalahan", "Harap pilih Menu terlebih dahulu!")
        else:
            menu = self.box.get(self.box.curselection())
            info = menu.split(" | ")
            
            hapus = config.db.hapus_menu(info[0])
            self.box.delete(ANCHOR)
            messagebox.showinfo("Info", "Berhasil menghapus {0}".format(info[0]))
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