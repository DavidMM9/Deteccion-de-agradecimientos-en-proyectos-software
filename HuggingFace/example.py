from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner")

nlp = pipeline('ner', model=model, tokenizer=tokenizer, agregation_strategy="simple")
nlp("This work was supported in part by EU H2020 project Serums (826278-SERUMS-H2020-SC1-FA-DTS-2018-2020), by National Science Foundation USA (NSF HDR:TRIPODS-1934884), and by National Research Foundation Singapore under its NRF Fellowship Programme [NRF-NRFFAI1-2019-0004] and AI Singapore Programme [AISG-RP-2018-005]. Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not reflect the views of National Research Foundation, Singapore.")

# tokenizer.save_pretrained("./prueba")
# model.save_pretrained("./prueba")

# tokenizer = AutoTokenizer.from_pretrained("./prueba")
# model = AutoModelForTokenClassification.from_pretrained("./prueba")