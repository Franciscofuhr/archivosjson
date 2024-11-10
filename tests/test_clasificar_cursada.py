import pytest
from io import StringIO
from unittest.mock import patch
from funciones_cursada.clasificar_cursada import ejecutar_opcion_cursada, clasificar_cursada
from variables_globales import NOTA_APROBACION, NOTA_PROMOCION

@pytest.fixture # lista de diccionarios con los datos de alumnos para usar en las pruebas 
def lista_diccionarios():
    return [
        {"Legajo": "1", "Nombre": "Juan", "Apellido": "Martinez", "nota1": "82", "nota2": "30"},
        {"Legajo": "2", "Nombre": "Pedro", "Apellido": "Perez", "nota1": "90", "nota2": "80"},
        {"Legajo": "3", "Nombre": "Juana", "Apellido": "Liz", "nota1": "100", "nota2": "98"},
        {"Legajo": "4", "Nombre": "Ana", "Apellido": "Gonzalez", "nota1": "76", "nota2": "88"},
        {"Legajo": "5", "Nombre": "Carlos", "Apellido": "Lopez", "nota1": "64", "nota2": "55"},
        {"Legajo": "6", "Nombre": "Luis", "Apellido": "Garcia", "nota1": "95", "nota2": "92"},
        {"Legajo": "7", "Nombre": "Maria", "Apellido": "Fernandez", "nota1": "85", "nota2": "22"},
        {"Legajo": "8", "Nombre": "Jorge", "Apellido": "Ramirez", "nota1": "59", "nota2": "67"},
        {"Legajo": "9", "Nombre": "Elena", "Apellido": "Hernandez", "nota1": "78", "nota2": "82"},
        {"Legajo": "10", "Nombre": "Laura", "Apellido": "Ruiz", "nota1": "89", "nota2": "91"},
        {"Legajo": "11", "Nombre": "Sofia", "Apellido": "Diaz", "nota1": "93", "nota2": "89"},
        {"Legajo": "12", "Nombre": "Raul", "Apellido": "Morales", "nota1": "74", "nota2": "36"},
        {"Legajo": "13", "Nombre": "Diego", "Apellido": "Castro", "nota1": "62", "nota2": "60"},
        {"Legajo": "14", "Nombre": "Valeria", "Apellido": "Ortega", "nota1": "88", "nota2": "86"},
        {"Legajo": "15", "Nombre": "Manuel", "Apellido": "Suarez", "nota1": "79", "nota2": "77"},
        {"Legajo": "16", "Nombre": "Rocio", "Apellido": "Romero", "nota1": "71", "nota2": "83"},
        {"Legajo": "17", "Nombre": "Pablo", "Apellido": "Mendoza", "nota1": "81", "nota2": "39"},
        {"Legajo": "18", "Nombre": "Clara", "Apellido": "Vega", "nota1": "66", "nota2": "58"},
        {"Legajo": "19", "Nombre": "Lucas", "Apellido": "Gutierrez", "nota1": "70", "nota2": "32"},
        {"Legajo": "20", "Nombre": "Carmen", "Apellido": "Jimenez", "nota1": "87", "nota2": "85"},
        {"Legajo": "21", "Nombre": "David", "Apellido": "Alonso", "nota1": "91", "nota2": "90"},
        {"Legajo": "22", "Nombre": "Lucia", "Apellido": "Torres", "nota1": "68", "nota2": "72"},
        {"Legajo": "23", "Nombre": "Fernando", "Apellido": "Navarro", "nota1": "94", "nota2": "87"},
        {"Legajo": "24", "Nombre": "Cristina", "Apellido": "Reyes", "nota1": "73", "nota2": "79"},
        {"Legajo": "25", "Nombre": "Sergio", "Apellido": "Molina", "nota1": "12", "nota2": "76"},
        {"Legajo": "26", "Nombre": "Alicia", "Apellido": "Ortega", "nota1": "25", "nota2": "84"},
        {"Legajo": "27", "Nombre": "Esteban", "Apellido": "Cruz", "nota1": "61", "nota2": "53"},
        {"Legajo": "28", "Nombre": "Marta", "Apellido": "Delgado", "nota1": "35", "nota2": "81"},
        {"Legajo": "29", "Nombre": "Andres", "Apellido": "Santos", "nota1": "17", "nota2": "74"},
        {"Legajo": "30", "Nombre": "Beatriz", "Apellido": "Martinez", "nota1": "92", "nota2": "88"},
        {"Legajo": "31", "Nombre": "Daniel", "Apellido": "Ramos", "nota1": "84", "nota2": "93"},
        {"Legajo": "32", "Nombre": "Paula", "Apellido": "Dominguez", "nota1": "67", "nota2": "71"},
        {"Legajo": "33", "Nombre": "Gabriel", "Apellido": "Vargas", "nota1": "58", "nota2": "62"},
        {"Legajo": "34", "Nombre": "Teresa", "Apellido": "Flores", "nota1": "86", "nota2": "89"},
        {"Legajo": "35", "Nombre": "Ignacio", "Apellido": "Herrera", "nota1": "12", "nota2": "95"},
        {"Legajo": "36", "Nombre": "Angela", "Apellido": "Carrasco", "nota1": "72", "nota2": "69"},
        {"Legajo": "37", "Nombre": "Martin", "Apellido": "Santana", "nota1": "60", "nota2": "57"},
        {"Legajo": "38", "Nombre": "Eva", "Apellido": "Medina", "nota1": "82", "nota2": "78"},
        {"Legajo": "39", "Nombre": "Victor", "Apellido": "Serrano", "nota1": "79", "nota2": "70"},
        {"Legajo": "40", "Nombre": "Natalia", "Apellido": "Iglesias", "nota1": "88", "nota2": "94"},
        {"Legajo": "41", "Nombre": "Mario", "Apellido": "Arias", "nota1": "65", "nota2": "66"},
        {"Legajo": "42", "Nombre": "Ines", "Apellido": "Pascual", "nota1": "81", "nota2": "80"},
        {"Legajo": "43", "Nombre": "Ruben", "Apellido": "Salas", "nota1": "87", "nota2": "84"},
        {"Legajo": "44", "Nombre": "Adriana", "Apellido": "Gallego", "nota1": "76", "nota2": "77"},
        {"Legajo": "45", "Nombre": "Cristian", "Apellido": "Moya", "nota1": "5", "nota2": "61"},
        {"Legajo": "46", "Nombre": "Andrea", "Apellido": "Aguilar", "nota1": "35", "nota2": "96"},
        {"Legajo": "47", "Nombre": "Francisco", "Apellido": "Blanco", "nota1": "92", "nota2": "23"},
        {"Legajo": "48", "Nombre": "Isabel", "Apellido": "Paredes", "nota1": "66", "nota2": "68"},
        {"Legajo": "49", "Nombre": "Gonzalo", "Apellido": "Moreno", "nota1": "14", "nota2": "73"},
        {"Legajo": "50", "Nombre": "Miriam", "Apellido": "Soto", "nota1": "13", "nota2": "82"},
        {"Legajo": "51", "Nombre": "Mati", "Apellido": "Rejio", "nota1": "85", "nota2": "82"}
    ]
        
        
