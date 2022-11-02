import json
import os

path = "/mnt/c/Users/david/Desktop/TFG/Deteccion-de-agradecimientos-en-proyectos-software/HuggingFace/Jean-Baptiste/"
compared = "/mnt/c/Users/david/Desktop/TFG/Deteccion-de-agradecimientos-en-proyectos-software/TEI/Json/"
allfiles = []
res = 0

for filename in os.listdir(path):
    allfiles.append(filename)

# print(allfiles)

for k in allfiles:
    # Abrimos el json
    f = open(path + k)
    data = json.load(f)
    c = open(compared + k)
    dataCompared = json.load(c)

    # print("Estoy en " + k)

    for i in data:
        for j in dataCompared:
            # i['word'] = lo que ha reconocido
            # i['entity_group'] = que ha dicho que es
            # print("Ha reconocido " + i['word'] + " como " + i['entity_group'])
            # print(j['word'])
            if ((i['word'] == j['word']) and (i['entity_group'] == j['entity_group'])):
                res = res + 1

    # Cerramos el json
    f.close()
    c.close()
print("De los resultados obtenidos " + str(res) + " estan bien")
