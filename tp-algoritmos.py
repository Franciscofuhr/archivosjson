import csv

with open('datosAlumnos.csv', mode='r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv, delimiter=';')  # Delimitador es una coma
    lista_diccionarios = [fila for fila in lector_csv]
for persona in lista_diccionarios:
    print(persona['Nombre'])

## funcion que lee las llaves de la lista

def leer_llaves_diccionario(diccionario):
    for persona in diccionario:
     print(persona.keys())

leer_llaves_diccionario(lista_diccionarios)