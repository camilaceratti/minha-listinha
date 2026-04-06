import tkinter as tk

janela = tk.Tk()
janela.title("Minha To-Do List")
janela.geometry("400x500")
janela.configure(bg="#dcdcdc")

caderno = tk.Frame(janela, bg="white", bd=2, relief="solid")
caderno.pack(padx=20, pady=20, fill="both", expand=True)

titulo = tk.Label(
    caderno,
    text="MINHA TO DO LIST ♡",
    font=("Segoe UI",20 , "bold"),
    bg="white"
)
titulo.pack(pady=15)

entrada = tk.Entry(caderno, width=30)
entrada.pack(pady=10)

def adicionar_tarefa():
    texto = entrada.get()
    tarefa = tk.Checkbutton(frame_tarefas, text=texto, bg="white")
    tarefa.pack(anchor="w")
    entrada.delete(0, tk.END)


botao_adicionar = tk.Button(
    caderno,
    text="Adicionar",
    command=adicionar_tarefa,
    bg="#4CAF50",
    fg="white",
    bd=0
)
botao_adicionar.pack(pady=10)

frame_tarefas = tk.Frame(caderno, bg="white")
frame_tarefas.pack(pady=10)

janela.mainloop()

