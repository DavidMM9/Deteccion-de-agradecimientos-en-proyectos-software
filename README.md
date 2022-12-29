# Deteccion de agradecimientos en proyectos software

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

## Requirements

- [Python 3.10.6](https://www.python.org/downloads/)
- [Docker 4.14.1](https://docs.docker.com/engine/install/)

## Guía de ejecución del pipeline:

1. Descargar el repositorio

```
 git clone https://github.com/DavidMM9/Deteccion-de-agradecimientos-en-proyectos-software.git
```

2. Abrir la carpeta Python y ejecutar el requirements.txt

```
cd Deteccion-de-agradecimientos-en-proyectos-software/Python/
```

**El paso 3 solo se necesita hacer la primera vez**

3. Ejecutar el requirements.txt

```
pip install -r requirements.txt
```

**Los pasos del 4 al 6 se pueden saltar si no se quiere usar la parte de Grobid**

4. Abrir Docker Desktop

**El paso 5 solo se necesita hacer la primera vez**

5. Descargar el contenedor Docker

```
docker pull lfoppiano/grobid:0.7.2
```

6. Ejecutar el contenedor

```
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```

7. Ejecutar main.py con los parametros que queramos

```
-h, --help            show this help message and exit

-a ARTICULOS, --articulos ARTICULOS
                      Carpeta de los articulos

-t TEI, --tei TEI     Carpeta para guardar los XML y TXT

-o OUTPUT, --output OUTPUT
                      Carpeta para guardar los json devueltos

-m MODEL, --model MODEL
                      Modelo de HuggingFace

-g, --grobid          Usar grobid para pasar articulos de PDF a XML

-x, --toTXT           Sacar la seccion de Acknowledgements en TXT

-f, --huggingface     Usar modelo de HuggingFace

-r, --regex           Mete al json del modelo lo encontrado con regex
```

Ejemplo:

```
python3 main.py -a ../Articulos/ -t ../TEI/ -o ../HuggingFace/ -m Jean-Baptiste/camembert-ner -g -x -f -r
```

Al ejecutar este ejemplo:

- Se cogerán los artículos de la carpeta ../Articulos/
- Se guardarán los archivos XML generados por el Grobid en la carpeta ../TEI/
- En la carpeta ../TEI/TXT/ se guardarán los txt de la sección de acknowledgements
- Los Json generados por el modelo se guardarán en la carpeta ../HuggingFace/Jean-Baptiste/camembert-ner/

El modelo de HuggingFace que se quiera utilizar se puede encontrar en su página web https://huggingface.co/ y pasar como parámetro al comando el nombre del modelo. Se puede copiar y pegar desde la propia página del modelo. Ejemplo:

![](/Python/modelo.png "Ejemplo para copiar el modelo")

## Explicación del output:

El output generado al utilizar este proyecto será un archivo .json con el fragmento de texto encontrado, el tipo de entidad reconocido y si proviene del modelo utilizado en HuggingFace o de las expresiones regulares.

Tipos de entidades a reconocer:

- PER -> Persona
- ORG -> Organización
- MISC -> Miscelaneo, no es ni persona ni organización
- Funding entity -> Proyecto o Grant id

Ejemplo:

```
    {
		"entity_group": "Funding entity",
		"word": "231913",
		"source": "REGEX"
	}
```

Si analizamos este fragmento de json, podemos ver que hemos detectado un proyecto o Grant id ya que el "entity_group" es "Funding entity". El fragmento de texto detectado es lo que hay dentro del campo "word", en este caso "231913" y, por úlitmo, podemos comprobar que esta detección se ha realizado mediante expresiones regulares al ser "REGEX" el campo "source".

## Calculo del F1-score

Para calcular la precisión, el recall y el f1-score de los json devueltos por el proyecto, tendremos que ejecutar el archivo calcF1Score.py.

```
options:
  -h, --help            show this help message and exit

  -j JSON, --json JSON
                        Carpeta con los Json a analizar

  -g GOLDSTANDARD, --goldstandard GOLDSTANDARD
                        Carpeta donde esta el goldstandard
```

Ejemplo:

```
python3 calcF1Score.py -j ../HuggingFace/Jean-Baptiste/camembert-ner/ -g ../Gold_standard/
```

Output con el ejemplo:

```
+---------------+-----------+--------+----------+
|   Model name  | Precision | Recall | F1-score |
+---------------+-----------+--------+----------+
| camembert-ner |    0.69   |  0.71  |   0.7    |
+---------------+-----------+--------+----------+
```
