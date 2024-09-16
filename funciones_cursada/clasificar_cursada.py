def clasificar_cursada(alumnos, nota_aprobacion=40, nota_promocion=80):
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
                print(f"Error: Una de las notas no es un número válido.")
        else:
            print(f"Error: Faltan las columnas 'nota1' o 'nota2' en los datos.")

    return promocionados, aprobados, aplazados

def ejecutar_opcion_cursada(lista_diccionarios):
    promocionados, aprobados, aplazados = clasificar_cursada(lista_diccionarios)
    bandera = True
    while bandera:
        print("\n--- Opciones de Cursada ---")
        print("1. Ver Promocionados")
        print("2. Ver Aprobados")
        print("3. Ver Aplazados")
        print("4. Volver al menú principal")
        
        opcion_cursada = input("Selecciona una opción (1, 2, 3, 4 para salir): ").lower()

        if opcion_cursada == '1':
            print("\n--- Promocionados ---")
            for alumno in promocionados:
                print(f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: 1er Parcial: {alumno[3]} / 2do Parcial: {alumno[4]}")
        elif opcion_cursada == '2':
            print("\n--- Aprobados ---")
            for alumno in aprobados:
                print(f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: 1er Parcial: {alumno[3]} / 2do Parcial: {alumno[4]}")
        elif opcion_cursada == '3':
            print("\n--- Aplazados ---")
            for alumno in aplazados:
                print(f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: 1er Parcial: {alumno[3]} / 2do Parcial: {alumno[4]}")
                
        elif opcion_cursada == '4':
            print("\n--- Volviendo al menú principal... ---")
            bandera = False 
        else:
            print("Opción no válida. Intenta nuevamente.")