# Use uma imagem base Python otimizada
FROM python:3.10-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY app/ ./app/
COPY model/ ./model/
COPY data/ ./data/

# Expõe a porta que o Uvicorn irá rodar
EXPOSE 8000

# Comando para rodar a aplicação com Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
