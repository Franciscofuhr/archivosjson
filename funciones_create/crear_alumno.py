import csv

def agregar_fila_csv(legajo, nombre, apellido, nota1, nota2):
    # Crea el archivo CSV si no existe, agregando el encabezado
    try:
        with open('C:/Users/lauta/OneDrive/Escritorio/archivosjson/datosAlumnos.csv', mode='x', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=';')
            # Escribe la primera línea con el encabezado
            writer.writerow(['Legajo', 'Nombre', 'Apellido', 'nota1', 'nota2'])
    except FileExistsError:
        # Si el archivo ya existe, pasamos
        pass
    
       
    with open('C:/Users/lauta/OneDrive/Escritorio/archivosjson/datosAlumnos.csv', mode='r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=';')
        next(lector_csv)  # Saltar el encabezado
        for fila in lector_csv:
            if fila[0] == str(legajo):
                raise ValueError(f"El legajo {legajo} ya existe.")

    # Agrega la fila al archivo
    with open('C:/Users/lauta/OneDrive/Escritorio/archivosjson/datosAlumnos.csv', mode='a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv, delimiter=';')
        writer.writerow([legajo, nombre, apellido, nota1, nota2])
        return [legajo, nombre, apellido, nota1, nota2]