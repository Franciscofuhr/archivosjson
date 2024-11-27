import csv
import os

def eliminar_fila_csv(legajo_a_eliminar):
    ruta_archivo = 'archivosjson\\datosAlumnos.csv'
    
    # Verificamos si el archivo existe
    if not os.path.exists(ruta_archivo):
        print("El archivo no existe.")
        return

    # Bandera para verificar si se eliminó alguna fila
    fila_eliminada = False

    # Leemos todas las filas y excluimos solo la que tiene el legajo a eliminar
    filas_restantes = []
    with open(ruta_archivo, mode='r', newline='') as archivo_csv:
        reader = csv.reader(archivo_csv, delimiter=';')
        encabezado = next(reader)  # Guardamos el encabezado
        filas_restantes.append(encabezado)  # Lo agregamos para reescribirlo luego
        for fila in reader:
            if int(fila[0]) == legajo_a_eliminar:  # Compara el legajo
                fila_eliminada = True  # Marca que se encontró y eliminó
            else:
                filas_restantes.append(fila)  # Mantiene las filas que no se eliminan

    # Si se eliminó alguna fila, reescribimos el archivo
    if fila_eliminada:
        with open(ruta_archivo, mode='w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=';')
            writer.writerows(filas_restantes)  # Escribimos todas las filas restantes
        return True
    else:
        return False
        
