from colorama import Fore, Back, Style


def buscar_alumno(lista_diccionarios):
    bandera_principal = True

    while bandera_principal:
        print(f"\n{Back.WHITE + Fore.BLUE}--- Opciones de búsqueda ---{Back.RESET}\n")
        print(f"{Fore.CYAN}1. {Fore.RESET}Buscar por ID")
        print(f"{Fore.CYAN}2. {Fore.RESET}Buscar por Nombre")
        print(f"{Fore.CYAN}3. {Fore.RESET}Buscar por Apellido")
        print(f"{Fore.CYAN}4. {Fore.RESET}Volver al menu principal")
        opcion = input(f"\n{Back.WHITE + Fore.BLUE}Elige una opción (1, 2, 3 o 4 para volver al menú principal): {Back.RESET}")

        if opcion == '4':
            print(f"\n{Fore.RED + Style.BRIGHT}Volviendo al menú principal...")
            bandera_principal = False
            continue

        resultado = None
        bandera_busqueda = True

        while bandera_busqueda:
            if opcion == '1':
                id_alumno = input(f"\n{Back.WHITE + Fore.BLUE}Introduce el ID del alumno o -1 para regresar al menú de búsqueda: {Back.RESET}")
                if id_alumno == '-1':
                    print(f"\n{Fore.RED + Style.BRIGHT}Volviendo al menú de búsqueda...")
                    bandera_busqueda = False
                    continue

                for persona in lista_diccionarios:
                    if persona['Legajo'] == id_alumno:
                        resultado = persona

            elif opcion == '2':
                nombre = input(f"\n{Back.WHITE + Fore.BLUE}Introduce el nombre del alumno o -1 para regresar al menú de búsqueda: {Back.RESET}")
                if nombre == '-1':
                    print(f"{Fore.RED + Style.BRIGHT}Volviendo al menú de búsqueda...")
                    bandera_busqueda = False
                    continue
                for persona in lista_diccionarios:
                    if persona['Nombre'].lower() == nombre:
                        resultado = persona

            elif opcion == '3':
                apellido = input(f"\n{Back.WHITE + Fore.BLUE}Introduce el apellido del alumno o -1 para regresar al menú de búsqueda: {Back.RESET}")
                if apellido == '-1':
                    print(f"\n{Fore.RED + Style.BRIGHT}Volviendo al menú de búsqueda...")
                    bandera_busqueda = False
                    continue
                for persona in lista_diccionarios:
                    if persona['Apellido'].lower() == apellido:
                        resultado = persona

            else:
                print(f"{Fore.RED}Opción no válida.")
                bandera_busqueda = False
                continue

            # Imprimir resultado de la búsqueda
            if resultado:
                print(f"\n{Fore.YELLOW}Legajo: {resultado['Legajo']}, {resultado['Nombre']} {resultado['Apellido']}: 1er Parcial: {resultado['nota1']} / 2do Parcial: {resultado['nota2']}")
            else:
                print(f"{Fore.RED}No se encontraron coincidencias")
            resultado = None
            print("")
