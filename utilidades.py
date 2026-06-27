import time, os

def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

# ============================================================
#  FUNCIONES AUXILIARES
# ============================================================
# Pide al usuario elegir de una lista de opciones validas.
def pedir_opcion(mensaje, opciones):
    print(mensaje)
    for i, op in enumerate(opciones, start=1):
        print(" ", i, "-", op)
    while True:
        eleccion = input("Elegí una opción: ").strip()
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(opciones):
            return opciones[int(eleccion) - 1]
        print("Opción inválida, probá de nuevo.")


# Devuelve el diccionario con ese id, o None si no existe.
def buscar_por_id(lista, id_buscado):
    for elemento in lista:
        if elemento["id"] == id_buscado:
            return elemento
    return None


# Pide un numero entero (un id). Insiste si meten algo invalido,
# pero un Enter vacio devuelve None para poder cancelar.
def pedir_id(texto):
    while True:
        valor = input(texto).strip()
        if valor == "":
            return None
        if valor.isdigit():
            return int(valor)
        print("Ingresá un número de ID, o Enter para cancelar.")


# Valida que sean solo números, pero devuelve el valor como texto (str).
# Así no se pierde un 0 al principio, por ejemplo en teléfonos tipo 011...
def pedir_entero(texto):
    while True:
        valor = input(texto).strip()
        if valor.isdigit():
            return valor
        print("Tenés que ingresar solo números. Probá de nuevo.")


# Pide un numero (puede tener decimales) y valida con un while.
def pedir_decimal(texto):
    while True:
        valor = input(texto).strip()
        try:
            return float(valor)
        except ValueError:
            print("Tenés que ingresar un número válido. Probá de nuevo.")