import csv 
from funciones_parcial.buscar_resultados_parcial import ejecutar_opcion_parcial
from funciones_alumnos.buscar_alumnos import buscar_alumno
from funciones_cursada.clasificar_cursada import ejecutar_opcion_cursada

def mostrar_menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Parcial")
    print("2. Cursada")
    print("3. Alumno")
    print("4. Salir")

def mostrar_menu_parcial():
    print("\n--- Parcial ---")
    print("1. 1er Parcial")
    print("2. 2do Parcial")
    

def mostrar_menu_cursada():
    print("\n--- Cursada ---")
    print("1. Promocionado")
    print("2. Aprobado")
    print("3. Aplazado")

def main():
    with open('datosAlumnos.csv', mode='r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv, delimiter=';')
        print("Encabezados del CSV:", lector_csv.fieldnames)  # Imprime los nombres de las columnas
        lista_diccionarios = [fila for fila in lector_csv]

    continuar = True
    while continuar:
        mostrar_menu_principal()
        opcion_principal = input("\nSelecciona una opción (1, 2, 3, 4 para salir): ").lower()

        if opcion_principal == '4':
            print("Saliendo del programa.")
            continuar = False
        elif opcion_principal == '1':
            mostrar_menu_parcial()
            opcion_parcial = input("Selecciona una opción (1, 2): ").lower()
            ejecutar_opcion_parcial(opcion_parcial, lista_diccionarios)
        elif opcion_principal == '2':
            mostrar_menu_cursada()
            ejecutar_opcion_cursada( lista_diccionarios)
        elif opcion_principal == '3':
            buscar_alumno(lista_diccionarios)
        else:
            print("Opción no válida. Intenta nuevamente.")