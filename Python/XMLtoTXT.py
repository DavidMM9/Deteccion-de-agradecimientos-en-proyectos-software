import os
from bs4 import BeautifulSoup as bs

def XMLtoTXT(path):
    content = []
    destination = "./../TEI/TXT"
    a,b = 'áéíóúäëïöüâêîôûàèìòùãõäëïöüåç','aeiouaeiouaeiouaeiouaoaeiouac'
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
                fp = open(destination + "/" + x + ".txt", 'w')
                texto = back.find("p").getText()
                texto = texto.translate(trans)
                fp.write(texto)
                fp.close()