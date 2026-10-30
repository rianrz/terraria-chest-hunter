import tkinter as tk
from tkinter import filedialog
import subprocess

def select_world_path():
    world_path = filedialog.askopenfilename(filetypes=[("World files", "*.wld")])
    if world_path:
        print(f"Caminho do mundo selecionado: {world_path}")
        subprocess.run(["python", "main.py", world_path])

def main():
    root = tk.Tk()
    root.title("Interface de Seleção de Mundo")

    label = tk.Label(root, text="Selecione o arquivo .wld do mundo de Terraria:")
    label.pack(pady=10)

    button = tk.Button(root, text="Selecionar", command=select_world_path)
    button.pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    main()
