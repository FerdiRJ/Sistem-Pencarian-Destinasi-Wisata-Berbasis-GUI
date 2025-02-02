
from tkinter import Tk, Frame, Entry, Button, PhotoImage,Label,Checkbutton, IntVar,messagebox,Canvas
from tkinter import *
import tkinter as tk
from tkinter import ttk

import csv,os

window = tk.Tk()
window.geometry("1476x867")
window.configure(bg="#FA9269")
window.title("Trip Explorer")

#canvas PAGE LOGIN (wadah gambar/teks)
frame = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
frame.place(x=0, y=0)
Label.pack(frame)

#LOGO / GAMBAR TEKS " TRIP EXPLORER"
img_logoteks = PhotoImage(file="logoteks.png")
logoteks_label = Label(frame, image=img_logoteks,bd=0).place(x=20, y =11)

#BUTTON PAGE TENTANG KAMI
img_tentangkami = PhotoImage(file="tentangkami.png")

#BUTTON REGISTER / Buat akun
img_reg = PhotoImage(file="Reg.png")

#LOGO / GAMBAR PETA
img_logopeta = PhotoImage(file="logoicon1.png")
logopeta_label = Label(frame, image=img_logopeta,bg="#FA9269",width=470,height=471).place(x=105, y=230)

#TEXT HEAD LINE
teks_headline= Label(frame, anchor="nw",bg="#FA9269", text="       TERUNGKAPNYA RAHASIA\nDESTINASI LUAR BIASA", font=("MontserratRoman ExtraBold", 40 * -1,"bold")).place(x=690,y=234)

"KOLOM INPUT EMAIL/USERNAME (PAGE LOGIN)"

def login():
    global nama,usia,gender
    email_username = entry_inputusname.get()
    password = entry_inputpas.get()

    with open('data_akun.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if (row[0] == email_username or row[1] == email_username) and row[2] == password:
                nama = row[3]
                usia = row[4]
                gender = row[5]
                messagebox.showinfo("Success", "Login Berhasil!")
                frame.destroy()
                laman_profil(nama,usia,gender)

                # Lakukan tindakan setelah login berhasil
                return

    messagebox.showerror("Error", "Username atau Password Salah!")

#WATERMARK PADA KOLOM ENTRY USERNAME/EMAIL (PAGE LOGIN)
def watermark_entryusname_in(event):
    if entry_inputusname.get() == "Masukkan Email/Username":
        entry_inputusname.delete(0, "end")
        entry_inputusname.config(fg="#000000")

def watermark_entryusname_out(event):
    if entry_inputusname.get() == "":
        entry_inputusname.insert(0, "Masukkan Email/Username")
        entry_inputusname.config(fg="#808080")

#ENTRY/INPUT EMAIL/USERNAME
img_inputusname = PhotoImage(file="inputusname.png")
inputusname_label = Label(frame, image=img_inputusname,bg="#FA9269").place(x=738,y=383)
entry_inputusname = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0,font=("Helvetica", 30))
entry_inputusname.insert(0, "Masukkan Email/Username")
entry_inputusname.bind("<FocusIn>", watermark_entryusname_in)
entry_inputusname.bind("<FocusOut>", watermark_entryusname_out)
entry_inputusname.place(x=835.0, y=386.0, width=430.0, height=99.0)
#ICON USER (PADA ENTRY USERNAME/EMAIL)
img_iconusname = PhotoImage(file="iconusname.png")
iconusname_label = Label(frame, image=img_iconusname,bg="#FFFFFF").place(x=751,y=396)

"KOLOM INPUT PASWORD (PAGE LOGIN)"

#UNTUK SESNSOR PASWORD (PAGE LOGIN)
def sesnsor_pass():
    if show_password.get() == 1:
        entry_inputpas.configure(show="")
    else:
        entry_inputpas.configure(show="*")

#WATERMARK PADA KOLOM ENTRY USERNAME/EMAIL (PAGE LOGIN)
def watermark_entrypas_in(event):
    if entry_inputpas.get() == "Masukkan Password":
        entry_inputpas.delete(0, "end")
        entry_inputpas.configure(show="*")
        entry_inputpas.configure(fg="#000000")

def watermark_entrypas_out(event):
    if entry_inputpas.get() == "":
        entry_inputpas.insert(0, "Masukkan Password")
        entry_inputpas.configure(show="")
        entry_inputpas.configure(fg="#808080")

#ENTRY/INPUT PASWORD (PAGE LOGIN)
img_inputpas = PhotoImage(file="inputpas.png")
inputpas_label = Label(frame, image=img_inputpas,bg="#FA9269").place(x=738,y=533)
entry_inputpas = Entry(frame, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0,font=("Helvetica", 30),show="")
entry_inputpas.insert(0, "Masukkan Password")
entry_inputpas.bind("<FocusIn>", watermark_entrypas_in)
entry_inputpas.bind("<FocusOut>", watermark_entrypas_out)
entry_inputpas.place(x=835.0, y=535.0, width=450.0, height=99.0)

#CHECKBUTTON SENSOR PASWORD (PAGE LOGIN)
show_password = IntVar()
show_password_checkbox = Checkbutton(frame, text="Tampilkan Password", variable=show_password, command=sesnsor_pass,bg="#FA9269", fg="#000000", selectcolor="#FA9269", activebackground="#FA9269", activeforeground="#000000")
show_password_checkbox.place(x=738, y=643)

#ICON PASWORD (PADA ENTRY PASWORD)
img_iconpass = PhotoImage(file="iconpass.png")
iconpass_label = Label(frame, image=img_iconpass,bg="#FFFFFF").place(x=750,y=546)
#BUTTON LOGIN/MASUK
img_buttonlogin = PhotoImage(file="buttonlogin.png")
button_login = Button(frame, image=img_buttonlogin, borderwidth=0, highlightthickness=0, command=login, relief="flat").place(x=738.0, y=682.0, width=570.0, height=74.0)

def laman_login():
    for widget in window.winfo_children():
        widget.destroy()
    #canvas PAGE LOGIN (wadah gambar/teks)
    frame = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
    frame.place(x=0, y=0)
    Label.pack(frame)

    #LOGO / GAMBAR TEKS " TRIP EXPLORER"

    logoteks_label = Label(frame, image=img_logoteks,bd=0).place(x=20, y =11)

    #BUTTON PAGE TENTANG KAMI
    button_tentangkami = Button(frame, image=img_tentangkami, borderwidth=0, highlightthickness=0, command=lamantentangkita, relief="flat").place(x=938.0, y=59.0, width=198.0, height=69.0)


    #BUTTON REGISTER / Buat akun
    button_reg = Button(frame, image=img_reg, borderwidth=0, highlightthickness=0, command=laman_daftarakun, relief="flat").place(x=1155.0, y=59.0, width=258.0, height=73.0)


    #LOGO / GAMBAR PETA

    logopeta_label = Label(frame, image=img_logopeta,bg="#FA9269",width=470,height=471).place(x=105, y=230)

    #TEXT HEAD LINE
    teks_headline= Label(frame, anchor="nw",bg="#FA9269", text="       TERUNGKAPNYA RAHASIA\nDESTINASI LUAR BIASA", font=("MontserratRoman ExtraBold", 40 * -1,"bold")).place(x=690,y=234)

    "KOLOM INPUT EMAIL/USERNAME (PAGE LOGIN)"

    def login():
        email_username = entry_inputusname.get()
        password = entry_inputpas.get()

        with open('data_akun.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                if (row[0] == email_username or row[1] == email_username) and row[2] == password:
                    nama = row[3]
                    usia = row[4]
                    gender = row[5]
                    messagebox.showinfo("Success", "Login Berhasil!")
                    frame.destroy()
                    laman_profil(nama,usia,gender)
                    # Lakukan tindakan setelah login berhasil
                    return

        messagebox.showerror("Error", "Username atau Password Salah!")

    #WATERMARK PADA KOLOM ENTRY USERNAME/EMAIL (PAGE LOGIN)
    def watermark_entryusname_in(event):
        if entry_inputusname.get() == "Masukkan Email/Username":
            entry_inputusname.delete(0, "end")
            entry_inputusname.config(fg="#000000")

    def watermark_entryusname_out(event):
        if entry_inputusname.get() == "":
            entry_inputusname.insert(0, "Masukkan Email/Username")
            entry_inputusname.config(fg="#808080")

    #ENTRY/INPUT EMAIL/USERNAME
    inputusname_label = Label(frame, image=img_inputusname,bg="#FA9269").place(x=738,y=383)
    entry_inputusname = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0,font=("Helvetica", 30))
    entry_inputusname.insert(0, "Masukkan Email/Username")
    entry_inputusname.bind("<FocusIn>", watermark_entryusname_in)
    entry_inputusname.bind("<FocusOut>", watermark_entryusname_out)
    entry_inputusname.place(x=835.0, y=386.0, width=430.0, height=99.0)
    #ICON USER (PADA ENTRY USERNAME/EMAIL)
    iconusname_label = Label(frame, image=img_iconusname,bg="#FFFFFF").place(x=751,y=396)

    "KOLOM INPUT PASWORD (PAGE LOGIN)"

    #UNTUK SESNSOR PASWORD (PAGE LOGIN)
    def sesnsor_pass():
        if show_password.get() == 1:
            entry_inputpas.configure(show="")
        else:
            entry_inputpas.configure(show="*")

    #WATERMARK PADA KOLOM ENTRY USERNAME/EMAIL (PAGE LOGIN)
    def watermark_entrypas_in(event):
        if entry_inputpas.get() == "Masukkan Password":
            entry_inputpas.delete(0, "end")
            entry_inputpas.configure(show="*")
            entry_inputpas.configure(fg="#000000")

    def watermark_entrypas_out(event):
        if entry_inputpas.get() == "":
            entry_inputpas.insert(0, "Masukkan Password")
            entry_inputpas.configure(show="")
            entry_inputpas.configure(fg="#808080")

    #ENTRY/INPUT PASWORD (PAGE LOGIN)
    inputpas_label = Label(frame, image=img_inputpas,bg="#FA9269").place(x=738,y=533)
    entry_inputpas = Entry(frame, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0,font=("Helvetica", 30),show="")
    entry_inputpas.insert(0, "Masukkan Password")
    entry_inputpas.bind("<FocusIn>", watermark_entrypas_in)
    entry_inputpas.bind("<FocusOut>", watermark_entrypas_out)
    entry_inputpas.place(x=835.0, y=535.0, width=450.0, height=99.0)

    #CHECKBUTTON SENSOR PASWORD (PAGE LOGIN)
    show_password = IntVar()
    show_password_checkbox = Checkbutton(frame, text="Tampilkan Password", variable=show_password, command=sesnsor_pass,bg="#FA9269", fg="#000000", selectcolor="#FA9269", activebackground="#FA9269", activeforeground="#000000")
    show_password_checkbox.place(x=738, y=643)

    #ICON PASWORD (PADA ENTRY PASWORD)
    iconpass_label = Label(frame, image=img_iconpass,bg="#FFFFFF").place(x=750,y=546)
    #BUTTON LOGIN/MASUK
    button_login = Button(frame, image=img_buttonlogin, borderwidth=0, highlightthickness=0, command=login, relief="flat").place(x=738.0, y=682.0, width=570.0, height=74.0)

#Gambar Laman TentangKita
img_masuk = PhotoImage(file="buttonmasuk.png")
img_iconmobil = PhotoImage(file="iconcar.png")
img_logoteks_tentangkita = PhotoImage(file="logoteks.png")

def lamantentangkita():
    frame1 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
    frame1.place(x=0, y=0)
    def kembali_lamantentangkita():
        frame1.destroy()  # Menghapus frame saat ini
    button_masuk = Button(frame1, image=img_masuk, borderwidth=0, highlightthickness=0, command=kembali_lamantentangkita, relief="flat")
    button_masuk.place(x=1115.0, y=59.0, width=258.0, height=73.0)

    label_icon_mobil = Label(frame1, image=img_iconmobil, bg="#FA9269")
    label_icon_mobil.place(x=918.0, y=230.0)

    isiteks_tentangkami = Label(frame1, anchor="nw", bg="#FA9269", text="SELAMAT DATANG DI TRIPEXPLORER - APLIKASI PENJELAJAHAN WISATA JAWA TIMUR !\nTRIPEXPLORER ADALAH APLIKASI YANG DIDEDIKASIKAN UNTUK MEMANDU ANDA DALAM MENGEKSPLORASI \nKEINDAHAN JAWA TIMUR. KAMI HADIR UNTUK MEMBERIKAN INFORMASI, REKOMENDASI, DAN INSPIRASI \nTENTANG TEMPAT-TEMPAT WISATA MENAKJUBKAN DI JAWA TIMUR. DARI PESONA ALAM YANG MEMUKAU \nHINGGA WARISAN BUDAYA YANG KAYA, KAMI INGIN MEMBANTU ANDA MERENCANAKAN PERJALANAN YANG \nTAK TERLUPAKAN.\n\nDALAM APLIKASI INI, ANDA AKAN MENEMUKAN BERAGAM ARTIKEL MENARIK YANG MEMBAHAS DESTINASI \nWISATA POPULER DI JAWA TIMUR. KAMI AKAN MEMBAWA ANDA MELALUI PERJALANAN VIRTUAL YANG \nMEMPERKENALKAN TEMPAT-TEMPAT MENARIK SEPERTI GUNUNG BROMO, TAMAN NASIONAL BALURAN, \nKAWAH IJEN, PANTAI MALANG, DAN MASIH BANYAK LAGI. ARTIKEL KAMI JUGA AKAN MEMBERIKAN \nWAWASAN TENTANG SEJARAH, BUDAYA, KULINER, DAN AKTIVITAS SERU YANG DAPAT ANDA NIKMATI SAAT \nBERADA DI JAWA TIMUR.\n\nKAMI SELALU BERUSAHA MEMBERIKAN REKOMENDASI TERBAIK UNTUK MEMBANTU ANDA MERENCANAKAN \nPERJALANAN ANDA. DARI PENGINAPAN YANG NYAMAN HINGGA PENGALAMAN UNIK YANG TIDAK BOLEH \nANDA LEWATKAN, KAMI AKAN MENYAJIKAN INFORMASI YANG AKURAT DAN TERKINI. DENGAN TRIPEXPLORER, \nANDA DAPAT MENJELAJAHI JAWA TIMUR DENGAN PERCAYA DIRI, MENIKMATI KEINDAHAN ALAMNYA, DAN \nMERASAKAN KERAMAHAN PENDUDUK SETEMPAT.\n\nKAMI BERKOMITMEN UNTUK TERUS MENGHADIRKAN KONTEN BERKUALITAS DAN BERMANFAAT UNTUK \nMEMENUHI KEBUTUHAN PERJALANAN ANDA. BERSAMA TRIPEXPLORER, MARI KITA JELAJAHI KEAJAIBAN \nJAWA TIMUR DAN MEMBUAT KENANGAN TAK TERLUPAKAN.\n\nSELAMAT MENJELAJAH!\nTIM TRIPEXPLORER", font=("MontserratRoman ExtraBold", 14 * -1),justify="left")
    isiteks_tentangkami.place(x=46.0, y=299.0)

    headline_labeltentangkami = Label(frame1, anchor="nw", bg="#FA9269", text="“TENTANG KAMI”", font=("MontserratRoman ExtraBold", 64 * -1, "bold"))
    headline_labeltentangkami.place(x=36.0, y=195.0)

    img_logoteks_tentangkita_label = Label(frame1, image=img_logoteks_tentangkita, bg="#FA9269")
    img_logoteks_tentangkita_label.place(x=427.0, y=11.0)



