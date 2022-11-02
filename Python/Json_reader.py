import json
import os

path = "/mnt/c/Users/david/Desktop/TFG/Deteccion-de-agradecimientos-en-proyectos-software/HuggingFace/Jean-Baptiste/"
compared = "/mnt/c/Users/david/Desktop/TFG/Deteccion-de-agradecimientos-en-proyectos-software/TEI/Json/"
allfiles = []

for filename in os.listdir(path):
    allfiles.append(filename)

# print(allfiles)

for k in allfiles:
    # Abrimos el json
    f = open(path + k)
    data = json.load(f)
    c = open(compared + k)
    dataCompared = json.load(c)

    print("Estoy en " + k)

    for i in data:
        # i['word'] = lo que ha reconocido
        # i['entity_group'] = que ha dicho que es
        print("Ha reconocido " + i['word'] + " como " + i['entity_group'])

    # Cerramos el json
    f.close()
    c.close()
