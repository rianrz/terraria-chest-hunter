import sys
import nbt

def list_chests(world_path):
    # Carrega o mundo do Terraria usando a biblioteca nbt
    world = nbt.load_file(world_path)
    
    # Filtra os objetos que são baús
    chests = [obj for obj in world.listtag('TileEntities') if obj.name == 'Chest']
    
    # Retorna os baús
    return chests

if __name__ == '__main__':
    world_path = sys.argv[1]
    chests = list_chests(world_path)
    
    for chest in chests:
        print(f"Baú em coordenadas ({chest['x'].value}, {chest['y'].value})")
        for item in chest['Items']:
            print(f"  Item: {item['id'].value}, Quantidade: {item['Count'].value}")
