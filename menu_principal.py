import csv
import customtkinter as ctk
from funciones_parcial.buscar_resultados_parcial import ejecutar_opcion_parcial
from funciones_alumnos.buscar_alumnos import buscar_alumno
from funciones_cursada.clasificar_cursada import ejecutar_opcion_cursada
from funciones_delete.menu_delete import mostrar_menu_delete
from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Personalización
        self.title("Programa de Notas Estudiantiles")
        self.geometry("1024x800")
        self._set_appearance_mode("system")
        self.configure(fg_color="#061b2c")

       
        self.lista_diccionarios = self.cargar_datos() # Guardar los diccionarios de los alumnos

        # Cargar la imagen como una variable
        try:
            self.my_image = ctk.CTkImage(light_image=Image.open("archivosjson\\assets\\uade_una_gran_universidad.png"),
                                         size=(400, 240))
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            self.my_image = None

        # Crear un Frame donde se muestren los diferentes menús
        self.frame_principal = ctk.CTkFrame(self)
        self.frame_principal.pack(pady=10, padx=10, fill="both", expand=True)
        self.frame_principal._set_appearance_mode("system")
        self.frame_principal.configure(fg_color="White")
        
        self.mostrar_menu_principal()

    def cargar_datos(self): # Cargar los datos de los alumnos desde el archivo CSV

        with open('C:/Users/lauta/OneDrive/Escritorio/archivosjson/datosAlumnos.csv', mode='r') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv, delimiter=';')
            return [fila for fila in lector_csv]

    # Menú principal
    def mostrar_menu_principal(self): 
        
        self.limpiar_frame()
        
        # Mostrar la imagen si se cargó correctamente
        if self.my_image: 
            ctk.CTkLabel(self.frame_principal, image=self.my_image, text="").pack()  
        else:
            ctk.CTkLabel(self.frame_principal, text="No se pudo cargar la imagen").pack()

        # Título del menú
        ctk.CTkLabel(self.frame_principal, text="Programa de Notas Estudiantiles", font=("#061b2c", 24), text_color="black").pack(pady=5)
        ctk.CTkLabel(self.frame_principal, text="Menú Principal", font=("Arial", 20), text_color="#061b2c").pack(pady=5)

        # Botones del menú principal
        ctk.CTkButton(self.frame_principal, text="Notas de Parciales", fg_color="#061b2c", width=200, command=self.mostrar_menu_parcial).pack(pady=5)
        ctk.CTkButton(self.frame_principal, text="Estado de Cursada", fg_color="#061b2c", width=200, command=self.ejecutar_estado_cursada).pack(pady=5)
        ctk.CTkButton(self.frame_principal, text="Alumnos", fg_color="#061b2c", width=200, command=self.mostrar_submenu_alumnos).pack(pady=5)
        ctk.CTkButton(self.frame_principal, text="Salir", fg_color="#061b2c", width=150, command=self.quit).pack(pady=10)


    # Submenú de Alumnos
    def mostrar_submenu_alumnos(self): 
        
        self.limpiar_frame()

        if self.my_image:
            ctk.CTkLabel(self.frame_principal, image=self.my_image, text="").pack()
        else:
            ctk.CTkLabel(self.frame_principal, text="No se pudo cargar la imagen").pack()

        ctk.CTkLabel(self.frame_principal, text="Programa de Notas Estudiantiles", font=("#061b2c", 24), text_color="black").pack(pady=5)
        ctk.CTkLabel(self.frame_principal, text="Alumnos", font=("Arial", 20), text_color="#061b2c").pack(pady=5)

        # Botones para gestionar alumnos
        ctk.CTkButton(self.frame_principal, text="Buscar Alumno", fg_color="#061b2c", width=200, command=self.buscar_alumnos).pack(pady=5)
        ctk.CTkButton(self.frame_principal, text="Crear Alumno", fg_color="#061b2c", width=200, command=self.mostrar_menu_crear_alumno).pack(pady=5)
        ctk.CTkButton(self.frame_principal, text="Modificar Alumno", fg_color="#061b2c", width=200, command=self.mostrar_menu_modificar_alumno).pack(pady=5)
        ctk.CTkButton(self.frame_principal, text="Eliminar Alumno", fg_color="red", width=200, command=lambda: mostrar_menu_delete(self.frame_principal, self)).pack(pady=5)
        
        ctk.CTkButton(self.frame_principal, text="Volver al menú principal", fg_color="#061b2c", width=175, command=self.mostrar_menu_principal).pack(pady=10)


    # Menú de creación de alumno
    def mostrar_menu_crear_alumno(self):
                
        from funciones_create.menu_crear import mostrar_menu_crear
        mostrar_menu_crear(self.frame_principal)

    # Menú de modificación de alumno
    def mostrar_menu_modificar_alumno(self):
        
        from funciones_update.menu_update import mostrar_menu_update
        self.limpiar_frame()
        mostrar_menu_update(self.frame_principal, self)

    # Menú de Parciales 
    def mostrar_menu_parcial(self):
        
        self.limpiar_frame()

        if self.my_image:
            ctk.CTkLabel(self.frame_principal, image=self.my_image, text="").pack()
        else:
            ctk.CTkLabel(self.frame_principal, text="No se pudo cargar la imagen").pack()
        
        ctk.CTkLabel(self.frame_principal, text="Programa de Notas Estudiantiles", font=("#061b2c", 24), text_color="black").pack(pady=5)
        ctk.CTkLabel(self.frame_principal, text="Notas de Parciales", font=("Arial", 20), text_color="#061b2c").pack(pady=5)

        ctk.CTkButton(self.frame_principal, text="1er Parcial", fg_color="#061b2c", width=200, command=lambda: self.ejecutar_opcion_parcial("1")).pack(pady=5)
        ctk.CTkButton(self.frame_principal, text="2do Parcial", fg_color="#061b2c", width=200, command=lambda: self.ejecutar_opcion_parcial("2")).pack(pady=5)
        ctk.CTkButton(self.frame_principal, text="Volver", fg_color="#061b2c", width=175, command=self.mostrar_menu_principal).pack(pady=10)


    # Menú de opción de notas de parciales
    def ejecutar_opcion_parcial(self, opcion_parcial):
        self.limpiar_frame()
        
        if self.my_image:
            ctk.CTkLabel(self.frame_principal, image=self.my_image, text="").pack()
        else:
            ctk.CTkLabel(self.frame_principal, text="No se pudo cargar la imagen").pack()

        ejecutar_opcion_parcial(opcion_parcial, self.lista_diccionarios, self.frame_principal)
        ctk.CTkButton(self.frame_principal, text="Volver al menú principal", fg_color="#061b2c", width=175, command=self.mostrar_menu_principal).pack(pady=5)

    
    # Mostrar el estado de cursada
    def ejecutar_estado_cursada(self):
        
        self.limpiar_frame()
        if self.my_image:
            ctk.CTkLabel(self.frame_principal, image=self.my_image, text="").pack()
        else:
            ctk.CTkLabel(self.frame_principal, text="No se pudo cargar la imagen").pack()
            
        ctk.CTkLabel(self.frame_principal, text="Programa de Notas Estudiantiles", font=("#061b2c", 24), text_color="black").pack(pady=5)
        ejecutar_opcion_cursada(self.lista_diccionarios, self.frame_principal)

    # Buscar alumnos en el archivo CSV
    def buscar_alumnos(self):
        
        self.limpiar_frame()
        if self.my_image:
            ctk.CTkLabel(self.frame_principal, image=self.my_image, text="").pack()
        else:
            ctk.CTkLabel(self.frame_principal, text="No se pudo cargar la imagen").pack()
            
        ctk.CTkLabel(self.frame_principal, text="Programa de Notas Estudiantiles", font=("#061b2c", 24), text_color="black").pack(pady=5)
        buscar_alumno(self.lista_diccionarios, self.frame_principal)

    # Limpiar el contenido del frame actual
    def limpiar_frame(self):
        self.lista_diccionarios = self.cargar_datos()
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

# Crear la instancia y ejecutar la aplicación
def main():
    app = App()
    app.mainloop()
if __name__ == "__main__":
    main()