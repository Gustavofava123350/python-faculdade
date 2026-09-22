import tkinter as tk
from tkinter import messagebox

def calcular_media():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        n3 = float(entry3.get())
        media = (n1 + n2 + n3) / 3
        messagebox.showinfo("Resultado", f"A média é {media:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números!")

# Criar janela
janela = tk.Tk()
janela.title("Calculadora de Média")

tk.Label(janela, text="Nota 1:").grid(row=0, column=0)
tk.Label(janela, text="Nota 2:").grid(row=1, column=0)
tk.Label(janela, text="Nota 3:").grid(row=2, column=0)

entry1 = tk.Entry(janela)
entry2 = tk.Entry(janela)
entry3 = tk.Entry(janela)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)

tk.Button(janela, text="Calcular Média", command=calcular_media).grid(row=3, columnspan=2)

janela.mainloop()
