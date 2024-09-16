def buscar_alumno(lista_diccionarios):
    bandera_principal = True

    while bandera_principal:
        print("Opciones de búsqueda:")
        print("1. Buscar por ID")
        print("2. Buscar por Nombre")
        print("3. Buscar por Apellido")
        print("4. Volver al menú principal")
        
        opcion = input("Elige una opción (1, 2, 3 o 4 para volver al menú principal): ")

        if opcion == '4':
            print("Volviendo al menú principal...")
            bandera_principal = False
            continue
        
        resultado = []
        bandera_busqueda = True
        
        while bandera_busqueda:
            if opcion == '1':
                id_alumno = input("Introduce el ID del alumno o -1 para regresar al menú de búsqueda: ")
                if id_alumno == '-1':
                    print("Volviendo al menú de búsqueda...")
                    bandera_busqueda = False
                    continue  
                for persona in lista_diccionarios:
                    if persona['Legajo'] == id_alumno:
                        resultado.append(persona)
            
            elif opcion == '2':
                nombre = input("Introduce el nombre del alumno o -1 para regresar al menú de búsqueda: ")
                if nombre == '-1':
                    print("Volviendo al menú de búsqueda...")
                    bandera_busqueda = False
                    continue  
                for persona in lista_diccionarios:
                    if persona['Nombre'] == nombre:
                        resultado.append(persona)
            
            elif opcion == '3':
                apellido = input("Introduce el apellido del alumno o -1 para regresar al menú de búsqueda: ")
                if apellido == '-1':
                    print("Volviendo al menú de búsqueda...")
                    bandera_busqueda = False
                    continue  
                for persona in lista_diccionarios:
                    if persona['Apellido'] == apellido:
                        resultado.append(persona)
            
            else:
                print("Opción no válida.")
                bandera_busqueda = False
                continue

            # Imprimir resultado de la búsqueda
            if resultado:
                for persona in resultado:
                    print(f"Legajo: {persona['Legajo']}, {persona['Nombre']} {persona['Apellido']}: 1er Parcial: {persona['nota1']} / 2do Parcial: {persona['nota2']}")
            else:
                print("No se encontraron coincidencias")
            print("")

