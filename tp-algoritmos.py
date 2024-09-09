import csv

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

def mostrar_menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Parcial")
    print("2. Cursada")
    print("3. Salir")

def mostrar_menu_parcial():
    print("\n--- Parcial ---")
    print("1. 1er Parcial")
    print("2. 2do Parcial")

def mostrar_menu_aprobados_desaprobados():
    print("\n--- Opciones ---")
    print("1. Aprobados")
    print("2. Desaprobados")

def mostrar_menu_cursada():
    print("\n--- Cursada ---")
    print("1. Promocionado")
    print("2. Aprobado")
    print("3. Aplazado")

def ejecutar_opcion_parcial(opcion_parcial, lista_diccionarios):
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
    opcion_aprobado_desaprobado = input("Selecciona una opción (1, 2): ").lower()

    aprobados, desaprobados = clasificar_parcial(lista_diccionarios, parcial)

    if opcion_aprobado_desaprobado == '1':
        print(f"\n--- Aprobados {parcial_nombre} ---")
        for alumno in aprobados:
            print(f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: {alumno[3]}")
    elif opcion_aprobado_desaprobado == '2':
        print(f"\n--- Desaprobados {parcial_nombre} ---")
        for alumno in desaprobados:
            print(f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: {alumno[3]}")
    else:
        print("Opción no válida. Intenta nuevamente.")

def ejecutar_opcion_cursada(opcion_cursada, lista_diccionarios):
    promocionados, aprobados, aplazados = clasificar_cursada(lista_diccionarios)

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
    else:
        print("Opción no válida. Intenta nuevamente.")

def main():
    with open('archivosjson\datosAlumnos.csv', mode='r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv, delimiter=';')
        print("Encabezados del CSV:", lector_csv.fieldnames)  # Imprime los nombres de las columnas
        lista_diccionarios = [fila for fila in lector_csv]

    continuar = True
    while continuar:
        mostrar_menu_principal()
        opcion_principal = input("\nSelecciona una opción (1, 2, 3 para salir): ").lower()

        if opcion_principal == '3':
            print("Saliendo del programa.")
            continuar = False
        elif opcion_principal == '1':
            mostrar_menu_parcial()
            opcion_parcial = input("Selecciona una opción (1, 2): ").lower()
            ejecutar_opcion_parcial(opcion_parcial, lista_diccionarios)
        elif opcion_principal == '2':
            mostrar_menu_cursada()
            opcion_cursada = input("Selecciona una opción (1, 2, 3): ").lower()
            ejecutar_opcion_cursada(opcion_cursada, lista_diccionarios)
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
