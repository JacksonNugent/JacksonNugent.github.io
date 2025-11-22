import hashlib
import tkinter as tk
from tkinter import filedialog
import os

# -------------------- Window Setup --------------------
root = tk.Tk()
root.title('Hash File Checker')
root.geometry("700x400")
root.configure(bg="#f5f5f5")

# -------------------- Variables --------------------
file1_path = ''
file2_path = ''

# -------------------- Functions --------------------
def select_file1():
    global file1_path
    file1_path = filedialog.askopenfilename()
    file1_label.config(text=file1_path)
    check_compare_ready()

def select_file2():
    global file2_path
    file2_path = filedialog.askopenfilename()
    file2_label.config(text=file2_path)
    check_compare_ready()

def hash_file(path):
    sha = hashlib.sha256()
    total_size = os.path.getsize(path)
    read_size = 0

    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha.update(chunk)
            read_size += len(chunk)
            if progress_label:
                percent = (read_size / total_size) * 100
                progress_label.config(text=f"Hashing {os.path.basename(path)}: {percent:.1f}%")
                progress_label.update()  # forces UI to refresh

    if progress_label:
        progress_label.config(text=f"Finished hashing {os.path.basename(path)}")
    return sha.hexdigest()

def compare_files():
    file1_hash = hash_file(file1_path)
    file2_hash = hash_file(file2_path)
    if file1_hash == file2_hash:
        result_label.config(text='The files are the same. No alteration detected.', fg="green")
    else:
        result_label.config(text='The files are different. Alterations may have occurred.', fg="red")

def check_compare_ready():
    # Enable compare button only if both files are selected
    if file1_path and file2_path:
        btn_compare.config(state="normal")
    else:
        btn_compare.config(state="disabled")

# -------------------- File Selection Frame --------------------
file_frame = tk.Frame(root, bg="#f5f5f5")
file_frame.grid(row=0, column=0, padx=20, pady=20)

# File 1
btn1 = tk.Button(file_frame, text='Select File 1', width=15, command=select_file1)
btn1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
file1_label = tk.Label(file_frame, text='No file selected', bg="#f5f5f5", anchor="w")
file1_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# File 2
btn2 = tk.Button(file_frame, text='Select File 2', width=15, command=select_file2)
btn2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
file2_label = tk.Label(file_frame, text='No file selected', bg="#f5f5f5", anchor="w")
file2_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# -------------------- Compare Button --------------------
btn_compare = tk.Button(root, text='Compare Files', width=20, command=compare_files, state="disabled")
btn_compare.grid(row=1, column=0, pady=10)

# -------------------- Progress Label --------------------
progress_label = tk.Label(root, text='', font=('Arial', 10), bg="#f5f5f5")
progress_label.grid(row=3, column=0, pady=5)

# -------------------- Result Label --------------------
result_label = tk.Label(root, text='', font=("Arial", 10), bg="#f5f5f5")
result_label.grid(row=2, column=0, pady=5)

# -------------------- Run App --------------------
root.mainloop()
