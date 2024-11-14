import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        root.title("Estatísticas de Preferências Musicais")
        root.geometry("450x650")
        root.configure(bg="#2F4F4F")
        
        # Frame com Scrollbar
        main_frame = tk.Frame(root, bg="#2F4F4F")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        canvas = tk.Canvas(main_frame, bg="#2F4F4F", highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#2F4F4F")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Label de título
        title = tk.Label(scrollable_frame, text="Estatísticas de Preferências Musicais", font=("Arial", 18, "bold"), fg="#FFD700", bg="#2F4F4F")
        title.pack(pady=15)
        
        # Dicionário para armazenar entradas
        self.generos = {}
        
        # Criar os campos de entrada para cada gênero
        generos = ["Funk", "Axé", "Pagode", "Samba", "Eletrônica", "Pop", "Rock", "Sertanejo", "Reggae", "Forró"]
        for genero in generos:
            self.add_input(scrollable_frame, genero)
        
        # Total de pessoas
        self.total_pessoas_label = tk.Label(scrollable_frame, text="Total de Pessoas Pesquisadas: 0", font=("Arial", 14, "bold"), fg="#FFD700", bg="#2F4F4F")
        self.total_pessoas_label.pack(pady=15)
        
        # Botão para exibir resultados
        button = tk.Button(scrollable_frame, text="Exibir Resultados", command=self.exibir_resultados, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        button.pack(pady=15)
        
        # Área para exibir resultados
        self.resultados_frame = tk.Frame(scrollable_frame, bg="#2F4F4F")
        self.resultados_frame.pack(pady=15)

    def add_input(self, frame, genero):
        input_frame = tk.Frame(frame, bg="#2F4F4F")
        input_frame.pack(pady=8)
        
        label = tk.Label(input_frame, text=f"{genero}:", font=("Arial", 10, "bold"), fg="white", bg="#2F4F4F")
        label.pack(side=tk.LEFT)
        
        entry = tk.Entry(input_frame, width=10, font=("Arial", 10), bg="#D3D3D3", relief="solid")
        entry.pack(side=tk.RIGHT)
        entry.bind("<KeyRelease>", self.calcular_total)
        
        self.generos[genero] = entry

    def calcular_total(self, event=None):
        total = 0
        for entry in self.generos.values():
            try:
                total += int(entry.get())
            except ValueError:
                pass
        self.total_pessoas_label.config(text=f"Total de Pessoas Pesquisadas: {total}")

    def exibir_resultados(self):
        for widget in self.resultados_frame.winfo_children():
            widget.destroy()

        total_pessoas = int(self.total_pessoas_label.cget("text").split(": ")[1])

        for genero, entry in self.generos.items():
            try:
                quantidade = int(entry.get())
            except ValueError:
                quantidade = 0

            porcentagem = (quantidade / total_pessoas * 100) if total_pessoas > 0 else 0

            result_label = tk.Label(self.resultados_frame, text=f"{genero}: {quantidade} pessoas ({porcentagem:.2f}%)", font=("Arial", 10), fg="white", bg="#2F4F4F")
            result_label.pack(anchor="w")

            # Barra de progresso
            progress_frame = tk.Frame(self.resultados_frame, bg="white", height=20, width=300)
            progress_frame.pack(pady=3, fill=tk.X)
            progress_bar = tk.Frame(progress_frame, bg="#FFD700", height=20, width=int(porcentagem * 3))
            progress_bar.pack(side=tk.LEFT, fill=tk.Y)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
