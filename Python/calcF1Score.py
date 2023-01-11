import json
import os
import argparse, getopt, sys

from prettytable import PrettyTable


def calcF1Score(jsonF, compared, modelo):
    myTable = PrettyTable(["Model name", "Precision", "Recall", "F1-score"])
    # Donde estan los json buenos
    res = 0
    total = 0
    total2 = 0

    # Hago un bucle para abrir de uno en uno los archivos
    for k in os.listdir(jsonF):
        # Abrimos el json
        f = open(jsonF + k)
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
                if (i["word"] == j["word"]) and (
                    i["entity_group"] == j["entity_group"]
                ):
                    res = res + 1
                    break

        # Voy añadiendo cuantos elementos hay en cada archivo para obtener el total
        total = total + len(data)
        total2 = total2 + len(dataCompared)

        # Cerramos el json
        f.close()
        c.close()

    print("El modelo ha detectado " + str(total - res) + " elementos que no existen")
    print("No ha encontrado " + str(total2 - res) + " elementos")
    print("De los resultados obtenidos " + str(res) + " estan bien")

    falsos_positivos = total - res
    falsos_negativos = total2 - res

    precision = res / (res + falsos_positivos)
    recall = res / (res + falsos_negativos)
    f1Score = 2 * ((precision * recall) / (precision + recall))

    print("La precision del modelo es: " + str(round(precision, 2)))
    print("El recall del modelo es: " + str(round(recall, 2)))
    print("La f1-score obtenida por el modelo es: " + str(round(f1Score, 2)))

    myTable.add_row([modelo, round(precision, 2), round(recall, 2), round(f1Score, 2)])
    print(myTable)


def main(argv):
    parser = argparse.ArgumentParser(description="Calculo del F1 score")

    parser.add_argument(
        "-j", "--json", type=str, help="Carpeta con los Json a analizar"
    )
    parser.add_argument(
        "-g", "--goldstandard", type=str, help="Carpeta donde esta el goldstandard"
    )
    parser.add_argument("-m", "--model", type=str, help="Nombre del modelo utilizado")

    args = parser.parse_args()

    json = ""
    goldstandard = ""
    model = ""

    opts, args = getopt.getopt(
        argv,
        "hj:g:m:",
        ["json=", "goldstandard=", "model="],
    )

    for opt, arg in opts:
        if opt == "-h":
            print("main.py -a <articulos> -j <json> -g <goldstandard>")
            sys.exit()
        elif opt in ("-j", "--json"):
            json = arg
        elif opt in ("-g", "--goldstandard"):
            goldstandard = arg
        elif opt in ("-m", "--model"):
            model = arg
    calcF1Score(json, goldstandard, model)


if __name__ == "__main__":
    main(sys.argv[1:])
