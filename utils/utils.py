def validar_es_numero(valor):
    try:
        float(valor)  # Intenta convertir el valor a un número
        return True   # Si lo logra, el valor es numérico
    except ValueError:
        return False  # Si falla, no es un número
def validar_numero_rango(valor):
    try:
        numero = float(valor)  # Convertimos el valor a número
        return 0 <= numero <= 100  # Validamos que esté entre 0 y 100
    except ValueError:
        return False  # Si no es un número, retorna False
def validar_sin_numeros(valor):
    return not any(char.isdigit() for char in valor)

def eliminar_widget(widget):
    widget.destroy()  
    return