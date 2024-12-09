import customtkinter as ctk
from funciones_delete.eliminar_alumno import eliminar_fila_csv
from PIL import Image
from utils.utils import validar_es_numero, eliminar_widget


def mostrar_menu_delete(frame_principal, app):
    # Clear the frame first
    app.limpiar_frame()
    
    # Cargar y mostrar la imagen
    try:
        image = ctk.CTkImage(light_image=Image.open("archivosjson\\assets\\uade_una_gran_universidad.png"),
                             size=(200, 120))
        ctk.CTkLabel(frame_principal, image=image, text="").pack()
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        ctk.CTkLabel(frame_principal, text="No se pudo cargar la imagen").pack()
        
    ctk.CTkLabel(frame_principal, text="Programa de Notas Estudiantiles", font=("#061b2c", 24), text_color="black").pack(pady=5)


    # Title and instruction label
    ctk.CTkLabel(frame_principal, text="Eliminar Alumno", font=("Arial", 20), text_color="#061b2c").pack(pady=5)
    ctk.CTkLabel(frame_principal, text="Ingrese el legajo del alumno a eliminar:", text_color="black").pack(pady=5)

    # Input field for 'legajo'
    entry_legajo = ctk.CTkEntry(frame_principal, width=200)
    entry_legajo.pack(pady=5)

    # Label to display success or error messages
    label_mensaje = ctk.CTkLabel(frame_principal, text="", text_color="red")
    label_mensaje.pack(pady=5)

    def vaciar_mensaje():
        label_mensaje.configure(text="")

    def eliminar_alumno():
        try:
            if not validar_es_numero(entry_legajo.get()):
                label_mensaje.configure(text="El legajo debe ser un numero", text_color="red")
                label_mensaje.after(3000,lambda: vaciar_mensaje())
                return
            
            legajo = int(entry_legajo.get())
            if eliminar_fila_csv(legajo):
                # Update message label to show success
                label_mensaje.configure(text="El alumno con Legajo: " + str(legajo) + " fue eliminado exitosamente.", text_color="green")
                label_mensaje.after(3000,lambda: vaciar_mensaje())
            else:
                # Update message label to show error for not found
                label_mensaje.configure(text="Legajo no encontrado.", text_color="red")
                label_mensaje.after(3000,lambda: vaciar_mensaje())
        except ValueError:
            # Update message label to show error for invalid input
            label_mensaje.configure(text="Ingrese un número de legajo válido.", text_color="red")
            label_mensaje.after(3000,lambda: vaciar_mensaje())

    # Delete button to trigger the delete function
    boton_eliminar = ctk.CTkButton(frame_principal, text="Eliminar", fg_color="red", width=200, command=eliminar_alumno)
    boton_eliminar.pack(pady=5)

    # Button to go back to the previous menu
    boton_volver = ctk.CTkButton(frame_principal, text="Volver", fg_color="#061b2c", width=150, command=app.mostrar_submenu_alumnos)
    boton_volver.pack(pady=10)
    
    # Label to display success or error messages
    label_mensaje = ctk.CTkLabel(frame_principal, text="", text_color="red")
    label_mensaje.pack(pady=5)