import csv

with open('archivosjson/datosAlumnos.csv', mode='r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv, delimiter=';')  # Delimitador es una coma
    lista_diccionarios = [fila for fila in lector_csv]
for persona in lista_diccionarios:
    print(persona['Nombre'])

## funcion que lee las llaves de la lista

def leer_llaves_diccionario(diccionario):
    for persona in diccionario:
     print(persona.keys())


# Función para buscar por ID, Nombre o Apellido
def buscar_alumno(lista_diccionarios):
    print("Opciones de búsqueda:")
    print("1. Buscar por ID")
    print("2. Buscar por Nombre")
    print("3. Buscar por Apellido")
    
    opcion = input("Elige una opción (1, 2 o 3): ")
    
    resultado = []
    
    if opcion == '1':
        id_alumno = input("Introduce el ID del alumno: ")
        for persona in lista_diccionarios:
            if persona['ID Alumno'] == id_alumno:
                resultado.append(persona)
    
    elif opcion == '2':
        nombre = input("Introduce el nombre del alumno: ")
        for persona in lista_diccionarios:
            if persona['Nombre'] == nombre:
                resultado.append(persona)
    
    elif opcion == '3':
        apellido = input("Introduce el apellido del alumno: ")
        for persona in lista_diccionarios:
            if persona['Apellido'] == apellido:
                resultado.append(persona)
    
    else:
        print("Opción no válida")
        return
    
    # Imprimir resultado de la búsqueda
    if resultado:
        for persona in resultado:
            print(f"ID: {persona['ID Alumno']}, Nombre: {persona['Nombre']}, Apellido: {persona['Apellido']}, P1: {persona['P1']}, P2: {persona['P2']}")
    else:
        print("No se encontraron coincidencias")

    



leer_llaves_diccionario(lista_diccionarios)
print("mati branch")

buscar_alumno(lista_diccionarios)