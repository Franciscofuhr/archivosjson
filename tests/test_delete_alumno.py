import csv
import unittest
from funciones_delete.eliminar_alumno import eliminar_fila_csv
from funciones_create.crear_alumno import agregar_fila_csv

class TestEliminarAlumno(unittest.TestCase):
    def setUp(self):
        self.ruta_archivo = '/archivosjson/datosAlumnos.csv'
        
    # Eliminar alumno existente
    def test_eliminar_alumno_existente(self):
        legajo = 9999
        nombre = "Fran"
        apellido = "Barite"
        nota1= 50
        nota2 = 60
        
        agregar_fila_csv(legajo,nombre,apellido,nota1,nota2)
        
        eliminar_fila_csv(9999)
        
        with open('/datosAlumnos.csv', mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader) # obtener la lista de alumnos
        
        assert ['9999', 'Fran', 'Barite', 50, 60] not in rows
    
    
    # Eliminar un alumno que no existe
    def test_eliminar_alumno_no_existente(self):
        
        with self.assertRaises(ValueError):
            eliminar_fila_csv(999999999999999999)
        
