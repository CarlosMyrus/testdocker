FROM alpine:3.10
# que descargue el so alpine

# adminitrador de paquetes, que añada el paquete python3, python necesita de pip
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip
# para crear una carpeta dentro del sistema, establece el directorio de trabajo
WORKDIR /app
# para copiar todas las carpetas
COPY . /app
# dentro del contenedor va a instalar los modulos listados en requirements.txt
RUN pip3 --no-cache-dir install -r requirements.txt

#una vez instalado hay que ejecutarlo
CMD ["python3", "src/app.py"]
