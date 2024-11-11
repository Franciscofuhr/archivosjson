import customtkinter as ctk
from funciones_update import modificar_fila_csv

def mostrar_menu_update(frame_principal):
    # Limpiar el contenido del frame actual
    for widget in frame_principal.winfo_children():
        widget.destroy()

    # Etiqueta de título
    ctk.CTkLabel(frame_principal, text="Modificar Alumno", font=("Arial", 24), text_color="#061b2c").pack(pady=20)

    # Crear campos de entrada para legajo, nombre, apellido y notas
    ctk.CTkLabel(frame_principal, text="Legajo:").pack(pady=5)
    entry_legajo = ctk.CTkEntry(frame_principal, placeholder_text="Ingrese el legajo del alumno")
    entry_legajo.pack(pady=5)

    ctk.CTkLabel(frame_principal, text="Nuevo Nombre:").pack(pady=5)
    entry_nombre = ctk.CTkEntry(frame_principal, placeholder_text="Ingrese el nuevo nombre")
    entry_nombre.pack(pady=5)

    ctk.CTkLabel(frame_principal, text="Nuevo Apellido:").pack(pady=5)
    entry_apellido = ctk.CTkEntry(frame_principal, placeholder_text="Ingrese el nuevo apellido")
    entry_apellido.pack(pady=5)

    ctk.CTkLabel(frame_principal, text="Nueva Nota 1:").pack(pady=5)
    entry_nota1 = ctk.CTkEntry(frame_principal, placeholder_text="Ingrese la nueva nota 1")
    entry_nota1.pack(pady=5)

    ctk.CTkLabel(frame_principal, text="Nueva Nota 2:").pack(pady=5)
    entry_nota2 = ctk.CTkEntry(frame_principal, placeholder_text="Ingrese la nueva nota 2")
    entry_nota2.pack(pady=5)

    def actualizar_datos():
        # Obtener el legajo y los nuevos valores desde las entradas
        try:
            legajo = int(entry_legajo.get())
            nuevo_nombre = entry_nombre.get() if entry_nombre.get() else None
            nuevo_apellido = entry_apellido.get() if entry_apellido.get() else None
            nueva_nota1 = float(entry_nota1.get()) if entry_nota1.get() else None
            nueva_nota2 = float(entry_nota2.get()) if entry_nota2.get() else None

            # Llamar a la función para modificar la fila
            modificar_fila_csv(legajo, nuevo_nombre, nuevo_apellido, nueva_nota1, nueva_nota2)
        except ValueError:
            # Si hay un error en los valores introducidos (por ejemplo, texto en lugar de número)
            ctk.CTkLabel(frame_principal, text="Por favor ingrese valores válidos", text_color="red").pack(pady=5)

    # Botón para ejecutar la actualización
    boton_actualizar = ctk.CTkButton(frame_principal, text="Actualizar Alumno", fg_color="#061b2c", width=200, command=actualizar_datos)
    boton_actualizar.pack(pady=20)

    # Botón para volver al menú anterior
    boton_volver = ctk.CTkButton(frame_principal, text="Volver al menú anterior", fg_color="#061b2c", width=200, command=lambda: frame_principal.pack_forget())
    boton_volver.pack(pady=10)
