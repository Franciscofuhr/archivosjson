from colorama import Fore, Style

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
                print(Fore.RED + "Error: Una de las notas no es un número válido." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Error: Faltan las columnas 'nota1' o 'nota2' en los datos." + Style.RESET_ALL)

    return promocionados, aprobados, aplazados

def ejecutar_opcion_cursada(opcion_cursada, lista_diccionarios):
    promocionados, aprobados, aplazados = clasificar_cursada(lista_diccionarios)

    if opcion_cursada == '1':
        print(Fore.YELLOW + "\n--- Promocionados ---" + Style.RESET_ALL)
        for alumno in promocionados:
            print(Fore.MAGENTA + f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: 1er Parcial: {alumno[3]} / 2do Parcial: {alumno[4]}" + Style.RESET_ALL)
    elif opcion_cursada == '2':
        print(Fore.YELLOW + "\n--- Aprobados ---" + Style.RESET_ALL)
        for alumno in aprobados:
            print(Fore.MAGENTA + f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: 1er Parcial: {alumno[3]} / 2do Parcial: {alumno[4]}" + Style.RESET_ALL)
    elif opcion_cursada == '3':
        print(Fore.YELLOW + "\n--- Aplazados ---" + Style.RESET_ALL)
        for alumno in aplazados:
            print(Fore.MAGENTA + f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: 1er Parcial: {alumno[3]} / 2do Parcial: {alumno[4]}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Opción no válida. Intenta nuevamente." + Style.RESET_ALL)
