from email.mime import image
from variables_globales import NOTA_APROBACION
import customtkinter as ctk
from PIL import Image

def clasificar_parcial(alumnos, parcial, nota_aprobacion):
    aprobados = []
    desaprobados = []

    for alumno in alumnos:
        legajo = alumno['Legajo']
        nombre = alumno['Nombre']
        apellido = alumno['Apellido']
        if parcial in alumno:
            nota = alumno[parcial]
            if nota.isdigit():
                nota = int(nota)
                if nota >= nota_aprobacion:
                    aprobados.append((legajo, nombre, apellido, nota))
                else:
                    desaprobados.append((legajo, nombre, apellido, nota))
            else:
                return f"Error: La nota '{nota}' no es un número válido."
        else:
            return f"Error: La columna '{parcial}' no existe en los datos."

    return aprobados, desaprobados


def ejecutar_opcion_parcial(opcion_parcial, lista_diccionarios, frame_principal):
    if opcion_parcial == '1':
        parcial = 'nota1'
        parcial_nombre = '1er Parcial'
    elif opcion_parcial == '2':
        parcial = 'nota2'
        parcial_nombre = '2do Parcial'
    else:
        return "Opción no válida."

    # Clasificar alumnos en aprobados y desaprobados
    aprobados, desaprobados = clasificar_parcial(lista_diccionarios, parcial, NOTA_APROBACION)

    # Mostrar botones para ver aprobados y desaprobados
    mostrar_botones_resultados(frame_principal, aprobados, desaprobados, parcial_nombre)


def mostrar_botones_resultados(frame_principal, aprobados, desaprobados, parcial_nombre):
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
        
    ctk.CTkLabel(frame_principal, text="Programa de Notas Estudiantiles", font=("#061b2c", 24), text_color="black").pack(pady=5)
    ctk.CTkLabel(frame_principal, text="Notas de Parciales", font=("Arial", 20), text_color="#061b2c").pack(pady=5)

    # Crear botones para mostrar aprobados y desaprobados
    boton_aprobados = ctk.CTkButton(frame_principal, text=f"Mostrar Aprobados", fg_color="#061b2c", width=200,
                                     command=lambda: mostrar_resultados(frame_principal, aprobados, parcial_nombre, "aprobados"))
    boton_aprobados.pack(pady=5)

    boton_desaprobados = ctk.CTkButton(frame_principal, text=f"Mostrar Desaprobados", fg_color="#061b2c", width=200,
                                        command=lambda: mostrar_resultados(frame_principal, desaprobados, parcial_nombre, "desaprobados"))
    boton_desaprobados.pack(pady=5)

    # Botón para Volver anterior
    boton_volver = ctk.CTkButton(frame_principal, text="Volver", fg_color="#061b2c", width=175, 
                                  command=lambda: frame_principal.master.mostrar_menu_parcial())
    boton_volver.pack(pady=10)


def mostrar_resultados(frame_principal, lista, parcial_nombre, tipo):
    # Limpiar el frame antes de mostrar resultados
    for widget in frame_principal.winfo_children():
        widget.destroy()
    try:
        image = ctk.CTkImage(light_image=Image.open('archivosjson\\assets\\uade_una_gran_universidad.png'),
                                         size=(200, 120))
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        image = None
        
    if image:
        ctk.CTkLabel(frame_principal, image=image, text="").pack()  # Mostrar la imagen
    else:
        ctk.CTkLabel(frame_principal, text="No se pudo cargar la imagen").pack()

    resultados_text = f"{parcial_nombre.upper()} - {tipo.upper()}\n"
    if lista:
        for alumno in lista:
            resultados_text += f"Legajo: {alumno[0]}, Apellido: {alumno[2]}, Nombre: {alumno[1]}, Nota {parcial_nombre}: {alumno[3]}\n"
    else:
        resultados_text += f"No hay alumnos {tipo}.\n"

    # Mostrar el resultado en un textbox en la ventana
    resultados_textbox = ctk.CTkTextbox(frame_principal, width=500, height=300)
    resultados_textbox.pack(pady=10)
    resultados_textbox.insert("0.0", resultados_text)
    resultados_textbox.configure(state="disabled")  # Deshabilitar edición del textbox

    # Botón para Volver al menu anterior
    boton_volver = ctk.CTkButton(frame_principal, text="Volver", fg_color="#061b2c", width=175, 
                                  command=lambda: frame_principal.master.mostrar_menu_parcial())
    boton_volver.pack(pady=10)
