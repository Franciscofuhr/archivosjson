import customtkinter as ctk
from funciones_delete.eliminar_alumno import eliminar_fila_csv

def mostrar_menu_delete(frame_principal, app):
    # Clear the frame first
    app.limpiar_frame()

    # Title and instruction label
    ctk.CTkLabel(frame_principal, text="Eliminar Alumno", font=("Arial", 20), text_color="#061b2c").pack(pady=5)
    ctk.CTkLabel(frame_principal, text="Ingrese el legajo del alumno a eliminar:", text_color="black").pack(pady=5)

    # Input field for 'legajo'
    entry_legajo = ctk.CTkEntry(frame_principal, width=200)
    entry_legajo.pack(pady=5)

    # Label to display success or error messages
    label_mensaje = ctk.CTkLabel(frame_principal, text="", text_color="red")
    label_mensaje.pack(pady=5)

    def eliminar_alumno():
        try:
            legajo = int(entry_legajo.get())
            if eliminar_fila_csv(legajo):
                # Update message label to show success
                label_mensaje.configure(text="El alumno con Legajo: " + str(legajo) + " fue eliminado exitosamente.", text_color="green")
            else:
                # Update message label to show error for not found
                label_mensaje.configure(text="Legajo no encontrado.", text_color="red")
        except ValueError:
            # Update message label to show error for invalid input
            label_mensaje.configure(text="Ingrese un número de legajo válido.", text_color="red")

    # Delete button to trigger the delete function
    boton_eliminar = ctk.CTkButton(frame_principal, text="Eliminar", fg_color="red", width=200, command=eliminar_alumno)
    boton_eliminar.pack(pady=5)

    # Button to go back to the previous menu
    boton_volver = ctk.CTkButton(frame_principal, text="Volver", fg_color="#061b2c", width=150, command=app.mostrar_submenu_alumnos)
    boton_volver.pack(pady=10)