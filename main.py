import customtkinter as ctk
import string
import random
import pyperclip
from tkinter import messagebox

MIN_T = 6
MAX_T = 30
STEPS = (MAX_T - MIN_T) + 1  # garante passos inteiros

def gerar():
    tamanho = int(round(scale_tamanho.get()))  # <-- CAST PARA INT
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
    
    if not caracteres:
        txt_senha.configure(state="normal")
        txt_senha.delete("0.0", "end")
        txt_senha.insert("0.0", "⚠️ Escolha pelo menos um tipo de caractere!")
        txt_senha.configure(state="disabled")
        return
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    txt_senha.configure(state="normal")
    txt_senha.delete("0.0", "end")
    txt_senha.insert("0.0", senha)
    txt_senha.configure(state="disabled")

def limpar():
    txt_senha.configure(state="normal")
    txt_senha.delete("0.0", "end")
    txt_senha.insert("0.0", "Gerador de senhas")
    txt_senha.configure(state="disabled")

def copiar():
    senha = txt_senha.get("0.0", "end").strip()
    if senha in ["Gerador de senhas", "⚠️ Escolha pelo menos um tipo de caractere!", ""]:
        messagebox.showwarning("Aviso", "Gere uma senha antes de copiar.")
        return
    pyperclip.copy(senha)
    messagebox.showinfo("Senha copiada", "Senha copiada com sucesso!")

# --- Janela --- #
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Gerador de Senhas")
root.geometry("600x400")
root.resizable(False, False)

titulo = ctk.CTkLabel(root, text="🔐 Gerador de Senhas", font=("Arial", 22, "bold"))
titulo.pack(pady=15)

txt_senha = ctk.CTkTextbox(root, height=60, width=500, font=("Courier New", 14))
txt_senha.pack(pady=10)
txt_senha.insert("0.0", "Gerador de senhas")
txt_senha.configure(state="disabled")

frame_opcoes = ctk.CTkFrame(root)
frame_opcoes.pack(pady=15)

check_numeros = ctk.CTkCheckBox(frame_opcoes, text="Números")
check_maiusculas = ctk.CTkCheckBox(frame_opcoes, text="Letras Maiúsculas")
check_minusculas = ctk.CTkCheckBox(frame_opcoes, text="Letras Minúsculas")
check_simbolos = ctk.CTkCheckBox(frame_opcoes, text="Símbolos")
check_numeros.grid(row=0, column=0, padx=15, pady=5)
check_maiusculas.grid(row=0, column=1, padx=15, pady=5)
check_minusculas.grid(row=0, column=2, padx=15, pady=5)
check_simbolos.grid(row=0, column=3, padx=15, pady=5)

scale_tamanho = ctk.CTkSlider(root, from_=MIN_T, to=MAX_T, number_of_steps=STEPS)  # <-- PASSOS INTEIROS
scale_tamanho.set(12)
label_tamanho = ctk.CTkLabel(root, text="Tamanho da Senha: 12")
scale_tamanho.pack(pady=5)
label_tamanho.pack()

def atualizar_label(valor):
    label_tamanho.configure(text=f"Tamanho da Senha: {int(round(float(valor)))}")  # <-- MOSTRA INT
scale_tamanho.configure(command=atualizar_label)

frame_botoes = ctk.CTkFrame(root)
frame_botoes.pack(pady=20)

btn_gerar = ctk.CTkButton(frame_botoes, text="Gerar Senha", command=gerar, width=150)
btn_limpar = ctk.CTkButton(frame_botoes, text="Limpar", command=limpar, width=150)
btn_copiar = ctk.CTkButton(frame_botoes, text="Copiar", command=copiar, width=150)
btn_gerar.grid(row=0, column=0, padx=10)
btn_limpar.grid(row=0, column=1, padx=10)
btn_copiar.grid(row=0, column=2, padx=10)

root.mainloop()
