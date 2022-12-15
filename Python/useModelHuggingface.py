import json
import os

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

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
            dic["word"] = dic["word"].translate(trans)
            dic["word"] = dic["word"].lstrip()
        # Cambiamos la estructura del modelo a Json y lo escribimos
        final = json.dumps(result)
        jsonFile.write(final)