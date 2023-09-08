import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("HAIII")

NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    pesan=("Hello {NAMA_DEPAN.get()}  {NAMA_BELAKANG.get()}")
    showinfo(title="haiii",message=pesan)

input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

NAMA_DEPAN_label = ttk.Label(input_frame, text="Nama Depan:")
NAMA_DEPAN_label.pack(padx=10, pady=10, fill="x", expand=True)

NAMA_DEPAN_entry = ttk.Entry(input_frame, textvariable="NAMA_DEPAN")
NAMA_DEPAN_entry.pack(padx=10, pady=10, fill="x", expand=True)

NAMA_BELAKANG_label = ttk.Label(input_frame, text="Nama Belakang:")
NAMA_BELAKANG_label.pack(padx=10, pady=10, fill="x", expand=True)

NAMA_BELAKANG_entry = ttk.Entry(input_frame, textvariable="NAMA_BELAKANG")
NAMA_BELAKANG_entry.pack(padx=10, pady=10, fill="x", expand=True)

tombol = ttk.Button(input_frame, text="Sapa!", command=tombol_click)
tombol.pack(fil="x", expand=True, padx=10, pady=10)

window.mainloop()