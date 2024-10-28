import csv

def agregar_fila_csv(legajo, nombre, apellido, nota1, nota2):
    # Crea el archivo CSV si no existe, agregando el encabezado
    try:
        with open('archivosjson-master\\archivosjson-master\\datosAlumnos.csv', mode='x', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=';')
            # Escribe la primera línea con el encabezado
            writer.writerow(['Legajo', 'Nombre', 'Apellido', 'nota1', 'nota2'])
    except FileExistsError:
        # Si el archivo ya existe, pasamos
        pass

    # Agrega la fila al archivo
    with open('archivosjson-master\\archivosjson-master\\datosAlumnos.csv', mode='a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv, delimiter=';')
        writer.writerow([legajo, nombre, apellido, nota1, nota2])
        return [legajo, nombre, apellido, nota1, nota2]

print(agregar_fila_csv( 243, 'Pedro', 'ka', 90, 80))