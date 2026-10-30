# Use a imagem oficial do Python 3.12
FROM python:3.12-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código para o diretório de trabalho
COPY . .

# Define o comando padrão para executar o script
CMD ["python", "main.py"]
