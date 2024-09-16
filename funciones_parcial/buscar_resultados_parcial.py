def mostrar_menu_aprobados_desaprobados():
    print("\n--- Opciones ---")
    print("1. Aprobados")
    print("2. Desaprobados")
    print("3. Salir")

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
                print(f"Error: La nota '{nota}' no es un número válido.")
        else:
            print(f"Error: La columna '{parcial}' no existe en los datos.")

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
            print("Opción no válida. Intenta nuevamente.")
            return

        mostrar_menu_aprobados_desaprobados()
    
        opcion_aprobado_desaprobado = input("Selecciona una opción (1, 2 o 3): ").lower()

        aprobados, desaprobados = clasificar_parcial(lista_diccionarios, parcial)
    
        
        if opcion_aprobado_desaprobado == '1':
            print(f"\n--- Aprobados {parcial_nombre} ---")
            for alumno in aprobados:
                print(f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: {alumno[3]}")
            continue
        elif opcion_aprobado_desaprobado == '2':
            print(f"\n--- Desaprobados {parcial_nombre} ---")
            for alumno in desaprobados:
                print(f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: {alumno[3]}")
            continue
        elif opcion_aprobado_desaprobado == '3':
            print(f"\n--- Saliendo... ---")
            bandera=False
            
        else:
            print("Opción no válida. Intenta nuevamente.")

