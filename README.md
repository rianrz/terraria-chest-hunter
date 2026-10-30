# terraria-chest-hunter

Este projeto lê arquivos de mapa do Terraria (.wld) para localizar e listar os baús e seus itens.

## Como subir o ambiente no Docker

1. Certifique-se de ter o Docker instalado em seu sistema.
2. Clone este repositório em sua máquina.
3. Navegue até o diretório do projeto.
4. Execute o seguinte comando para construir e iniciar o container:

   ```sh
   docker-compose up --build
   ```

5. O projeto será iniciado e você poderá ver a saída no terminal.

## Como rodar o projeto

1. Certifique-se de que o arquivo do mundo do Terraria (.wld) esteja na pasta `./Terraria/Worlds`.
2. Execute o seguinte comando:

   ```sh
   docker-compose run terraria-chest-hunter python main.py ./Terraria/Worlds/your_world.wld
   ```

   Substitua `your_world.wld` pelo nome do seu arquivo do mundo.
