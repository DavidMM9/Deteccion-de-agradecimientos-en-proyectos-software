import json
import os

# De donde cojo los json para probar
path = "/mnt/c/Users/david/Desktop/TFG/Deteccion-de-agradecimientos-en-proyectos-software/HuggingFace/Jean-Baptiste/"
# Donde estan los json buenos
compared = "/mnt/c/Users/david/Desktop/TFG/Deteccion-de-agradecimientos-en-proyectos-software/TEI/Json/"
allfiles = []
res = 0
total = 0
total2 = 0

# Meto todos los archivos de la carpeta en una variable
for filename in os.listdir(path):
    allfiles.append(filename)

# Hago un bucle para abrir de uno en uno los archivos
for k in allfiles:
    # Abrimos el json
    f = open(path + k)
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
            if ((i['word'] == j['word'])):
                if ((i['entity_group'] == j['entity_group'])):
                    res = res + 1

    # Voy añadiendo cuantos elementos hay en cada archivo para obtener el total
    total = total + len(data)
    total2 = total2 + len(dataCompared)

    # Cerramos el json
    f.close()
    c.close()

print(total)
print(total2)
print("De los resultados obtenidos " + str(res) + " estan bien")