button_tentangkami = Button(frame, image=img_tentangkami, borderwidth=0, highlightthickness=0, command=lamantentangkita, relief="flat").place(x=938.0, y=59.0, width=198.0, height=69.0)

#gambar laman login
img_btnbuatakun = PhotoImage(file="btnbuatakun.png")
img_btnbacklamanlogin = PhotoImage(file="btnbacklamanlogin.png")
img_logoteks_lamandaftar = PhotoImage(file="logoteks.png")
img_email_lamandaftar = PhotoImage(file="entry_lamandaftarakun.png")
img_username_lamandaftar = PhotoImage(file="entry_lamandaftarakun.png")
img_pasword_lamandaftar = PhotoImage(file="entry_lamandaftarakun.png")
img_nama_lamandaftar = PhotoImage(file="entry_lamandaftarakun.png")
img_usia_lamandaftar = PhotoImage(file="entry_lamandaftarakun.png")
img_gender_lamandaftar = PhotoImage(file="entry_lamandaftarakun.png")


def laman_daftarakun():
    global frame3
    frame3 = Frame(window, bg="#FA9269",height=867,bd=0, highlightthickness=0, relief="ridge")
    frame3.place(x=0, y=0, width=1476, height=867)
    #simpan data registrasi ke csv


    def save_account():
        email = entry_email_lamandaftar.get()
        username = entry_username_lamandaftar.get()
        password = entry_pasword_lamandaftar.get()
        nama = entry_nama_lamandaftar.get()
        usia = entry_usia_lamandaftar.get()
        gender = entry_gender_lamandaftar.get()

        if not email or not username or not password:
            messagebox.showerror("Error", "Semua Data Wajib Terisi!")
            return

        # Cek jika email tanpa tanda "@"
        if "@" not in email:
            messagebox.showerror("Error", "Masukan Alamat Email Yang Valid!")
            return

        # Cek apakah file CSV sudah ada
        file_exists = os.path.isfile('data_akun.csv')

        # Simpan data akun ke dalam file CSV
        with open('data_akun.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            # Tulis nama kolom jika file CSV belum ada
            if not file_exists:
                writer.writerow(['Email', 'Username', 'Password', 'Nama', 'Usia', 'Gender'])

            writer.writerow([email, username, password, nama, usia, gender])
            # Tampilkan data pada halaman profil

        # Hapus input di field setelah disimpan
        entry_email_lamandaftar.delete(0, 'end')
        entry_username_lamandaftar.delete(0, 'end')
        entry_pasword_lamandaftar.delete(0, 'end')
        entry_nama_lamandaftar.delete(0, 'end')
        entry_usia_lamandaftar.delete(0, 'end')
        entry_gender_lamandaftar.delete(0, 'end')

        messagebox.showinfo("Success", "Daftar Akun Berhasil! Silahkan Masuk.")
        laman_profil(nama,usia,gender)


    
    button_buatakun = Button(frame3, image=img_btnbuatakun, borderwidth=0, highlightthickness=0, command=save_account, relief="flat")
    button_buatakun.place(x=404.0, y=623.0, width=554.0, height=99.0)
    
    def kembali_lamanlogin():
        frame3.destroy()  # Menghapus frame saat ini
    button_btnbacklamanlogin = Button(frame3, image=img_btnbacklamanlogin, borderwidth=0, highlightthickness=0, command=kembali_lamanlogin, relief="flat")
    button_btnbacklamanlogin.place(x=1130.0, y=47.0, width=258.0, height=91.0)

    #Headline label (Buat Akun)
    headline_label_buatakun = Label(frame3, text="BUAT AKUN", bg="#FA9269", fg="#000000", font=("MontserratRoman ExtraBold", 64,"bold"))
    headline_label_buatakun.place(x=75.0, y=159.0)

    #LOGO / GAMBAR TEKS " TRIP EXPLORER"
    logoteks_label_lamandaftar = Label(frame3, image=img_logoteks_lamandaftar, bg="#FA9269")
    logoteks_label_lamandaftar.place(x=20.0, y=11.0)


    "========entry email (page registrasi)========="
    #watermark entry email (page regis)
    def watermark_entryemail_in(event):
        if entry_email_lamandaftar.get() == "Masukkan Email":
            entry_email_lamandaftar.delete(0, "end")
            entry_email_lamandaftar.config(fg="#000000")

    def watermark_entryemail_out(event):
        if entry_email_lamandaftar.get() == "":
            entry_email_lamandaftar.insert(0, "Masukkan Email")
            entry_email_lamandaftar.config(fg="#808080")
    #entry email (page regis)
    label_email_lamandaftar = Label(frame3, image=img_email_lamandaftar,bg="#FA9269").place(x=85,y=265)
    entry_email_lamandaftar = Entry(frame3, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0,font=("Helvetica", 30))
    entry_email_lamandaftar.insert(0, "Masukkan Email")
    entry_email_lamandaftar.bind("<FocusIn>", watermark_entryemail_in)
    entry_email_lamandaftar.bind("<FocusOut>", watermark_entryemail_out)
    entry_email_lamandaftar.place(x=95.0, y=268.0, width=547.0, height=68.0)

    "========entry USERNAME (page registrasi)========="

    #watermark entry username (page regis)
    def watermark_entryusname_in(event):
        if entry_username_lamandaftar.get() == "Masukkan Username":
            entry_username_lamandaftar.delete(0, "end")
            entry_username_lamandaftar.config(fg="#000000")

    def watermark_entryusname_out(event):
        if entry_username_lamandaftar.get() == "":
            entry_username_lamandaftar.insert(0, "Masukkan Username")
            entry_username_lamandaftar.config(fg="#808080")

    #entry USERNAME (page regis)
    label_username_lamandaftar = Label(frame3, image=img_username_lamandaftar,bg="#FA9269").place(x=85,y=370)
    entry_username_lamandaftar = Entry(frame3, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0,font=("Helvetica", 30))
    entry_username_lamandaftar.insert(0, "Masukkan Username")
    entry_username_lamandaftar.bind("<FocusIn>", watermark_entryusname_in)
    entry_username_lamandaftar.bind("<FocusOut>", watermark_entryusname_out)
    entry_username_lamandaftar.place(x=95.0, y=373.0, width=547.0, height=68.0)
    
    "========entry PASSWORD (page registrasi)========="

        #UNTUK SESNSOR PASWORD (PAGE REGIS)
    def sensor_pass():
            if show_password.get() == 1:
                entry_pasword_lamandaftar.configure(show="")
            else:
                entry_pasword_lamandaftar.configure(show="*")

        #WATERMARK PADA KOLOM ENTRY PASSWORD (PAGE REGIS)
    def watermark_entrypas_in1(event):
            if entry_pasword_lamandaftar.get() == "Masukkan Password":
                entry_pasword_lamandaftar.delete(0, "end")
                entry_pasword_lamandaftar.configure(show="*")
                entry_pasword_lamandaftar.configure(fg="#000000")

    def watermark_entrypas_out1(event):
            if entry_pasword_lamandaftar.get() == "":
                entry_pasword_lamandaftar.insert(0, "Masukkan Password")
                entry_pasword_lamandaftar.configure(show="")
                entry_pasword_lamandaftar.configure(fg="#808080")
    
    #entry PASSWORD (page regis)
    label_pasword_lamandaftar = Label(frame3, image=img_pasword_lamandaftar,bg="#FA9269").place(x=85,y=475)
    entry_pasword_lamandaftar = Entry(frame3, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0,font=("Helvetica", 30),show="")
    entry_pasword_lamandaftar.insert(0, "Masukkan Password")
    entry_pasword_lamandaftar.bind("<FocusIn>", watermark_entrypas_in1)
    entry_pasword_lamandaftar.bind("<FocusOut>", watermark_entrypas_out1)
    entry_pasword_lamandaftar.place(x=835.0, y=535.0, width=450.0, height=99.0)
    entry_pasword_lamandaftar.place(x=95.0, y=478.0, width=547.0, height=68.0)
    #CHECKBUTTON SENSOR PASWORD (PAGE REGIS)
    show_password = IntVar()
    show_password_checkbox = Checkbutton(frame3, text="Tampilkan Password", variable=show_password, command=sensor_pass,bg="#FA9269", fg="#000000", selectcolor="#FA9269", activebackground="#FA9269", activeforeground="#000000")
    show_password_checkbox.place(x=80, y=557)
    
    "========entry NAMA (page registrasi)========="

    #watermark entry nama (page regis)
    def watermark_entryusname_in(event):
        if entry_nama_lamandaftar.get() == "Masukkan Nama":
            entry_nama_lamandaftar.delete(0, "end")
            entry_nama_lamandaftar.config(fg="#000000")

    def watermark_entryusname_out(event):
        if entry_nama_lamandaftar.get() == "":
            entry_nama_lamandaftar.insert(0, "Masukkan Nama")
            entry_nama_lamandaftar.config(fg="#808080")

    #entry NAMA (PAGE REGIS)
    label_nama_lamandaftar = Label(frame3, image=img_nama_lamandaftar,bg="#FA9269").place(x=726,y=265)
    entry_nama_lamandaftar = Entry(frame3, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 ,font=("Helvetica", 30))
    entry_nama_lamandaftar.insert(0, "Masukkan Nama")
    entry_nama_lamandaftar.bind("<FocusIn>", watermark_entryusname_in)
    entry_nama_lamandaftar.bind("<FocusOut>", watermark_entryusname_out)
    entry_nama_lamandaftar.place(x=736.0, y=268.0, width=547.0, height=68.0)

    "========entry USIA (page registrasi)========="
    #watermark entry Usia (page regis)
    def watermark_entryusname_in(event):
        if entry_usia_lamandaftar.get() == "Masukkan Usia":
            entry_usia_lamandaftar.delete(0, "end")
            entry_usia_lamandaftar.config(fg="#000000")

    def watermark_entryusname_out(event):
        if entry_usia_lamandaftar.get() == "":
            entry_usia_lamandaftar.insert(0, "Masukkan Usia")
            entry_usia_lamandaftar.config(fg="#808080")
    
    #entry Usia (page regis)
    label_usia_lamandaftar = Label(frame3, image=img_usia_lamandaftar,bg="#FA9269").place(x=726,y=370)
    entry_usia_lamandaftar = Entry(frame3, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0,font=("Helvetica", 30))
    entry_usia_lamandaftar.insert(0, "Masukkan Usia")
    entry_usia_lamandaftar.bind("<FocusIn>", watermark_entryusname_in)
    entry_usia_lamandaftar.bind("<FocusOut>", watermark_entryusname_out)
    entry_usia_lamandaftar.place(x=736.0, y=373.0, width=547.0, height=68.0)

    "========entry GENDER (page registrasi)========="
    #watermark entry gender (page regis)
    def watermark_entryusname_in(event):
        if entry_gender_lamandaftar.get() == "Masukkan Jenis Kelamin":
            entry_gender_lamandaftar.delete(0, "end")
            entry_gender_lamandaftar.config(fg="#000000")

    def watermark_entryusname_out(event):
        if entry_gender_lamandaftar.get() == "":
            entry_gender_lamandaftar.insert(0, "Masukkan Jenis Kelamin")
            entry_gender_lamandaftar.config(fg="#808080")
    
    #entry Gender (page regis)
    label_gender_lamandaftar = Label(frame3, image=img_gender_lamandaftar,bg="#FA9269").place(x=726,y=475)
    entry_gender_lamandaftar = Entry(frame3, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0,font=("Helvetica", 30))
    entry_gender_lamandaftar.insert(0, "Masukkan Jenis Kelamin")
    entry_gender_lamandaftar.bind("<FocusIn>", watermark_entryusname_in)
    entry_gender_lamandaftar.bind("<FocusOut>", watermark_entryusname_out)
    entry_gender_lamandaftar.place(x=736.0, y=478.0, width=547.0, height=68.0)

button_reg = Button(frame, image=img_reg, borderwidth=0, highlightthickness=0, command=laman_daftarakun, relief="flat").place(x=1155.0, y=59.0, width=258.0, height=73.0)

#Gambar toggle menu
img_logoteks_toggle = PhotoImage(file="logoteks_toggle.png")
img_togggle_btn = PhotoImage(file="togglemenu.png")


def ALLmenu_toggle(frame=None):
    #head frame untuk menampilan logoteks & tempat button toggle menu
    global head_frame
    head_frame = Frame(window, bg="#FA9269")
    head_frame.place(x=0, y=0, relwidth=1, height=100)
    head_frame.pack_propagate(False)
    head_frame.configure(height=100)

    def toggle_menu():
        #SISTEM UNTUK MEMBUKA & TUTUP TOGGLE MENU
        def collapse_toggle_menu():
            toggle_menu_frame.destroy()
            toggle_btn.config(text='☰')
            toggle_btn.config(command=toggle_menu)

        #FRAME TOGGLE MENU
        toggle_menu_frame = Frame(window, bg="#FA9269")

        #BUTTON ISI FRAME TOGGLE MENU
        
        profil_button = Button(toggle_menu_frame, text="PROFIL", font=("bold", 20), bd=0, bg="#FA9269", fg="black", activebackground='#FA9269', activeforeground='white',command=lambda: switch_frame(lambda:laman_profil(nama,usia,gender)))
        profil_button.place(x=20, y=40)

        Jelajahi_button = Button(toggle_menu_frame, text="JELAJAHI", font=("bold", 20), bd=0, bg="#FA9269", fg="black", activebackground='#FA9269', activeforeground='white',command=lambda: switch_frame(laman_jelajahi))
        Jelajahi_button.place(x=20, y=90)
        
        berita_button = Button(toggle_menu_frame, text="BERITA", font=("bold", 20), bd=0, bg="#FA9269", fg="black", activebackground='#FA9269', activeforeground='white',command=lambda: switch_frame(laman_berita))
        berita_button.place(x=20, y=140)

        unggah_btn = Button(toggle_menu_frame, text="Unggah Berita", font=("bold", 20), bd=0, bg="black", fg="white", activebackground='black', activeforeground='white',command=lambda: switch_frame(upload_berita))
        unggah_btn.place(x=20, y=190)

        #KONFIGURASI FRAME TOGGLE MENU
        frame_height = window.winfo_height()
        toggle_menu_frame.place(x=0, y=90, height=frame_height, width=300)
        toggle_btn.config(text='X')
        toggle_btn.config(command=collapse_toggle_menu)

    toggle_btn = Button(head_frame, image=img_togggle_btn, borderwidth=0, highlightthickness=0, command=toggle_menu)
    toggle_btn.place(x=39,y=23, width=59,height=64)

    headline_headframe = Label(head_frame, image=img_logoteks_toggle, bd=0 )
    headline_headframe.place(x=530,y=16)
    def switch_frame(new_frame):
        if frame:
            frame.destroy()
        new_frame()
        

 
#Gambar Laman Profil
img_bground_profil = PhotoImage(file="bground_profilpage.png")
img_keluar_profil= PhotoImage(file="keluar.png")

def laman_profil(nama,usia,gender):
    for widget in window.winfo_children():
        widget.destroy()
    global frame4

    frame4 = Frame(window, bg="#FFFFFF",height=867,bd=0, highlightthickness=0, relief="ridge")
    frame4.place(x=0, y=0, width=1476, height=867)
    label_bground_profil = Label(frame4, image=img_bground_profil,bg="#FFFFFF")
    label_bground_profil.place(x=0, y=0, relwidth=1, relheight=1)

    keluar_btn = Button(frame4, image=img_keluar_profil, bd=0, highlightthickness=0,command=laman_login)
    keluar_btn.place(x=1148,y=680)

    # Menampilkan data profil
    nama_label = Label(frame4, text="Nama: " + nama, font=("Helvetica", 20,"bold"),justify="center", bg="#FA9269")
    nama_label.place(x=487, y=561)

    usia_label = Label(frame4, text="Usia: " + usia, font=("Helvetica", 20,"bold"),justify="center", bg="#FA9269")
    usia_label.place(x=489, y=603)

    gender_label = Label(frame4, text="Gender: " + gender, font=("Helvetica", 20,"bold"),justify="center", bg="#FA9269")
    gender_label.place(x=489,y=644)

    ALLmenu_toggle(frame4)


#Gambar Laman Berita
button_image_1 = PhotoImage(file="ber1.png")
button_image_2 = PhotoImage(file="ber2.png")
button_image_3 = PhotoImage(file="ber3.png")
button_image_4 = PhotoImage(file="ber4.png")
button_image_5 = PhotoImage(file="ber5.png")
button_image_6 = PhotoImage(file="ber6.png")


berita_list = []
def laman_berita():
    global frame5
    for widget in window.winfo_children():
        widget.destroy()
    # membuat scrollbar
    scrollbar = tk.Scrollbar(window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas = tk.Canvas(window, yscrollcommand=scrollbar.set)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)    

    frame5 = Frame(canvas, bg="#FA9269", height=2000, width=1476, bd=0, highlightthickness=0, relief="ridge")
    frame5.place(x=0, y=0)
    canvas.create_window((0, 0), window=frame5, anchor='nw')

    berita_apk = Label(frame5, text="BERITA SEPUTAR WISATA:", font=("bold", 20), bg="#FA9269", fg="black")
    berita_apk.place(x=137, y=102)

    button_1 = Button(frame5, image=button_image_1, borderwidth=0, highlightthickness=0, command=beritasurabaya, relief="flat")
    button_1.place(x=111.0, y=359.0, width=584.0, height=203.0)

    button_2 = Button(frame5, image=button_image_2, borderwidth=0, highlightthickness=0, command=beritabltr, relief="flat")
    button_2.place(x=738.0, y=361.0, width=584.0, height=203.0)

    button_3 = Button(frame5, image=button_image_3, borderwidth=0, highlightthickness=0, command=beritamuseumsby, relief="flat")
    button_3.place(x=111.0, y=128.0, width=584.0, height=203.0)

    button_4 = Button(frame5, image=button_image_4, borderwidth=0, highlightthickness=0, command=beritapacitan, relief="flat")
    button_4.place(x=738.0, y=590.0, width=584.0, height=203.0)

    button_5 = Button(frame5, image=button_image_5, borderwidth=0, highlightthickness=0, command=beritadespro, relief="flat")
    button_5.place(x=738.0, y=128.0, width=584.0, height=203.0)

    button_6 = Button(frame5, image=button_image_6, borderwidth=0, highlightthickness=0, command=beritamalang, relief="flat")
    button_6.place(x=111.0, y=590.0, width=584.0, height=203.0)

    batas_artikel = Label(frame5, text="ARTIKEL PENGGUNA:", font=("bold", 20), bg="#FA9269", fg="black")
    batas_artikel.place(x=137, y=795)

    for i, berita in enumerate(berita_list):
        judul = berita['judul']
        teks = berita['teks']
        button = Button(frame5, text=judul, font=("bold", 16), bd=0, bg="black", fg="white", activebackground='#FFFFFF', activeforeground='black', command=lambda i=i: tampilkan_berita(i))
        button.place(x=111, y=850 + i * 50,width=300, height=50)
    #  mengatur scrollregion pada canvas agar bisa melakukan scroll ke bawah
    frame5.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))

    # menghubungkan scrollbar dengan canvas
    scrollbar.config(command=canvas.yview)
    ALLmenu_toggle(frame5)

