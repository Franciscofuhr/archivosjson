import csv
import os

def modificar_fila_csv(legajo_a_modificar, nuevo_nombre=None, nuevo_apellido=None, nueva_nota1=None, nueva_nota2=None):
    ruta_archivo = 'archivosjson\\datosAlumnos.csv'
    
    if not os.path.exists(ruta_archivo):
        print("El archivo no existe.")
        return

    fila_modificada = False

    # Leer todas las filas y modificar la que coincide con el legajo dado
    filas_actualizadas = []
    with open(ruta_archivo, mode='r', newline='') as archivo_csv:
        reader = csv.reader(archivo_csv, delimiter=';')
        encabezado = next(reader)  # Guardamos el encabezado
        filas_actualizadas.append(encabezado)  # Lo agregamos para reescribirlo luego
        for fila in reader:
            if int(fila[0]) == legajo_a_modificar:
                # Modificamos los campos de la fila según los nuevos valores dados
                fila[1] = nuevo_nombre if nuevo_nombre is not None else fila[1]
                fila[2] = nuevo_apellido if nuevo_apellido is not None else fila[2]
                fila[3] = nueva_nota1 if nueva_nota1 is not None else fila[3]
                fila[4] = nueva_nota2 if nueva_nota2 is not None else fila[4]
                fila_modificada = True
            filas_actualizadas.append(fila)

    # Si se encontró y modificó la fila, reescribimos el archivo
    if fila_modificada:
        with open(ruta_archivo, mode='w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=';')
            writer.writerows(filas_actualizadas)  # Escribimos todas las filas actualizadas
        print(f"Registro con legajo {legajo_a_modificar} modificado.")
    else:
        print(f"No se encontró ningún registro con legajo {legajo_a_modificar}.")

# Ejemplo de uso
#modificar_fila_csv(243, nuevo_nombre='Luis', nueva_nota1=85)