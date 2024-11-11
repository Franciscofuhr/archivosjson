from variables_globales import NOTA_APROBACION, NOTA_PROMOCION
import customtkinter as ctk
from PIL import Image

def clasificar_cursada(alumnos, nota_aprobacion, nota_promocion):
    promocionados = []
    aprobados = []
    aplazados = []

    #Tomar datos de alumnos
    for alumno in alumnos:
        legajo = alumno['Legajo']
        nombre = alumno['Nombre']
        apellido = alumno['Apellido']
        if 'nota1' in alumno and 'nota2' in alumno:
            nota1 = alumno['nota1']
            nota2 = alumno['nota2']
            if nota1.isdigit() and nota2.isdigit():
                nota1 = int(nota1)
                nota2 = int(nota2)
                # Clasificación
                if nota1 >= nota_promocion and nota2 >= nota_promocion:
                    promocionados.append((legajo, nombre, apellido, nota1, nota2))
                elif nota1 >= nota_aprobacion and nota2 >= nota_aprobacion:
                    aprobados.append((legajo, nombre, apellido, nota1, nota2))
                else:
                    aplazados.append((legajo, nombre, apellido, nota1, nota2))
    
    return promocionados, aprobados, aplazados

def mostrar_resultados(frame_principal, lista, tipo):
    for widget in frame_principal.winfo_children():
        widget.destroy()
        
    try:
        image = ctk.CTkImage(light_image=Image.open("archivosjson\\assets\\uade_una_gran_universidad.png"),
                                         size=(200, 120))
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        image = None
        
    if image:
        ctk.CTkLabel(frame_principal, image=image, text="").pack()
    else:
        ctk.CTkLabel(frame_principal, text="No se pudo cargar la imagen").pack()

    resultados_text = f"{tipo.upper()}\n" # Almacenar datos
    
    # Cargar datos si hay
    if lista:
        for alumno in lista:
            resultados_text += f"Legajo: {alumno[0]}, {alumno[1]} {alumno[2]}: 1er Parcial: {alumno[3]} / 2do Parcial: {alumno[4]}\n"
    else:
        resultados_text += f"No hay alumnos {tipo}.\n"

    # Mostrar el resultado en un textbox en la ventana
    resultados_textbox = ctk.CTkTextbox(frame_principal, width=500, height=300)
    resultados_textbox.pack(pady=10)
    resultados_textbox.insert("0.0", resultados_text)
    resultados_textbox.configure(state="disabled")  # Deshabilitar edición del textbox

    # Botón para volver al menú anterior
    boton_volver = ctk.CTkButton(frame_principal, text="Volver al menú anterior", fg_color="#061b2c", width=175, 
                                  command=lambda: mostrar_menu_cursada(frame_principal, frame_principal.master.lista_diccionarios))
    boton_volver.pack(pady=5)

# Mostrar las opciones de promoción, aprobación y aplazamiento en el frame.
def mostrar_menu_cursada(frame, lista_diccionarios):
    
    for widget in frame.winfo_children():
        widget.destroy()
        
    try:
        image = ctk.CTkImage(light_image=Image.open("archivosjson\\assets\\uade_una_gran_universidad.png"),
                                         size=(400, 240))
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        image = None
        
    if image:
        ctk.CTkLabel(frame, image=image, text="").pack()  # Mostrar la imagen
    else:
        ctk.CTkLabel(frame, text="No se pudo cargar la imagen").pack()
        
    ctk.CTkLabel(frame, text="Programa de Notas Estudiantiles", font=("#061b2c", 24), text_color="black").pack(pady=5)    
    ctk.CTkLabel(frame, text="Estado de Cursada", font=("Arial", 20), text_color="#061b2c").pack(pady=5)

    # Clasificar los alumnos una sola vez y mostrar los resultados
    promocionados, aprobados, aplazados = clasificar_cursada(lista_diccionarios, NOTA_APROBACION, NOTA_PROMOCION)

    # Botones de opción de clasificación
    boton_promocionados = ctk.CTkButton(frame, text="Ver Promocionados", fg_color="#061b2c", width=200, 
                                          command=lambda: mostrar_resultados(frame, promocionados, "Promocionados"))
    boton_promocionados.pack(pady=5)

    boton_aprobados = ctk.CTkButton(frame, text="Ver Aprobados", fg_color="#061b2c", width=200, 
                                      command=lambda: mostrar_resultados(frame, aprobados, "Aprobados"))
    boton_aprobados.pack(pady=5)

    boton_aplazados = ctk.CTkButton(frame, text="Ver Aplazados", fg_color="#061b2c", width=200, 
                                      command=lambda: mostrar_resultados(frame, aplazados, "Aplazados"))
    boton_aplazados.pack(pady=5)

    boton_volver = ctk.CTkButton(frame, text="Volver al menú principal", fg_color="#061b2c", width=175, 
                                  command=lambda: frame.master.mostrar_menu_principal())
    boton_volver.pack(pady=5)
    
#Inicia la opción de cursada, mostrando el menú.
def ejecutar_opcion_cursada(lista_diccionarios, frame_principal):
    mostrar_menu_cursada(frame_principal, lista_diccionarios)
