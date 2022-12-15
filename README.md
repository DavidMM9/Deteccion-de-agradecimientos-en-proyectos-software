# Deteccion de agradecimientos en proyectos software

Guía de ejecución del pipeline:

1. Abrir Docker Desktop

2. Descargar y ejecutar el contenedor Docker:
  > docker pull lfoppiano/grobid:0.7.2
  
  > docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
  
3. Ir a Python/Json_reader.py y elegir los parámetros que queremos pasar a las funciones

4. Ejecutar el programa:
  > python3 Json_reader.py
