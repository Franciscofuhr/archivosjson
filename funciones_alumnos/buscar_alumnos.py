def buscar_alumno(lista_diccionarios):
    print("Opciones de búsqueda:")
    print("1. Buscar por ID")
    print("2. Buscar por Nombre")
    print("3. Buscar por Apellido")
    
    opcion = input("Elige una opción (1, 2 o 3): ")
    
    resultado = []
    
    if opcion == '1':
        id_alumno = input("Introduce el ID del alumno: ")
        for persona in lista_diccionarios:
            if persona['Legajo'] == id_alumno:
                resultado.append(persona)
    
    elif opcion == '2':
        nombre = input("Introduce el nombre del alumno: ")
        for persona in lista_diccionarios:
            if persona['Nombre'] == nombre:
                resultado.append(persona)
    
    elif opcion == '3':
        apellido = input("Introduce el apellido del alumno: ")
        for persona in lista_diccionarios:
            if persona['Apellido'] == apellido:
                resultado.append(persona)
    
    else:
        print("Opción no válida")
        return
    
    # Imprimir resultado de la búsqueda
    if resultado:
        for persona in resultado:
            print(f"Legajo: {persona['Legajo']}, {persona['Nombre']} {persona['Apellido']}: 1er Parcial: {persona['nota1']} / 2do Parcial: {persona['nota2']}")
    else:
        print("No se encontraron coincidencias")