def upload_berita():
    global frame11
    frame11 = Frame(window, bg="#FA9269",height=867,bd=0, highlightthickness=0, relief="ridge")
    frame11.place(x=0, y=0, width=1476, height=867)
    # Membuat label judul
    judul_label = Label(frame11, text="Judul Berita", font=("bold", 20), bg="#FA9269", fg="black")
    judul_label.place(x=111, y=100)

    # Membuat input judul berita
    judul_entry = Entry(frame11, font=("bold", 16), bd=0, width=70)
    judul_entry.place(x=111, y=150)

    # Membuat label teks berita
    teks_label = Label(frame11, text="Teks Berita", font=("bold", 20), bg="#FA9269", fg="black")
    teks_label.place(x=111, y=200)

    # Membuat input teks berita menggunakan Text widget
    teks_text = Text(frame11, font=("bold", 16), bd=0, width=70, height=15)
    teks_text.place(x=111, y=250)

    # Membuat tombol simpan berita
    simpan_btn = Button(frame11, text="Simpan", font=("bold", 20), bd=0, bg="#FFFFFF", fg="black", activebackground='#FFFFFF', activeforeground='black', command=lambda: simpan_berita(judul_entry.get(), teks_text.get("1.0", "end-1c")))
    simpan_btn.place(x=111, y=650)

    # Membuat tombol batal unggah berita
    batal_btn = Button(frame11, text="Batal", font=("bold", 20), bd=0, bg="#FFFFFF", fg="black", activebackground='#FFFFFF', activeforeground='black')
    batal_btn.place(x=250, y=650)
    ALLmenu_toggle(frame11)


def simpan_berita(judul, teks):
    # Di sini Anda dapat menambahkan logika untuk menyimpan berita yang diunggah
    # Misalnya, menyimpan informasi berita ke dalam list atau dictionary
    berita = {
        'judul': judul,
        'teks': teks,
    }
    berita_list.append(berita)
    laman_berita()

def tampilkan_berita(index):
    berita = berita_list[index]
    judul = berita['judul']
    teks = berita['teks']

    # Membersihkan tampilan laman berita sebelumnya
    for widget in window.winfo_children():
        widget.destroy()

    # Membuat frame baru untuk menampilkan informasi berita
    frame_berita = Frame(window, bg="#FA9269")
    frame_berita.pack(fill=tk.BOTH, expand=True)

    # Membuat judul berita
    label_judul = Label(frame_berita, text=judul, bg="#FA9269", fg="#241F1F",justify="center",
                        font=("MontserratRoman Bold", 40))
    label_judul.pack(pady=20)

    # Membuat teks berita
    label_teks = Label(frame_berita, text=teks, bg="#FA9269", fg="#241F1F",justify="left", font=("MontserratRoman Bold", 15,"bold"))
    label_teks.pack(padx=20, pady=10)

    # Menambahkan gambar berita
    # Ganti dengan kode untuk menampilkan gambar, misalnya menggunakan PIL atau library lainnya
    # ...

    # Menambahkan tombol kembali ke laman berita
    backbtn = Button(frame_berita, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_berita, relief="flat")
    backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

#gambar isi laman berita
img_bermussby = PhotoImage(file="3wisata museum.png")

#ISI LAMAN BERITA
def beritadespro():
    global frame6
    for widget in window.winfo_children():
        widget.destroy()
    # membuat scrollbar
    scrollbar = tk.Scrollbar(window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas1 = tk.Canvas(window, yscrollcommand=scrollbar.set)
    canvas1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)    

    frame6 = Frame(canvas1, bg="#FA9269", height=2000, width=1476, bd=0, highlightthickness=0, relief="ridge")
    frame6.place(x=0, y=0)
    canvas1.create_window((0, 0), window=frame6, anchor='nw')

    backbtn = Button(frame6, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_berita, relief="flat")
    backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

    logoteks_isiberita = Label(frame6, image=img_logoteks_toggle, bd=0 )
    logoteks_isiberita.place(x=530,y=16)
    label_title = Label(frame6, text="10 inspirasi destinasi wisata yang ada di probolinggo", bg="#FA9269", fg="#241F1F",justify="center",
                        font=("MontserratRoman Bold", 40))
    label_title.place(x=221, y=87, anchor="nw")

    label_description = Label(frame6,
                            text="1. Wisata di probolinggo pertama adalah Gunung Bromo. Gunung bromo merupakan ikon wisata jawa timur. Letaknya meliputi : probolinggo malang, \nlumajang, dan pasuruan. Gunung ini merupakan gunung aktif dengan tinggi 2.392 mdpl yang memiliki ngarai dan lembah disekitar gunung yang tampak elok.\n\n2. Wisata di probolinggo kedua adalah Gunung Argopuro. Gunung ini meliputi daerah probolinggo, lumajang, jember, bondowoso, dan \nsitubondo, dengan ketinggian 3.088 mdpl. Gunung ini memiliki beberapa puncak. Puncak paling tinggi rengganis, yang dipercaya sebagai kediaman \nDewi Rengganis, putri Raja Brawijaya.\n\n3. Wisata di probolinggo yang ketiga adalah Air Terjun Watu Lawang. Diberi nama air terjun watu lawang karena memiliki tebing besar yang menyerupai lawang (pintu).\n\n4. Wisata di probolinggo yang keempat adalah Air Terjun Triban. Air terjun ini memiliki ketinggian sekitar 5 meter, dan memiliki air yang sangat segar. \nDi air terjun ini anda bisa mandi dan bermain air karena memiliki kolam yang menampung air terjun sekitar 3-5 meter sehingga anda bisa berenang, \ndan bisa melompat dari atas tebing.\n\n5. Wisata di probolinggo yang kelima adalah Puncak B29 Bromo. Puncak ini merupakan viem point untuk menikmati keindahan gunung bromo. \nBerada dikawasan taman nasional bromo tengger semeru. Tepatnya diperbatasan argosari, senduro, lumajang dengan ngadirejo, sukapura, probolinggo. \nDiberi nama B29 karena puncak ini terletak di ketinggian 2.900 mdpl.\n\n6. Wisata di probolinggo yang keenam adalah Air Terjun Madakaripura. Berlokasi di sapih, branggah, kecamatan lumbang, \nair terjun ini merupakan air terjun tertinggi kedua di pulau jawa. Air terjun ini terletak di kawasan lereng gunung bromo yang memiliki ketinggian 200 meter. \nAir terjun ini juga disebut air terjun abadi karena air yang mengalir melimpah dan tidak pernah berkurang.\n\n\n7. Wisata di probolinggo yang ketujuh adalah Candi Jabung. Candi ini terletak di desa jabung, kecamatan paiton, kabupaten probolinggo. \nArsitektur candi ini mirip dengan candi bahal yang berada di Sumatera Utara, yang terdiri dari bagian batur, kaki, tubuh dan atap.\n\n8. Wisata di probolinggo yang kedelapan adalah Candi Kedaton. Candi ini terletak di dusun lawang kedaton, desa andung biru, kecamatan tiris, \nkabupaten probolinggo. Wisata ini berasal dari masa akhir kerajaan majapahit sekitar abad ke 14. \nCandi ini juga memiliki relief yang menceritakan kisah arjunawiwaha di sisi barat, kisah garudeya di sisi selatan, dan kisah bhomantaka di sisi timur.\n\n9. Wisata di probolinggo yang kesembilan adalah Museum Probolinggo. Museum ini menyimpan peninggalan masa lalu seperti artefak, \nuang kertas probolinggo, replika patung, benda pusaka hingga foto probolinggo pada masa laampau. \nMuseum ini dulunya merupakan gedung Societiet Gebow Harmony yang digunakan sebagai tempat berkumpulnya orang belanda untuk kegiatan hiburan.\n\n10. Wisata di probolinggo yang kesepuluh adalah Museum Dr. Mohamad Saleh. Museum ini terletak di jalan Dr. mohamad Saleh, probolinggo. \nDulunya tempat ini merupakan rumah dokter pribumi pertama di probolinggo yaitu Dr. mohamad Saleh. Di rumah ini dulunya para pemuda dari \nberbagai suku sering berkumpul untuk berdiskusi bersama Dr. mohamad Saleh yang merupakan pendiri Boedi Oetomo sehingga rumah itu sering \ndisebut rumah bhinneka tunggal ika. Museum ini menyimpan koleksi peralatan medis yang sering digunakan pada masa belanda.",
                            bg="#FA9269", fg="#241F1F",justify="left", font=("MontserratRoman Bold", 15,"bold"))
    label_description.place(x=127, y=150, anchor="nw")

    #  mengatur scrollregion pada canvas agar bisa melakukan scroll ke bawah
    frame6.update_idletasks()
    canvas1.config(scrollregion=canvas1.bbox('all'))

    # menghubungkan scrollbar dengan canvas
    scrollbar.config(command=canvas1.yview)

