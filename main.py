import tkinter as tk
import string
import random
import pyperclip
from tkinter import messagebox

def gerar():
    tamanho = scale_tamanho.get()
    incluir_numeros = check_numeros.get()
    incluir_maiusculas = check_maiusculas.get()
    incluir_minusculas = check_minusculas.get()
    incluir_simbolos = check_simbolos.get()
    
    caracteres = ''
    if incluir_numeros:
        caracteres += string.digits
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_simbolos:
        caracteres += string.punctuation
    
    if not (incluir_numeros or incluir_maiusculas or incluir_minusculas or incluir_simbolos):
        txt_senha.config(text="Escolha um tipo de caractere para a senha.")
        return
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    txt_senha.config(text=f"{senha}")

def lipar():
    txt_senha.config(text="")

def copiar():
    tamanho = scale_tamanho.get()
    incluir_numeros = check_numeros.get()
    incluir_maiusculas = check_maiusculas.get()
    incluir_minusculas = check_minusculas.get()
    incluir_simbolos = check_simbolos.get()
    senha = txt_senha.cget("text").split(": ")[-1]

    if not (incluir_numeros or incluir_maiusculas or incluir_minusculas or incluir_simbolos):
        txt_senha.config(text="Gere uma senha primeiro.")
        return
    else:
        pyperclip.copy(senha)
        messagebox.showinfo("Senha copiada", "Senha copiada com sucesso!")

root = tk.Tk()
root.title("Gerador de senhas")
root.geometry("600x300")
root.resizable(False, False)


txt_titulo = tk.Label(root, text="Senha gerada: ").place(x=50, y=25)

txt_senha = tk.Label(root, text="Gerador de senhas", font=("Courier New", 12), bd="2", relief="solid", width="50", height="3")
txt_senha.place(x=(600 - txt_senha.winfo_reqwidth()) / 2, y=(150 - txt_senha.winfo_reqheight()) / 2)

check_numeros = tk.BooleanVar()
check_maiusculas = tk.BooleanVar()
check_minusculas = tk.BooleanVar()
check_simbolos = tk.BooleanVar()

tk.Checkbutton(root, text="Números", variable=check_numeros).place(x=10, y=110)
tk.Checkbutton(root, text="Letras Maiúsculas", variable=check_maiusculas).place(x=150, y=110)
tk.Checkbutton(root, text="Letras Minúsculas", variable=check_minusculas).place(x=300, y=110)
tk.Checkbutton(root, text="Símbolos", variable=check_simbolos).place(x=450, y=110)

scale_tamanho = tk.Scale(root, from_=4, to=20, orient=tk.HORIZONTAL, label="Tamanho da senha")
scale_tamanho.place(x=10, y=150, width=580)

tk.Button(root, text="Gerar Senha", command=gerar).place(x=10,     y=220, width=186, height=40)
tk.Button(root, text="Limpar Senha", command=lipar).place(x=206,   y=220, width=186, height=40)
tk.Button(root, text="Copiar Senha", command=copiar).place(x=402,   y=220, width=186, height=40)

root.mainloop()