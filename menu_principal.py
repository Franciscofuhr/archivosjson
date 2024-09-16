import csv
import colorama
from colorama import Fore, Style
from funciones_parcial.buscar_resultados_parcial import ejecutar_opcion_parcial
from funciones_alumnos.buscar_alumnos import buscar_alumno
from funciones_cursada.clasificar_cursada import ejecutar_opcion_cursada

colorama.init(autoreset=True)  # Inicializar colorama con auto-reset para no acumular estilos

def mostrar_menu_principal():
    print(f"\n{Fore.YELLOW}--- Menú Principal ---")
    print(f"{Fore.CYAN}1. {Fore.RESET}Parcial")
    print(f"{Fore.CYAN}2. {Fore.RESET}Cursada")
    print(f"{Fore.CYAN}3. {Fore.RESET}Alumno")
    print(f"{Fore.CYAN}4. {Fore.RESET}Salir")

def mostrar_menu_parcial():
    print(f"\n{Fore.YELLOW}--- Parcial ---")
    print(f"{Fore.CYAN}1. {Fore.RESET}1er Parcial")
    print(f"{Fore.CYAN}2. {Fore.RESET}2do Parcial")

def mostrar_menu_cursada():
    print(f"\n{Fore.YELLOW}--- Cursada ---")
    print(f"{Fore.CYAN}1. {Fore.RESET}Promocionado")
    print(f"{Fore.CYAN}2. {Fore.RESET}Aprobado")
    print(f"{Fore.CYAN}3. {Fore.RESET}Aplazado")

def main():
    with open('archivosjson\datosAlumnos.csv', mode='r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv, delimiter=';')
        print(f"{Fore.GREEN}Encabezados del CSV: {Fore.RESET}{lector_csv.fieldnames}")  # Encabezados en verde
        lista_diccionarios = [fila for fila in lector_csv]

    continuar = True
    while continuar:
        mostrar_menu_principal()
        opcion_principal = input(f"\n{Fore.GREEN}Selecciona una opción (1, 2, 3, 4 para salir): {Fore.RESET}").lower()

        if opcion_principal == '4':
            print(f"{Fore.RED}Saliendo del programa.")
            continuar = False
        elif opcion_principal == '1':
            mostrar_menu_parcial()
            opcion_parcial = input(f"{Fore.GREEN}Selecciona una opción (1, 2): {Fore.RESET}").lower()
            ejecutar_opcion_parcial(opcion_parcial, lista_diccionarios)
        elif opcion_principal == '2':
            mostrar_menu_cursada()
            opcion_cursada = input(f"{Fore.GREEN}Selecciona una opción (1, 2, 3): {Fore.RESET}").lower()
            ejecutar_opcion_cursada(opcion_cursada, lista_diccionarios)
        elif opcion_principal == '3':
            buscar_alumno(lista_diccionarios)
        else:
            print(f"{Fore.RED}Opción no válida. Intenta nuevamente.")
