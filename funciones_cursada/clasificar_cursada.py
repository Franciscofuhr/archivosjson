from variables_globales import NOTA_APROBACION, NOTA_PROMOCION
from colorama import Fore, Style


def clasificar_cursada(alumnos, nota_aprobacion, nota_promocion):
    promocionados = []
    aprobados = []
    aplazados = []

    for alumno in alumnos:
        legajo = alumno['Legajo']
        nombre = alumno['Nombre']
        apellido = alumno['Apellido']
        if 'nota1' in alumno and 'nota2' in alumno:
            nota1 = alumno['nota1']
            nota2 = alumno['nota2']
            if nota1.isdigit() and nota2.isdigit():
                nota1 = int(nota1)
                nota2 = int(nota2)
                if nota1 >= nota_promocion and nota2 >= nota_promocion:
                    promocionados.append((legajo, nombre, apellido, nota1, nota2))
                elif nota1 >= nota_aprobacion and nota2 >= nota_aprobacion:
                    aprobados.append((legajo, nombre, apellido, nota1, nota2))
                else:
                    aplazados.append((legajo, nombre, apellido, nota1, nota2))
            else:
                print(Fore.RED + "Error: Una de las notas no es un número válido." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Error: Faltan las columnas 'nota1' o 'nota2' en los datos." + Style.RESET_ALL)

    return promocionados, aprobados, aplazados

def ejecutar_opcion_cursada(lista_diccionarios):
    promocionados, aprobados, aplazados = clasificar_cursada(lista_diccionarios, NOTA_APROBACION, NOTA_PROMOCION)
    bandera = True
    while bandera:
        print(f"\n{Fore.YELLOW}--- Cursada ---")
        print(f"{Fore.CYAN}1. {Fore.RESET}Ver Promocionados")
        print(f"{Fore.CYAN}2. {Fore.RESET}Ver Aprobados")
        print(f"{Fore.CYAN}3. {Fore.RESET}Ver Aplazados")
        print(f"{Fore.CYAN}4. {Fore.RESET}Volver al menú principal")
        
        opcion_cursada = input(f"{Fore.GREEN}Selecciona una opción (1, 2, 3, 4 para salir): ").lower()

        if opcion_cursada == '1':
            print(f"\n{Fore.YELLOW}--- Promocionados ---")
            for alumno in promocionados:
                print(Fore.MAGENTA + f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: 1er Parcial: {alumno[3]} / 2do Parcial: {alumno[4]}" + Style.RESET_ALL)
            if len(promocionados) == 0:
                print(f"\n{Fore.RED}No hay alumnos promocionados.")
        elif opcion_cursada == '2':
            print(f"\n{Fore.YELLOW}--- Aprobados ---")
            for alumno in aprobados:
                print(Fore.MAGENTA + f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: 1er Parcial: {alumno[3]} / 2do Parcial: {alumno[4]}" + Style.RESET_ALL)
            if len(aprobados) == 0:
                print(f"\n{Fore.RED}No hay alumnos aprobados.")
        elif opcion_cursada == '3':
            print(f"\n{Fore.YELLOW}--- Aplazados ---")
            for alumno in aplazados:
                print(Fore.MAGENTA + f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: 1er Parcial: {alumno[3]} / 2do Parcial: {alumno[4]}" + Style.RESET_ALL)
            if len(aplazados) == 0:
                print(f"\n{Fore.RED}No hay alumnos aplazados.")
        elif opcion_cursada == '4':
            print(f"\n{Fore.YELLOW}--- Volviendo al menú principal... ---")
            bandera = False 
        else:
            print(f"\n{Fore.RED}Opción no válida. Intenta nuevamente.")
