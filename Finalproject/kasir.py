from tkinter import *
from tkinter import messagebox
import home,kasir,menu,history,akun
import config.db
import time
import os

class KasirWindows:
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
        self.win.title('Kasir')

    
    def add_frame(self):
        with open('session.txt') as f:
            session = f.readlines()
        info = session[0].split('|')
        self.username_login = info[0]
        role = info[1]
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

        if role == 'Admin':
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
        #Daftar Meja
        self.Labelframe1 = LabelFrame(self.win)
        self.Labelframe1.place(relheight=0.40, relwidth=0.40, x=18, y=190)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='DAFTAR MEJA')
        self.Labelframe1.configure(background="#d9d9d9")
        #tombol tambah
        self.Buttona = Button(self.win, command=self.pembelian)
        self.Buttona.place(height=40, width=74, x=50, y=230)
        self.Buttona.configure(activebackground="#ececec")
        self.Buttona.configure(activeforeground="#000000")
        self.Buttona.configure(background="#008080")
        self.Buttona.configure(disabledforeground="#a3a3a3")
        self.Buttona.configure(foreground="#000000")
        self.Buttona.configure(highlightbackground="#d9d9d9")
        self.Buttona.configure(highlightcolor="black")
        self.Buttona.configure(pady="0")
        self.Buttona.configure(text='TAMPILKAN')
        
        if role == 'Admin':
            self.Buttona = Button(self.win, command=self.tambah)
            self.Buttona.place(height=40, width=60, x=127, y=230)
            self.Buttona.configure(activebackground="#ececec")
            self.Buttona.configure(activeforeground="#000000")
            self.Buttona.configure(background="#2980B9")
            self.Buttona.configure(disabledforeground="#a3a3a3")
            self.Buttona.configure(foreground="#000000")
            self.Buttona.configure(highlightbackground="#d9d9d9")
            self.Buttona.configure(highlightcolor="black")
            self.Buttona.configure(pady="0")
            self.Buttona.configure(text='TAMBAH')
            
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

        self.slabel = Label(self.win, text='Cari : ')
        self.slabel.place(height=40, width=60, x=250, y=230)
        self.slabel.config(font=("Arial", 12), bg='#d9d9d9')

        self.sbox = Entry(self.win)
        self.sbox.place(height=40, width=130, x=310, y=230)
        self.sbox.config(font=("Arial", 15))
        
        self.search = Button(self.win, command=self.cari)
        self.search.place(height=40, width=60, x=450, y=230)
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
        self.Buttona.place(height=40, width=60, x=520, y=230)
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
        self.sframe.place(height=200, relwidth=0.350, x=50, y=290)
        self.scrollbar = Scrollbar(self.sframe, orient=VERTICAL)
        self.box = Listbox(self.win, yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack()
        self.scrollbar.config(command=self.box.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.box.place(height=200, relwidth=0.340, x=50, y=290)
        self.box.config(font=("Arial", 18))
        meja = self.tampilkan_meja()
        for hpr in meja:
            self.box.insert(END, hpr)

        #Data PEMBILIAN
        self.Labelframe2 = LabelFrame(self.win)
        self.Labelframe2.place(relheight=0.75, relwidth=0.550, x=650, y=190)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='DATA PEMBELIAN')
        self.Labelframe2.configure(background="#d9d9d9")

        self.sframe2 = Frame(self.win, bg='#d9d9d9')
        self.sframe2.place(height=510, relwidth=0.500, x=680, y=290)
        self.scrollbar2 = Scrollbar(self.sframe2, orient=VERTICAL)
        self.box2 = Listbox(self.win, yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.pack()
        self.scrollbar2.config(command=self.box2.yview)
        self.scrollbar2.pack(side=RIGHT, fill=Y)
        self.box2.place(height=510, relwidth=0.490, x=680, y=290)
        self.box2.config(font=("Arial", 18))

        self.Buttona = Button(self.win, command=self.tambah_beli)
        self.Buttona.place(height=40, width=60, x=680, y=230)
        self.Buttona.configure(activebackground="#ececec")
        self.Buttona.configure(activeforeground="#000000")
        self.Buttona.configure(background="#008080")
        self.Buttona.configure(disabledforeground="#a3a3a3")
        self.Buttona.configure(foreground="#000000")
        self.Buttona.configure(highlightbackground="#d9d9d9")
        self.Buttona.configure(highlightcolor="black")
        self.Buttona.configure(pady="0")
        self.Buttona.configure(text='TAMBAH')

        self.Buttona = Button(self.win, command=self.hapus_beli)
        self.Buttona.place(height=40, width=60, x=750, y=230)
        self.Buttona.configure(activebackground="#ececec")
        self.Buttona.configure(activeforeground="#000000")
        self.Buttona.configure(background="#ff0000")
        self.Buttona.configure(disabledforeground="#a3a3a3")
        self.Buttona.configure(foreground="#000000")
        self.Buttona.configure(highlightbackground="#d9d9d9")
        self.Buttona.configure(highlightcolor="black")
        self.Buttona.configure(pady="0")
        self.Buttona.configure(text='HAPUS')

        self.slabel2 = Label(self.win, text='Cari : ')
        self.slabel2.place(height=40, width=60, x=960, y=230)
        self.slabel2.config(font=("Arial", 12), bg='#d9d9d9')

        self.sbox2 = Entry(self.win)
        self.sbox2.place(height=40, width=180, x=1020, y=230)
        self.sbox2.config(font=("Arial", 15))
        
        self.search = Button(self.win, command=self.cari_beli)
        self.search.place(height=40, width=60, x=1210, y=230)
        self.search.configure(activebackground="#ececec")
        self.search.configure(activeforeground="#000000")
        self.search.configure(background="#008080")
        self.search.configure(disabledforeground="#a3a3a3")
        self.search.configure(foreground="#000000")
        self.search.configure(highlightbackground="#d9d9d9")
        self.search.configure(highlightcolor="black")
        self.search.configure(pady="0")
        self.search.configure(text='CARI')
        
        self.Buttona = Button(self.win, command=self.refresh_beli)
        self.Buttona.place(height=40, width=60, x=1280, y=230)
        self.Buttona.configure(activebackground="#ececec")
        self.Buttona.configure(activeforeground="#000000")
        self.Buttona.configure(background="#008080")
        self.Buttona.configure(disabledforeground="#a3a3a3")
        self.Buttona.configure(foreground="#000000")
        self.Buttona.configure(highlightbackground="#d9d9d9")
        self.Buttona.configure(highlightcolor="black")
        self.Buttona.configure(pady="0")
        self.Buttona.configure(text='SELESAI')

        self.Buttona = Button(self.win, command=self.bayar)
        self.Buttona.place(height=40, width=60, x=1350, y=230)
        self.Buttona.configure(activebackground="#ececec")
        self.Buttona.configure(activeforeground="#000000")
        self.Buttona.configure(background="#2980B9")
        self.Buttona.configure(disabledforeground="#a3a3a3")
        self.Buttona.configure(foreground="#000000")
        self.Buttona.configure(highlightbackground="#d9d9d9")
        self.Buttona.configure(highlightcolor="black")
        self.Buttona.configure(pady="0")
        self.Buttona.configure(text='BAYAR')

        self.Labelframe3 = LabelFrame(self.win)
        self.Labelframe3.place(relheight=0.320, relwidth=0.195, x=20, y=560)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(text='TRANSAKSI SELESAI')
        self.Labelframe3.configure(background="#d9d9d9")

        judul = Label(self.Labelframe3, text='TRANSAKSI SELESAI', font=('Helvetica',16,'bold'), bg='#d9d9d9')
        judul.place(relheight=0.100, relwidth=0.900, x = 10, y=30)

        jmlh = Label(self.Labelframe3, text='{0}'.format(config.db.jumlah_riwayat_selesai()), font=('Helvetica',70,'bold'), bg='#d9d9d9')
        jmlh.place(relheight=0.300, relwidth=0.900, x = 10, y=100)
        
        self.Labelframe4 = LabelFrame(self.win)
        self.Labelframe4.place(relheight=0.320, relwidth=0.193, x=335, y=560)
        self.Labelframe4.configure(relief='groove')
        self.Labelframe4.configure(foreground="black")
        self.Labelframe4.configure(text='TRANSAKSI PENDING')
        self.Labelframe4.configure(background="#d9d9d9")

        judul = Label(self.Labelframe4, text='TRANSAKSI PENDING', font=('Helvetica',16,'bold'), bg='#d9d9d9')
        judul.place(relheight=0.100, relwidth=0.900, x = 10, y=30)

        jmlh = Label(self.Labelframe4, text='{0}'.format(config.db.jumlah_riwayat()), font=('Helvetica',70,'bold'), bg='#d9d9d9')
        jmlh.place(relheight=0.300, relwidth=0.900, x = 10, y=100)


        self.win.mainloop()
    #FUNGSI PEMBELIAN
    def bayar(self):
        abel = self.box.get(ANCHOR)
        if abel == "":
            messagebox.showinfo("Kesalahan", "Harap pilih meja terlebih dahulu!")
        else:
            getpembelian = self.tampilkan_pembelian()
            self.box2.delete('0', 'end')
            if getpembelian[0] == "Belum/Tidak Ada Pembelian..":
                self.box2.insert(END, getpembelian[0])
                messagebox.showinfo("Kesalahan", "Belum/Tidak Ada Pembelian.")
            else:
                for hpr in getpembelian:
                    self.box2.insert(END, hpr)
                pm = config.db.pembelian(abel)
                self.htotal=0
                for hpr in pm:
                    self.htotal += int(hpr[2])
                rp = config.db.rupiah_format(self.htotal)
                self.tambah = Toplevel()
                self.tambah.title('Bayar Pesanan')
                self.tambah.geometry('600x600')
                self.tambah.resizable(width=False, height=False)
                
                self.Canvasb = Canvas(self.tambah)
                self.Canvasb.place(relheight=1, relwidth=1, x = 0, y=0)
                self.Canvasb.configure(background="#2980B9")
                self.Canvasb.configure(borderwidth="2")
                self.Canvasb.configure(insertbackground="black")
                self.Canvasb.configure(relief="ridge")
                self.Canvasb.configure(selectbackground="#c4c4c4")
                self.Canvasb.configure(selectforeground="black")
                
                self.Labelframeb = LabelFrame(self.tambah)
                self.Labelframeb.place(relheight=0.863, relwidth=0.963, x=10, y=70)
                self.Labelframeb.configure(relief='groove')
                self.Labelframeb.configure(foreground="black")
                self.Labelframeb.configure(text='Menu Bayar')
                self.Labelframeb.configure(background="#d9d9d9")
                
                judul = Label(self.tambah, text='Bayar pesanan {0}'.format(abel), font=('Helvetica',16), bg='#2980B9')
                judul.place(relheight=0.100, relwidth=0.400, x = 175, y=10)
                
                #text = Text
                self.sframe3 = Frame(self.tambah, bg='#d9d9d9')
                self.sframe3.place(relheight=0.450, relwidth=0.867, x=40, y=100)
                self.scrollbar3 = Scrollbar(self.sframe3, orient=VERTICAL)
                self.box3 = Listbox(self.tambah, yscrollcommand=self.scrollbar3.set)
                self.scrollbar3.pack()
                self.scrollbar3.config(command=self.box3.yview)
                self.scrollbar3.pack(side=RIGHT, fill=Y)
                self.box3.place(relheight=0.450, relwidth=0.837, x=40, y=100)
                self.box3.config(font=("Arial", 20))
                getpembelian = self.tampilkan_pembelian()
                for hpr in getpembelian:
                    ea = hpr.split(' | ')
                    show = '{0} | {1} | {2}'.format(ea[1],ea[2],ea[3])
                    self.box3.insert(END, show)
                
                self.slabel3 = Label(self.tambah, text='Total Bayar : ')
                self.slabel3.place(height=40, width=100, x=180, y=380)
                self.slabel3.config(font=("Arial", 12), bg='#d9d9d9')

                self.slabel3 = Label(self.tambah, text='{0}'.format(rp))
                self.slabel3.place(height=40, width=120, x=440, y=380)
                self.slabel3.config(font=("Arial", 15), bg='#d9d9d9')
                
                self.slabel3 = Label(self.tambah, text='Uang : ')
                self.slabel3.place(height=40, width=100, x=201, y=430)
                self.slabel3.config(font=("Arial", 12), bg='#d9d9d9')
                
                self.sbox3 = Entry(self.tambah)
                self.sbox3.place(height=40, width=160, x=400, y=430)
                self.sbox3.config(font=("Arial", 15),justify='right')

                self.Buttona = Button(self.tambah, command=self.bayar_pembelian)
                self.Buttona.place(height=40, width=60, x=490, y=500)
                self.Buttona.configure(activebackground="#ececec")
                self.Buttona.configure(activeforeground="#000000")
                self.Buttona.configure(background="#2980B9")
                self.Buttona.configure(disabledforeground="#a3a3a3")
                self.Buttona.configure(foreground="#000000")
                self.Buttona.configure(highlightbackground="#d9d9d9")
                self.Buttona.configure(highlightcolor="black")
                self.Buttona.configure(pady="0")
                self.Buttona.configure(text='BAYAR')

    def bayar_pembelian(self):
        #self.slabelno.delete('0', 'end')
        jmlh = self.sbox3.get()
        if jmlh == "":
            self.slabelno = Label(self.tambah, text='Harap isi total uang!')
            self.slabelno.place(height=18, width=220, x=360, y=476)
            self.slabelno.config(font=("Arial", 12), bg='#d9d9d9',foreground='#ff0000')
        elif int(jmlh) < self.htotal:
            self.slabelno = Label(self.tambah, text='Total uang tidak mencukupi!')
            self.slabelno.place(height=18, width=220, x=360, y=476)
            self.slabelno.config(font=("Arial", 12), bg='#d9d9d9',foreground='#ff0000')
        else:
            abel = self.box.get(ANCHOR)
            info = config.db.pembelian(abel)
            for hpr in info:
                data = [
                    hpr[1],
                    hpr[2],
                    hpr[3],
                    hpr[4],
                    self.username_login,
                    hpr[5],
                    config.db.hari_ini()
                    ]
                tmbhhapus = config.db.selesai(data)
                hapus = config.db.hapus_pembelian(hpr[0])

            self.box2.delete('0', 'end')
            getpembelian = self.tampilkan_pembelian()
            for hpr in getpembelian:
                self.box2.insert(END, hpr)
            kembalian = int(jmlh)-self.htotal
            self.tambah.destroy()
            messagebox.showinfo("Kesalahan", "Transaksi Selesai! Uang Kembalian {0}".format(config.db.rupiah_format(kembalian)))

            jmlh = Label(self.Labelframe3, text='{0}'.format(config.db.jumlah_riwayat_selesai()), font=('Helvetica',70,'bold'), bg='#d9d9d9')
            jmlh.place(relheight=0.300, relwidth=0.900, x = 10, y=100)

            jmlh = Label(self.Labelframe4, text='{0}'.format(config.db.jumlah_riwayat()), font=('Helvetica',70,'bold'), bg='#d9d9d9')
            jmlh.place(relheight=0.300, relwidth=0.900, x = 10, y=100)

    def refresh_beli(self):
        self.box2.delete('0', 'end')
        getpembelian = self.tampilkan_pembelian()
        if getpembelian == False:
            self.box2.insert(END, 'Menu tidak ditemukan...')
        else:
            for hpr in getpembelian:
                self.box2.insert(END, hpr)
    def cari_beli(self):
        abel = self.box.get(ANCHOR)
        nama = self.sbox2.get()
        if nama == "":
            messagebox.showinfo("Kesalahan", "Harap isi kolom nama menu!")
        elif abel== "":
            messagebox.showinfo("Kesalahan", "Harap pilih meja terlebih dahulu!")
        else:
            self.sbox2.delete('0', 'end')
            getnmenu = config.db.cari_pembelian(nama,abel)
            self.box2.delete('0', 'end')
            if getnmenu:
                output = []
                for hpr in getnmenu:
                    self.rupiah = hpr[2]
                    output.append('ID = {2} | {0} | {1} | {3}'.format(hpr[1],self.rupiah_format(),hpr[0],hpr[3]))
                for nmenu in output:
                    self.box2.insert(END, nmenu)
            else:
                self.box2.insert(END, 'Menu tidak ditemukan...')
    def hapus_beli(self):
        abel = self.box2.get(ANCHOR)
        if abel == "":
            messagebox.showinfo("Kesalahan", "Harap pilih Pembelian terlebih dahulu!")
        else:
            menu = self.box2.get(self.box2.curselection())
            info = menu.split(" | ")
            info2 = info[0].split(" = ")
            imenu = config.db.info_pembelian(info2[1])
            data = [
                imenu[1],
                imenu[2],
                imenu[3],
                imenu[4],
                self.username_login,
                imenu[5],
                config.db.hari_ini()
            ]
            tmbhhapus = config.db.tambah_hapus_pembelian(data)
            hapuspembelian = config.db.hapus_pembelian(info2[1])
            self.box2.delete(ANCHOR)
            jmlh = Label(self.Labelframe3, text='{0}'.format(config.db.jumlah_riwayat_selesai()), font=('Helvetica',70,'bold'), bg='#d9d9d9')
            jmlh.place(relheight=0.300, relwidth=0.900, x = 10, y=100)

            jmlh = Label(self.Labelframe4, text='{0}'.format(config.db.jumlah_riwayat()), font=('Helvetica',70,'bold'), bg='#d9d9d9')
            jmlh.place(relheight=0.300, relwidth=0.900, x = 10, y=100)
            messagebox.showinfo("Info", "Berhasil menghapus {0}".format(info[1]))

    def tambah_beli(self):
        datam = self.box.get(ANCHOR)
        if datam == "":
            messagebox.showinfo("Kesalahan", "Harap pilih Meja terlebih dahulu!")
        else:
            getpembelian = self.tampilkan_pembelian()
            self.box2.delete('0', 'end')
            for hpr in getpembelian:
                self.box2.insert(END, hpr)
            #data = self.box.get(self.box.curselection())
            #meja = data.split(" | ")
            #self.meja2 = meja[0].split(" = ")
            self.tambah = Toplevel()
            self.tambah.title('Tambah Pesanan')
            self.tambah.geometry('600x600')
            self.tambah.resizable(width=False, height=False)
            
            self.Canvasb = Canvas(self.tambah)
            self.Canvasb.place(relheight=1, relwidth=1, x = 0, y=0)
            self.Canvasb.configure(background="#2980B9")
            self.Canvasb.configure(borderwidth="2")
            self.Canvasb.configure(insertbackground="black")
            self.Canvasb.configure(relief="ridge")
            self.Canvasb.configure(selectbackground="#c4c4c4")
            self.Canvasb.configure(selectforeground="black")
            
            self.Labelframeb = LabelFrame(self.tambah)
            self.Labelframeb.place(relheight=0.863, relwidth=0.963, x=10, y=70)
            self.Labelframeb.configure(relief='groove')
            self.Labelframeb.configure(foreground="black")
            self.Labelframeb.configure(text='DAFTAR MENU')
            self.Labelframeb.configure(background="#d9d9d9")
            
            judul = Label(self.tambah, text='Tambah pesanan {0}'.format(datam), font=('Helvetica',16), bg='#2980B9')
            judul.place(relheight=0.100, relwidth=0.400, x = 175, y=10)
            
            self.Buttonab = Button(self.tambah, command=self.tambahkan_menu_kasir)
            self.Buttonab.place(height=40, width=60, x=50, y=110)
            self.Buttonab.configure(activebackground="#ececec")
            self.Buttonab.configure(activeforeground="#000000")
            self.Buttonab.configure(background="#008080")
            self.Buttonab.configure(disabledforeground="#a3a3a3")
            self.Buttonab.configure(foreground="#000000")
            self.Buttonab.configure(highlightbackground="#d9d9d9")
            self.Buttonab.configure(highlightcolor="black")
            self.Buttonab.configure(pady="0")
            self.Buttonab.configure(text='TAMBAH')
            
            self.slabel3 = Label(self.tambah, text='Cari : ')
            self.slabel3.place(height=40, width=40, x=180, y=110)
            self.slabel3.config(font=("Arial", 12), bg='#d9d9d9')
            
            self.sbox3 = Entry(self.tambah)
            self.sbox3.place(height=40, width=190, x=230, y=110)
            self.sbox3.config(font=("Arial", 15))
            
            self.search = Button(self.tambah, command=self.cari_menu_pembelian)
            self.search.place(height=40, width=60, x=430, y=110)
            self.search.configure(activebackground="#ececec")
            self.search.configure(activeforeground="#000000")
            self.search.configure(background="#008080")
            self.search.configure(disabledforeground="#a3a3a3")
            self.search.configure(foreground="#000000")
            self.search.configure(highlightbackground="#d9d9d9")
            self.search.configure(highlightcolor="black")
            self.search.configure(pady="0")
            self.search.configure(text='CARI')
            
            self.Buttona = Button(self.tambah, command=self.refresh_menu_pembelian)
            self.Buttona.place(height=40, width=60, x=500, y=110)
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
            self.sframe3 = Frame(self.tambah, bg='#d9d9d9')
            self.sframe3.place(relheight=0.65, relwidth=0.867, x=40, y=160)
            self.scrollbar3 = Scrollbar(self.sframe3, orient=VERTICAL)
            self.box3 = Listbox(self.tambah, yscrollcommand=self.scrollbar3.set)
            self.scrollbar3.pack()
            self.scrollbar3.config(command=self.box3.yview)
            self.scrollbar3.pack(side=RIGHT, fill=Y)
            self.box3.place(relheight=0.65, relwidth=0.837, x=40, y=160)
            self.box3.config(font=("Arial", 20))
            data = self.tampilkan_menu()
            for hpr in data:
                self.box3.insert(END, hpr)

        """

        self.nama = Label(self.tambah, text="Nama Meja", font=('Arial',12))
        self.nama.grid(row=1,column=0, sticky=W, padx=10)

        self.nbox = Entry(self.tambah)
        self.nbox.grid(row=1,column=1)

        self.tmbh = Button(self.tambah, text="Tambah",command=self.tambah_meja).grid(row=2,column=1,padx=10,pady=10)
        """
    def refresh_menu_pembelian(self):
        self.box3.delete('0', 'end')
        #self.box.delete(0, END)
        data = self.tampilkan_menu()
        for hpr in data:
            self.box3.insert(END, hpr)
    def cari_menu_pembelian(self):
        nama = self.sbox3.get()
        if nama == "":
            messagebox.showinfo("Kesalahan", "Harap isi kolom nama menu!")
        else:
            self.sbox3.delete('0', 'end')
            self.box3.delete('0', 'end')
            getnmenu = config.db.cari_menu(nama)
            if getnmenu:
                output = []
                for hpr in getnmenu:
                    output.append('{0} | {1} | {2}'.format(hpr[1],hpr[2],hpr[3]))
                for nmenu in output:
                    self.box3.insert(END, nmenu)
            else:
                self.box3.insert(END, 'Menu tidak ditemukan...')
    def refresh_menu(self):
        self.box3.delete('0', 'end')
        #self.box.delete(0, END)
        data = self.tampilkan_menu()
        for hpr in data:
            self.box3.insert(END, hpr)
    def tampilkan_menu(self):
        getmenu = config.db.data_menu()
        if getmenu:
            output = []
            for hpr in getmenu:
                self.rupiah = hpr[2]
                output.append('{0} | {1} | {2}'.format(hpr[1],self.rupiah_format(),hpr[3]))
            return(output)
        else:
            output =[]
            output.append('Gagal Mengambil data..')
            self.box3.insert(END, output)
    def tambahkan_menu_kasir(self):
        datam = self.box3.get(ANCHOR)
        if datam == "":
            self.slabel3 = Label(self.tambah, text='Harap pilih menu terlebih dahulu!')
            self.slabel3.place(height=15, width=300, x=160, y=83)
            self.slabel3.config(font=("Arial", 12), bg='#d9d9d9',foreground='#f5010a')
        else:
            #self.box2.delete('0', 'end')
            #self.box.delete(0, END)
            meja = self.box.get(ANCHOR)
            menu = self.box3.get(self.box3.curselection())
            info = menu.split(' | ')
            ekse = config.db.info_menu(info[0])
            if ekse:
                data = [
                    ekse[1],
                    ekse[2],
                    ekse[3],
                    self.username_login,
                    config.db.hari_ini(),
                    meja
                ]
                minput = config.db.tambah_menu_meja(data)
                if minput == 1:
                    getpembelian = config.db.pembelian(meja)
                    self.tambah.destroy()
                    messagebox.showinfo("Pesan", "{0} Berhasil di tambahkan!".format(ekse[1]))
                    jmlh = Label(self.Labelframe3, text='{0}'.format(config.db.jumlah_riwayat_selesai()), font=('Helvetica',70,'bold'), bg='#d9d9d9')
                    jmlh.place(relheight=0.300, relwidth=0.900, x = 10, y=100)
                        
                    jmlh = Label(self.Labelframe4, text='{0}'.format(config.db.jumlah_riwayat()), font=('Helvetica',70,'bold'), bg='#d9d9d9')
                    jmlh.place(relheight=0.300, relwidth=0.900, x = 10, y=100)
                    
                    if getpembelian:
                        self.box2.delete('0', 'end')
                        output = []
                        for hpr in getpembelian:
                            self.rupiah = hpr[2]
                            output.append('ID = {2} | {0} | {1} | {3}'.format(hpr[1],self.rupiah_format(),hpr[0],hpr[3]))
                        for ea in output:
                            self.box2.insert(END, ea)
                    else:
                        output =[]
                        output.append('Belum/Tidak Pembelian..')
                        self.box2.insert(END, output)
                else:
                    getpembelian = config.db.pembelian(meja)
                    if getpembelian:
                        self.box2.delete('0', 'end')
                        output = []
                        for hpr in getpembelian:
                            self.rupiah = hpr[2]
                            output.append('ID = {2} | {0} | {1} | {3}'.format(hpr[1],self.rupiah_format(),hpr[0],hpr[3]))
                            for ea in output:
                                self.box2.insert(END, ea)
                    else:
                        self.box2.insert(END, 'Belum/Tidak Pembelian..')

                    self.tambah.destroy()
                    messagebox.showinfo("kesalahan", "{0} Gagal di tambahkan!".format(ekse[1]))
                    
            else:
                messagebox.showinfo("Kesalahan", "{0} Gagal di tambahkan!".format(ekse[1]))
    #AKHIR FUNGSI PEMBELIAN
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
    def tampilkan_pembelian(self):
        mpilih = self.box.get(ANCHOR)
        if mpilih == "":
            messagebox.showinfo("Kesalahan", "Harap pilih Meja terlebih dahulu!")
        else:
            tbeli = config.db.pembelian(mpilih)
            if tbeli:
                output = []
                for hpr in tbeli:
                    self.rupiah = hpr[2]
                    output.append('ID = {2} | {0} | {1} | {3}'.format(hpr[1],self.rupiah_format(),hpr[0],hpr[3]))
                return(output)
            else:
                output =[]
                output.append("Belum/Tidak Ada Pembelian..")
                return(output)
    def pembelian(self):
        datam = self.box.get(ANCHOR)
        if datam == "":
            messagebox.showinfo("Kesalahan", "Harap pilih Meja terlebih dahulu!")
        else:
            self.box2.delete('0', 'end')
            getpembelian = self.tampilkan_pembelian()
            for hpr in getpembelian:
                self.box2.insert(END, hpr)

    def hapus(self):
        meja = self.box.get(ANCHOR)
        if meja == "":
            messagebox.showinfo("Kesalahan", "Harap pilih Meja terlebih dahulu!")
        else:
            hapus = config.db.hapus_meja(meja)
            self.box.delete('0', 'end')
            data = self.tampilkan_meja()
            for hpr in data:
                self.box.insert(END, hpr)
            messagebox.showinfo("Info", "Berhasil menghapus {0}".format(meja))
    def refresh(self):
        self.box.delete('0', 'end')
        #self.box.delete(0, END)
        data = self.tampilkan_meja()
        for hpr in data:
            self.box.insert(END, hpr)
    def cari(self):
        nama = self.sbox.get()
        if nama == "":
            messagebox.showinfo("Kesalahan", "Harap isi kolom nama meja!")
        else:
            self.sbox.delete('0', 'end')
            getnmenu = config.db.cari_meja(nama)
            self.box.delete('0', 'end')
            if getnmenu:
                output = []
                for hpr in getnmenu:
                    output.append('{0}'.format(hpr[1]))
                for nmeja in output:
                    self.box.insert(END, nmeja)
            else:
                self.box.insert(END, 'Nama meja tidak ditemukan...')
    def tampilkan_meja(self):
        getmeja = config.db.meja()
        if getmeja:
            output = []
            for hpr in getmeja:
                output.append('{0}'.format(hpr[1]))
            return(output)
        else:
            self.box.insert(END, 'Gagal Mengambil data..')
    def tambah(self):
        self.tambah = Tk()
        self.tambah.title('Tambah Meja')
        self.tambah.geometry('300x200')
        self.tambah.resizable(width=False, height=False)

        judul = Label(self.tambah, text='Tambah Meja', font=('Helvetica',16))
        judul.grid(row=0,column=0,columnspan=2, pady="10")

        self.nama = Label(self.tambah, text="Nama Meja", font=('Arial',12))
        self.nama.grid(row=1,column=0, sticky=W, padx=10)

        self.nbox = Entry(self.tambah)
        self.nbox.grid(row=1,column=1)

        self.tmbh = Button(self.tambah, text="Tambah",command=self.tambah_meja).grid(row=2,column=1,padx=10,pady=10)
    def tambah_meja(self):
        if self.nbox.get() == "":
            self.tambah.destroy()
            messagebox.showinfo("Kesalahan", "Harap isi nama meja!")
        else:
            nama = self.nbox.get()
            tambah = config.db.tambah_meja(nama)
            self.tambah.destroy()
            self.box.delete('0', 'end')
            data = self.tampilkan_meja()
            for hpr in data:
                self.box.insert(END, hpr)
            messagebox.showinfo("Info", "{0} berhasil diinput!".format(nama))
    def meja(self):
        self.tambah = Tk()
        self.tambah.title('Pesanan')
        self.tambah.geometry('300x200')
        self.tambah.resizable(width=False, height=False)
                
        judul = Label(self.tambah, text=self.nama_meja, font=('Helvetica',16))
        judul.grid(row=0,column=0,columnspan=2, pady="10")
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