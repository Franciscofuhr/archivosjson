import os
import unittest
import csv
from funciones_update.funciones_update import modificar_fila_csv
from funciones_create.crear_alumno import agregar_fila_csv

class TestActualizarAlumno(unittest.TestCase):

    def test_actualizar_alumno_existente(self):
        agregar_fila_csv(9999, 'Juan', 'Pérez', 80, 90)
        nuevos_datos = ['9999', 'Juan', 'Pérez', 85, 95]
        modificar_fila_csv(9999, nuevos_datos)

        with open("C:/Users/lauta/OneDrive/Escritorio/archivosjson/datosAlumnos.csv", mode='r') as file:
            reader = csv.reader(file, delimiter=';') 
            rows = list(reader)
        
        # Verifica que la fila actualizada esté presente en el archivo
        self.assertIn(nuevos_datos, rows)