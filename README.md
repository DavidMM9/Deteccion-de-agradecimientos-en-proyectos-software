# Deteccion de agradecimientos en proyectos software

## Requirements

- Python3
- Docker

## Guía de ejecución del pipeline:

1. Descargar el repositorio

```
 git clone https://github.com/DavidMM9/Deteccion-de-agradecimientos-en-proyectos-software.git
```

2. Abrir la carpeta Python y ejecutar el requirements.txt

```
cd Deteccion-de-agradecimientos-en-proyectos-software/Python/
pip install -r requirements.txt
```

**Los pasos 3 y 4 se pueden saltar si no se quiere usar la parte de Grobid**

3. Abrir Docker Desktop

4. Descargar y ejecutar el contenedor Docker

```
docker pull lfoppiano/grobid:0.7.2
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```

5. Ejecutar main.py con los parametros que queramos

```
-h, --help            show this help message and exit

-a ARTICULOS, --articulos ARTICULOS
                      Carpeta de los articulos

-t TEI, --tei TEI     Carpeta para guardar los XML y TXT

-o OUTPUT, --output OUTPUT
                      Carpeta para guardar los json devueltos

-m MODEL, --model MODEL
                      Modelo de HuggingFace

-s GOLDSTANDARD, --goldstandard GOLDSTANDARD
                      Carpeta donde esta el goldstandard

-g, --grobid          Usar grobid para pasar articulos de PDF a XML

-x, --toTXT           Sacar la seccion de Acknowledgements en TXT

-f, --huggingface     Usar modelo de HuggingFace

-r, --regex           Mete al json del modelo lo encontrado con regex

-c, --calcF1          Calcula el F1 score en una tabla
```

Ejemplo:

```
python3 main.py -a ../Articulos/ -t ../TEI/ -o ../HuggingFace/prueba/ -m Jean-Baptiste/camembert-ner -s ../Gold_standard/ -g -x -f -r -c
```

El modelo de HuggingFace que se quiera utilizar se puede encontrar en su página web https://huggingface.co/ y pasar como parámetro al comando el nombre del modelo. Se puede copiar y pegar desde la propia página del modelo. Ejemplo:

![](/Python/modelo.png "Ejemplo para copiar el modelo")
