import csv
import customtkinter as ctk
from funciones_parcial.buscar_resultados_parcial import ejecutar_opcion_parcial
from funciones_alumnos.buscar_alumnos import buscar_alumno
from funciones_cursada.clasificar_cursada import ejecutar_opcion_cursada
from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Programa de Notas Estudiantiles")
        self.geometry("800x600")
        self._set_appearance_mode("system")
        self.configure(fg_color="#061b2c")

        # Cargar los datos al iniciar
        self.lista_diccionarios = self.cargar_datos()

        # Cargar la imagen y almacenar en un atributo
        try:
            self.my_image = ctk.CTkImage(light_image=Image.open("archivosjson\\assets\\uade_una_gran_universidad.png"),
                                         size=(400, 240))
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            self.my_image = None  # Asignar None si hay un error

        # Crear un Frame para mostrar los diferentes menús
        self.frame_principal = ctk.CTkFrame(self)
        self.frame_principal.pack(pady=10, padx=10, fill="both", expand=True)
        self.frame_principal._set_appearance_mode("system")
        self.frame_principal.configure(fg_color="White")
        
        self.mostrar_menu_principal()

    def cargar_datos(self):
        with open('archivosjson\\datosAlumnos.csv', mode='r') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv, delimiter=';')
            return [fila for fila in lector_csv]

    def mostrar_menu_principal(self):
        self.limpiar_frame()
        
        # Mostrar la imagen
        if self.my_image: 
            ctk.CTkLabel(self.frame_principal, image=self.my_image, text="").pack()  
        else:
            ctk.CTkLabel(self.frame_principal, text="No se pudo cargar la imagen").pack()

        ctk.CTkLabel(self.frame_principal, text="Programa de Notas Estudiantiles", font=("#061b2c", 24), text_color="black").pack(pady=5)
        ctk.CTkLabel(self.frame_principal, text="Menú Principal", font=("Arial", 20), text_color="#061b2c").pack(pady=5)

        boton_notas_parciales = ctk.CTkButton(self.frame_principal, text="Notas de Parciales", fg_color="#061b2c", width=200, command=self.mostrar_menu_parcial)
        boton_notas_parciales.pack(pady=5)

        boton_estado_cursada = ctk.CTkButton(self.frame_principal, text="Estado de Cursada", fg_color="#061b2c", width=200, command=self.ejecutar_estado_cursada)
        boton_estado_cursada.pack(pady=5)

        # Cambiar aquí de "Búsqueda de Alumnos" a "Alumnos"
        boton_alumnos = ctk.CTkButton(self.frame_principal, text="Alumnos", fg_color="#061b2c", width=200, command=self.mostrar_submenu_alumnos)
        boton_alumnos.pack(pady=5)

        boton_salir = ctk.CTkButton(self.frame_principal, text="Salir", fg_color="#061b2c", width=150, command=self.quit)
        boton_salir.pack(pady=10)

    def mostrar_submenu_alumnos(self):
        self.limpiar_frame()  # Limpiar el contenido del frame actual

        if self.my_image:
            ctk.CTkLabel(self.frame_principal, image=self.my_image, text="").pack()  # Mostrar la imagen
        else:
            ctk.CTkLabel(self.frame_principal, text="No se pudo cargar la imagen").pack()

        ctk.CTkLabel(self.frame_principal, text="Programa de Notas Estudiantiles", font=("#061b2c", 24), text_color="black").pack(pady=5)
        ctk.CTkLabel(self.frame_principal, text="Alumnos", font=("Arial", 20), text_color="#061b2c").pack(pady=5)

        boton_busqueda_alumnos = ctk.CTkButton(self.frame_principal, text="Búsqueda de Alumnos", fg_color="#061b2c", width=200, command=self.buscar_alumnos)
        boton_busqueda_alumnos.pack(pady=5)

        # Agregar botón para "Crear Alumno"
        boton_crear_alumno = ctk.CTkButton(self.frame_principal, text="Crear Alumno", fg_color="#061b2c", width=200, command=self.mostrar_menu_crear_alumno)
        boton_crear_alumno.pack(pady=5)

        boton_volver = ctk.CTkButton(self.frame_principal, text="Volver al menú principal", fg_color="#061b2c", width=175, command=self.mostrar_menu_principal)
        boton_volver.pack(pady=10)

    def mostrar_menu_crear_alumno(self):
        # Llamar a la función de creación de alumno (debe estar implementada en funciones_alumnos/menu_crear.py)
        from funciones_create.menu_crear import mostrar_menu_crear
        mostrar_menu_crear(self.frame_principal)

    def mostrar_menu_parcial(self):
        self.limpiar_frame()  # Limpiar el contenido del frame actual

        if self.my_image:
            ctk.CTkLabel(self.frame_principal, image=self.my_image, text="").pack()  # Mostrar la imagen
        else:
            ctk.CTkLabel(self.frame_principal, text="No se pudo cargar la imagen").pack()
        
        ctk.CTkLabel(self.frame_principal, text="Programa de Notas Estudiantiles", font=("#061b2c", 24), text_color="black").pack(pady=5)
        ctk.CTkLabel(self.frame_principal, text="Notas de Parciales", font=("Arial", 20), text_color="#061b2c").pack(pady=5)

        boton_1er_parcial = ctk.CTkButton(self.frame_principal, text="1er Parcial", fg_color="#061b2c", width=200, command=lambda: self.ejecutar_opcion_parcial("1"))
        boton_1er_parcial.pack(pady=5)

        boton_2do_parcial = ctk.CTkButton(self.frame_principal, text="2do Parcial", fg_color="#061b2c", width=200, command=lambda: self.ejecutar_opcion_parcial("2"))
        boton_2do_parcial.pack(pady=5)

        boton_volver = ctk.CTkButton(self.frame_principal, text="Volver al menú principal", fg_color="#061b2c", width=175, command=self.mostrar_menu_principal)
        boton_volver.pack(pady=10)

    def ejecutar_opcion_parcial(self, opcion_parcial):
        self.limpiar_frame()  # Limpiar el contenido del frame actual
        
        if self.my_image:
            ctk.CTkLabel(self.frame_principal, image=self.my_image, text="").pack()  # Mostrar la imagen
        else:
            ctk.CTkLabel(self.frame_principal, text="No se pudo cargar la imagen").pack()

        ejecutar_opcion_parcial(opcion_parcial, self.lista_diccionarios, self.frame_principal)  # Mostrar el resultado en un frame
        
        boton_volver = ctk.CTkButton(self.frame_principal, text="Volver al menú principal", fg_color="#061b2c", width=175, command=self.mostrar_menu_principal) 
        boton_volver.pack(pady=5)  # Agregar un botón "Volver" para regresar al menú principal

    def ejecutar_estado_cursada(self):
        self.limpiar_frame()
        if self.my_image:
            ctk.CTkLabel(self.frame_principal, image=self.my_image, text="").pack()  # Mostrar la imagen
        else:
            ctk.CTkLabel(self.frame_principal, text="No se pudo cargar la imagen").pack()
            
        ctk.CTkLabel(self.frame_principal, text="Programa de Notas Estudiantiles", font=("#061b2c", 24), text_color="black").pack(pady=5)

        ejecutar_opcion_cursada(self.lista_diccionarios, self.frame_principal)  # Pasar el frame_principal

    def buscar_alumnos(self):
        self.limpiar_frame()
        if self.my_image:
            ctk.CTkLabel(self.frame_principal, image=self.my_image, text="").pack()  # Mostrar la imagen
        else:
            ctk.CTkLabel(self.frame_principal, text="No se pudo cargar la imagen").pack()
            
        ctk.CTkLabel(self.frame_principal, text="Programa de Notas Estudiantiles", font=("#061b2c", 24), text_color="black").pack(pady=5)

        # Buscar alumnos en el archivo CSV
        buscar_alumno(self.lista_diccionarios, self.frame_principal)
        
        boton_volver = ctk.CTkButton(self.frame_principal, text="Volver al menú principal", fg_color="#061b2c", width=175, command=self.mostrar_menu_principal)
        boton_volver.pack(pady=5)

    def limpiar_frame(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

# Ejecución de la aplicación
def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()