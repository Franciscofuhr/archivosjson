import customtkinter as ctk
from funciones_update.funciones_update import modificar_fila_csv
from utils.utils import validar_es_numero, validar_numero_rango, validar_sin_numeros, eliminar_widget
from PIL import Image

def mostrar_menu_update(frame_principal, app):
    """
    Muestra la interfaz para modificar los datos de un alumno.
    """
    def inicializar_pantalla():
        app.lista_diccionarios = app.cargar_datos()
        # Limpiar todos los widgets actuales
        for widget in frame_principal.winfo_children():
            widget.destroy()

        # Cargar y mostrar la imagen
        try:
            image = ctk.CTkImage(light_image=Image.open("archivosjson\\assets\\uade_una_gran_universidad.png"),
                                 size=(200, 120))
            ctk.CTkLabel(frame_principal, image=image, text="").pack()
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            ctk.CTkLabel(frame_principal, text="No se pudo cargar la imagen").pack()
            
        ctk.CTkLabel(frame_principal, text="Programa de Notas Estudiantiles", font=("#061b2c", 24), text_color="black").pack(pady=5)

        # Título y campos de entrada
        ctk.CTkLabel(frame_principal, text="Modificar Alumno", font=("Arial", 24), text_color="#061b2c").pack(pady=5)
        ctk.CTkLabel(frame_principal, text="Ingrese Legajo del Alumno", font=("Arial", 16), text_color="#061b2c").pack(pady=5)
        legajo_entry = ctk.CTkEntry(frame_principal, placeholder_text="Legajo del alumno", width=200)
        legajo_entry.pack(pady=5)

        def buscar_y_mostrar():
            # Obtener y validar el legajo
            legajo = legajo_entry.get()
            try:
                legajo = int(legajo)
            except ValueError:
                legajo_valido_error = ctk.CTkLabel(frame_principal, text="Por favor ingrese un número de legajo válido.", font=("Arial", 14), text_color="red")
                legajo_valido_error.pack(pady=5)
                legajo_valido_error.after(3000, lambda : eliminar_widget(legajo_valido_error))
                return

            # Buscar el alumno
            alumno = next((a for a in app.lista_diccionarios if int(a["Legajo"]) == legajo), None)
            if alumno is None:
                no_encontrado_error = ctk.CTkLabel(frame_principal, text="No se encontró ningún alumno con ese legajo.", font=("Arial", 14), text_color="red")
                no_encontrado_error.pack(pady=5)
                no_encontrado_error.after(3000, lambda : eliminar_widget(no_encontrado_error))
                return

            # Mostrar los campos editables
            inicializar_campos_editables(alumno, legajo)

        # Botón para buscar
        ctk.CTkButton(frame_principal, text="Buscar Alumno", fg_color="#061b2c", command=buscar_y_mostrar).pack(pady=5)

        # Botón para volver al menú principal
        ctk.CTkButton(frame_principal, text="Volver", fg_color="#061b2c", command=lambda: frame_principal.master.mostrar_submenu_alumnos()).pack(pady=10)

    def inicializar_campos_editables(alumno, legajo):
        # Limpiar los widgets actuales
        for widget in frame_principal.winfo_children():
            widget.destroy()
            
        try:
            app.my_image = ctk.CTkImage(light_image=Image.open('archivosjson\\assets\\uade_una_gran_universidad.png'),
                                         size=(400, 240))
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            app.my_image = None

        # Mostrar campos editables
        ctk.CTkLabel(frame_principal, text="Modificar Alumno", font=("Arial", 24), text_color="#061b2c").pack(pady=10)
        
        ctk.CTkLabel(frame_principal, text="Nombre", font=("Arial", 16), text_color="#061b2c").pack(pady=5)
        nombre_entry = ctk.CTkEntry(frame_principal, placeholder_text=alumno["Nombre"], width=200)
        nombre_entry.pack(pady=5)
        
        ctk.CTkLabel(frame_principal, text="Apellido", font=("Arial", 16), text_color="#061b2c").pack(pady=5)
        apellido_entry = ctk.CTkEntry(frame_principal, placeholder_text=alumno["Apellido"], width=200)
        apellido_entry.pack(pady=5)
        
        ctk.CTkLabel(frame_principal, text="Nota 1er Parcial", font=("Arial", 16), text_color="#061b2c").pack(pady=5)
        nota1_entry = ctk.CTkEntry(frame_principal, placeholder_text=alumno["nota1"], width=200)
        nota1_entry.pack(pady=5)
        
        ctk.CTkLabel(frame_principal, text="Nota 2do Parcial", font=("Arial", 16), text_color="#061b2c").pack(pady=5)
        nota2_entry = ctk.CTkEntry(frame_principal, placeholder_text=alumno["nota2"], width=200)
        nota2_entry.pack(pady=5)

        def guardar_modificaciones():
            # Obtener los nuevos valores
            nuevo_nombre = nombre_entry.get() or alumno["Nombre"]
            nuevo_apellido = apellido_entry.get() or alumno["Apellido"]
            nueva_nota1 = nota1_entry.get() or alumno["nota1"]
            nueva_nota2 = nota2_entry.get() or alumno["nota2"]
            
            if not legajo or not nuevo_nombre or not nuevo_apellido or not nueva_nota1 or not nueva_nota2:
                contenido_error = ctk.CTkLabel(frame_principal, text="Por favor complete todos los campos", text_color="red")
                contenido_error.pack(pady=5)
                contenido_error.after(3000,lambda: eliminar_widget(contenido_error))
                return

            if not validar_es_numero(legajo):
                legajo_error = ctk.CTkLabel(frame_principal, text="El legajo debe ser un numero", text_color="red")
                legajo_error.pack(pady=5)
                legajo_error.after(3000,lambda: eliminar_widget(legajo_error))
                return

            if not validar_es_numero(nueva_nota1) or not validar_es_numero(nueva_nota2) or not validar_numero_rango(nueva_nota1) or not validar_numero_rango(nueva_nota2):
                notas_error = ctk.CTkLabel(frame_principal, text="Las notas deben ser un numero entre 0 y 100", text_color="red")
                notas_error.pack(pady=5)
                notas_error.after(3000,lambda: eliminar_widget(notas_error))
                return


            if not validar_sin_numeros(nuevo_nombre) or not validar_sin_numeros(nuevo_apellido):
                nombre_error = ctk.CTkLabel(frame_principal, text="El nombre y apellido no debe contener numeros", text_color="red")
                nombre_error.pack(pady=5)
                nombre_error.after(3000,lambda: eliminar_widget(nombre_error))
                return

            # Guardar las modificaciones
            modificar_fila_csv(legajo, nuevo_nombre, nuevo_apellido, nueva_nota1, nueva_nota2)
            eliminado_exito = ctk.CTkLabel(frame_principal, text="¡Alumno modificado con éxito!", font=("Arial", 16), text_color="green")
            eliminado_exito.pack(pady=10)
            eliminado_exito.after(3000,lambda: eliminar_widget(eliminado_exito))

        # Botón para guardar
        ctk.CTkButton(frame_principal, text="Guardar Cambios", fg_color="#061b2c", command=guardar_modificaciones).pack(pady=10)

        # Botón para volver al estado inicial
        ctk.CTkButton(frame_principal, text="Volver", fg_color="#061b2c", command=inicializar_pantalla).pack(pady=10)

    # Inicializar la pantalla principal
    inicializar_pantalla()
