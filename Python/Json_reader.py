from useGrobid import useGrobid
from XMLtoTXT import XMLtoTXT
from useModelHuggingface import useModel
from addRegex import addRegex
from calcF1Score import calcF1Score

camembert_NER = "Jean-Baptiste/camembert-ner"
bert_base_NER = "dslim/bert-base-NER"
bert_large_NER = "dslim/bert-large-NER"
bert_base_multilingual_cased_ner_hrl = "Davlan/bert-base-multilingual-cased-ner-hrl"
roberta_large_ner_english = "Jean-Baptiste/roberta-large-ner-english"

# useGrobid("./../Articulos", "./../TEI/XML")
# XMLtoTXT("./../TEI/XML")
useModel(camembert_NER, "./../TEI/TXT/", "./../HuggingFace/")
addRegex(camembert_NER, "./../TEI/TXT/", "./../HuggingFace/")
# calcF1Score("./../HuggingFace/" + camembert_NER + "/", "./../TEI/Json/")