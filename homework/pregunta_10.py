"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    resultado = []

    with open("files/input/data.csv", "r") as file:
        for line in file:
            valores = line.strip().split("\t")
            letra = valores[0]
            elementos_columna4 = len(valores[3].split(","))  
            elementos_columna5 = len(valores[4].split(","))

            resultado.append((letra, elementos_columna4, elementos_columna5))

    return resultado
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
