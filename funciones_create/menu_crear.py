import customtkinter as ctk
import csv
from utils.utils import validar_es_numero, validar_numero_rango, validar_sin_numeros
from funciones_create.crear_alumno import agregar_fila_csv

def mostrar_menu_crear(frame):
    # Limpiar el frame para el formulario de crear alumno
    for widget in frame.winfo_children():
        widget.destroy()

    # Crear los campos de entrada para el nuevo alumno
    ctk.CTkLabel(frame, text="Crear Nuevo Alumno", font=("Arial", 20), text_color="#061b2c").pack(pady=10)

    # Campos de texto para ingresar los datos del alumno
    legajo_label = ctk.CTkLabel(frame, text="Legajo")
    legajo_label.pack(pady=5)
    legajo_entry = ctk.CTkEntry(frame)
    legajo_entry.pack(pady=5)

    nombre_label = ctk.CTkLabel(frame, text="Nombre")
    nombre_label.pack(pady=5)
    nombre_entry = ctk.CTkEntry(frame)
    nombre_entry.pack(pady=5)

    apellido_label = ctk.CTkLabel(frame, text="Apellido")
    apellido_label.pack(pady=5)
    apellido_entry = ctk.CTkEntry(frame)
    apellido_entry.pack(pady=5)

    # Nota 1er Parcial
    nota1_label = ctk.CTkLabel(frame, text="Nota 1er Parcial")
    nota1_label.pack(pady=5)
    nota1_entry = ctk.CTkEntry(frame)
    nota1_entry.pack(pady=5)

    # Nota 2do Parcial
    nota2_label = ctk.CTkLabel(frame, text="Nota 2do Parcial")
    nota2_label.pack(pady=5)
    nota2_entry = ctk.CTkEntry(frame)
    nota2_entry.pack(pady=5)

    # Función para guardar el alumno
    def guardar_alumno():
        # Eliminar mensajes previos
        for widget in frame.winfo_children():
            if isinstance(widget, ctk.CTkLabel) and widget.cget("text_color") in ["red", "green"]:
                widget.destroy()

        # Obtener los datos de los campos de texto
        legajo = legajo_entry.get()
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        nota1 = nota1_entry.get()
        nota2 = nota2_entry.get()

        # Validar que todos los campos estén completos
        if not legajo or not nombre or not apellido or not nota1 or not nota2:
            ctk.CTkLabel(frame, text="Por favor complete todos los campos", text_color="red").pack(pady=5)
            return
        
        # Validar que todos los campos estén completos
        if not validar_es_numero(legajo):
            ctk.CTkLabel(frame, text="El legajo debe ser un numero", text_color="red").pack(pady=5)
            return
        
        # Validar que todos los campos estén completos
        if not validar_es_numero(nota1) or not validar_es_numero(nota2) or not validar_numero_rango(nota1) or not validar_numero_rango(nota2):
            ctk.CTkLabel(frame, text="Las notas deben ser un numero entre 0 y 100", text_color="red").pack(pady=5)
            return
        
        # Validar que todos los campos estén completos
        if not validar_sin_numeros(nombre) or not validar_sin_numeros(apellido):
            ctk.CTkLabel(frame, text="El nombre y apellido no debe contener numeros", text_color="red").pack(pady=5)
            return
            
        agregar_fila_csv(legajo, nombre, apellido, nota1, nota2)

        # Mostrar mensaje de éxito
        mensaje_exito = ctk.CTkLabel(frame, text="Alumno creado exitosamente", text_color="green")
        mensaje_exito.pack(pady=5)

        # Limpiar los campos después de guardar
        legajo_entry.delete(0, 'end')
        nombre_entry.delete(0, 'end')
        apellido_entry.delete(0, 'end')
        nota1_entry.delete(0, 'end')
        nota2_entry.delete(0, 'end')

        # No realizar la búsqueda ni volver al menú de alumnos
        # Si no quieres recargar los datos de los alumnos ni llamar a `buscar_alumnos()`, simplemente comenta o elimina esa parte
        # frame.master.lista_diccionarios = frame.master.cargar_datos()
        # frame.master.buscar_alumnos()

    # Botón para guardar el nuevo alumno
    boton_guardar = ctk.CTkButton(frame, text="Guardar", fg_color="#061b2c", width=200, command=guardar_alumno)
    boton_guardar.pack(pady=20)

    # Botón para volver al menú de alumnos
    boton_volver = ctk.CTkButton(frame, text="Volver al menú de alumnos", fg_color="#061b2c", width=175, command=lambda: frame.master.mostrar_submenu_alumnos())
    boton_volver.pack(pady=10)
