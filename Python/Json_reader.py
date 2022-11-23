import json
import os
from grobid_client_python.grobid_client.grobid_client import GrobidClient
from bs4 import BeautifulSoup as bs

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

camembert_NER = "Jean-Baptiste/camembert-ner"
bert_base_NER = "dslim/bert-base-NER"
bert_large_NER = "dslim/bert-large-NER"
bert_base_multilingual_cased_ner_hrl = "Davlan/bert-base-multilingual-cased-ner-hrl"
roberta_large_ner_english = "Jean-Baptiste/roberta-large-ner-english"
bert_base_NER_uncased = "dslim/bert-base-NER-uncased"

def useGrobid(input, output):
    client = GrobidClient(config_path="./config.json")
    client.process("processFulltextDocument", input, output, force = True, verbose = True)

def XMLtoTXT(path):
    content = []
    destination = "./../TEI/TXT"
    a,b = 'áéíóúü','aeiouu'
    trans = str.maketrans(a,b)
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
                texto = back.find("p").getText()
                texto = texto.translate(trans)
                fp.write(texto)
                fp.close()

def useModel(modelo, path, output):
    # Inicializamos el tokenizer y el modelo
    tokenizer = AutoTokenizer.from_pretrained(modelo)
    model = AutoModelForTokenClassification.from_pretrained(modelo)

    # Cargamos el modelo
    nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")

    target = output + modelo
    # Vemos si la carpeta donde queremos guardar los Json existe, si no la creamos
    if not os.path.exists(target):
        os.makedirs(target)
    # Recorremos los directorios de la carpeta
    for x in os.listdir(path):
        f = open(path + x)
        contents = f.read()
        # Aplicamos el modelo al texto
        result = nlp(contents)
        jsonFile = open(target + "/" + x + ".json", "w")
        # Cambiamos los scores a string para poder pasarlo a Json
        for dic in result:
            dic["score"] = str(dic["score"])
            dic["word"] = dic["word"].lstrip()
        # Cambiamos la estructura del modelo a Json y lo escribimos
        final = json.dumps(result)
        jsonFile.write(final)

def calcF1Score (modelo, compared):
    # Donde estan los json buenos
    res = 0
    total = 0
    total2 = 0

    # Hago un bucle para abrir de uno en uno los archivos
    for k in os.listdir(modelo):
        print(k)
        # Abrimos el json
        f = open(modelo + k)
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

    falsos_positivos = total - res
    falsos_negativos = total2 - res

    precision = res/(res + falsos_positivos)
    recall = res/(res + falsos_negativos)
    f1Score = 2*((precision * recall)/(precision + recall))

    print("La precision del modelo es: " + str(precision))
    print("El recall del modelo es: " + str(recall))
    print("La f1-score obtenida por el modelo es: " + str(f1Score))


# useGrobid("./../Articulos", "./../TEI/XML")
# XMLtoTXT("./../TEI/XML")
useModel(camembert_NER, "./../TEI/TXT/", "./../HuggingFace/")
calcF1Score("./../HuggingFace/" + camembert_NER + "/", "./../TEI/Json/")