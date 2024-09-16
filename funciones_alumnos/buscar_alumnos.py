from colorama import Fore, Style


def buscar_alumno(lista_diccionarios):
    bandera_principal = True

    while bandera_principal:
        print(f"{Fore.YELLOW}--- Opciones de búsqueda ---{Style.RESET_ALL}")
        print(f"{Fore.CYAN}1. {Fore.RESET}Buscar por ID")
        print(f"{Fore.CYAN}2. {Fore.RESET}Buscar por Nombre")
        print(f"{Fore.CYAN}3. {Fore.RESET}Buscar por Apellido")
        opcion = input(f"{Fore.GREEN}Elige una opción (1, 2, 3 o 4 para volver al menú principal): ")

        if opcion == '4':
            print(f"{Fore.YELLOW}Volviendo al menú principal...{Style.RESET_ALL}")
            bandera_principal = False
            continue

        resultado = None
        bandera_busqueda = True

        while bandera_busqueda:
            if opcion == '1':
                id_alumno = input(f"{Fore.CYAN}Introduce el ID del alumno o -1 para regresar al menú de búsqueda: ")
                if id_alumno == '-1':
                    print(f"{Fore.YELLOW}Volviendo al menú de búsqueda...")
                    bandera_busqueda = False
                    continue

                for persona in lista_diccionarios:
                    if persona['Legajo'] == id_alumno:
                        resultado = persona

            elif opcion == '2':
                nombre = input(f"{Fore.CYAN}Introduce el nombre del alumno o -1 para regresar al menú de búsqueda: ")
                if nombre == '-1':
                    print(f"{Fore.YELLOW}Volviendo al menú de búsqueda...")
                    bandera_busqueda = False
                    continue
                for persona in lista_diccionarios:
                    if persona['Nombre'] == nombre:
                        resultado = persona

            elif opcion == '3':
                apellido = input(f"{Fore.CYAN}Introduce el apellido del alumno o -1 para regresar al menú de búsqueda: ")
                if apellido == '-1':
                    print(f"{Fore.YELLOW}Volviendo al menú de búsqueda...")
                    bandera_busqueda = False
                    continue
                for persona in lista_diccionarios:
                    if persona['Apellido'] == apellido:
                        resultado = persona

            else:
                print(f"{Fore.YELLOW}Opción no válida.")
                bandera_busqueda = False
                continue

            # Imprimir resultado de la búsqueda
            if resultado:
                print(f"{Fore.MAGENTA}Legajo: {resultado['Legajo']}, {resultado['Nombre']} {resultado['Apellido']}: 1er Parcial: {resultado['nota1']} / 2do Parcial: {resultado['nota2']}")
            else:
                print(f"{Fore.RED}No se encontraron coincidencias")
            resultado = None
            print("")
