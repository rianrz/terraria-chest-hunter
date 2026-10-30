import os
import sys

def list_chests(world_path):
    if not os.path.exists(world_path):
        print(f"Arquivo do mundo não encontrado: {world_path}")
        return

    print(f"Lendo arquivo do mundo: {world_path}")
    # Adicione a lógica para ler o arquivo .wld e listar os baús aqui

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python main.py <caminho_do_arquivo_wld>")
        sys.exit(1)

    world_path = sys.argv[1]
    list_chests(world_path)
