import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk, Image
import os

root = tk.Tk()
root.title("Jenil's QR Studio")
root.geometry("400x550")
root.configure(bg='#1e1b4b')

def generate_qr():
    data = link_entry.get()
    if not data:
        messagebox.showwarning("Warning", "Pehle koi link ya text to dalo!")
        return
        
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        img_path = "my_qrcode.png"
        img.save(img_path)

        pil_img = Image.open(img_path)
        pil_img = pil_img.resize((200, 200))
        tk_img = ImageTk.PhotoImage(pil_img)
        
        qr_label.config(image=tk_img)
        qr_label.image = tk_img 
        
        messagebox.showinfo("Success", "QR Code ban gaya aur save ho gaya! 🎉")
        
    except Exception as e:
        messagebox.showerror("Error", f"Kuch gadbad hui: {e}")

tk.Label(root, text="✨ QR CODE GENERATOR ✨", font=("Arial", 16, "bold"), bg='#1e1b4b', fg='#f43f5e').pack(pady=25)
tk.Label(root, text="Enter Text or URL:", font=("Arial", 10), bg='#1e1b4b', fg='white').pack()

link_entry = tk.Entry(root, font=("Arial", 12), width=30, justify='center')
link_entry.pack(pady=10, ipady=4)

gen_btn = tk.Button(root, text="GENERATE QR CODE 🚀", font=("Arial", 11, "bold"), bg='#f43f5e', fg='white', bd=0, padx=10, pady=6, command=generate_qr)
gen_btn.pack(pady=15)

qr_label = tk.Label(root, bg='#1e1b4b')
qr_label.pack(pady=20)

root.mainloop()
