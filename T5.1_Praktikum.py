import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os

# Fungsi untuk load user dari file
def load_users():
    if not os.path.exists("users.txt"):
        return {}
    with open("users.txt", "r") as f:
        lines = f.readlines()
    return {line.strip().split(",")[0]: line.strip().split(",")[1] for line in lines}

# Fungsi untuk simpan user ke file
def save_user(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")

# Dictionary user (dimuat dari file)
users = load_users()

# Fungsi login
def login():
    username = user.get()
    pwd = password.get()

    if not username or not pwd:
        messagebox.showwarning("Peringatan", "Username dan password tidak boleh kosong.")
    elif username in users and users[username] == pwd:
        messagebox.showinfo("Berhasil", f"Login berhasil! Selamat datang, {username}.")
    else:
        messagebox.showerror("Gagal", "Username atau password salah.")

# Fungsi untuk membuka jendela register
def open_register_window():
    register_window = tk.Toplevel(window)
    register_window.title("Register")
    register_window.configure(bg="#f0f0ff")
    register_window.minsize(320, 200)

    frame = tk.Frame(register_window, bg="#f0f0ff")
    frame.pack(pady=10, padx=10)

    # Widget 1: Username
    tk.Label(frame, text="Username:", bg="#f0f0ff").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    new_user = tk.Entry(frame, width=25, bg="#e0f7fa")
    new_user.grid(row=0, column=1, pady=5)

    # Widget 2: Password
    tk.Label(frame, text="Password:", bg="#f0f0ff").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    new_password = tk.Entry(frame, width=25, show="*", bg="#ffe0b2")
    new_password.grid(row=1, column=1, pady=5)

    # Widget 3: Confirm Password
    tk.Label(frame, text="Confirm Password:", bg="#f0f0ff").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    confirm_password = tk.Entry(frame, width=25, show="*", bg="#ffe0b2")
    confirm_password.grid(row=2, column=1, pady=5)

    # Fungsi simpan user baru
    def register():
        uname = new_user.get()
        pwd = new_password.get()
        confirm = confirm_password.get()

        if not uname or not pwd or not confirm:
            messagebox.showwarning("Peringatan", "Semua field harus diisi.", parent=register_window)
        elif uname in users:
            messagebox.showerror("Gagal", "Username sudah terdaftar.", parent=register_window)
        elif pwd != confirm:
            messagebox.showerror("Gagal", "Password dan konfirmasi tidak cocok.", parent=register_window)
        else:
            users[uname] = pwd
            save_user(uname, pwd)
            messagebox.showinfo("Berhasil", "Registrasi berhasil!", parent=register_window)
            register_window.destroy()

    register_btn = tk.Button(frame, text="Register", command=register, bg="#4caf50", fg="white")
    register_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Window utama
window = tk.Tk()
window.title("Login App")
window.configure(bg="#e3f2fd")
window.minsize(320, 180)

frame = tk.Frame(window, bg="#e3f2fd")
frame.pack(pady=20, padx=20)

tk.Label(frame, text="Username:", bg="#e3f2fd").grid(row=0, column=0, padx=5, pady=5, sticky="e")
user = tk.Entry(frame, width=25, bg="#e0f7fa")
user.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Password:", bg="#e3f2fd").grid(row=1, column=0, padx=5, pady=5, sticky="e")
password = tk.Entry(frame, width=25, show="*", bg="#ffe0b2")
password.grid(row=1, column=1, pady=5)

login_button = tk.Button(frame, text="Login", command=login, bg="#2196f3", fg="white")
login_button.grid(row=2, column=0, pady=10)

register_button = tk.Button(frame, text="Register", command=open_register_window, bg="#ff9800", fg="white")
register_button.grid(row=2, column=1, pady=10)

window.mainloop()
