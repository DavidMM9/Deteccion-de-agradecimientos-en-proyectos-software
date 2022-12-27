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
        prueba = jsonFile.read()
        print(prueba[0] + "\n")
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
                dicts.update(
                    {"entity_group": "Funding entity", "word": y[0], "source": "REGEX"}
                )
                dicts_copy = dicts.copy()
                send.append(dicts_copy)
        for z in proyNumber:
            if len(z[0]) < 5:
                continue
            dicts.update(
                {"entity_group": "Funding entity", "word": z[0], "source": "REGEX"}
            )
            # print(z[0])
            dicts_copy = dicts.copy()
            send.append(dicts_copy)

        data = json.loads(prueba)
        final = data + send
        for x in final:
            if x["source"] == "REGEX":
                print(x["word"] + "\n")
                # m = re.search("\w*" + x["word"] + "\w*", final)
                # print(m.group())

        finalJson = json.dumps(final)
        jsonFile.seek(0)
        jsonFile.write(finalJson)
        jsonFile.truncate()
