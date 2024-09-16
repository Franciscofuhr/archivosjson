from variables_globales import NOTA_APROBACION
from colorama import Fore, Back, Style


def mostrar_menu_aprobados_desaprobados():
    print()
    print(f"{Back.WHITE + Fore.BLUE + Style.BRIGHT}--- Opciones ---")
    print()
    print(f"{Fore.CYAN}1. {Fore.RESET}Aprobados")
    print(f"{Fore.CYAN}2. {Fore.RESET}Desaprobados")
    print(f"{Fore.CYAN}3. {Fore.RESET}Volver al menu principal")
    print()


def clasificar_parcial(alumnos, parcial, nota_aprobacion):
    aprobados = []
    desaprobados = []

    for alumno in alumnos:
        legajo = alumno['Legajo']
        nombre = alumno['Nombre']
        apellido = alumno['Apellido']
        if parcial in alumno:
            nota = alumno[parcial]
            if nota.isdigit():
                nota = int(nota)
                if nota >= nota_aprobacion:
                    aprobados.append((legajo, nombre, apellido, nota))
                else:
                    desaprobados.append((legajo, nombre, apellido, nota))
            else:
                print(Fore.RED + f"Error: La nota '{nota}' no es un número válido." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Error: La columna '{parcial}' no existe en los datos." + Style.RESET_ALL)

    return aprobados, desaprobados


def ejecutar_opcion_parcial(opcion_parcial, lista_diccionarios):
    bandera = True
    while bandera:
        if opcion_parcial == '1':
            parcial = 'nota1'
            parcial_nombre = '1er Parcial'
        elif opcion_parcial == '2':
            parcial = 'nota2'
            parcial_nombre = '2do Parcial'
        elif opcion_parcial == '3':
            print()
            print(f"{Fore.RED + Style.BRIGHT}--- Volviendo al menú principal... ---")
            bandera = False
            continue
        else:
            print(f"{Fore.RED}Opción no válida. Intenta nuevamente.")
            return

        mostrar_menu_aprobados_desaprobados()

        opcion_aprobado_desaprobado = input(f"{Back.WHITE + Fore.BLUE + Style.BRIGHT}Selecciona una opción (1, 2 o 3): {Back.RESET + Fore.RESET + Style.RESET_ALL}").lower()

        aprobados, desaprobados = clasificar_parcial(lista_diccionarios, parcial, NOTA_APROBACION)

        if opcion_aprobado_desaprobado == '1':
            print()
            print(f"{Fore.GREEN + Style.BRIGHT}--- Aprobados {parcial_nombre} ---")
            print()
            for alumno in aprobados:
                print(Fore.GREEN + f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: {alumno[3]}" + Style.RESET_ALL)
            if len(aprobados) == 0:
                print(f"\n{Fore.RED}No hay alumnos aprobados.")
            continue
        elif opcion_aprobado_desaprobado == '2':
            print(f"{Fore.RED + Style.BRIGHT}\n--- Desaprobados {parcial_nombre} ---")
            print()
            for alumno in desaprobados:
                print(Fore.RED + f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: {alumno[3]}" + Style.RESET_ALL)
            if len(desaprobados) == 0:
                print(f"\n{Fore.RED}No hay alumnos desaprobados.")
            continue
        elif opcion_aprobado_desaprobado == '3':
            print()
            print(f"{Fore.RED + Style.BRIGHT}--- Volviendo al menu principal... ---")
            bandera = False

        else:
            print(f"{Fore.RED + Back.WHITE}Opción no válida. Intenta nuevamente.")
