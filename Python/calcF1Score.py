import json
import os

from prettytable import PrettyTable


def calcF1Score(modelo, compared):
    myTable = PrettyTable(["Model name", "Precision", "Recall", "F1-score"])
    # Donde estan los json buenos
    res = 0
    total = 0
    total2 = 0
    nombre_modelo = modelo.split("/")
    nombre_modelo = nombre_modelo[-2]

    # Hago un bucle para abrir de uno en uno los archivos
    for k in os.listdir(modelo):
        # Abrimos el json
        f = open(modelo + k)
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

    # print("El modelo ha detectado " + str(total) + " elementos")
    # print("Hay que encontrar " + str(total2) + " elementos")
    # print("De los resultados obtenidos " + str(res) + " estan bien")

    falsos_positivos = total - res
    falsos_negativos = total2 - res

    precision = res / (res + falsos_positivos)
    recall = res / (res + falsos_negativos)
    f1Score = 2 * ((precision * recall) / (precision + recall))

    # print("La precision del modelo es: " + str(precision))
    # print("El recall del modelo es: " + str(recall))
    # print("La f1-score obtenida por el modelo es: " + str(f1Score))

    myTable.add_row(
        [nombre_modelo, round(precision, 2), round(recall, 2), round(f1Score, 2)]
    )
    print(myTable)
