import tkinter as tk 
import hashlib
from utils import admin_password_hash
from backend import add_employee, list_employees

# ---------------- Main Window ---------------- #
root = tk.Tk()
root.title('Employee Database')
root.geometry('500x300')
root.configure(bg='#f5f5f5')    

# ---------------- Login Hashing ---------------- #
def verify_login():
    username = username_entry.get()
    password = password_entry.get()
    
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    if username == 'admin' and password_hash == admin_password_hash:
        login_frame.pack_forget()
        employee_frame.pack(fill='both', expand=True)
    else:
        login_status_label.config(text='Invalid username or password', fg='red')

# ---------------- Frames ---------------- #
login_frame = tk.Frame(root, bg='#f5f5f5')
employee_frame = tk.Frame(root, bg='#f5f5f5')

login_frame.pack(fill='both', expand=True)

# ---------------- Login Frame ---------------- #
tk.Label(login_frame, text='Login', font=('Arial', 16), bg='#f5f5f5').pack(pady=10)

tk.Label(login_frame, text='Username:', bg='#f5f5f5').pack(pady=5)
username_entry = tk.Entry(login_frame)
username_entry.pack(pady=5)

tk.Label(login_frame, text='Password:', bg='#f5f5f5').pack(pady=5)
password_entry = tk.Entry(login_frame, show='*')
password_entry.pack(pady=5)
password_entry.bind('<Return>', lambda event: verify_login())

login_status_label = tk.Label(login_frame, text='', bg='#f5f5f5')
login_status_label.pack(pady=10)


login_button = tk.Button(login_frame, text='Login')
login_button.pack(pady=10)
login_button.config(command=verify_login)

# ---------------- Employee Frame ---------------- #
tk.Label(employee_frame, text='Employee Management Panel', font=('Arial', 16), bg='#f5f5f5').pack(pady=10)
tk.Label(employee_frame, text='WIP', bg='#f5f5f5').pack(pady=10)





        
    









root.mainloop()