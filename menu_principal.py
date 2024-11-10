import csv
import colorama
from colorama import Fore, Back, Style
from funciones_parcial.buscar_resultados_parcial import ejecutar_opcion_parcial
from funciones_alumno.buscar_alumnos import buscar_alumno
from funciones_cursada.clasificar_cursada import ejecutar_opcion_cursada

# Inicializar colorama con auto-reset para no acumular estilos
colorama.init(autoreset=True)


def mostrar_menu_principal():
    print(f"\n{Back.WHITE + Fore.BLUE + Style.BRIGHT}--- Programa de Notas Estudiantiles---")
    print(f"\n{Back.WHITE + Fore.BLUE + Style.BRIGHT}--- Menú Principal ---")
    print()
    print(f"{Fore.BLUE}1. {Fore.WHITE}Notas de Parciales")
    print(f"{Fore.BLUE}2. {Fore.WHITE}Estado de Cursada")
    print(f"{Fore.BLUE}3. {Fore.WHITE}Busqueda de Alumnos")
    print(f"{Fore.BLUE}4. {Fore.WHITE}Salir del programa")


def mostrar_menu_parcial():
    print(f"\n{Back.WHITE + Fore.BLUE + Style.BRIGHT}--- Notas de Parciales ---")
    print(f"\n{Back.WHITE + Fore.BLUE + Style.BRIGHT}--- Seleccione un parcial ---")
    print()
    print(f"{Fore.BLUE}1. {Fore.RESET}1er Parcial")
    print(f"{Fore.BLUE}2. {Fore.RESET}2do Parcial")
    print(f"{Fore.BLUE}3. {Fore.RESET}Volver al menu principal")
    print()


def main():
    with open('D:/archivosjson/datosAlumnos.csv', mode='r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv, delimiter=';')
        lista_diccionarios = [fila for fila in lector_csv]

    continuar = True
    while continuar:
        mostrar_menu_principal()
        opcion_principal = input(f"\n{Back.WHITE + Fore.BLUE + Style.BRIGHT}Selecciona una opción: {Fore.RESET + Back.RESET}").lower()

        if opcion_principal == '4':
            print(f"{Fore.RED + Back.RESET}Saliendo del programa.")
            continuar = False
        elif opcion_principal == '1':
            mostrar_menu_parcial()
            opcion_parcial = input(f"{Back.WHITE + Fore.BLUE + Style.BRIGHT}Selecciona una opción (1, 2 o 3): {Fore.RESET + Back.RESET}").lower()
            ejecutar_opcion_parcial(opcion_parcial, lista_diccionarios)
        elif opcion_principal == '2':
            ejecutar_opcion_cursada(lista_diccionarios)
        elif opcion_principal == '3':
            buscar_alumno(lista_diccionarios)
        else:
            print(f"{Fore.RED}Opción no válida. Intenta nuevamente.")
