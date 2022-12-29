import re
import json
import os


def addRegex(modelo, path, output):
    send = []
    sendGrant = []
    final = []
    dicts = {}
    target = output + modelo
    for x in os.listdir(path):
        if os.path.isdir(path + x):
            continue
        f = open(path + x)
        jsonFile = open(target + "/" + x + ".json", "r+")
        texto = jsonFile.read()
        prueba = json.loads(texto)
        # print(prueba[0]["word"])
        contents = f.read()
        smthProy = re.findall("(\S+(\s+[pP]roject(s)*))", contents)
        proyNumber = re.findall(
            "((?![.()(\[\])-,\\/\*])\S*(\S*([a-zA-Z]\S*[0-9])|([0-9]\S*))\S*(?<![.()(\[\])-,\\/\*]))",
            contents,
        )
        send = []
        dicts = {}
        for y in smthProy:
            if y[0][0] == y[0][0].lower() or y[0][0].isdigit() == False:
                continue
            else:
                for i in prueba.copy():
                    if y[0] in i["word"]:
                        prueba.remove(i)
                dicts.update(
                    {"entity_group": "Funding entity", "word": y[0], "source": "REGEX"}
                )
                dicts_copy = dicts.copy()
                send.append(dicts_copy)
        for z in proyNumber:
            if len(z[0]) < 5 and z[0][0].isdigit() == True:
                if len(z[0]) < 4 or (len(z[0]) == 4 and int(z[0][0]) < 3):
                    continue
            for i in prueba.copy():
                if z[0] in i["word"]:
                    prueba.remove(i)
            dicts.update(
                {"entity_group": "Funding entity", "word": z[0], "source": "REGEX"}
            )
            dicts_copy = dicts.copy()
            send.append(dicts_copy)

        data = json.dumps(prueba)
        data = json.loads(data)
        final = data + send

        finalJson = json.dumps(final)
        jsonFile.seek(0)
        jsonFile.write(finalJson)
        jsonFile.truncate()
