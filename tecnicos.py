import utilidades
from data import database

# ============================================================
#  MÓDULO 4: TÉCNICOS
# ============================================================

def agregar_tecnico(id_actual):
    print('')
    print('--- NUEVO TÉCNICO ---')
    nombre = input("Nombre: ").strip().title()
    especialidad = utilidades.pedir_opcion("Especialidad:",
                                ["refrigeración", "eléctrica", "trabajos simples"])
    disponible = utilidades.pedir_opcion("¿Disponible?", ["si", "no"]) == "si"

    tecnico = {
        "id": id_actual,
        "nombre": nombre,
        "especialidad": especialidad,
        "disponible": disponible,
    }
    database.listTecnicos.append(tecnico)
    print("Técnico agregado con ID", id_actual)
    return id_actual + 1


def listar_tecnicos():
    print('')
    print('--- LISTA DE TÉCNICOS ---')
    if not database.listTecnicos:
        print("No hay técnicos cargados.")
        return
    for t in database.listTecnicos:
        disp = "disponible" if t["disponible"] else "ocupado"
        print("[", t["id"], "]", t["nombre"], "-", t["especialidad"], "(", disp, ")")


def editar_tecnico():
    listar_tecnicos()
    id_buscado = utilidades.pedir_id("\nID del técnico a editar: ")
    tecnico = utilidades.buscar_por_id(database.listTecnicos, id_buscado)
    if tecnico is None:
        print("No existe un técnico con ese ID.")
        return
    nuevo_nombre = input("Nombre [" + tecnico["nombre"] + "] (Enter mantiene): ").strip().title()
    if nuevo_nombre:
        tecnico["nombre"] = nuevo_nombre
    if utilidades.pedir_opcion("¿Cambiar especialidad?", ["si", "no"]) == "si":
        tecnico["especialidad"] = utilidades.pedir_opcion("Nueva especialidad:",
                                               ["refrigeración", "eléctrica", "trabajos simples"])
    tecnico["disponible"] = utilidades.pedir_opcion("¿Disponible?", ["si", "no"]) == "si"
    print("Técnico actualizado.")


def eliminar_tecnico():
    listar_tecnicos()
    id_buscado = utilidades.pedir_id("\nID del técnico a eliminar: ")
    tecnico = utilidades.buscar_por_id(database.listTecnicos, id_buscado)
    if tecnico is None:
        print("No existe un técnico con ese ID.")
        return
    database.listTecnicos.remove(tecnico)
    print("Técnico eliminado.")


def modulo_tecnicos(id_actual):
    opcion = utilidades.pedir_opcion("=== TÉCNICOS ===",
                          ["Agregar", "Listar", "Editar", "Eliminar", "Volver"])
    if opcion == "Agregar":
        id_actual = agregar_tecnico(id_actual)
        database.guardar_todo()
    elif opcion == "Listar":
        listar_tecnicos()
    elif opcion == "Editar":
        editar_tecnico()
        database.guardar_todo()
    elif opcion == "Eliminar":
        eliminar_tecnico()
        database.guardar_todo()
    return id_actual