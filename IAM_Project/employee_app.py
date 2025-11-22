import tkinter as tk 


# ---------------- Main Window ---------------- #
root = tk.Tk()
root.title('Employee Database')
root.geometry('500x300')
root.configure(bg='#f5f5f5')    

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

login_button = tk.Button(login_frame, text='Login')
login_button.pack(pady=10)

# ---------------- Employee Frame ---------------- #
tk.Label(employee_frame, text='Employee Management Panel', font=('Arial', 16), bg='#f5f5f5').pack(pady=10)
tk.Label(employee_frame, text='WIP', bg='#f5f5f5').pack(pady=10)

# ---------------- Switch to Employee Frame ---------------- #
def show_employee_frame():
    login_frame.pack_forget()
    employee_frame.pack(fill='both', expand=True)

login_button.config(command=show_employee_frame)

# ---------------- Login Hashing ---------------- #










root.mainloop()