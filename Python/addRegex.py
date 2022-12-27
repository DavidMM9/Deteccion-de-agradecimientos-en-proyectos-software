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
        contents = f.read()
        smthProy = re.findall(
            "(\S+(\s+[pP]roject(s)*))", contents
        )  # para este regex comprobar que la primera letra de cada palabra de la lista sea mayuscula
        proyNumber = re.findall(
            "([pP]roject(s)* (no. |No. |[Nn]umber )+([^\s]+))", contents
        )
        grantAgreement = re.findall(
            "([gG]rant(s)* ([aA]greement )*([Nn]o(\.*) )*(number )*([a-zA-Z\-:/\.#0-9]+)*(['\"].+['\"])*)",
            contents,
        )
        proySmth = re.findall("([pP]roject(s)* ([^\s]+))", contents)
        projects = re.findall("([\(\[][a-zA-Z0-9]+[\-:/]+[^\s]+)", contents)
        send = []
        sendGrant = []
        dicts = {}
        for y in smthProy:
            if y[0][0] == y[0][0].lower():
                continue
            else:
                dicts.update(
                    {"entity_group": "Funding entity", "word": y[0], "source": "REGEX"}
                )
                dicts_copy = dicts.copy()
                send.append(dicts_copy)
        for z in proyNumber:
            dicts.update(
                {"entity_group": "Funding entity", "word": z[0], "source": "REGEX"}
            )
            dicts_copy = dicts.copy()
            send.append(dicts_copy)
        for p in grantAgreement:
            dicts.update(
                {"entity_group": "Funding entity", "word": p[0], "source": "REGEX"}
            )
            dicts_copy = dicts.copy()
            sendGrant.append(dicts_copy)
        for i in proySmth:
            var = i[0].split(" ")[1]
            if (
                var[0].isalpha() == True
                or var[0].isdigit() == True
                or var[0] == "'"
                or var[0] == '"'
            ):
                if var[0] == var[0].upper():
                    dicts.update(
                        {
                            "entity_group": "Funding entity",
                            "word": i[0],
                            "source": "REGEX",
                        }
                    )
                    dicts_copy = dicts.copy()
                    send.append(dicts_copy)
        for j in projects:
            if j[-1] == "," or j[-1] == ".":
                j = j.replace(j[-1], "")
            tieneNumero = any(char.isdigit() for char in j)
            if j == j.upper() and tieneNumero == True:
                dicts.update(
                    {"entity_group": "Funding entity", "word": j[0], "source": "REGEX"}
                )
                dicts_copy = dicts.copy()
                sendGrant.append(dicts_copy)

        send.extend(sendGrant)
        jsonFile = open(target + "/" + x + ".json", "r+")
        prueba = jsonFile.read()
        data = json.loads(prueba)
        final = data + send
        finalJson = json.dumps(final)
        jsonFile.seek(0)
        jsonFile.write(finalJson)
        jsonFile.truncate()
