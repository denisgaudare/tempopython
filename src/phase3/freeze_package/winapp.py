import tkinter as tk
from tkinter import messagebox

def on_hello():
    messagebox.showinfo("Bonjour", "Salut à toi 👋")

def on_quit():
    root.destroy()

# Crée la fenêtre principale
root = tk.Tk()
root.title("Fenêtre simple")
root.geometry("300x150")

# Ajoute un label (texte)
label = tk.Label(root, text="Bienvenue dans cette fenêtre !", font=("Arial", 12))
label.pack(pady=10)

# Ajoute des boutons
btn_hello = tk.Button(root, text="Dire bonjour", command=on_hello)
btn_hello.pack(pady=5)

btn_quit = tk.Button(root, text="Quitter", command=on_quit)
btn_quit.pack(pady=5)

# Boucle principale
root.mainloop()