def beritamuseumsby():
    global frame6
    for widget in window.winfo_children():
        widget.destroy()
    # membuat scrollbar
    scrollbar = tk.Scrollbar(window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas1 = tk.Canvas(window, yscrollcommand=scrollbar.set)
    canvas1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)    

    frame6 = Frame(canvas1, bg="#FA9269", height=2000, width=1476, bd=0, highlightthickness=0, relief="ridge")
    frame6.place(x=0, y=0)
    canvas1.create_window((0, 0), window=frame6, anchor='nw')

    backbtn = Button(frame6, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_berita, relief="flat")
    backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

    logoteks_isiberita = Label(frame6, image=img_logoteks_toggle, bd=0 )
    logoteks_isiberita.place(x=530,y=16)

    gambarberitamuseumsby = Label(frame6, image=img_bermussby,bg="#FA9269")
    gambarberitamuseumsby.place(x=414,y=148)

    label_title = Label(frame6, text="3 Wisata Museum Gratis Tiket Masuk di Surabaya", bg="#FA9269", fg="#241F1F",justify="center",
                        font=("MontserratRoman Bold", 40))
    label_title.place(x=280, y=87, anchor="nw")

    label_description = Label(frame6,
                            text="1.Musem Olahraga \n\nMuseum yang berlokasi di Jl. Indragiri No.6, daerah Darmo kota Surabaya ini menyajikan cerita sejarah olahraga serta benda-benda peninggalan \npara Atlet dan Pahlawan Olahraga Surabaya. \n\nMuseum ini juga menyimpan koleksi-koleksi penghargaan dari para Atlet Surabaya. \nTidak hanya itu, design bangunannya yang instagramable juga cocok untuk kamu yang mau foto-foto. Museum ini buka dari jam 08.00 dsampai 15.00 WIB. \n\n 2.Museum Pendidikan \n\nMenempati sebuah bangunan di jalan Genteng Kali no. 10 yang merupakan bekas Gedung Sekolah Taman Siswa, \nMuseum Pendidikan didirikan untuk melestarikan sejarah dan budaya sebagai upaya mendukung kegiatan edukasi, riset dan rekreasi di Kota Surabaya. \n\nDisini kamu bisa melihat sejarah pendidikan di Indonesia, pahlawan- pahlawan pendidikan, dan juga ada open space yang luas untuk bersantai atau pun berfoto.\nMuseum ini dibuka dari jam 8 pagi sampai jam 3 sore. \n\n 3.Museum WR. Supratman\n\nMuseum ini adalah rumah yang ditinggali oleh WR. Supratman pada tahun 1937, sampai akhirnya meninggal pada 17 Agustus 1938. Di museum ini banyak sekali foto \nWR. Supratman dan kerabatnya yang terpampang di ruang tamu lalu ada koleksi baju dan juga replika biolammnya.\n\nBiasanya orang-orang yang berkunjuung ke tempat ini akan berfoto di patung paling ikonik dari museum ini, yaitu patung WR. Supratman yang berppose \nmemainkan biola yang ada di depan museum.\n\nMuseum ini dibuka dari pukul 08.00 sampai 15.00.Itulah 3 musem yang bisa kamu kunjungi dengan tiket masuk yang gratis. \nTapi kamu tetap harus melakukan reservasi melalui tiketwisata.surabaya.go.id.\n\n sumber berita : https://www.liputan6.com/regional/read/5174063/3-wisata-museum-gratis-tiket-masuk-di-surabaya",
                            bg="#FA9269", fg="#241F1F",justify="left", font=("MontserratRoman Bold", 15,"bold"))
    label_description.place(x=127, y=540, anchor="nw")

    #  mengatur scrollregion pada canvas agar bisa melakukan scroll ke bawah
    frame6.update_idletasks()
    canvas1.config(scrollregion=canvas1.bbox('all'))

    # menghubungkan scrollbar dengan canvas
    scrollbar.config(command=canvas1.yview)

def beritabltr():
    global frame6
    for widget in window.winfo_children():
        widget.destroy()
    # membuat scrollbar
    scrollbar = tk.Scrollbar(window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas1 = tk.Canvas(window, yscrollcommand=scrollbar.set)
    canvas1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)    

    frame6 = Frame(canvas1, bg="#FA9269", height=2000, width=1476, bd=0, highlightthickness=0, relief="ridge")
    frame6.place(x=0, y=0)
    canvas1.create_window((0, 0), window=frame6, anchor='nw')

    backbtn = Button(frame6, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_berita, relief="flat")
    backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

    logoteks_isiberita = Label(frame6, image=img_logoteks_toggle, bd=0 )
    logoteks_isiberita.place(x=530,y=16)

    gambarberitamuseumsby = Label(frame6, image=img_bermussby,bg="#FA9269")
    gambarberitamuseumsby.place(x=414,y=148)

    label_title = Label(frame6, text="10 Tempat Wisata di Blitar Terbaru Yang Paling Hits", bg="#FA9269", fg="#241F1F",justify="center",
                        font=("MontserratRoman Bold", 40))
    label_title.place(x=280, y=87, anchor="nw")

    label_description = Label(frame6,
                            text="1. Pantai Tambakrejo \n\nPantai ini berlokasi di desa tambakrejo kecamatan wonotirto, yang memiliki panjang sekitar 10 km yang terbentang menjadi teluk. \n\nDi pantai ini anda bisa mandi karena ombaknya tidak terlalu besar. Biasanya juga diadakan acara larung sesaji untuk memperingati tahun baru islam. \n\n2. Candi Penataran \n\nCandi ini berlokasi di desa penataran, kecamatan nglegok, kabupaten blitar, jawa timur dan berada di kaki gunung kelud. Candi ini merupakan kompleks candi terbesar di provinsi jawa timur. Kompleks candi ini ditemukan oleh Sir Thomas Stamford Reffles, yang merupakan letnan gubernur jendral masa kolonial inggris di Indonesia. \n\n3. Goa Embultuk \n\nGoa ini berada di desa tumpakkepuh, kecamatan bakung, blitar. Dipenghujung perjalanan dalam goa kita dapat beristirahat di sebuah kubah yang menyerupai aula besar dimana dapat menampung ribuan orang. Goa ini dulunya sempat menjadi tempat persembunyian gerakan sebuah partai terlarang (PKI).\n\n4. Arca Warak \n\nBerlokasi di desa modangan, kecamatan ngledgok, kabupaten blitar. Pada situs ini ditemukan artefak seperti batu candi, jaladwara, kemuncak, dan lumpang. Jaladwara adalah unsur bangunan yang berfungsi mengalirkan air. \n\n5. Candi Sawentar \n\nCandi ini berada di desa sawentar, kecamatan kanigoro, blitar, jawa timur. Dalam kitab negarakertagama, candi sawentar disebut lwa wentar. Tinggi candi sampai ke puncak 10,65 M. \n\n6. Makam Bung Karno \n\nBerlokasi di desa bendogerit, kompleks makam bung karno adalah bangunan berbentuk joglo khas jawa, di dalamnya terdapat makam bung karno yang diapit makam kedua orang tuanya. Di area makam juga terdapat perpustakaan tempat menyimpan buku dan tulisan bung karno. \n\n7. Curug dan Kedung Badrun \n\nBerlokasi diperbatasan desa tumpakoyot dan desa bululawang, kecamatan bakung, kabupaten blitar. Curug Badrun terdiri dari curug bertingkat dan kedung di bawahnya. Air terjun ini memiliki ketinggian 8 meter, sementara kedung atau kolamnya memiliki lebar 10 meter. \n\n8. Kampung Afrika Blitar \n\nKampung tradisional ini memiliki beberapa model bangunan dengan tambahan corak kental dengan nuansa ala afrika. Selain itu disediakan wahana bermain mulai dari ATV mini dan flying fox. \n\n9. Blitar Park \n\nBlitar park merupakan tempat bermain dengan wahana bermain terlengkap. Blitar park mengusung konsep Place ti Play and Education, sehingga cocok untuk berlibur keluarga. \n\n10. Hutan Pinus Gogoniti \n\nHutan ini memiliki banyak spot foto instagramable yang kece. Beberapa spot yang tidak boleh dilewatkan adalah rumah pohon, gembok cinta serta hammock yang menjadi andalan tempat yang sejuk dan asri.",
                            bg="#FA9269", fg="#241F1F",justify="left", font=("MontserratRoman Bold", 15,"bold"))
    label_description.place(x=127, y=540, anchor="nw")

    #  mengatur scrollregion pada canvas agar bisa melakukan scroll ke bawah
    frame6.update_idletasks()
    canvas1.config(scrollregion=canvas1.bbox('all'))

    # menghubungkan scrollbar dengan canvas
    scrollbar.config(command=canvas1.yview)

def beritamalang():
    global frame6
    for widget in window.winfo_children():
        widget.destroy()
    # membuat scrollbar
    scrollbar = tk.Scrollbar(window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas1 = tk.Canvas(window, yscrollcommand=scrollbar.set)
    canvas1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)    

    frame6 = Frame(canvas1, bg="#FA9269", height=2000, width=1476, bd=0, highlightthickness=0, relief="ridge")
    frame6.place(x=0, y=0)
    canvas1.create_window((0, 0), window=frame6, anchor='nw')

    backbtn = Button(frame6, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_berita, relief="flat")
    backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

    logoteks_isiberita = Label(frame6, image=img_logoteks_toggle, bd=0 )
    logoteks_isiberita.place(x=530,y=16)

    gambarberitamuseumsby = Label(frame6, image=img_bermussby,bg="#FA9269")
    gambarberitamuseumsby.place(x=414,y=148)

    label_title = Label(frame6, text="Tempat Wisata di Malang Yang Wajib Dikunjungi", bg="#FA9269", fg="#241F1F",justify="center",
                        font=("MontserratRoman Bold", 40))
    label_title.place(x=280, y=87, anchor="nw")

    label_description = Label(frame6,
                            text="1. Jatimpark 3 \n\nJatimpark 3 memiliki lebih dari 8 area tematik, mulai dari Dino Land hingga Fun Tech Plaza. Selanjutnya terdapat perkampungan Korea Selatan, selain itu juga ada zona India, Cina serta Eropa di dalam jatimpark 3. Terdapat juga patung lilin tokoh penting Indonesia dan mancanegara. \n\n2. Pulau Sempu \n\nSegara anakan merupakan daya tarik utama dari pulau ini. Air dari telaga berasal dari ombak laut selatan yang masuk melalui lubang tebing di sisi danau. Kamu bisa bebas berenang, memancing atau bermain di pasir putih yang landai. \n\n3. Paralayang dan Rumah Pohon \n\nArea ini berada di atas Gunung Banyak. Dari atas bisa melihat pemandangan seluruh kota Batu. Jika malam hari anda bisa menikmati pemandangan kerlap kerlip kota Batu lengkap dengan gemerlap bintang yang menghiasi malam. \n\n4. Selecta Malang \n\nAnda bisa menikmati berbagai wahana menarik dan berkeliling melihat pemandangan taman bunga dengan sky bike hingga bermain air dengan berbagai seluncuran di water park selecta malang. \n\n5. Museum Angkut  \n\nTerdapat banyak jenis transportasi dari sepeda onthel, delman, mobil listrik hingga mobil balap F1. Ada 10 zona yang bisa dikunjungi yaiu zona edukasi, italia, inggris, prancis, las vegas, jerman, hollwood, jepang, gangster dan croadway. \n\n6. Batu Night Spectacular \n\nWisata ini memiliki air mancur yang dapat menari dan berubah warna sesuai musik yang diputar. Lampion Garden juga tidak kalah menarik. Terdapat berbagai warna dan bentuk lampion yang cantik. Ada juga rumah hantu, baby wheel, mouse coaster, art trick, gravitron dan avatar. \n\n7. Coban Pelangi \n\nAnda bisa melihat pelangi diantara aliran air terjun setinggi 30 meter jika anda beruntung. Bisa juga bermain air di tepi air terjun atau duduk di pendopo yang ada. Wisata in berada di ketinggian 1.299 meter di atas permukaan laut. \n\n8. Pantai Balekambang \n\nPura yang dihubungkan dengan jembatan beton sepanjang 100 meter terlihat cantik terutama saat senja. Hamparan pasir dan ombak kecil pun menjadi pemandangan menarik, kamu juga bisa berenang atau bermain air. \n\n9. Taman Ramah Lingkungan \n\nTaman ini berisi kebun binatang mini dan informasi mengenai pemeliharaan lingkungan. Saat masuk akan disambut patung gajah yang terbuat dari televisi. Salah satu wahana yang ada seperti jungle adventure, anda dapat berkeliling hutan buatan dengan kereta buatan. \n\n10. Jatimpark 1 \n\nTempat ini memiliki kolam renang berlatar Ken Arok. Untuk wahana edukasi, terdapat Science stadium yang merupakan laboratorium outdoor dan indoor yang berisi informasi dan peragaan kacamata, biologi, kimia hingga matematika.",
                            bg="#FA9269", fg="#241F1F",justify="left", font=("MontserratRoman Bold", 15,"bold"))
    label_description.place(x=127, y=540, anchor="nw")

    #  mengatur scrollregion pada canvas agar bisa melakukan scroll ke bawah
    frame6.update_idletasks()
    canvas1.config(scrollregion=canvas1.bbox('all'))

    # menghubungkan scrollbar dengan canvas
    scrollbar.config(command=canvas1.yview)

