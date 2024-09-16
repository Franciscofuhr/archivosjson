from colorama import Fore, Style

def mostrar_menu_aprobados_desaprobados():
    print(f"{Fore.YELLOW}\n--- Opciones ---{Style.RESET_ALL}")
    print(f"{Fore.CYAN}1. {Fore.RESET}Aprobados")
    print(f"{Fore.CYAN}2. {Fore.RESET}Desaprobados")

def clasificar_parcial(alumnos, parcial, nota_aprobacion=60):
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
    if opcion_parcial == '1':
        parcial = 'nota1'
        parcial_nombre = '1er Parcial'
    elif opcion_parcial == '2':
        parcial = 'nota2'
        parcial_nombre = '2do Parcial'
    else:
        print(Fore.RED + "Opción no válida. Intenta nuevamente." + Style.RESET_ALL)
        return

    mostrar_menu_aprobados_desaprobados()
    opcion_aprobado_desaprobado = input(Fore.GREEN + "Selecciona una opción (1, 2): " + Style.RESET_ALL).lower()

    aprobados, desaprobados = clasificar_parcial(lista_diccionarios, parcial)

    if opcion_aprobado_desaprobado == '1':
        print(Fore.GREEN + f"\n--- Aprobados {parcial_nombre} ---" + Style.RESET_ALL)
        for alumno in aprobados:
            print(Fore.MAGENTA + f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: {alumno[3]}" + Style.RESET_ALL)
    elif opcion_aprobado_desaprobado == '2':
        print(Fore.GREEN + f"\n--- Desaprobados {parcial_nombre} ---" + Style.RESET_ALL)
        for alumno in desaprobados:
            print(Fore.MAGENTA + f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: {alumno[3]}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Opción no válida. Intenta nuevamente." + Style.RESET_ALL)
