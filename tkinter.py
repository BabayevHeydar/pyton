import tkinter as tk
import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(12))
    entry.delete(0, tk.END)
    entry.insert(0, password)

root = tk.Tk()
root.title("Random Güclü Şifrə Generatoru")
root.geometry("400x150")

entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=10)

button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12))
button.pack()

root.mainloop()
