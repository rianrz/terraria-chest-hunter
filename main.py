import sys
import lihzahrd

def list_chests(world_path):
    # Carrega o mundo do Terraria
    world = lihzahrd.World(world_path)
    
    # Filtra os objetos que são baús
    chests = [obj for obj in world.objects if obj.type == 'Chest']
    
    # Retorna os baús
    return chests

if __name__ == '__main__':
    world_path = sys.argv[1]
    chests = list_chests(world_path)
    
    for chest in chests:
        print(f"Baú em coordenadas ({chest.x}, {chest.y})")
        for item in chest.items:
            print(f"  Item: {item.name}, Quantidade: {item.quantity}")
