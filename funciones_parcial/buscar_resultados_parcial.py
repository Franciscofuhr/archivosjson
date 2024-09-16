from colorama import Fore, Style

def mostrar_menu_aprobados_desaprobados():
    print(f"{Fore.YELLOW}\n--- Opciones ---{Style.RESET_ALL}")
    print(f"{Fore.CYAN}1. {Fore.RESET}Aprobados")
    print(f"{Fore.CYAN}2. {Fore.RESET}Desaprobados")
    print(f"{Fore.CYAN}3. {Fore.RESET}Salir")

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
    bandera=True
    while bandera:
        if opcion_parcial == '1':
            parcial = 'nota1'
            parcial_nombre = '1er Parcial'
        elif opcion_parcial == '2':
            parcial = 'nota2'
            parcial_nombre = '2do Parcial'
        else:
            print(f"{Fore.RED}Opción no válida. Intenta nuevamente.")
            return

        mostrar_menu_aprobados_desaprobados()
    
        opcion_aprobado_desaprobado = input(f"{Fore.GREEN}Selecciona una opción (1, 2 o 3): ").lower()

        aprobados, desaprobados = clasificar_parcial(lista_diccionarios, parcial)
    
        
        if opcion_aprobado_desaprobado == '1':
            print(f"{Fore.YELLOW}\n--- Aprobados {parcial_nombre} ---")
            for alumno in aprobados:
               print(Fore.MAGENTA + f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: {alumno[3]}" + Style.RESET_ALL)
            continue
        elif opcion_aprobado_desaprobado == '2':
            print(f"{Fore.YELLOW}\n--- Desaprobados {parcial_nombre} ---")
            for alumno in desaprobados:
                print(Fore.MAGENTA + f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: {alumno[3]}" + Style.RESET_ALL)
            continue
        elif opcion_aprobado_desaprobado == '3':
            print(f"{Fore.RED}\n--- Saliendo... ---")
            bandera=False
            
        else:
           print(f"{Fore.RED}Opción no válida. Intenta nuevamente.")