def beritasurabaya():
    global frame6
    for widget in window.winfo_children():
        widget.destroy()
    # membuat scrollbar
    scrollbar = tk.Scrollbar(window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas1 = tk.Canvas(window, yscrollcommand=scrollbar.set)
    canvas1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)    

    frame6 = Frame(canvas1, bg="#FA9269", height=2000, width=1476, bd=0, highlightthickness=0, relief="ridge")
    frame6.place(x=0, y=0)
    canvas1.create_window((0, 0), window=frame6, anchor='nw')

    backbtn = Button(frame6, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_berita, relief="flat")
    backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

    logoteks_isiberita = Label(frame6, image=img_logoteks_toggle, bd=0 )
    logoteks_isiberita.place(x=530,y=16)

    gambarberitamuseumsby = Label(frame6, image=img_bermussby,bg="#FA9269")
    gambarberitamuseumsby.place(x=414,y=148)

    label_title = Label(frame6, text="Rekomendasi Destinasi Wisata Terbaik di Surabaya", bg="#FA9269", fg="#241F1F",justify="center",
                        font=("MontserratRoman Bold", 40))
    label_title.place(x=280, y=87, anchor="nw")

    label_description = Label(frame6,
                            text="1. Klenteng Sanggar Agung \n\nKlenteng ini memiliki arsitektur yang sangat indah karena lokasinya yang dipinggir pantai. Sekitar klenteng juga terdapat hutan bakau yang jadi spot hunting foto instagramable. \n\n2. Monumen Kapal Selam \n\nMonumen ini terbuat dari kapal selam asli yang digunakan untuk melakukan pembebasan Irian Barat dari penjajah Belanda.\n\n3. Patung Buddha Berwajah 4 \n\nWisata ini merupakan wisata religi yang menyuguhkan patung buddha empat wajah. Patung empat wajah ini juga dinobatkan sebagai patung tertinggi di Indonesia. \n\n4. Museum 10 November \n\nHari bersejarah kota Surabaya diperingati sebagai hari pahlawan. Untuk mengenang, anda bisa mengunjungi museum 10 november. Disana anda bisa melihat beberapa peninggalan Bung Tomo dan pejuang lainnya. Anda juga bisa melihat diorama dari penggalan peristiwa bersejarah. \n\n5. Gereja Perawan Maria Tak Berdosa  \n\nUntuk yang ingin berburu arsitektur sekaligus wisata religi, gereja perawan tak berdosa wajib dikunjungi. Dengan nuansa arsitekturnya yang klasik era kolonial bangunan ini juga merupakan bangunan bersejarah. \n\n6. Jembatan Suramadu \n\nJembatan ini sangat megah dan membentang diatas lautan yang menghubungkan kota Surabaya dengan Pulau Madu. Kemegahannya menjadi daya tarik terutama malam hari saat jembatan suramadu dihujani cahaya lampu. \n\n7. Kebun Raya Mangrove Gunung Anyar \n\nLuas lahan hutan ini mencapai 25 hektar. Pengunjung juga bisa menikmati berjalan santai dengan panjang rute 630 meter. \n\n8. Masjid Sunan Ampel \n\nMasjid ini diatas tanah 120 x 180 meterpersegi. Pertama kali didirikan tahun 1421 oleh Sunan Ampel yang dibantu beberapa sahabatnya. Sejak tahun 1972, pemerintah menetapkan masjid agung sunan ampel sebagai destinasi wisata religi. \n\n9. Kembang Jepun \n\nWisata ini menyuguhkan wisata ala-ala negeri Tiongkok. Selain bisa berfoto, kamu juga bisa berkeliling dan merasakan kuliner. Di siang hari banyak orang melakukan kegiatan jual beli, sedangkan malam hari menawarkan berbagai kuliner. \n\n10. Taman Bungkul \n\nTaman ini merupakan area wisata religi. Tempat ini merupakan makam salah satu ulama penyebar agama islam yakni Ki Ageng Supo atau Sunan Bungkul. Fasilitas yang ditawarkan tempat ini adalah tempat bermain anak. \n\n sumber berita : https://www.liputan6.com/regional/read/5174063/3-wisata-museum-gratis-tiket-masuk-di-surabaya",
                            bg="#FA9269", fg="#241F1F",justify="left", font=("MontserratRoman Bold", 15,"bold"))
    label_description.place(x=127, y=540, anchor="nw")

    #  mengatur scrollregion pada canvas agar bisa melakukan scroll ke bawah
    frame6.update_idletasks()
    canvas1.config(scrollregion=canvas1.bbox('all'))

    # menghubungkan scrollbar dengan canvas
    scrollbar.config(command=canvas1.yview)

def beritapacitan():
    global frame6
    for widget in window.winfo_children():
        widget.destroy()
    # membuat scrollbar
    scrollbar = tk.Scrollbar(window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas1 = tk.Canvas(window, yscrollcommand=scrollbar.set)
    canvas1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)    

    frame6 = Frame(canvas1, bg="#FA9269", height=2000, width=1476, bd=0, highlightthickness=0, relief="ridge")
    frame6.place(x=0, y=0)
    canvas1.create_window((0, 0), window=frame6, anchor='nw')

    backbtn = Button(frame6, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_berita, relief="flat")
    backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

    logoteks_isiberita = Label(frame6, image=img_logoteks_toggle, bd=0 )
    logoteks_isiberita.place(x=530,y=16)

    gambarberitamuseumsby = Label(frame6, image=img_bermussby,bg="#FA9269")
    gambarberitamuseumsby.place(x=414,y=148)

    label_title = Label(frame6, text=" 7 Rekomendasi Wisata Pantai di Pacitan", bg="#FA9269", fg="#241F1F",justify="center",
                        font=("MontserratRoman Bold", 40))
    label_title.place(x=280, y=87, anchor="nw")

    label_description = Label(frame6,
                            text="1. Pantai Klayar \n\nPantai ini memiliki pasir putih yang indah dan diapit oleh tebing-tebing tinggi. Terdapat juga menara pandang yang dapat digunakan untuk menikmati pemandangan. Salah satu tebing yang ada terlihat seperti sphinx di Mesir. \n\n2. Pantai Watu Karung \n\nPantai ini memiliki bukit karang, air biru kehijauan, pasir putih , dan tempat berselancar. Pantai ini juga terletak menghadap Samudra Hindia, sehingga ombaknya mencapai 5 meter. n\n3. Pantai Soge Pacitan \n\nPantai Soge bergaya futuristik terbuat dari pipa melengkung dibagian atasnya sehingga seperti kubah  besar. Pantai ini juga memiliki jembatan sepanjang 50 meter. Jembatan Soge menjadi ikon jalan selatan Pacitan karena desainnya berbeda dengan jembatan lainnya. \n\n4. Pantai Kasap \n\nPantai kasap merupakan pantai yang menyerupai wisata Raja Ampat. Ombak yang menggulung ke arah bibir pantai hingga hamparan birunya laut. Pulau kecil dan tebing di tengah laut Pantai Kasap. Pantai ini juga memiliki semilir sepoi angin laut yang membuat tempat ini sejuk. \n\n5. Pantai Banyu Tibo \n\nPantai ini memiliki pasir putih dengan air terjun yang jatuh langsung bermuara ke pantai. Sumber air terjun berasal dari air tawar di bawah tanah perbukitan di sekitar pantai. Mengalir seperti sungai dengan air jernih ke bibir pantai lalu turun ke pantai sebagai air terjun. Pantai ini juga memiliki bebatuan serta gugusan bukit yang menambah keindahan. \n\n6. Pantai Srau \n\nPantai ini dijuluki palm beach karena banyak pohon kelapa. Pasir putih lembut dan batu karang menghiasi pantai. Memiliki ombak yang besar pantai ini sering digunakan unjuk gigi para peselancar. Di pantai ini juga kita bisa ngecamp di dekat pantai untuk menikmati rasi bintang di malam hari dan menyaksikan sunrise. \n\n7. Pantai Pidakan \n\nPantai ini terkenal hamparan kerikil yang menyelimuti pasir di sepanjang pantai. Kerikil di pantai ini berwarna putih bersih, lalu 70% material pantai berupa bebatuan yang bervariasi bentuk maupun ukuran. Adanya mercusuar didekat pantai menambah daya tarik, serta pohon kelapa membuat sejuk suasana. n\n8. Pantai Ngiroboyo \n\nPantai ini memiliki pasir hitam yang sangat menakjubkan. Ketika terpapar sinar matahari, pasir hitam akan berkilau, terutama setelah ombak menyapu daratan pasir. Saat ini kawasan pantai dijadikan tempat konservasi penyu. \n\n9. Pantai Watu Bale Pacitan \n\nPantai ini memiliki wahana berupa jembatan gantung sepanjang 100 meter menghubungkan pesisir karang pantai ke suatu pulau. Pantai ini juga memiliki ikon khas berbentuk batu karang yang mirip bale atau balai. Pantai ini pun tidak berpasir serta berada di antara tebing tinggi dan perbukitan. Terdapat juga pantai lepas, birunya lautan, karang kokoh, deburan ombak, dan rimbunnya pohon pandan. \n\n10. Pantai Taman Ngadirojo Pacitan \n\nMemiliki pasir putih yang lembut, ombak yang memecah karang, dan lambaian pohon kelapa. Terdapat juga wahana flying fox untuk menikmati keindahan pantai dari ketinggian. Pantai ini juga memiliki konservasi penyu, di pesisir pantai digunakan penyu untuk bertelur. Setelah itu telurnya ditinggal dan penyu akan kembali ke perairan Australia. Telur penyu akan dipindahkan ke lokasi penetasan lalu akan dilepaskan kembali ke lautan.",
                            bg="#FA9269", fg="#241F1F",justify="left", font=("MontserratRoman Bold", 15,"bold"))
    label_description.place(x=127, y=540, anchor="nw")

    #  mengatur scrollregion pada canvas agar bisa melakukan scroll ke bawah
    frame6.update_idletasks()
    canvas1.config(scrollregion=canvas1.bbox('all'))

    # menghubungkan scrollbar dengan canvas
    scrollbar.config(command=canvas1.yview)

