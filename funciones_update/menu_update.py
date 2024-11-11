import customtkinter as ctk
from funciones_update.funciones_update import modificar_fila_csv

def mostrar_menu_update(frame_principal, app):
    """
    Muestra la interfaz para modificar los datos de un alumno.
    Esta interfaz permite ingresar el legajo de un alumno y, si se encuentra, editar los campos de su registro.
    """
    # Limpiar la pantalla actual
    for widget in frame_principal.winfo_children():
        widget.destroy()

    ctk.CTkLabel(frame_principal, text="Modificar Alumno", font=("Arial", 24), text_color="#061b2c").pack(pady=10)

    # Ingreso del legajo a modificar (esto solo se muestra en la pantalla inicial)
    legajo_label = ctk.CTkLabel(frame_principal, text="Ingrese Legajo del Alumno", font=("Arial", 16), text_color="#061b2c")
    legajo_label.pack(pady=5)
    legajo_entry = ctk.CTkEntry(frame_principal, placeholder_text="Legajo del alumno", width=200)
    legajo_entry.pack(pady=10)

    # Variable para almacenar los widgets que se mostrarán después de ingresar el legajo
    campos_editables = []

    # Función para buscar el alumno por su legajo y mostrar los campos editables
    def buscar_y_mostrar():
        legajo = legajo_entry.get()

        # Limpiar los widgets previos en caso de haber mostrado los campos de un alumno antes
        for widget in frame_principal.winfo_children():
            if widget != legajo_entry and widget != legajo_label:  # No eliminar el campo de legajo y su label
                widget.destroy()

        # Validar que el legajo sea un número entero
        try:
            legajo = int(legajo)
        except ValueError:
            ctk.CTkLabel(frame_principal, text="Por favor ingrese un número de legajo válido.", font=("Arial", 14), text_color="red").pack(pady=5)
            return

        # Buscar el alumno (modificar si existe)
        alumno_encontrado = False
        for alumno in app.lista_diccionarios:
            if int(alumno["Legajo"]) == legajo:
                alumno_encontrado = True
                # Eliminar el campo de legajo y su etiqueta, solo si se encuentra el alumno
                legajo_label.destroy()
                legajo_entry.destroy()

                # Mostrar los campos editables con la información actual
                ctk.CTkLabel(frame_principal, text="Nombre", font=("Arial", 16), text_color="#061b2c").pack(pady=5)
                nombre_entry = ctk.CTkEntry(frame_principal, placeholder_text=alumno["Nombre"], width=200)
                nombre_entry.pack(pady=10)

                ctk.CTkLabel(frame_principal, text="Apellido", font=("Arial", 16), text_color="#061b2c").pack(pady=5)
                apellido_entry = ctk.CTkEntry(frame_principal, placeholder_text=alumno["Apellido"], width=200)
                apellido_entry.pack(pady=10)

                ctk.CTkLabel(frame_principal, text="Nota 1", font=("Arial", 16), text_color="#061b2c").pack(pady=5)
                nota1_entry = ctk.CTkEntry(frame_principal, placeholder_text=alumno["nota1"], width=200)
                nota1_entry.pack(pady=10)

                ctk.CTkLabel(frame_principal, text="Nota 2", font=("Arial", 16), text_color="#061b2c").pack(pady=5)
                nota2_entry = ctk.CTkEntry(frame_principal, placeholder_text=alumno["nota2"], width=200)
                nota2_entry.pack(pady=10)

                # Función para guardar los cambios
                def guardar_modificaciones():
                    nuevo_nombre = nombre_entry.get() if nombre_entry.get() else None
                    nuevo_apellido = apellido_entry.get() if apellido_entry.get() else None
                    nueva_nota1 = nota1_entry.get() if nota1_entry.get() else None
                    nueva_nota2 = nota2_entry.get() if nota2_entry.get() else None

                    # Actualizar los datos en el CSV
                    modificar_fila_csv(legajo, nuevo_nombre, nuevo_apellido, nueva_nota1, nueva_nota2)
                    ctk.CTkLabel(frame_principal, text="¡Alumno modificado con éxito!", font=("Arial", 16), text_color="green").pack(pady=10)

                # Botón para guardar cambios
                ctk.CTkButton(frame_principal, text="Guardar Cambios", fg_color="#061b2c", command=guardar_modificaciones).pack(pady=10)

                # Agregar los widgets de la modificación a la lista
                campos_editables.append(nombre_entry)
                campos_editables.append(apellido_entry)
                campos_editables.append(nota1_entry)
                campos_editables.append(nota2_entry)

                break

        if not alumno_encontrado:
            ctk.CTkLabel(frame_principal, text="No se encontró ningún alumno con ese legajo.", font=("Arial", 14), text_color="red").pack(pady=5)

        # Botón Volver
        ctk.CTkButton(frame_principal, text="Volver", fg_color="#061b2c", command=volver_a_ingresar_legajo).pack(pady=10)

    # Botón para buscar y mostrar los campos editables
    ctk.CTkButton(frame_principal, text="Buscar Alumno", fg_color="#061b2c", command=buscar_y_mostrar).pack(pady=10)

    # Botón para volver al menú de alumnos
    boton_volver = ctk.CTkButton(frame_principal, text="Volver al menú de alumnos", fg_color="#061b2c", width=175, command=lambda: frame_principal.master.mostrar_submenu_alumnos())
    boton_volver.pack(pady=10)
    
    # Botón para volver a la pantalla de ingresar legajo
    def volver_a_ingresar_legajo():
        for widget in frame_principal.winfo_children():
            widget.destroy()

        ctk.CTkLabel(frame_principal, text="Modificar Alumno", font=("Arial", 24), text_color="#061b2c").pack(pady=10)
        ctk.CTkLabel(frame_principal, text="Ingrese Legajo del Alumno", font=("Arial", 16), text_color="#061b2c").pack(pady=5)
        legajo_entry = ctk.CTkEntry(frame_principal, placeholder_text="Legajo del alumno", width=200)
        legajo_entry.pack(pady=10)
        ctk.CTkButton(frame_principal, text="Buscar Alumno", fg_color="#061b2c", command=buscar_y_mostrar).pack(pady=10)
        
        # Botón para volver al menú de alumnos
        boton_volver = ctk.CTkButton(frame_principal, text="Volver al menú de alumnos", fg_color="#061b2c", width=175, command=lambda: frame_principal.master.mostrar_submenu_alumnos())
        boton_volver.pack(pady=10)
