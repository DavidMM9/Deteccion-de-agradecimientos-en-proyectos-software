from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline, PipelineDataFormat
import os
import json

tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner")

nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")

path = "./../TEI/TXT/"
target = "./prueba/"
if not os.path.exists(target):
   os.makedirs(target)
for x in os.listdir(path):
    f = open(path + x)
    contents = f.read()
    result = nlp(contents)
    jsonFile = open(target + x + ".json", "w")
    for dic in result:
        dic["score"] = str(dic["score"])
    final = json.dumps(result)
    jsonFile.write(final)