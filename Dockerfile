# Imagen base oficial de Python
FROM python:3.13-slim

# Crear directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema (para Pillow y fonts)
RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Comando para ejecutar el bot
CMD ["python", "bot.py"]
