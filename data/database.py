# ============================================================
#  PERSISTENCIA EN ARCHIVOS (CSV separado por ;)
# ============================================================
# Nombres de los tres archivos donde se guardan los datos.
ARCHIVO_CLIENTES = "data/clientes.txt"
ARCHIVO_TECNICOS = "data/tecnicos.txt"
ARCHIVO_TRABAJOS = "data/trabajos.txt"

listClientes = []
listTecnicos = []
listTrabajos = []

# Valores válidos (sacados del análisis - Módulo 2 y 3)
estados = ["Pendiente", "Realizado", "Incompleto", "Reprogramado", "Cancelado"]
medios_pago = ["Efectivo", "Transferencia"]

# Guarda una lista de diccionarios en un archivo.
# 'campos' es el orden en que se escriben las columnas.
def guardar_lista(nombre_archivo, lista, campos):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for elemento in lista:
            # Convierto cada campo a texto y los uno con ;
            valores = [str(elemento[c]) for c in campos]
            f.write(";".join(valores) + "\n")


# Guarda las tres listas. Se llama cada vez que algo cambia.
def guardar_todo():
    guardar_lista(ARCHIVO_CLIENTES, listClientes,
                  ["id", "nombre", "telefono", "direccion",
                   "piso_depto", "observaciones", "es_empresa"])
    guardar_lista(ARCHIVO_TECNICOS, listTecnicos,
                  ["id", "nombre", "especialidad", "disponible"])
    guardar_lista(ARCHIVO_TRABAJOS, listTrabajos,
                  ["id", "id_cliente", "id_tecnico", "tipo_servicio",
                   "descripcion", "fecha", "horario", "estado",
                   "importe", "estado_pago", "medio_pago"])


# Lee un archivo y devuelve una lista de listas (cada linea separada por ;).
# Si el archivo no existe todavia, devuelve una lista vacia.
def leer_archivo(nombre_archivo):
    filas = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:  # ignoro lineas vacias
                    filas.append(linea.split(";"))
    except FileNotFoundError:
        pass  # primera vez que se ejecuta: todavia no hay archivo
    return filas


# Carga las tres listas desde los archivos al arrancar el programa.
def cargar_todo():
    for fila in leer_archivo(ARCHIVO_CLIENTES):
        listClientes.append({
            "id": int(fila[0]),
            "nombre": fila[1],
            "telefono": fila[2],
            "direccion": fila[3],
            "piso_depto": fila[4],
            "observaciones": fila[5],
            "es_empresa": fila[6] == "True",
        })
    for fila in leer_archivo(ARCHIVO_TECNICOS):
        listTecnicos.append({
            "id": int(fila[0]),
            "nombre": fila[1],
            "especialidad": fila[2],
            "disponible": fila[3] == "True",
        })
    for fila in leer_archivo(ARCHIVO_TRABAJOS):
        listTrabajos.append({
            "id": int(fila[0]),
            "id_cliente": int(fila[1]),
            "id_tecnico": int(fila[2]),
            "tipo_servicio": fila[3],
            "descripcion": fila[4],
            "fecha": fila[5],
            "horario": fila[6],
            "estado": fila[7],
            "importe": float(fila[8]),
            "estado_pago": fila[9],
            "medio_pago": fila[10],
        })


# Devuelve el proximo ID a usar: el mayor ID de la lista + 1.
def proximo_id(lista):
    if not lista:
        return 1
    mayor = 0
    for elemento in lista:
        if elemento["id"] > mayor:
            mayor = elemento["id"]
    return mayor + 1