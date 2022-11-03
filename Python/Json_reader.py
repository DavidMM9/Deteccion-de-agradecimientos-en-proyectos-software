import json
import os

# De donde cojo los json para probar
pathBert = "/mnt/c/Users/david/Desktop/TFG/Deteccion-de-agradecimientos-en-proyectos-software/HuggingFace/bert-large-NER/"
pathJean = "/mnt/c/Users/david/Desktop/TFG/Deteccion-de-agradecimientos-en-proyectos-software/HuggingFace/Jean-Baptiste/"
# Donde estan los json buenos
compared = "/mnt/c/Users/david/Desktop/TFG/Deteccion-de-agradecimientos-en-proyectos-software/TEI/Json/"
allFiles = []
res = 0
total = 0
total2 = 0

# Meto todos los archivos de la carpeta en una variable
for filename in os.listdir(pathBert):
    allFiles.append(filename)

# Hago un bucle para abrir de uno en uno los archivos
for k in allFiles:
    # Abrimos el json
    f = open(pathBert + k)
    data = json.load(f)
    c = open(compared + k)
    dataCompared = json.load(c)

    # Bucle para cada uno de los elementos del archivo
    for i in data:
        # Bucle para comparar los elementos de los dos archivos
        for j in dataCompared:
            # i['word'] = lo que ha reconocido
            # i['entity_group'] = que ha dicho que es
            # Compruebo que tanto el entity_group como el word sean iguales para comprobar
            # si el modelo ha detectado bien el elemento
            if ((i['word'] == j['word']) and (i['entity_group'] == j['entity_group'])):
                res = res + 1
                break

    # Voy añadiendo cuantos elementos hay en cada archivo para obtener el total
    total = total + len(data)
    total2 = total2 + len(dataCompared)

    # Cerramos el json
    f.close()
    c.close()

print("El modelo ha detectado " + str(total) + " elementos")
print("Hay que encontrar " + str(total2) + " elementos")
print("De los resultados obtenidos " + str(res) + " estan bien")
