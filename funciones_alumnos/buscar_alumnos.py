import customtkinter as ctk
from PIL import Image
from utils.utils import eliminar_widget, validar_es_numero, validar_sin_numeros

def buscar_alumno(lista_diccionarios, frame_principal):
    
    # Limpiar el frame antes de mostrar resultados
    for widget in frame_principal.winfo_children():
        widget.destroy()
        
    try:
        image = ctk.CTkImage(light_image=Image.open('archivosjson\\assets\\uade_una_gran_universidad.png'),
                                     size=(400, 240))
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        image = None
        
        if image:
            ctk.CTkLabel(frame_principal, image=image, text="").pack()  # Mostrar la imagen
        else:
            ctk.CTkLabel(frame_principal, text="No se pudo cargar la imagen").pack()

    def mostrar_resultado_alumno(alumno):
        
        for widget in frame_principal.winfo_children():
            widget.destroy()
            
        try: #cargar imagen
            image = ctk.CTkImage(light_image=Image.open('archivosjson\\assets\\uade_una_gran_universidad.png'),
                                     size=(200, 120))
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            image = None
        
        if image:
            ctk.CTkLabel(frame_principal, image=image, text="").pack()  # Mostrar la imagen
        else:
            ctk.CTkLabel(frame_principal, text="No se pudo cargar la imagen").pack() 

        resultados_text = f"Legajo: {alumno['Legajo']}, Apellido: {alumno['Apellido']}, Nombre: {alumno['Nombre']}: "
        resultados_text += f"1er Parcial: {alumno['nota1']} / 2do Parcial: {alumno['nota2']}\n"

        resultados_textbox = ctk.CTkTextbox(frame_principal, width=500, height=150)
        resultados_textbox.pack(pady=10)
        resultados_textbox.insert("0.0", resultados_text)
        resultados_textbox.configure(state="disabled")

        boton_volver = ctk.CTkButton(frame_principal, text="Volver", command=mostrar_menu_busqueda)
        boton_volver.pack(pady=10)

    def buscar_por_criterio(criterio):
        # Limpiar el frame antes de mostrar el formulario de búsqueda
        for widget in frame_principal.winfo_children():
            widget.destroy()
            
        try:
            image = ctk.CTkImage(light_image=Image.open('archivosjson\\assets\\uade_una_gran_universidad.png'),
                                         size=(400, 240))
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            image = None
        
        if image:
            ctk.CTkLabel(frame_principal, image=image, text="").pack()  # Mostrar la imagen
        else:
            ctk.CTkLabel(frame_principal, text="No se pudo cargar la imagen").pack()
            
        ctk.CTkLabel(frame_principal, text="Programa de Notas Estudiantiles", font=("Arial", 24), text_color="#061b2c").pack(pady=5)
        ctk.CTkLabel(frame_principal, text=(f"Búsqueda por {criterio}"), font=("Arial", 20), text_color="#061b2c").pack(pady=5)

        entry = ctk.CTkEntry(frame_principal, placeholder_text=f"Ingrese el {criterio}") # Tomar criterio del usuario
        entry.pack(pady=5)

        
        def realizar_busqueda():
            valor = entry.get().lower()
            resultado = None

            if criterio == "ID" and not validar_es_numero(valor):
                id_no_valido = ctk.CTkLabel(frame_principal, text="El valor ingresado no debe contener letras.", text_color="red")
                id_no_valido.pack(pady=10)
                id_no_valido.after(3000,lambda: eliminar_widget(id_no_valido))
                return

            if criterio == "Nombre" and not validar_sin_numeros(valor):
                texto_invalido = ctk.CTkLabel(frame_principal, text="El valor ingresado no debe contener numeros.", text_color="red")
                texto_invalido.pack(pady=10)
                texto_invalido.after(3000,lambda: eliminar_widget(texto_invalido))
                return

            if criterio == "Apellido" and not validar_sin_numeros(valor):
                texto_invalido = ctk.CTkLabel(frame_principal, text="El valor ingresado no debe contener numeros.", text_color="red")
                texto_invalido.pack(pady=10)
                texto_invalido.after(3000,lambda: eliminar_widget(texto_invalido))
                return
            
            # Buscar por criterio (ID, Nombre o Apellido)
            for persona in lista_diccionarios:
                if (criterio == 'ID' and persona['Legajo'] == valor) or \
                   (criterio == 'Nombre' and persona['Nombre'].lower() == valor) or \
                   (criterio == 'Apellido' and persona['Apellido'].lower() == valor):
                    resultado = persona
                    break  # Salir del bucle si se encuentra el resultado

            if resultado:
                mostrar_resultado_alumno(resultado)
            else:
                sin_coincidendias = ctk.CTkLabel(frame_principal, text="No se encontraron coincidencias.", text_color="red")
                sin_coincidendias.pack(pady=10)
                sin_coincidendias.after(3000,lambda: eliminar_widget(sin_coincidendias))

        boton_buscar = ctk.CTkButton(frame_principal, text="Buscar", fg_color="#061b2c", width=200, command=realizar_busqueda)
        boton_buscar.pack(pady=5)

        boton_volver = ctk.CTkButton(frame_principal, text="Volver", fg_color="#061b2c", width=200, command=mostrar_menu_busqueda)
        boton_volver.pack(pady=10)

    # Menu de buscar alumno
    def mostrar_menu_busqueda():

        for widget in frame_principal.winfo_children():
            widget.destroy()
            
        try:
            image = ctk.CTkImage(light_image=Image.open('archivosjson\\assets\\uade_una_gran_universidad.png'),
                                         size=(400, 240))
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            image = None
        
        if image:
            ctk.CTkLabel(frame_principal, image=image, text="").pack()  # Mostrar la imagen
        else:
            ctk.CTkLabel(frame_principal, text="No se pudo cargar la imagen").pack()
            
        ctk.CTkLabel(frame_principal, text="Programa de Notas Estudiantiles", font=("Arial", 24), text_color="#061b2c").pack(pady=5)
        ctk.CTkLabel(frame_principal, text="Opciones de búsqueda", font=("Arial", 20), text_color="#061b2c").pack(pady=5)

        boton_buscar_id = ctk.CTkButton(frame_principal, text="Buscar por Legajo", fg_color="#061b2c", width=200, command=lambda: buscar_por_criterio('ID'))
        boton_buscar_id.pack(pady=5)

        boton_buscar_nombre = ctk.CTkButton(frame_principal, text="Buscar por Nombre", fg_color="#061b2c", width=200, command=lambda: buscar_por_criterio('Nombre'))
        boton_buscar_nombre.pack(pady=5)

        boton_buscar_apellido = ctk.CTkButton(frame_principal, text="Buscar por Apellido", fg_color="#061b2c", width=200, command=lambda: buscar_por_criterio('Apellido'))
        boton_buscar_apellido.pack(pady=5)

        boton_volver = ctk.CTkButton(frame_principal, text="Volver", fg_color="#061b2c", width=175, command=frame_principal.master.mostrar_menu_principal)
        boton_volver.pack(pady=10)

    mostrar_menu_busqueda()  # Mostrar el menú de búsqueda al inicio