import mysql.connector
from datetime import datetime
import hashlib

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd ="",
    database="kasir_gui"
)

cursor = con.cursor()
def hash_password(password):
    return(hashlib.md5("{0}".format(password).encode('utf-8')).hexdigest())
def rupiah_format(rp):
    str_value = str(rp)
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
def user_login(tup):
    try:
        cursor.execute("SELECT * FROM `user` WHERE `username`=%s AND `password`=%s",tup)
        return (cursor.fetchone())
    except:
        return False
def data_menu():
    try:
        cursor.execute("SELECT * FROM `menu`")
        return (cursor.fetchall())
    except:
        return False
def hapus_menu(info):
    try:
        cursor.execute("DELETE FROM `menu` WHERE `nama_menu`=%s",(info,))
        con.commit()
        return(cursor.fetchall())
    except:
        return False
def tambah_menu(data):
    try:
        cursor.execute("INSERT INTO menu (nama_menu,harga_menu,jenis_menu) VALUES (%s,%s,%s)",(data))
        con.commit()
        return(cursor.fetchall())
    except:
        return False
def cari_menu(menu):
    try:
        cursor.execute("SELECT * FROM `menu` WHERE `nama_menu` LIKE '%{0}%'".format(menu))
        return (cursor.fetchall())
    except:
        return False
def meja():
    try:
        cursor.execute("SELECT * FROM `meja`")
        return (cursor.fetchall())
    except:
        return False
def tambah_meja(data):
    try:
        cursor.execute("INSERT INTO meja (nama) VALUES (%s)",(data,))
        con.commit()
        return(cursor.fetchall())
    except:
        return False
def hapus_meja(info):
    try:
        cursor.execute("DELETE FROM `meja` WHERE `nama`=%s",(info,))
        con.commit()
        return(cursor.fetchall())
    except:
        return False
def cari_meja(meja):
    try:
        cursor.execute("SELECT * FROM `meja` WHERE `nama` LIKE '%{0}%'".format(meja))
        return (cursor.fetchall())
    except:
        return False
def pembelian(meja):
    try:
        cursor.execute("SELECT * FROM riwayat WHERE nama_meja=%s",(meja,))
        return (cursor.fetchall())
    except:
        return False
def cari_pembelian(nama,hid):
    try:
        cursor.execute("SELECT * FROM `riwayat` WHERE `nama_menu` LIKE '%{0}%' AND `nama_meja` LIKE '%{1}%'".format(nama,hid))
        return (cursor.fetchall())
    except:
        return False
def info_pembelian(data):
    try:
        cursor.execute("SELECT * FROM `riwayat` WHERE `id`=%s",(data,))
        return (cursor.fetchone())
    except:
        return False
def hapus_pembelian(data):
    try:
        cursor.execute("DELETE FROM `riwayat` WHERE `id`=%s",(data,))
        con.commit()
        return(cursor.fetchall())
    except:
        return False
def tambah_hapus_pembelian(data):
    try:
        cursor.execute("INSERT INTO riwayat_hapus (nama_menu,harga_menu,jenis_menu,user_input,user_hapus,waktu_input,waktu_hapus) VALUES (%s,%s,%s,%s,%s,%s,%s)",(data))
        con.commit()
        return(cursor.fetchall())
    except:
        return False
def edit_menu(info):
    try:
        
        cursor.execute("UPDATE menu SET harga_menu = %s, jenis_menu = %s WHERE nama_menu = %s",(info))
        con.commit()
        return(cursor.fetchall())
    except:
        return False
    
def info_menu(menu):
    try:
        cursor.execute("SELECT * FROM `menu` WHERE `nama_menu`=%s",(menu,))
        return (cursor.fetchone())
    except:
        return False
def tambah_menu_meja(data):
    try:
        cursor.execute("INSERT INTO riwayat (nama_menu,harga_menu,jenis_menu,by_user,waktu_input,nama_meja) VALUES (%s,%s,%s,%s,%s,%s)",(data))
        ea = con.commit()
        return(cursor.rowcount)
    except:
        return False
def selesai(data):
    try:
        cursor.execute("INSERT INTO riwayat_selesai (nama_menu,harga_menu,jenis_menu,user_input,user_selesai,waktu_input,waktu_selesai) VALUES (%s,%s,%s,%s,%s,%s,%s)",(data))
        con.commit()
        return(cursor.fetchall())
    except:
        return False
def jumlah_riwayat():
    try:
        cursor.execute("SELECT COUNT(*) FROM riwayat")
        ea = cursor.fetchone()
        return (ea[0])
    except:
        return False
def jumlah_riwayat_selesai():
    try:
        cursor.execute("SELECT COUNT(*) FROM riwayat_selesai")
        ea = cursor.fetchone()
        return (ea[0])
    except:
        return False
def hari_ini():
    return(datetime.today().strftime('%Y-%m-%d'))
def trx_hariini():
    hini = datetime.today().strftime('%d')
    #SELECT tanggal,COUNT(*) AS jumlah_harian FROM tbl_data WHERE tanggal=DATE(NOW()) GROUP BY tanggal
    cursor.execute("SELECT harga_menu FROM riwayat_selesai WHERE DAY(waktu_selesai)={0}".format(hini))
    ea = cursor.fetchall()
    total=0
    for hpr in ea:
        total += int(hpr[0])
    return(rupiah_format(total))
    #SELECT id_penghasilan, date_format(tanggal, '%Y-%m') as periode,pemasukan,pengeluaran,(pemasukan - pengeluaran) as profit FROM penghasilan ORDER BY tanggal ASC
def trx_bulanini():
    hini = datetime.today().strftime('%m')
    cursor.execute("SELECT harga_menu FROM riwayat_selesai WHERE MONTH(waktu_selesai)={0}".format(hini))
    ea = cursor.fetchall()
    total=0
    for hpr in ea:
        total += int(hpr[0])
    return(rupiah_format(total))
def data_akun():
    try:
        cursor.execute("SELECT * FROM `user`")
        return (cursor.fetchall())
    except:
        return False
def cari_akun(data):
    try:
        cursor.execute("SELECT * FROM `user` WHERE `username` LIKE '%{0}%'".format(data))
        return (cursor.fetchall())
    except:
        return False
def hapus_akun(data):
    try:
        cursor.execute("DELETE FROM `user` WHERE `username`=%s",(data,))
        con.commit()
        return(cursor.fetchall())
    except:
        return False
def edit_akun(info):
    try:
        cursor.execute("UPDATE user SET nama = %s, role = %s WHERE username = %s",(info))
        con.commit()
        return(cursor.fetchall())
    except:
        return False
def ganti_password_akun(info):
    try:
        cursor.execute("UPDATE user SET password = %s WHERE username = %s",(info))
        con.commit()
        return(cursor.fetchall())
    except:
        return False
def tambah_akun(data):
    try:
        cursor.execute("INSERT INTO user (username,password,nama,role) VALUES (%s,%s,%s,%s)",(data))
        con.commit()
        return(cursor.fetchall())
    except:
        return False
def history_hariini():
    hini = datetime.today().strftime('%d')
    cursor.execute("SELECT * FROM riwayat_selesai WHERE DAY(waktu_selesai)={0}".format(hini))
    ea = cursor.fetchall()
    return ea