def laman_jelajahi():
    global frame7
    frame7 = Frame(window, bg="#FA9269")
    frame7.place(x=0, y=0, width=1476, height=866)

    def filter_data(event=None): #digunakan utk memanggil algoritma linear search dan bubble sort
        location = selected_location.get() #mendapatkan lokasi yg dipilih dari elemen selected location
        keyword = search_entry.get() #mendapatkan nilai dri elemen search entry
        attractions = []
        if location == 'Jawa Timur':
            for data in all_data:
                attractions.append(data[1])
        else:
            for data in all_data:
                if data[0] == location:
                    attractions.append(data[1])
        filtered_data = linear_search(attractions, keyword)
        selection_sort(filtered_data)  # Menjalankan algoritma sorting setelah filtering
        display_filtered_data(filtered_data)
        search_entry.bind('<KeyRelease>', filter_data)

    def linear_search(arr, target):
        filtered_data = []
        for item in arr:
            if target.lower() in item.lower():
                filtered_data.append(item)
        return filtered_data
        
    def selection_sort(arr):
        n = len(arr)
        for i in range(n-1):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

    #membaca data dari file csv
    all_data = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader: #menambahkan semua data csv ke dalam list bernama all_data.append(row)
            all_data.append(row)


    selected_location = StringVar()
    selected_location.set('Jawa Timur')

    # Membuat radio button untuk memilih lokasi wisata
    surabaya_radio = Radiobutton(frame7, text='Surabaya', variable=selected_location, bg="#FA9269", value='Surabaya')
    malang_radio = Radiobutton(frame7, text='Malang', variable=selected_location, bg="#FA9269", value='Malang')
    kediri_radio = Radiobutton(frame7, text='Kediri', variable=selected_location, bg="#FA9269", value='Kediri')
    probolinggo_radio = Radiobutton(frame7, text='Probolinggo', variable=selected_location, bg="#FA9269", value='Probolinggo')
    blitar_radio = Radiobutton(frame7, text='Blitar', variable=selected_location, bg="#FA9269", value='Blitar')
    mojokerto_radio = Radiobutton(frame7, text='Mojokerto', variable=selected_location, bg="#FA9269", value='Mojokerto')
    jawa_timur_radio = Radiobutton(frame7, text='Jawa Timur', variable=selected_location, bg="#FA9269", value='Jawa Timur')
    pasuruan_radio = Radiobutton(frame7, text='Pasuruan', variable=selected_location, bg="#FA9269", value='Pasuruan')
    batu_radio = Radiobutton(frame7, text='Batu', variable=selected_location, bg="#FA9269", value='Batu')
    madiun_timur_radio = Radiobutton(frame7, text='Madiun', variable=selected_location, bg="#FA9269", value='Madiun')

    # Menampilkan radio button pada GUI
    jawa_timur_radio.place(x=200, y=210)
    surabaya_radio.place(x=300, y=210)
    malang_radio.place(x=400, y=210)
    kediri_radio.place(x=500, y=210)
    probolinggo_radio.place(x=600, y=210)
    blitar_radio.place(x=720, y=210)
    mojokerto_radio.place(x=800, y=210)
    pasuruan_radio.place(x=900, y=210)
    batu_radio.place(x=1000, y=210)
    madiun_timur_radio.place(x=1070, y=210)

    search_entry = Entry(frame7,bd=0)
    search_button = Button(frame7, text='Search',bd=0,bg="black",fg="white", command=filter_data)
    # Menampilkan kolom entry pada GUI
    search_entry.place(x=495, y=131, width=271, height=30)
    search_button.place(x=796, y=131, width=80, height=30)
    ALLmenu_toggle(frame7)

    def display_filtered_data(filtered_data):
            global frame8
                    # Membuat frame untuk menampilkan hasil filter
            frame8 = Frame(window, bg="#FFFFFF")
            frame8.place(x=0, y=276, width=1476, height=510)
            # Menghapus widget sebelumnya
            for widget in frame8.winfo_children():
                widget.destroy()

            # Menambahkan Treeview widget untuk menampilkan hasil filter
            tree = ttk.Treeview(frame8, columns=('attraction',), show='headings')
            tree.heading('attraction', text='Hasil Pencarian')
            tree.pack(fill=BOTH, expand=YES)  # Mengisi seluruh area Frame

            # Mengatur gaya (style) untuk Treeview
            style = ttk.Style()
            style.configure('Custom.Treeview', font=('Arial', 15))
            tree.configure(style='Custom.Treeview')
                # Mengatur lebar kolom Treeview
            tree.column('attraction', width=500, anchor='center')
            
            # Menampilkan data yang telah difilter dengan warna selang-seling
            for i, item in enumerate(filtered_data):
                if i % 2 == 0:
                    tree.insert('', 'end', values=(item,), tags=('item_even',))
                else:
                    tree.insert('', 'end', values=(item,), tags=('item_odd',))

            tree.tag_configure('item_even', background='lightblue')
            tree.tag_configure('item_odd', background='lightgreen')
            tree.bind('<<TreeviewSelect>>', display_detail)

            search_entry.place(x=495, y=131, width=271, height=30)
            search_button.place(x=796, y=131, width=80, height=30)

    def display_detail(event):
            # Mendapatkan item yang dipilih dari Treeview
            item = event.widget.item(event.widget.selection())['values'][0]
            if item == 'Tugu Pahlawan':
                detailwisata_tupal()
            if item == 'Museum Surabaya':
                detailwisata_museumsurabaya()
            if item == 'Monumen Kapal Selam':
                detailwisata_monkasel()
            if item == 'Kebun Binatang Surabaya':
                detailwisata_bonbin()
            if item == 'Surabaya North Quay':
                detailwisata_snq()
            if item == 'Taman Bungkul':
                detailwisata_bungkul()
            if item == 'Kenjeran':
                detailwisata_kenjeran()
            if item == 'Romokalisari Adventure':
                detailwisata_romokalisari()
            if item == 'Museum Jalasveva Jayamahe':
                detailwisata_jalasveva()
            if item == 'Kebun Bibit':
                detailwisata_bibit()
            if item == 'Hutan Mangrove':
                detailwisata_mangrove()
            if item == 'Museum House Of Sampoerna':
                detailwisata_sampoerna()
            if item == 'Taman Prestasi':
                detailwisata_prestasi()
            if item == 'Klenteng Sanggar Agung':
                detailwisata_klenteng()
            if item == 'Kya Kya':
                detailwisata_kyakya()
            if item == 'Malang Night Paradise':
                detailwisata_mnp()
            if item == 'Alun Alun Malang':
                detailwisata_alunmalang()
            if item == 'Kampung Warna Warni':
                detailwisata_kww()
            if item == 'Hawai Waterpark':
                detailwisata_hawai()
            if item == 'Florawisata Santerra De Laponte':
                detailwisata_delaponte()
            if item == 'Pantai Sempu':
                detailwisata_sempu()
            if item == 'Kampung Tridi':
                detailwisata_tridi()
            if item == 'Taman Wisata Wendit':
                detailwisata_wendit()
            if item == 'Coban Pelangi':
                detailwisata_pelangi()
            if item == 'Pantai Balekambang':
                detailwisata_balekambang()            
            if item == 'Pantai Parang Dowo':
                detailwisata_parangdowo()
            if item == 'Coban Rondo':
                detailwisata_rondo()
            if item == 'Kebun Teh Wonosari':
                detailwisata_bunteh()
            if item == 'Sumber Sira Putukrejo':
                detailwisata_sumbersirah()
            if item == 'Air Terjun Seweru':
                detailwisata_airterjunseweru()
            if item == 'Monumen Kresek':
                detailwisata_monumenkresek()
            if item == 'Gunung Kendil':
                detailwisata_gunungkendil()
            if item == 'Hutan Pinus Nongko Ijo':
                detailwisata_hpni()
            if item == 'Air Terjun Kertoembo':
                detailwisata_atk()
            if item == 'Taman Kota Caruban':
                detailwisata_tkc()
            if item == 'Wahana Bermain Sekar Arum':
                detailwisata_wbsa()
            if item == 'Dumilah Waterpark':
                detailwisata_dw()
            if item == 'Air Terjun Banyulawe Dong':
                detailwisata_atbd()
            if item == 'Air Terjun Kucur':
                detailwisata_Atk()
            if item == 'Bukit Gandrung':
                detailwisata_gandrung()
            if item == 'Monumen Syu':
                detailwisata_syu()
            if item == 'Monumen Airlangga':
                detailwisata_airlangga()
            if item == 'Kediri Eco Park':
                detailwisata_kep()
            if item == 'Museum Fotografi':
                detailwisata_fotografi()
            if item == 'Taman Tirtoyoso':
                detailwisata_tirtoyoso()
            if item == 'Candi Surowono':
                detailwisata_surowono()
            if item == 'Bukit Ongakan':
                detailwisata_ongakan()
            if item == 'Gunung Kelud':
                detailwisata_kelud()
            if item == 'Simpang Lima Gumul':
                detailwisata_gumul()
            if item == 'Bee Jay Bakau Resort':
                detailwisata_bjbr()
            if item == 'Gunung Argopuro':
                detailwisata_argopuro()
            if item == 'Pantai Bentar':
                detailwisata_bentar()
            if item == 'Gili Ketapang':
                detailwisata_ketapang()
            if item == 'Air Terjun Madakaripura':
                detailwisata_madakaripura()
            if item == 'Air terjun Umbulan':
                detailwisata_umbulan()
            if item == 'Danau Ranu Agung':
                detailwisata_agung()            
            if item == 'Museum Probolinggo':
                detailwisata_muspro()
            if item == 'Candi Jabung':
                detailwisata_jabung()
            if item == 'Pantai Duta':
                detailwisata_duta()

            else:
                # Menghapus widget sebelumnya
                for widget in frame8.winfo_children():
                    widget.destroy()

                # Menambahkan label untuk menampilkan judul detail wisata
                detail_label = Label(frame8, text='Detail Wisata:')
                detail_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

                # Menampilkan detail wisata yang dipilih
                detail = 'Detail wisata {} belum tersedia.'.format(item)
                for data in all_data:
                    if data[1] == item:
                        detail = 'Detail wisata {}: Gambar={}, Alamat={}, Komponen={}'.format(item, data[2], data[3], data[4])
                detail_text = Text(frame8, height=10, width=50)
                detail_text.insert(END, detail)
                detail_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=W)

#Template Gambar Detail Wisata
img_backbtndetailwisata = PhotoImage(file="back btn detail wisata.png")
img_logoteks_toggle = PhotoImage(file="logoteks_toggle.png")
templatedetailwisata = PhotoImage(file="template detail wisata.png")
# SURABAYA
img_tupal = PhotoImage(file="fototupal.png")
img_museumsby = PhotoImage(file="museum surabaya.png")
img_kbs = PhotoImage(file="kbs.png")
img_monkasel = PhotoImage(file="monkasel.png")
img_snq = PhotoImage(file="snq.png")
img_bungkul = PhotoImage(file="bungkul.png")
img_kenjeran = PhotoImage(file="kenjeran.png")
img_romo = PhotoImage(file='romokalisari.png')
img_jalasveva = PhotoImage(file='jalasveva.png')
img_bibit = PhotoImage(file='bibit.png')
img_bambu = PhotoImage(file='bambu.png')
img_mangrove = PhotoImage(file='mangrove.png')
img_sampoerna = PhotoImage(file='sampoerna.png')
img_prestasi = PhotoImage(file='prestasi.png')
img_klenteng = PhotoImage(file='klenteng.png')
img_kyakya = PhotoImage(file='kyakya.png')


