from colorama import Fore, Style

def buscar_alumno(lista_diccionarios):
    print(f"{Fore.YELLOW}--- Opciones de búsqueda ---{Style.RESET_ALL}")
    print(f"{Fore.CYAN}1. {Fore.RESET}Buscar por ID")
    print(f"{Fore.CYAN}2. {Fore.RESET}Buscar por Nombre")
    print(f"{Fore.CYAN}3. {Fore.RESET}Buscar por Apellido")
    
    opcion = input(Fore.GREEN + "Elige una opción (1, 2 o 3): " + Style.RESET_ALL)
    
    resultado = []
    
    if opcion == '1':
        id_alumno = input(Fore.CYAN + "Introduce el ID del alumno: " + Style.RESET_ALL)
        for persona in lista_diccionarios:
            if persona['Legajo'] == id_alumno:
                resultado.append(persona)
    
    elif opcion == '2':
        nombre = input(Fore.CYAN + "Introduce el nombre del alumno: " + Style.RESET_ALL)
        for persona in lista_diccionarios:
            if persona['Nombre'] == nombre:
                resultado.append(persona)
    
    elif opcion == '3':
        apellido = input(Fore.CYAN + "Introduce el apellido del alumno: " + Style.RESET_ALL)
        for persona in lista_diccionarios:
            if persona['Apellido'] == apellido:
                resultado.append(persona)
    
    else:
        print(Fore.RED + "Opción no válida" + Style.RESET_ALL)
        return
    
    # Imprimir resultado de la búsqueda
    if resultado:
        for persona in resultado:
            print(Fore.MAGENTA + f"Legajo: {persona['Legajo']}, {persona['Nombre']} {persona['Apellido']}: 1er Parcial: {persona['nota1']} / 2do Parcial: {persona['nota2']}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "No se encontraron coincidencias" + Style.RESET_ALL)
