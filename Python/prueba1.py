from useGrobid import useGrobid
from XMLtoTXT import XMLtoTXT
from useModelHuggingface import useModel
from addRegex import addRegex
from calcF1Score import calcF1Score


# Modelos de Huggingface utilizados
camembert_NER = "Jean-Baptiste/camembert-ner"
bert_base_NER = "dslim/bert-base-NER"
bert_large_NER = "dslim/bert-large-NER"
bert_base_multilingual_cased_ner_hrl = "Davlan/bert-base-multilingual-cased-ner-hrl"
roberta_large_ner_english = "Jean-Baptiste/roberta-large-ner-english"

# Campos: useGrobid(carpeta origen de los artículos, carpeta destino donde guardar los XML)
# useGrobid("./../Articulos", "./../TEI/XML")

# Campos: XMLtoTXT(carpeta de origen de los XML)
# XMLtoTXT("./../TEI/XML")

# Campos: useModel(modelo Huggingface a utilizar, carpeta origen de los TXT, carpeta destino donde guardar los json generados por el modelo)
useModel(camembert_NER, "./../TEI/TXT/", "./../HuggingFace/prueba/")
# useModel(bert_base_NER, "./../TEI/TXT/", "./../HuggingFace/")
# useModel(bert_large_NER, "./../TEI/TXT/", "./../HuggingFace/")
# useModel(bert_base_multilingual_cased_ner_hrl, "./../TEI/TXT/", "./../HuggingFace/")
# useModel(roberta_large_ner_english, "./../TEI/TXT/", "./../HuggingFace/")

# Campos: addRegex(modelo Huggingface utilizado, carpeta origen de los TXT, carpeta destino donde guardar los json generados por el modelo)
addRegex(camembert_NER, "./../TEI/TXT/", "./../HuggingFace/prueba/")
# addRegex(bert_base_NER, "./../TEI/TXT/", "./../HuggingFace/")
# addRegex(bert_large_NER, "./../TEI/TXT/", "./../HuggingFace/")
# addRegex(bert_base_multilingual_cased_ner_hrl, "./../TEI/TXT/", "./../HuggingFace/")
# addRegex(roberta_large_ner_english, "./../TEI/TXT/", "./../HuggingFace/")

# Campos: calcF1Score(carpeta origen de los json creados por el modelo + modelo utilizado + /, carpeta origen del gold standard)
calcF1Score("./../HuggingFace/" + camembert_NER + "/", "./../Json/")
# calcF1Score("./../HuggingFace/" + bert_base_NER + "/", "./../TEI/Json/")
# calcF1Score("./../HuggingFace/" + bert_large_NER + "/", "./../TEI/Json/")
# calcF1Score("./../HuggingFace/" + bert_base_multilingual_cased_ner_hrl + "/", "./../TEI/Json/")
# calcF1Score("./../HuggingFace/" + roberta_large_ner_english + "/", "./../TEI/Json/")