def test_clasificar_promocionados(lista_diccionarios):
    inputs = ['1', '4', '4']  # Entradas simuladas
    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new=StringIO()) as salida_simulada:
            ejecutar_opcion_cursada(lista_diccionarios)
            assert "Juana Liz" in salida_simulada.getvalue()
            assert "Luis Garcia" in salida_simulada.getvalue()

def test_clasificar_aprobados(lista_diccionarios):
    inputs = ['2', '4', '4']  # Entradas simuladas de usuario
    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new=StringIO()) as salida_simulada:
            ejecutar_opcion_cursada(lista_diccionarios)
            assert "Carlos Lopez" in salida_simulada.getvalue()
            assert "Ana Gonzalez" in salida_simulada.getvalue()

def test_clasificar_aplazados(lista_diccionarios):
    inputs = ['3', '4', '4']  # Entradas simuladas de usuario
    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new=StringIO()) as salida_simulada:
            ejecutar_opcion_cursada(lista_diccionarios)
            assert "Juan Martinez" in salida_simulada.getvalue()
            assert "Gonzalo Moreno" in salida_simulada.getvalue()

def test_faltan_notas(lista_diccionarios):
    # Entradas para verificar alumnos con datos faltantes
    alumnos_faltan_notas = [
        {'Legajo': 9, 'Nombre': 'Elena', 'Apellido': 'Hernandez', 'nota1': '78'},  # Falta nota2
        {'Legajo': 10, 'Nombre': 'Laura', 'Apellido': 'Ruiz', 'nota2': '91'},  # Falta nota1
    ]
    inputs = ['1','2','3']  # No se ingresan alumnos válidos
    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new=StringIO()) as salida_simulada:
            clasificar_cursada(alumnos_faltan_notas,NOTA_APROBACION,NOTA_PROMOCION)
            assert "Error: Faltan las columnas 'nota1' o 'nota2' en los datos." in salida_simulada.getvalue()


