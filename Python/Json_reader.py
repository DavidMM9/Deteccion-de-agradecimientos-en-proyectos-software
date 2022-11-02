import json
import os

allfiles = []
for filename in os.listdir("/mnt/c/Users/david/Desktop/TFG/Deteccion-de-agradecimientos-en-proyectos-software/HuggingFace/Jean-Baptiste"):
    allfiles.append(filename)

# print(allfiles)

for k in allfiles:
    # Abrimos el json
    f = open(
        "/mnt/c/Users/david/Desktop/TFG/Deteccion-de-agradecimientos-en-proyectos-software/HuggingFace/Jean-Baptiste/" + k)
    data = json.load(f)

    print("Estoy en " + k)
    for i in data:
        # i['word'] = lo que ha reconocido
        # i['entity_group'] = que ha dicho que es
        print("Ha reconocido " + i['word'] + " como " + i['entity_group'])

    # Cerramos el json
    f.close()
