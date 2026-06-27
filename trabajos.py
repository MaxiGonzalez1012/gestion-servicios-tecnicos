import clientes, utilidades, tecnicos
from data import database

# ============================================================
#  MÓDULO 2: TRABAJOS
# ============================================================

def agregar_trabajo(id_actual):
    print('')
    print('--- NUEVO TRABAJO ---')
    if not database.listClientes:
        print("Primero cargá al menos un cliente.")
        return id_actual
    if not database.listTecnicos:
        print("Primero cargá al menos un técnico.")
        return id_actual

    clientes.listar_clientes()
    id_cli = utilidades.pedir_id("ID del cliente: ")
    if utilidades.buscar_por_id(database.listClientes, id_cli) is None:
        print("Ese cliente no existe.")
        return id_actual

    tecnicos.listar_tecnicos()
    id_tec = utilidades.pedir_id("ID del técnico asignado: ")
    if utilidades.buscar_por_id(database.listTecnicos, id_tec) is None:
        print("Ese técnico no existe.")
        return id_actual

    tipo = utilidades.pedir_opcion("Tipo de servicio:",
                        ["aire", "eléctrico", "soporte"])
    descripcion = input("Descripción del problema: ").strip()
    fecha = input("Fecha (dd/mm/aaaa): ").strip()
    horario = input("Horario: ").strip()

    trabajo = {
        "id": id_actual,
        "id_cliente": id_cli,
        "id_tecnico": id_tec,
        "tipo_servicio": tipo,
        "descripcion": descripcion,
        "fecha": fecha,
        "horario": horario,
        "estado": "Pendiente",
        # --- campos de cobro (Módulo 3) ---
        "importe": 0.0,
        "estado_pago": "Pendiente",
        "medio_pago": "",
    }
    database.listTrabajos.append(trabajo)
    print("Trabajo agregado con ID", id_actual)
    return id_actual + 1


def mostrar_trabajo(t):
    cliente = utilidades.buscar_por_id(database.listClientes, t["id_cliente"])
    tecnico = utilidades.buscar_por_id(database.listTecnicos, t["id_tecnico"])
    nombre_cli = cliente["nombre"] if cliente else "(cliente borrado)"
    nombre_tec = tecnico["nombre"] if tecnico else "(técnico borrado)"
    print("[", t["id"], "]", t["tipo_servicio"].upper(), "-", nombre_cli,
          "| Técnico:", nombre_tec, "|", t["fecha"], t["horario"])
    print("     Problema:", t["descripcion"])
    print("     Estado:", t["estado"], "| Pago:", t["estado_pago"],
          "( $", t["importe"], ")", t["medio_pago"])


def listar_trabajos():
    print('')
    print('--- LISTA DE TRABAJOS ---')
    if not database.listTrabajos:
        print("No hay trabajos cargados.")
        return
    for t in database.listTrabajos:
        mostrar_trabajo(t)


def editar_trabajo():
    listar_trabajos()
    id_buscado = utilidades.pedir_id("\nID del trabajo a editar: ")
    trabajo = utilidades.buscar_por_id(database.listTrabajos, id_buscado)
    if database.listTrabajos is None:
        print("No existe un trabajo con ese ID.")
        return
    if utilidades.pedir_opcion("¿Cambiar estado del trabajo?", ["si", "no"]) == "si":
        trabajo["estado"] = utilidades.pedir_opcion("Nuevo estado:", database.estados)
    if utilidades.pedir_opcion("¿Reasignar técnico?", ["si", "no"]) == "si":
        tecnicos.listar_tecnicos()
        id_tec = utilidades.pedir_id("ID del nuevo técnico: ")
        if utilidades.buscar_por_id(database.listTecnicos, id_tec):
            trabajo["id_tecnico"] = id_tec
        else:
            print("Técnico inexistente, no se cambió.")
    nueva_fecha = input("Fecha [" + trabajo["fecha"] + "] (Enter mantiene): ").strip()
    if nueva_fecha:
        trabajo["fecha"] = nueva_fecha
    print("Trabajo actualizado.")


def eliminar_trabajo():
    listar_trabajos()
    id_buscado = utilidades.pedir_id("\nID del trabajo a eliminar: ")
    trabajo = utilidades.buscar_por_id(database.listTrabajos, id_buscado)
    if trabajo is None:
        print("No existe un trabajo con ese ID.")
        return
    database.listTrabajos.remove(trabajo)
    print("Trabajo eliminado.")


def modulo_trabajos(id_actual):
    opcion = utilidades.pedir_opcion("=== TRABAJOS ===",
                          ["Agregar", "Listar", "Editar estado/datos",
                           "Eliminar", "Volver"])
    if opcion == "Agregar":
        id_actual = agregar_trabajo(id_actual)
        database.guardar_todo()
    elif opcion == "Listar":
        listar_trabajos()
    elif opcion == "Editar estado/datos":
        editar_trabajo()
        database.guardar_todo()
    elif opcion == "Eliminar":
        eliminar_trabajo()
        database.guardar_todo()
    return id_actual