def detailwisata_tupal():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailtupal = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailtupal.place(x=530,y=16)

        fototupal = Label(frame9, image=img_tupal, bg="#FA9269")
        fototupal.place(x=176.0, y=127.0)

        templtdetailtupal = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailtupal.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Monumen Tugu Pahlawan", fg="#FFFFFF", font=("MontserratRoman Bold", 30))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_tupal = Label(frame9, anchor="nw", bg="black", text="8/10", fg="#FFFFFF", font=("MontserratRoman Bold", 30))
        rating_tupal.place(x=951.0, y=380.0)

        alamat_tupal = Label(frame9, anchor="nw", bg="black", text="Jl. Pahlawan, Alun-alun Contong, Kec.\nBubutan, Surabaya, Jawa Timur 60174",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_tupal.place(x=738.0, y=276.0)

        sejarah_tupal = Label(frame9, anchor="nw", bg="black", text="Museum Sepuluh November Surabaya adalah \nsalah satu museum yang terletak di Kota \nSurabaya, dibangun pada tahun 1945. Museum ini \ndibangun dengan tujuan untuk mempelajari dan \nmemperdalam peristiwa Pertempuran Sepuluh\n November 1945, Museum Sepuluh November \nberalamat di Jalan Pahlawan, Surabaya",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_tupal.place(x=736.0, y=451.0)

def detailwisata_museumsurabaya():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailtupal = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailtupal.place(x=530,y=16)

        fototupal = Label(frame9, image=img_museumsby, bg="#FA9269")
        fototupal.place(x=176.0, y=127.0)

        templtdetailtupal = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailtupal.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Museum Surabaya", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_tupal = Label(frame9, anchor="nw", bg="black", text="4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_tupal.place(x=951.0, y=380.0)

        alamat_tupal = Label(frame9, anchor="nw", bg="black", text="Jl. Tunjungan No.1, Genteng, Kec. Genteng\nSurabaya, Jawa Timur 60275",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_tupal.place(x=738.0, y=276.0)

        sejarah_tupal = Label(frame9, anchor="nw", bg="black", text="Gedung pemerintahan & museum dengan\nartefak yang mempertontonkan sejarah\ndomestik & sipil.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_tupal.place(x=736.0, y=451.0)

def detailwisata_monkasel():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailtupal = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailtupal.place(x=530,y=16)

        fototupal = Label(frame9, image=img_monkasel, bg="#FA9269")
        fototupal.place(x=176.0, y=127.0)

        templtdetailtupal = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailtupal.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Monumen Kapal Selam Surabaya", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_tupal = Label(frame9, anchor="nw", bg="black", text="4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 28))
        rating_tupal.place(x=951.0, y=380.0)

        alamat_tupal = Label(frame9, anchor="nw", bg="black", text="Jl. Pemuda No.39, Embong Kaliasin, Kec.\nGenteng, Surabaya, Jawa Timur 60271",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_tupal.place(x=738.0, y=276.0)

        sejarah_tupal = Label(frame9, anchor="nw", bg="black", text="Monumen Kapal Selam, atau disingkat Monkasel,\n adalah sebuah museum kapal selam yang\nterdapat di Embong Kaliasin, Genteng, Surabaya. \nTerletak di pusat kota yaitu di Jalan Pemuda,\ntepat di sebelah Plaza Surabaya, dan terdapat\npintu akses untuk mengakses mal dari\ndalam monumen",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_tupal.place(x=736.0, y=451.0)

def detailwisata_bonbin():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_kbs, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Kebun Binatang Surabaya", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Setail No.1, Darmo, Kec. Wonokromo, \nSurabaya, Jawa Timur 60241",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Kebun Binatang Surabaya adalah salah satu \nkebun binatang yang populer di Indonesia dan \nterletak di Surabaya. KBS merupakan kebun \nbinatang yang pernah terlengkap se-Asia Tenggara, \ndi dalamnya terdapat lebih dari 230 spesies satwa \nyang berbeda yang terdiri lebih dari \n2179 ekor satwa.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_snq():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_snq, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Surabaya North Quay", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Perak Utara, Kec. Pabean Cantikan, \nSurabaya, Jawa Timur 60165",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Dek di atap gedung pencakar langit yang \nmenawarkan panorama indah pelabuhan, \nlaut, & kapal pesiar yang lewat.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_bungkul():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_snq, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Taman Bungkul", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,6/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Taman Bungkul, Darmo, \nKec. Wonokromo, Surabaya, Jawa Timur \n60241",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Taman Bungkul adalah taman wisata\nkota yang terletak di pusat\nkota Surabaya, tepatnya di Jalan\nRaya Darmo. Taman ini berdiri di area\nseluas 900 meter persegi.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_kenjeran():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_kenjeran, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Kenjeran", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Kenjeran, Kec. Bulak, Surabaya,\nJawa Timur 60123",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Ini adalah pantai legendaris di Surabaya,\ndekat dengan Jembatan Suramadu. Di dalamnya\nbanyak kuliner khas Surabaya, seperti\nsate kerang, es kelapa muda dan olahan makanan\nkhas pantai. Dengan harga yang terjangkau\ninilah salah satu wisata favorit di Surabaya.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_romokalisari():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_romo, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Romokalisari Adventure", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Romokalisari I, Romokalisari,\nKec. Benowo, Surabaya, Jawa Timur\n60192",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Surabaya punya tempat wisata baru.\nWali Kota Surabaya Eri Cahyadi telah\nmeresmikan Romokalisari Adventure Land.\nDi sini, ada tujuh wahana menarik\ndan seru untuk dikunjungi bersama\nkeluarga dan teman.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_jalasveva():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_jalasveva, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Museum Jalasveva Jayamahe", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,6/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text=" Armada Timur Ujung, Ujung, Kec.\nSemampir, Surabaya, Jawa Timur 60155",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text=" Monumen ini menggambarkan sosok Perwira TNI Angkatan Laut\nberbusana Pakaian Dinas Upacara (PDU) lengkap dengan\npedang kehormatan yang sedang menerawang ke arah laut,\nserasa siap menantang gelombang dan badai di lautan,\nbegitu pula yang ingin di perlihatkan bahwa\nangkatan laut Indonesia siap berjaya. Patung\ntersebut berdiri di atas bangunan dan\ntingginya mencapai 30,6 meter. Monumen\nJalesveva Jayamahe menggambarkan generasi penerus\nbangsa yang yakin dan optimis untuk\nmencapai cita-cita bangsa Indonesia.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_bibit():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_bibit, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Kebun Bibit", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Raya Wonorejo, Rungkut,\nSurabaya, East Java 60296",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Hutan kota dengan area piknik tepi\nsungai & taman bermain anak,\nserta bumi perkemahan & rusa.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_mangrove():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_bibit, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Hutan Mangrove", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,3/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Wonorejo Timur No.1, Wonorejo,\nKec. Rungkut, Surabaya, Jawa Timur 60296",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Hutan Wisata Mangrove Surabaya merupakan wisata\nyang menggabungkan wisata rekreasi dan edukasi.\nDi area dengan luas kurang lebih 200 hektar\nini tumbuh berbagai tanaman bakau. Pemerintah\nkota Surabaya tentu mengelola tempat\nwisata ini dengan baik. Sehingga wisata ini\ndiminati pengunjung karena rapi dan bersih.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_sampoerna():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_sampoerna, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Museum House Of Sampoerna", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Rajawali No.82-I, RT.007/RW.15,\nKrembangan Sel., Kec. Krembangan,\nKota SBY, Jawa Timur 60175",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="House of Sampoerna adalah sebuah\nmuseum tembakau dan markas besar\nSampoerna yang terletak di Surabaya. Gaya arsitektur\ndari bangunan utamanya yang dipengaruhi oleh gaya\nkolonial Belanda dibangun pada 1862 dan sekarang\nmenjadi situs sejarah.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_prestasi():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_prestasi, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Taman Prestasi", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4.6/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Ketabang Kali No.6, Ketabang, Kec.\nGenteng, Surabaya, Jawa Timur 60272",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Taman tepi sungai dengan fasilitas\ntempat bermain, lapangan tenis, area\npiknik dan kebun bersuasana tropis.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_klenteng():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_klenteng, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Klenteng Sanggar Agung", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4.5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Sukolilo No.100, Sukolilo Baru,\nKec. Bulak, Surabaya, Jawa Timur 60122",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Kelenteng Sanggar Agung atau Klenteng Hong\nSan Tang adalah sebuah klenteng di Kota Surabaya.\nAlamatnya berada di Jalan Sukolilo Nomor 100,\nPantai Ria Kenjeran, Surabaya. Kuil ini,\nselain menjadi tempat ibadah bagi pemeluk Tridharma,\njuga menjadi tempat tujuan wisata bagi para wisatawan. ",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_kyakya():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_kyakya, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Kya Kya", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4.4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Kembang Jepun St, Bongkaran, \nPabean Cantikan, Surabaya, East Java 60161",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="adalah tempat yang dulunya ramai\nsebagai pasar malam di kawasan pecinan\nkota Surabaya. Di sepanjang jalan Kembang Jepun\ndidirikan kios-kios yang menjual berbagai\nmacam makanan baik masakan Tionghoa,\nmakanan khas Surabaya maupun makanan lainnya.\nKata kya-kya diambil dari salah satu dialek\nbahasa Tionghoa yang berarti jalan-jalan.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)


#MALANG
img_mnp= PhotoImage(file="malang night paradise.png")
img_kww = PhotoImage(file="kampung warna warni.png")
img_hawai = PhotoImage(file="hawai wat.png")
img_delaponte = PhotoImage(file="de laponte.png")
img_alunalunmalang = PhotoImage(file="alun alun malang.png")
img_sempu = PhotoImage(file='sempu.png')
img_tridi = PhotoImage(file='tridi.png')
img_wendit = PhotoImage(file='wendit.png')
img_pelangi = PhotoImage(file='pelangi.png')
img_balekambang = PhotoImage(file='balekambang.png')
img_parangdowo = PhotoImage(file='parangdowo.png')
img_rondo = PhotoImage(file='rondo.png')
img_bunteh = PhotoImage(file='bunteh.png')
img_ngantep = PhotoImage(file='ngantep.png')
img_sumbersirah = PhotoImage(file='sumbersirah.png')

def detailwisata_mnp():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_mnp, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Malang Night Paradise", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Graha Kencana Raya Jl. Raya Karanglo No.66, \nKaranglo, Balearjosari, Kec. Blimbing, Kota Malang, \nJawa Timur 65126",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Taman hiburan malam hari dengan instalasi \nlampu warna-warni, replika dinosaurus & naik perahu.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_kww():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_kww, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Kampung Warna Warni", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Zaenal Zakse Jl. Ir. H. Juanda 6, Jodipan, \nKec. Blimbing, Kota Malang, Jawa Timur",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

def detailwisata_hawai():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_hawai, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Hawai Waterpark", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Graha Kencana Utara V, Karanglo, \nBanjararum, Kec. Singosari, Kabupaten Malang, Jawa Timur 65153",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Taman rekreasi air dengan seluncuran warna-warni, \nkolam ombak & area panjat tebing anak, serta food court.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_delaponte():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_delaponte, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Florawisata Santerra De Laponte", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,6/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jalan Raya Madya, Jurangrejo, Pandesari, \nKec. Pujon, Kabupaten Malang, Jawa Timur 65391",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Tujuan foto populer dengan taman bunga penuh warna, \narea bertema budaya, dan wahana anak-anak.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_alunmalang():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_alunalunmalang, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Alun Alun Malang", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Merdeka Selatan, Kiduldalem, \nKec. Klojen, Kota Malang, Jawa Timur 65119",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Alun-alun populer di pusat kota yang \nmemiliki pohon rindang, jalan setapak, & air \nmancur di tengahnya.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)
                
def detailwisata_sempu():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_sempu, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Pantai Sempu", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text=" Kabupaten Malang, Jawa Timur, Indonesia",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Pulau Sempu adalah sebuah pulau kecil\nyang terletak di sebelah selatan Pulau\nJawa; secara administratif berada di\nDesa Tambakrejo, Kecamatan Sumbermanjing\nWetan, Kabupaten Malang, Jawa Timur.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)
        
def detailwisata_tridi():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_tridi, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Kampung Tridi", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Temenggungan Ledok, Kesatrian,\nKec. Blimbing, Kota Malang, Jawa Timur 65121",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Desa bernuansa ceria plus spot\nuntuk berfoto ini memiliki\nrumah penuh warna berdekorasi\ntrendi & seni publik.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_wendit():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_wendit, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Taman Wisata Wendit", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,1/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Raya Wendit Tim., Lowoksoro,\nMangliawan, Kec. Pakis, Kabupaten\nMalang, Jawa Timur 65154",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Taman rekreasi Wendit menyediakan\nkolam renang (alami serta buatan)\nyang luas, baik untuk dewasa\nmaupun anak-anak",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_pelangi():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_pelangi, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Coban Pelangi", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Dusun Ngadas, Kec. Poncokusumo,\nKabupaten Malang, Jawa Timur 65157",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Tersirat pelangi pada namanya\nkarena di air terjun ini sering\nmuncul penampakan Pelangi. Air\nterjunnya memiliki ketinggian\nhingga 110 meter. Lokasi wisata\nini dikelilingi oleh Taman Nasional\nBromo Tengger Semeru dengan suhu\nudara mencapai 19 hingga 23 derajat Celsius.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_balekambang():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_balekambang, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Coban Pelangi", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jalan Balekambang, Dusun Sumber Jambe,\nDesa Srigonco, Kecamatan Bantur, Malang, Jawa Timur",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Pantai Balekambang selain sebagai\nwisata alam, juga bisa disebut\nsebagai tempat wisata religi. Karena\npada hari-hari tertentu, ribuan pengunjung\ndatang ke pantai ini untuk melakukan ritual.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_parangdowo():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_parangdowo, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Pantai Parang Dowo", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Desa Gajahrejo, Kecamatan Gedangan,\nKabupaten Malang, Jawa Timur",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Disebut Parang Dowo karena terdapat\nsebuah pengangkatan karang dengan tinggi\nsekitar 2 meter dan panjang sekitar\n1 km yang membatasi bibir pantai dengan\nlautan lepas. Karang tersebut layaknya\ntanggul yang menghadang setiap ombak yang datang.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_rondo():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_rondo, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Coban Rondo", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Coban Rondo, Krajan, Pandesari,\nKec. Pujon, Kabupaten Malang, Jawa Timur 65391",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Air terjun ini mudah dijangkau oleh\nkendaraan umum. Akses yang paling mudah\ndengan melalui jalan raya dari Malang\nke Batu, dari sebelah timur atau\ndari Kediri ke Pare menuju\nMalang dari arah barat.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_bunteh():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_bunteh, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Kebun Teh Wonosari", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Bodean Putuk, Toyomarto, Kec. Singosari,\nKabupaten Malang, Jawa Timur 65153",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Kebun teh dataran tinggi dengan pemandian\nair panas plus jalur untuk mendaki & bersepeda.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_ngantep():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_ngantep, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Pantai Ngantep", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,6/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Area Gn., Sidurejo, Gedangan,\nKabupaten Malang, Jawa Timur 65178",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Pantai ini baru setahun dikenalkan kepada\nmasyarakat luas. Itu pun baru sebatas\npromosi lisan dari mulut ke mulut. Meski\nbegitu, sejumlah wisatawan asing sudah kerap datang\nke Pantai Nganteb untuk berselancar. Di wilayah\npantai Malang Selatan, barangkali hanya Pantai\nNganteb inilah tempat paling sesuai berselancar.\nOmbak di pantai ini tidak begitu besar,\ntapi merata.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_sumbersirah():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_sumbersirah, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Pantai Ngantep", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jalan Sunan Kalijaga I RT.05/RW.02,\nPutuk Utara, Putukrejo, Kec. Gondanglegi,\nKabupaten Malang, Jawa Timur 65174",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Destinasi bernuansa tenang dengan\nkolam renang alami yang jernih dan\ntumbuhan rimbun di dekat sawah.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)


#Madiun
img_airterjunseweru= PhotoImage(file="airterjunseweru.png")
img_monumenkresek= PhotoImage(file="Monumenkresek.png")
img_gunungkendil = PhotoImage(file="gunungkendil.png")
img_hpni = PhotoImage(file="HutanPinusNongkoIjoKare.png")
img_atk = PhotoImage(file="airterjunkertoembo.png")
img_tkc = PhotoImage(file="tamankotacaruban.png")
img_wbsa = PhotoImage(file="wahanabermainsekararum.png")
img_dw = PhotoImage(file="dumilahwaterpark.png")
img_atbd = PhotoImage(file="AirTerjunBanyulaweDong.png")
img_Atk = PhotoImage(file="AirTerjunKucur.png")

def detailwisata_airterjunseweru():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_airterjunseweru, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Air Terjun Seweru", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Air Terjun Seweru Desa Kare, Kecamatan\nKare Kabupaten Madiun, Jawa Timur 63182",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Dikenal dengan Serondo atau Selampir,\nyang dipadukan dengan pemandangan hutan\nyang memperkaya keindahan alam.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_monumenkresek():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_monumenkresek, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Monumen Kresek", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="3,8/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Raya Monumen Kresek, Kecamatan Wungu,\nKabupaten Madiun, Jawa Timur 63182",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Wisata edukasi sejarah mengenai perjuangan\nbangsa di tengah keindahan alam pegunungan.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_gunungkendil():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_gunungkendil, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Gunung Kendil", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,2/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Desa Pilangrejo, Kecamatan Wungu,\nKabupaten Madiun, Jawa Timur 63182",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Wisata ini memiliki area tebing,\nterdapat lokasi off-road, memiliki tiga tipe\nkolam renang, memiliki area pendopo.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_hpni():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_hpni, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Hutan Pinus Nongko Ijo", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,2/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Desa Kare, Kecamatan Kare,\nKabupaten Madiun, Jawa Timur 63182",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Berlokasi di atas lembah sehingga\nmemiliki suasana sejuk dan dapat\nmenjadi lokasi piknik yang asyik.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_atk():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_atk, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Air Terjun Kertoembo", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Kampung Kertoembo, Sumberagung, Kecamatan Kare,\nKabupaten Madiun, Jawa Timur 63182",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Air terjun yang memiliki suasana air\nterjun yang asri, sepi, dan tenang.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_tkc():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_tkc, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Taman Kota Caruban", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,3/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Anggur, Lingkungan Dua, Purwosari,\nWonosari, Kabupaten Madiun, Jawa Timur 63182",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Taman ini memiliki banyak fasilitas\ndan wahana bermain menarik yang sangat cocok\nsebagai tempat rekreasi bersama keluarga.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_wbsa():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_wbsa, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Wahana Bermain Sekar Arum", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="3,9/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Desa Kare, Kabupaten Madiun,\nJawa Timur 63182",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Tempat rekreasi edukatif yang memiliki\narum jeram, luncur gantung hingga\npermainan yang berbasis alam.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_dw():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_dw, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Dumilah Waterpark", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,1/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Kecamatan Madiun, Jawa Timur 63182",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Terdapat tempat bermain seperti flying\nfox dan mini game. Selain itu terdapat food\ncourt yang menyediakan kuliner khas Madiun.\nTerdapat juga Garden Zone yang menjadi tempat\ntumbuhan langka terawat dengan baik.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_atbd():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_atbd, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Air Terjun Banyulawe Dong", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,7/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Desa Kepel, Kecamatan Kare,\nMadiun, Jawa Timur 63182",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Memiliki nama yang unik menjadi daya tarik\nyang mampu menarik wisatawan untuk berkunjung.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 18))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_Atk():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_atbd, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Air Terjun Kucur", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,7/5", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Desa Kepel, Kecamatan Kare,\nMadiun, Jawa Timur 63182",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Memiliki nama yang unik menjadi daya tarik\nyang mampu menarik wisatawan untuk berkunjung.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 20))
        sejarah_wisata.place(x=736.0, y=451.0)


#Kediri
img_gandrung= PhotoImage(file="gandrung.png")
img_syu= PhotoImage(file="syu.png")
img_airlangga = PhotoImage(file="airlangga.png")
img_ecopark = PhotoImage(file="ecopark.png")
img_fotografi = PhotoImage(file="fotografi.png")
img_tirtoyoso = PhotoImage(file="tirtoyoso.png")
img_surowono = PhotoImage(file="surowono.png")
img_ongakan = PhotoImage(file="ongakan.png")
img_kelud = PhotoImage(file="kelud.png")
img_gumul = PhotoImage(file="gumul.png")

def detailwisata_gandrung():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_gandrung, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Bukit Gandrung", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,3/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Medowo, Kec. Kandangan,\nKabupaten Kediri, Jawa Timur 64294",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Tempat wisata Bukit Gandrung Tanggulasi\nini sebenarnya mirip dengan Bukit Panguk Kediwung\nJogja yang menawarkan keindahan alam dari ketinggian.\nNamun tempat ini memiliki view Gunung Welirang\ntepat di depan mata.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_syu():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_syu, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Monumen Syu", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. KH Wachid Hasyim, Mojoroto, Kec. Mojoroto,\nKota Kediri, Jawa Timur 64114",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text=" Monumen ini adalah patung seorang pria dengan\nseragam tentara Jepang khas yang mewakili tentara\nPETA. Patung emas raksasa itu akan menyapa\nsetiap pengunjung yang melewati bundaran kecil\nyang menghubungkan Jaksa Agung Suprapto\ndan jalan KH Wakhid Hasyim.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_airlangga():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_airlangga, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Museum Airlangga", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Lingkar Maskumambang, Pojok, Kec.\nMojoroto, Kota Kediri, Jawa Timur 64115",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Status museum ini ialah museum daerah.\nFungsi khususnya adalah mengoleksi benda cagar\nbudaya yang berasal dari alun-alun Kota Kediri.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_kep():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_ecopark, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Kediri Eco Park", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Ahmad Yani No.123, Sukorejo,\nKec. Ngasem, Kabupaten Kediri, Jawa Timur 64129",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Kediri Eco Park merupakan wahana wisata\nalam dengan konsep edukasi. Pengunjung bisa\nberwisata sambil belajar, membuat kompos, budidaya jamur.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_fotografi():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_fotografi, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Museum Fotografi", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Kapten Tendean No.60/160, Ngronggo,\nKec. Kota, Kota Kediri, Jawa Timur 64127",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Museum Fotografi Kediri merupakan sebuah\nmuseum foto yang menyimpan sejarah kota\nKediri yang diabadikan dalam bentuk seni fotografi.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_tirtoyoso():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_tirtoyoso, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Taman Tirtoyoso", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,3/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jalan Jenderal Ahmad Yani No.123, Banjaran,\nKec. Kota, Kabupaten Kediri, Jawa Timur 64129",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Taman rekreasi besar yang cocok untuk\nkeluarga, dengan area bermain anak, kolam renang\ndan wahana kecil.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_surowono():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_surowono, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Candi Surowono", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,3/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Surowono, Canggu, Kec. Badas,\nKabupaten Kediri, Jawa Timur 64217",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Candi Surowono menyimpan sejarah Raja Wengker.\nDia merupakan salah satu raja bawahan selama pemerintahan\nRaja Hayam Wuruk dari kerajaan Majapahit. Bentuk\nbangunan candi berupa bujursangkar berukuran 8 x 8 meter\ndiperkirakan dibuat pada abad 15, sekitar tahun 1400 masehi.\nCandi yang dibangun dengan latar belakang agama Hindu",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_ongakan():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_ongakan, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Bukit Ongakan", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Hutan, Besowo, Kec. Kepung,\nKabupaten Kediri, Jawa Timur 64293",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Bukit Ongakan ini berada di lereng\nGunung Kelud bagian timur laut. Jadi,\nAnda harus mau berjalan kaki melewati\nhutan pinus jika datang ke sini.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_kelud():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_kelud, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Gunung Kelud", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Kediri, Jawa Timur",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Gunung Kelud adalah sebuah gunung berapi\ndi Jawa Timur yang hingga sekarang tergolong aktif. ",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_gumul():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_gumul, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Simpang Lima Gumul", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,6/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Tugurejo, Kec. Ngasem,\nKabupaten Kediri, Jawa Timur 64182",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="ikon Kabupaten Kediri yang bentuknya menyerupai\nArc de Triomphe yang berada di Paris, Prancis.\nSLG mulai dibangun pada tahun 2003 dan\ndiresmikan pada tahun 2008, yang digagas\noleh Bupati Kediri saat itu, Sutrisno.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

#Probolinggo
img_bjbr= PhotoImage(file="bjbr.png")
img_argopuro= PhotoImage(file="argopuro.png")
img_bentar = PhotoImage(file="bentar.png")
img_ketapang = PhotoImage(file="ketapang.png")
img_madakaripura = PhotoImage(file="madakaripura.png")
img_umbulan = PhotoImage(file="umbulan.png")
img_agung = PhotoImage(file="agung.png")
img_muspro = PhotoImage(file="muspro.png")
img_jabung = PhotoImage(file="jabung.png")
img_duta = PhotoImage(file="duta.png")


def detailwisata_bjbr():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_bjbr, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Bee Jay Bakau Resort", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,3/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Pelabuhan PPP Mayangan, Wisata Primadona, Mangunharjo, ",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="BJBR merupakan sebuah ekowisata bakau dengan\nluas 5 hektar yang terletak di Pelabuhan Perikanan Pantai Mayangan.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_argopuro():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_argopuro, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Gunung Argopuro", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Probolinggo, Jawa Timur",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Gunung Argapura mempunyai ketinggian setinggi 3.088 meter.\nGunung Argapura merupakan bekas gunung berapi yang kini\nsudah tidak aktif lagi. Puncak Gunung Argapura\nadalah titik tertinggi di Pegunungan Iyang.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_bentar():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_bentar, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Pantai Bentar", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,0/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jalur Pantura Mayangan, Karang Anyar, Curahsawo, Kec. Gending,\nKabupaten Probolinggo, Jawa Timur 67211",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Pantai populer berlatar belakang hutan bakau terkenal\ndengan dermaga kayu panjang & hiu paus yang bermigrasi",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_ketapang():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_ketapang, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Gili Ketapang", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Selat Madura, 8 km lepas pantai utara Probolinggo.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Gili Ketapang adalah daerah yang menjadi satu dengan\ndaratan Probolinggo, yakni dengan desa Ketapang dan\nhanya terpisahkan oleh sungai. Namun dikarenakan gempa\nakibat meletusnya Gunung Semeru, menyebabkan daratan tersebut\nterpisah hingga sejauh 5 mil dan menuju tengah lautan.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_madakaripura():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_madakaripura, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Air Terjun Madakaripura", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Branggah, Sapih, Kec. Lumbang, Kabupaten Probolinggo, Jawa Timur 67183",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Air terjun Madakaripura adalah sebuah air terjun yang\nterletak di Kabupaten Probolinggo, Provinsi Jawa Timur.\nAir terjun setinggi 200 meter ini merupakan air terjun\ntertinggi di Pulau Jawa dan tertinggi kedua di Indonesia.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_umbulan():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_umbulan, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Air Terjun Umbulan", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Watulumpang, Sukapura, Kec. Sukapura,\nKabupaten Probolinggo, Jawa Timur 67254",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Air Terjun Umbalan karena masih jarang didatangi oleh wisatawan,\nkondisi lingkungannya masih sangat asri dan alami.\nDi sana anda bisa melihat pemandangan indah",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_agung():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_agung, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Danau Ranu Agung", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,5/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Krajan, Ranuagung, Kec. Tiris, Kabupaten Probolinggo, Jawa Timur 67287",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Sebagai pengetahuan bahwa sebenarnya danau ranu agung\nmerupakan sebuah danau vulkanik yang terbentuk dari\nGunung Lamongan atau Lemongan yang masih aktif.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_muspro():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_muspro, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Museum Probolinggo", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,4/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Jl. Suroyo No.25, Tisnonegaran, Kec.\nKanigaran, Kota Probolinggo, Jawa Timur 67211",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Museum Probolinggo adalah sebuah museum di Kota Probolinggo,\nprovinsi Jawa Timur, Indonesia. Gedung Panti Budaya sebagai\ngedung yang dewasa ini dijadikan sebagai Museum Probolinggo\ntelah menjadi ikon pariwisata di Kota Probolinggo.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_jabung():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_jabung, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Candi Jabung", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,6/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text=" Dusun Candi, Jabung Candi, Kec. Paiton,\nKabupaten Probolinggo, Jawa Timur 67291",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Candi jabung adalah salah satu candi hindu peninggalan kerajaan Majapahit.\nCandi hindu ini terletak di Desa Jabung, Kecamatan Paiton, Kabupaten\nProbolinggo, Jawa Timur. Struktur bangunan candi yang\nhanya dari bata merah ini mampu bertahan ratusan tahun",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)

