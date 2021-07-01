from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
import pymysql


class login:
    def __init__(self, root):
        self.root = root
        self.root.title = ("LOGIN DAN REGISTER SISTEM UNTUK APLIKASI")
        self.root.geometry("1366x700+0+0")
        self.loginform()

    def loginform(self):
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x="0", y="0", height=700, width=1366)

        self.img = ImageTk.PhotoImage(file="gambar2.JPG")
        img = Label(Frame_login, image=self.img).place(
            x=0, y=0, height=700, width=1366)

        frame_input_login = Frame(self.root, bg='white')
        frame_input_login.place(x=320, y=130, height=450, width=350)

        label1 = Label(frame_input_login, text="Login Disini", font=(
            'impact', 32, 'bold'), fg="black", bg="white")
        label1.place(x=75, y=20)

        label2 = Label(frame_input_login, text="Username", font=(
            'Goudy old sytle', 20, 'bold'), fg="orangered", bg="white")
        label2.place(x=30, y=95)

        self.email_text = Entry(frame_input_login, font=(
            "times new roman", 15, 'bold'), bg='lightgray')
        self.email_text.place(x=30, y=145, height=35, width=270)

        label3 = Label(frame_input_login, text="Password", font=(
            'Goudy old sytle', 20, 'bold'), fg="orangered", bg="white")
        label3.place(x=30, y=195)

        self.password_text = Entry(frame_input_login, show='*', font=(
            "times new roman", 15, 'bold'), bg='lightgray')
        self.password_text.place(x=30, y=245, height=35, width=270)

        btn1 = Button(frame_input_login, text="Lupa Password?", command=self.forget_pass,
                      cursor='hand2', font=('calibri', 10), bg='white', fg='black', bd=0)
        btn1.place(x=125, y=305)

        btn2 = Button(frame_input_login, text="LOGIN", command=self.login, cursor='hand2', font=(
            'times new roman', 15), bg='orangered', fg='white', bd=0, height=1, width=15)
        btn2.place(x=90, y=340)

        btn3 = Button(frame_input_login, text="Belum Registrasi? Register dulu..",
                      command=self.register, cursor='hand2', font=('calibri', 10), bg='white', fg='black', bd=0)
        btn3.place(x=100, y=390)

    def forget_pass(self):
        print('forget password')

    def login(self):
        if self.email_text.get() == "" or self.password_text.get() == "":
            messagebox.showerror(
                "Error", "Username Dan Password Masih Kosong", parent=self.root)
        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="", database="aplikasimanagementsiswa")
                cur = con.cursor()
                cur.execute("SELECT * FROM register WHERE username =%s and password=%s",
                            (self.email_text.get(), self.password_text.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Username Atau Password Salah")
                    self.loginclear()
                    self.email_text.focus()

                else:
                    self.tambahData()
                    con.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due To : {str(es)}", parent=self.root)

    def loginclear(self):
        self.email_text.delete(0, END)
        self.password_text.delete(0, END)

    def tambahData(self):
        print("ini from Tambah Data")

    def register(self):
        Frame_Register = Frame(self.root, bg="#c5ded0")
        Frame_Register.place(x=0, y=0, height=700, width=1366)

        self.img = ImageTk.PhotoImage(file="gambar.JPG")
        img = Label(Frame_Register, image=self.img).place(
            x=0, y=0, width=1366, height=700)

        frame_input_register = Frame(self.root, bg="white")
        frame_input_register.place(x=320, y=130, width=630, height=450)

        label1 = Label(frame_input_register, text="Form Register", font=(
            "Goudy Old Style", 20, "bold"), fg="orangered", bg="white")
        label1.place(x=45, y=20)

        label2 = Label(frame_input_register, text="UserName", font=(
            "Goudy Old Style", 20, "bold"), fg="orangered", bg="white")
        label2.place(x=30, y=95)

        self.username_text = Entry(frame_input_register, font=(
            "times new roman", 15, "bold"), bg="lightgray")
        self.username_text.place(x=30, y=145, height=35, width=270)

        label3 = Label(frame_input_register, text="Password", font=(
            "Goudy Old Style", 20, "bold"), fg="orangered", bg="white")
        label3.place(x=30, y=195)

        self.password_regis_text = Entry(frame_input_register, font=(
            "times new roman", 15, "bold"), bg="lightgray")
        self.password_regis_text.place(x=30, y=245, height=35, width=270)

        label4 = Label(frame_input_register, text="Email", font=(
            "Goudy Old Style", 20, "bold"), fg="orangered", bg="white")
        label4.place(x=330, y=95)

        self.email_regis_text = Entry(frame_input_register, font=(
            "times new roman", 15, "bold"), bg="lightgray")
        self.email_regis_text.place(x=330, y=145, height=35, width=270)

        label5 = Label(frame_input_register, text="Konfirmasi Password", font=(
            "Goudy Old Style", 20, "bold"), fg="orangered", bg="white")
        label5.place(x=330, y=195)

        self.konfirmasi_regis_text = Entry(frame_input_register, font=(
            "times new roman", 15, "bold"), bg="lightgray")
        self.konfirmasi_regis_text.place(x=330, y=245, height=35, width=270)

        btn1 = Button(frame_input_register, text="REGISTER", command=self.regis,
                      cursor='hand2', font=('times new roman', 15), bg='orangered', fg='white', bd=0, width=15, height=1)
        btn1.place(x=90, y=340)

        btn2 = Button(frame_input_register, text="Sudah Registrasi? Kembali Ke Login...", command=self.loginform, cursor='hand2', font=(
            'calibri', 10), bg='white', fg='black', bd=0)
        btn2.place(x=110, y=390)

    def regis(self):
        if self.username_text.get() == "" or self.email_regis_text.get() == "" or self.password_regis_text.get() == "" or self.konfirmasi_regis_text.get() == "":
            messagebox.showerror(
                "Error", "Semua Entry Field Harus Di Isi", parent=self.root)
        elif self.password_regis_text.get() != self.konfirmasi_regis_text.get():
            messagebox.showerror(
                "Error", "Password Dan Konfirmasi Password Tidak Sama")
        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="", database="aplikasimanagementsiswa")
                cur = con.cursor()
                cur.execute("SELECT * FROM register WHERE username=%s",
                            self.username_text.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "Username Sudah Ada, Silahkan Buat Username Baru", parent=self.root)
                    self.username_text.focus()
                else:
                    cur.execute(
                        "INSERT INTO register(username,emailid,password,konfirmasiPassword) values('%s','%s','%s','%s')" % (self.username_text.get(), self.email_regis_text.get(), self.password_regis_text.get(), self.konfirmasi_regis_text.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registrasi Berhasil")
                    self.regclear()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due To:{str(es)}")

    def regclear(self):
        self.username_text.delete(0, END)
        self.email_regis_text.delete(0, END)
        self.password_regis_text.delete(0, END)
        self.konfirmasi_regis_text.delete(0, END)


root = Tk()
Aplikasi = login(root)
root.mainloop()
