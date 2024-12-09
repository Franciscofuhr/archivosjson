import customtkinter as ctk
import csv
from utils.utils import validar_es_numero, validar_numero_rango, validar_sin_numeros 
from funciones_create.crear_alumno import agregar_fila_csv
from PIL import Image

# Menú de "Create"
def mostrar_menu_crear(frame):
    for widget in frame.winfo_children():
        widget.destroy()
        
    try:
        image = ctk.CTkImage(light_image=Image.open('archivosjson\\assets\\uade_una_gran_universidad.png'),
                                         size=(200, 120))
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        image = None
        
    if image:
        ctk.CTkLabel(frame, image=image, text="").pack()  # Mostrar la imagen
    else:
        ctk.CTkLabel(frame, text="No se pudo cargar la imagen").pack()
        
    ctk.CTkLabel(frame, text="Programa de Notas Estudiantiles", font=("#061b2c", 24), text_color="black").pack(pady=5)

    # Crear los campos de entrada para el nuevo alumno
    ctk.CTkLabel(frame, text="Crear Nuevo Alumno", font=("Arial", 20), text_color="#061b2c").pack(pady=5)

    # Campos de texto para ingresar los datos del alumno
    legajo_label = ctk.CTkLabel(frame, text="Legajo", text_color="#061b2c")
    legajo_label.pack(pady=0)
    legajo_entry = ctk.CTkEntry(frame, width=200)
    legajo_entry.pack(pady=0)

    nombre_label = ctk.CTkLabel(frame, text="Nombre", text_color="#061b2c")
    nombre_label.pack(pady=0)
    nombre_entry = ctk.CTkEntry(frame, width=200)
    nombre_entry.pack(pady=0)

    apellido_label = ctk.CTkLabel(frame, text="Apellido", text_color="#061b2c")
    apellido_label.pack(pady=0)
    apellido_entry = ctk.CTkEntry(frame, width=200)
    apellido_entry.pack(pady=0)

    # Nota 1er Parcial
    nota1_label = ctk.CTkLabel(frame, text="Nota 1er Parcial", text_color="#061b2c")
    nota1_label.pack(pady=0)
    nota1_entry = ctk.CTkEntry(frame, width=200)
    nota1_entry.pack(pady=0)

    # Nota 2do Parcial
    nota2_label = ctk.CTkLabel(frame, text="Nota 2do Parcial", text_color="#061b2c")
    nota2_label.pack(pady=0)
    nota2_entry = ctk.CTkEntry(frame, width=200)
    nota2_entry.pack(pady=0)


    def guardar_alumno():
        # Eliminar mensajes previos
        for widget in frame.winfo_children():
            if isinstance(widget, ctk.CTkLabel) and widget.cget("text_color") in ["red", "green"]:
                widget.destroy()

        # Tomar los datos ingresados en los campos de texto
        legajo = legajo_entry.get()
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        nota1 = nota1_entry.get()
        nota2 = nota2_entry.get()

        # Validar que todos los campos de texto
        if not legajo or not nombre or not apellido or not nota1 or not nota2:
            ctk.CTkLabel(frame, text="Por favor complete todos los campos", text_color="red").pack(pady=5)
            return
        
        if not validar_es_numero(legajo):
            ctk.CTkLabel(frame, text="El legajo debe ser un numero", text_color="red").pack(pady=5)
            return
        
        if not validar_es_numero(nota1) or not validar_es_numero(nota2) or not validar_numero_rango(nota1) or not validar_numero_rango(nota2):
            ctk.CTkLabel(frame, text="Las notas deben ser un numero entre 0 y 100", text_color="red").pack(pady=5)
            return
        else:
            nota1 = int(nota1_entry.get())
            nota2 = int(nota2_entry.get())

        
        if not validar_sin_numeros(nombre) or not validar_sin_numeros(apellido):
            ctk.CTkLabel(frame, text="El nombre y apellido no debe contener numeros", text_color="red").pack(pady=5)
            return
            
        try:
            agregar_fila_csv(legajo, nombre, apellido, nota1, nota2)
            
            # Mensaje de éxito
            mensaje_exito = ctk.CTkLabel(frame, text="Alumno creado exitosamente", text_color="green")
            mensaje_exito.pack(pady=5)

            # Limpiar los campos después de guardar
            legajo_entry.delete(0, 'end')
            nombre_entry.delete(0, 'end')
            apellido_entry.delete(0, 'end')
            nota1_entry.delete(0, 'end')
            nota2_entry.delete(0, 'end')

        except ValueError as e:
            # Mostrar el mensaje de error en la interfaz
            ctk.CTkLabel(frame, text=str(e), text_color="red").pack(pady=5)

        # No realizar la búsqueda ni Volver al menu de alumnos
        # Si no quieres recargar los datos de los alumnos ni llamar a `buscar_alumnos()`, simplemente comenta o elimina esa parte
        # frame.master.lista_diccionarios = frame.master.cargar_datos()
        # frame.master.buscar_alumnos()

    # Botón para guardar el nuevo alumno
    boton_guardar = ctk.CTkButton(frame, text="Guardar", fg_color="#061b2c", width=200, command=guardar_alumno)
    boton_guardar.pack(pady=20)

    # Botón para Volver al menu de alumnos
    boton_volver = ctk.CTkButton(frame, text="Volver", fg_color="#061b2c", width=175, command=lambda: frame.master.mostrar_submenu_alumnos())
    boton_volver.pack(pady=10)