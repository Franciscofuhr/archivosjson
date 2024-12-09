import os
import unittest
import csv
from funciones_update.funciones_update import modificar_fila_csv
from funciones_create.crear_alumno import agregar_fila_csv
from funciones_delete.eliminar_alumno import eliminar_fila_csv

class TestActualizarAlumno(unittest.TestCase):
    
    
    def test_actualizar_alumno_existente(self):

        agregar_fila_csv(9999, 'Juan', 'Pérez', 80, 90)

        modificar_fila_csv(9999, nuevo_nombre="aaaaaaaaaaaaa", nuevo_apellido="Carnuccio", nueva_nota1=70, nueva_nota2=80)

        # traer datos del csv
        with open('/datosAlumnos.csv', mode='r') as file:
            reader = csv.reader(file, delimiter=';') 
            lista = list(reader)

        # Buscar la fila que corresponde al legajo 9999
        fila_actualizada = None
        for fila in lista:
            if fila[1] == 'aaaaaaaaaaaaa':  
                fila_actualizada = fila
                break

        # Verificar que la fila actualizada contenga los nuevos datos
        self.assertEqual(fila_actualizada[1], 'aaaaaaaaaaaaa', "El nombre no se actualizó correctamente.")
        self.assertEqual(fila_actualizada[2], 'Carnuccio', "El nombre no se actualizó correctamente.")
        self.assertEqual(fila_actualizada[3], '70', "La nota1 no se actualizó correctamente.")
        self.assertEqual(fila_actualizada[4], '80', "La nota1 no se actualizó correctamente.")
        
        eliminar_fila_csv(9999)

    def test_actualizar_alumno_no_existente(self):
        with self.assertRaises(ValueError) as context:
            modificar_fila_csv(1111111111111111, nuevo_nombre="Francisco")

        # Verifica que el mensaje de error sea el esperado
        self.assertEqual(str(context.exception), "No se encontró ningún alumno con ese legajo.")
        
