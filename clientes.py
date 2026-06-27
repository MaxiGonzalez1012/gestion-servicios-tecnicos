from data import database
import utilidades

# ============================================================
#  MÓDULO 1: CLIENTES
# ============================================================

def agregar_cliente(id_actual):
    utilidades.printPausa('')
    utilidades.printPausa('--- NUEVO CLIENTE ---')
    nombre = input("Nombre (persona o empresa): ").strip().title()
    telefono = utilidades.pedir_entero("Teléfono (solo números): ")
    direccion = input("Dirección: ").strip().title()
    piso_depto = input("Piso/Depto (Enter si no corresponde): ").strip()
    observaciones = input("Observaciones: ").strip()
    es_empresa = utilidades.pedir_opcion("¿Es empresa/consorcio?", ["si", "no"]) == "si"

    cliente = {
        "id": id_actual,
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion,
        "piso_depto": piso_depto,
        "observaciones": observaciones,
        "es_empresa": es_empresa,
    }
    database.listClientes.append(cliente)
    utilidades.printPausa("Cliente agregado con ID", id_actual)
    return id_actual + 1


def listar_clientes():
    utilidades.printPausa('')
    utilidades.printPausa('--- LISTA DE CLIENTES ---')
    if not database.listClientes:
        utilidades.printPausa("No hay clientes cargados.")
        return
    for c in database.listClientes:
        tipo = "EMPRESA" if c["es_empresa"] else "particular"
        piso = c["piso_depto"] if c["piso_depto"] else "-"
        utilidades.printPausa("[", c["id"], "]", c["nombre"], "(", tipo, ") - Tel:",
              c["telefono"], "-", c["direccion"], "-", piso)


def editar_cliente():
    listar_clientes()
    id_buscado = utilidades.pedir_id("\nID del cliente a editar: ")
    cliente = utilidades.buscar_por_id(database.listClientes, id_buscado)
    if cliente is None:
        utilidades.printPausa("No existe un cliente con ese ID.")
        return
    utilidades.printPausa("Dejá vacío (Enter) para mantener el valor actual.")
    nuevo_nombre = input("Nombre [" + cliente["nombre"] + "]: ").strip().title()
    if nuevo_nombre:
        cliente["nombre"] = nuevo_nombre
    if utilidades.pedir_opcion("¿Cambiar teléfono?", ["si", "no"]) == "si":
        cliente["telefono"] = utilidades.pedir_entero("Nuevo teléfono (solo números): ")
    nueva_dir = input("Dirección [" + cliente["direccion"] + "]: ").strip().title()
    if nueva_dir:
        cliente["direccion"] = nueva_dir
    nuevo_piso = input("Piso/Depto [" + cliente["piso_depto"] + "]: ").strip()
    if nuevo_piso:
        cliente["piso_depto"] = nuevo_piso
    utilidades.printPausa("Cliente actualizado.")


def eliminar_cliente():
    listar_clientes()
    id_buscado = utilidades.pedir_id("\nID del cliente a eliminar: ")
    cliente = utilidades.buscar_por_id(database.listClientes, id_buscado)
    if cliente is None:
        utilidades.printPausa("No existe un cliente con ese ID.")
        return
    # Aviso si tiene trabajos asociados
    asociados = [t for t in database.listTrabajos if t["id_cliente"] == id_buscado]
    if asociados:
        utilidades.printPausa("Atención: este cliente tiene", len(asociados), "trabajo(s) asociado(s).")
        if utilidades.pedir_opcion("¿Eliminar igual?", ["si", "no"]) == "no":
            utilidades.printPausa("Cancelado.")
            return
    database.listClientes.remove(cliente)
    utilidades.printPausa("Cliente eliminado.")


def modulo_clientes(id_actual):
    opcion = utilidades.pedir_opcion("=== CLIENTES ===",
                          ["Agregar", "Listar", "Editar", "Eliminar", "Volver"])
    if opcion == "Agregar":
        id_actual = agregar_cliente(id_actual)
        database.guardar_todo()
    elif opcion == "Listar":
        listar_clientes()
    elif opcion == "Editar":
        editar_cliente()
        database.guardar_todo()
    elif opcion == "Eliminar":
        eliminar_cliente()
        database.guardar_todo()
    return id_actual