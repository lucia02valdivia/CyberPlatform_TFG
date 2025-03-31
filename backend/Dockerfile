FROM python:3.11-slim 
#USa una versión ligera de python 3.11 lo que reduce el tamaño de la imagen
WORKDIR /app
#Crea un directorio de trabajo llamado app
COPY . /app
#Copia el contenido de la carpeta backend al directorio de trabajo en el contenedor
#Este directorio contendrá el código fuente de la aplicación
COPY requirements.txt /app/
#Copia el archivo requirements.txt al contenedor
#Este archivo contiene las dependencias necesarias para el proyecto
RUN pip install --no-cache-dir -r requirements.txt
#Instala las dependencias del archivo requirements.txt
EXPOSE 5000
#Expone el puerto 5000 para que la aplicación sea accesible desde fuera del contenedor
#Este puerto es el que usará la aplicación Flask
CMD ["python", "main.py"]
#Comando para ejecutar el script main.py
#Este script contiene la aplicación Flask