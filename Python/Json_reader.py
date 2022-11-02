import json

f = open(
    "/mnt/c/Users/david/Desktop/TFG/Deteccion-de-agradecimientos-en-proyectos-software/HuggingFace/Jean-Baptiste/Renewable_energy_in_Europe-2020.json"
)
data = json.load(f)

for i in data:
    print(i)

f.close()
