import csv
import unittest
import os
from funciones_create.crear_alumno import agregar_fila_csv 

class TestCrearAlumno(unittest.TestCase):

    def setUp(self):
        self.ruta_archivo = 'C:/Users/lauta/OneDrive/Escritorio/archivosjson/datosAlumnos.csv'

    def test_agregar_fila_csv(self,):
        legajo = 9999
        nombre = "Test"
        apellido = "User "
        nota1 = 80
        nota2 = 90

        agregar_fila_csv(legajo, nombre, apellido, nota1, nota2)

        # Verificar que el alumno se haya agregado correctamente
        with open(self.ruta_archivo, mode='r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv, delimiter=';')
            next(lector_csv)  # Saltar el encabezado
            for fila in lector_csv:
                if fila[0] == str(legajo):
                    self.assertEqual(fila, [str(legajo), nombre, apellido, str(nota1), str(nota2)])
                    break

        self.eliminar_alumno(legajo)
        
    def test_agregar_legajo_duplicado(self):
        legajo = 8888
        nombre = "Test"
        apellido = "Duplciado"
        nota1 = 60
        nota2 = 80

        agregar_fila_csv(legajo, nombre, apellido, nota1, nota2)

        # Intentar agregar el mismo legajo
        with self.assertRaises(ValueError):
            agregar_fila_csv(legajo, "Otro Nombre", "Otro Apellido", 85, 95)
        
        self.eliminar_alumno(legajo)
        
    def test_agregar_alumno_con_datos_invalidos(self):
        legajo = 7777
        nombre = "Invalid"
        apellido = "User "
        
        # Notas fuera de rango
        nota1 = 110  
        nota2 = -10  

        with self.assertRaises(ValueError):
            agregar_fila_csv(legajo, nombre, apellido, nota1, nota2)

    # Eliminar alumno de prueba
    def eliminar_alumno(self, legajo_a_eliminar):
        filas_restantes = []
        with open(self.ruta_archivo, mode='r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv, delimiter=';')
            encabezado = next(lector_csv)  # Guardamos el encabezado
            filas_restantes.append(encabezado)
            for fila in lector_csv:
                if int(fila[0]) != legajo_a_eliminar:  # Agregamos las filas que no tienen el legajo a eliminar
                    filas_restantes.append(fila)

        # Si se eliminó alguna fila, reescribimos el archivo
        with open(self.ruta_archivo, mode='w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=';')
            writer.writerows(filas_restantes)  # Escribimos el csv

