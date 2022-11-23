import json
import os
from grobid_client_python.grobid_client.grobid_client import GrobidClient
from bs4 import BeautifulSoup as bs

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

def useGrobid(input, output):
    client = GrobidClient(config_path="./config.json")
    client.process("processFulltextDocument", input, output, force = True, verbose = True)

def XMLtoTXT(path):
    content = []
    destination = "./../TEI/TXT"
    # Read the XML file
    for x in os.listdir(path):
        with open(path + "/" + x, "r", encoding="UTF-8") as file:
            # Read each line in the file, readlines() returns a list of lines
            content = file.readlines()
            # Combine the lines in the list into a string
            content = "".join(content)
            bs_content = bs(content, "html.parser")
            if(bs_content.find("div", {"type": "acknowledgement"})):
                back = bs_content.find("div", {"type": "acknowledgement"})
            else:
                continue
            if(bs_content.find("div", {"type": "acknowledgement"}).find("p")):
                print(x)
                fp = open(destination + "/" + x + ".txt", 'w')
                fp.write(back.find("p").getText())
                fp.close()
                # print(back.find("p").getText() + "\n")

def useModel(modelo, input, output):
    tokenizer = AutoTokenizer.from_pretrained(modelo)
    model = AutoModelForTokenClassification.from_pretrained(modelo)

    nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")

    path = "./../TEI/TXT/"
    target = "./../HuggingFace/" + modelo
    if not os.path.exists(target):
        os.makedirs(target)
    for x in os.listdir(path):
        f = open(path + x, "r")
        contents = f.read()
        result = nlp(contents)
        jsonFile = open(target + x + ".json", "w")
    for dic in result:
        dic["score"] = str(dic["score"])
    final = json.dumps(result)
    jsonFile.write(final)


useGrobid("./../Articulos", "./../TEI/XML")
XMLtoTXT("./../TEI/XML")
useModel("Jean-Baptiste/camembert-ner")


# # De donde cojo los json para probar
# pathBert = "./../HuggingFace/bert-large-NER"
# pathJean = "./../HuggingFace/Jean-Baptiste"
# # Donde estan los json buenos
# compared = "./../TEI/Json"
# res = 0
# total = 0
# total2 = 0

# # Hago un bucle para abrir de uno en uno los archivos
# for k in os.listdir(pathBert):
#     # Abrimos el json
#     f = open(pathBert + "\\" + k)
#     data = json.load(f)
#     c = open(compared + "\\" + k)
#     dataCompared = json.load(c)

#     # Bucle para cada uno de los elementos del archivo
#     for i in data:
#         # Bucle para comparar los elementos de los dos archivos
#         for j in dataCompared:
#             # i['word'] = lo que ha reconocido
#             # i['entity_group'] = que ha dicho que es
#             # Compruebo que tanto el entity_group como el word sean iguales para comprobar
#             # si el modelo ha detectado bien el elemento
#             if ((i['word'] == j['word']) and (i['entity_group'] == j['entity_group'])):
#                 res = res + 1
#                 break

#     # Voy añadiendo cuantos elementos hay en cada archivo para obtener el total
#     total = total + len(data)
#     total2 = total2 + len(dataCompared)

#     # Cerramos el json
#     f.close()
#     c.close()

# print("El modelo ha detectado " + str(total) + " elementos")
# print("Hay que encontrar " + str(total2) + " elementos")
# print("De los resultados obtenidos " + str(res) + " estan bien")