def detailwisata_duta():
        global frame9
        for widget in frame8.winfo_children():
            widget.destroy()
        frame9 = Frame(window, bg="#FA9269", height=867, width=1476, bd=0, highlightthickness=0, relief="ridge")
        frame9.place(x=0, y=0)

        backbtn = Button(frame9, image=img_backbtndetailwisata, borderwidth=0, highlightthickness=0, command=laman_jelajahi, relief="flat")
        backbtn.place(x=28.0, y=20.0, width=83.0, height=67.0)

        logoteks_detailwisata = Label(frame9, image=img_logoteks_toggle, bd=0 )
        logoteks_detailwisata.place(x=530,y=16)

        fotowisata = Label(frame9, image=img_duta, bg="#FA9269")
        fotowisata.place(x=176.0, y=127.0)

        templtdetailwisata = Label(frame9, image=templatedetailwisata, bg="#FA9269")
        templtdetailwisata.place(x=721.0, y=127.0)

        Nama_wisata = Label(frame9, anchor="nw", bg="black", text="Pantai Duta", fg="#FFFFFF", font=("MontserratRoman Bold", 32))
        Nama_wisata.place(x=738.0, y=161.0)

        rating_wisata = Label(frame9, anchor="nw", bg="black", text="4,2/5", fg="#FFFFFF", font=("MontserratRoman Bold", 26))
        rating_wisata.place(x=951.0, y=380.0)

        alamat_wisata = Label(frame9, anchor="nw", bg="black", text="Dusun Gilin, Randutatah, Kec. Paiton,\nKabupaten Probolinggo, Jawa Timur 67291",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        alamat_wisata.place(x=738.0, y=276.0)

        sejarah_wisata = Label(frame9, anchor="nw", bg="black", text="Diambil dari nama desa yaitu Randutatah, pantai tersebut\ndiberi nama Duta. Adapun keistimewaan dari pantai\nini adalah pemandangan sunset yang begitu indah dan jelas\nditempat paling timur dari kabupaten Probolinggo.",justify="left", fg="#FFFFFF", font=("MontserratRoman Bold", 16))
        sejarah_wisata.place(x=736.0, y=451.0)



window.mainloop()
##########################

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Fungsi untuk membagi dataset menjadi subset acak
def bootstrap_sample(X, y):
    indices = np.random.choice(len(X), len(X), replace=True)
    return X[indices], y[indices]

# Fungsi untuk menghitung Gini Impurity
def calculate_gini(y):
    unique_classes, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)
    gini = 1 - np.sum(probabilities**2)
    return gini

# Fungsi untuk membagi dataset berdasarkan suatu kondisi
def split_dataset(X, y, feature_index, threshold):
    mask = X[:, feature_index] <= threshold
    X_left, y_left = X[mask], y[mask]
    X_right, y_right = X[~mask], y[~mask]
    return X_left, y_left, X_right, y_right

# Fungsi untuk membangun pohon keputusan
def build_decision_tree(X, y, max_depth=None):
    if max_depth == 0 or len(np.unique(y)) == 1:
        # Mencapai batas kedalaman atau semua sampel memiliki label yang sama
        return np.unique(y)[0]

    num_features = X.shape[1]
    best_gini = float('inf')
    best_feature_index = None
    best_threshold = None

    for feature_index in range(num_features):
        thresholds = np.unique(X[:, feature_index])
        for threshold in thresholds:
            X_left, y_left, X_right, y_right = split_dataset(X, y, feature_index, threshold)
            gini_left = calculate_gini(y_left)
            gini_right = calculate_gini(y_right)
            weighted_gini = (len(y_left) * gini_left + len(y_right) * gini_right) / len(y)

            if weighted_gini < best_gini:
                best_gini = weighted_gini
                best_feature_index = feature_index
                best_threshold = threshold

    if best_gini == float('inf'):
        # Tidak ada pemisahan yang dapat dilakukan
        return np.unique(y)[0]

    # Rekursif membangun subtree
    left_subtree = build_decision_tree(X_left, y_left, max_depth - 1 if max_depth is not None else None)
    right_subtree = build_decision_tree(X_right, y_right, max_depth - 1 if max_depth is not None else None)

    return (best_feature_index, best_threshold, left_subtree, right_subtree)

# Fungsi untuk melakukan prediksi dengan menggunakan pohon keputusan
def predict_tree(tree, sample):
    if isinstance(tree, np.ndarray):
        # Ini adalah daun, mengembalikan label
        return tree
    feature_index, threshold, left_subtree, right_subtree = tree
    if sample[feature_index] <= threshold:
        return predict_tree(left_subtree, sample)
    else:
        return predict_tree(right_subtree, sample)

# Fungsi untuk melakukan prediksi menggunakan Random Forest
def predict_random_forest(forest, X):
    predictions = np.zeros(len(X))
    for tree in forest:
        tree_predictions = np.array([predict_tree(tree, sample) for sample in X])
        predict
