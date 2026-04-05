import tkinter as tk

janela = tk.Tk()
janela.title("Minha To-Do List")
janela.geometry("400x500")
janela.configure(bg="#ffd6e7")

titulo = tk.Label(
    janela,
    text="Minha To-Do List ♡",
    font=("Segoe Print", 16, "bold"),
    bg="#ffd6e7"
)
titulo.pack(pady=15)

janela.mainloop()
