import trabajos, utilidades
from data import database

# ============================================================
#  MÓDULO 3: COBROS
# ============================================================

# Define cuanto se cobra por un trabajo.
def registrar_importe():
    trabajos.listar_trabajos()
    id_buscado = utilidades.pedir_id("\nID del trabajo: ")
    trabajo = utilidades.buscar_por_id(database.listTrabajos, id_buscado)
    if trabajo is None:
        utilidades.printPausa("No existe un trabajo con ese ID.")
        return
    trabajo["importe"] = utilidades.pedir_decimal("Importe a cobrar: ")
    utilidades.printPausa("Importe registrado.")


# Marca un trabajo como pagado e indica el medio.
def registrar_pago():
    pendientes = [t for t in database.listTrabajos if t["estado_pago"] == "Pendiente"]
    if not pendientes:
        utilidades.printPausa("No hay trabajos pendientes de cobro.")
        return
    utilidades.printPausa('')
    utilidades.printPausa('--- TRABAJOS PENDIENTES DE COBRO ---')
    for t in pendientes:
        trabajos.mostrar_trabajo(t)
    id_buscado = utilidades.pedir_id("\nID del trabajo cobrado: ")
    trabajo = utilidades.buscar_por_id(database.listTrabajos, id_buscado)
    if trabajo is None or trabajo["estado_pago"] == "Pagado":
        utilidades.printPausa("Trabajo inexistente o ya cobrado.")
        return
    trabajo["medio_pago"] = utilidades.pedir_opcion("Medio de pago:", database.medios_pago)
    trabajo["estado_pago"] = "Pagado"
    utilidades.printPausa("Pago registrado. El trabajo sale de los pendientes.")


# Liquidacion: todos los trabajos impagos de un cliente empresa.
def cobros_pendientes_por_empresa():
    empresas = [c for c in database.listClientes if c["es_empresa"]]
    if not empresas:
        utilidades.printPausa("No hay clientes empresariales cargados.")
        return
    utilidades.printPausa('')
    utilidades.printPausa('--- EMPRESAS ---')
    for c in empresas:
        utilidades.printPausa("[", c["id"], "]", c["nombre"])
    id_cli = utilidades.pedir_id("ID de la empresa: ")
    cliente = utilidades.buscar_por_id(database.listClientes, id_cli)
    if cliente is None:
        utilidades.printPausa("Cliente inexistente.")
        return
    pendientes = [t for t in database.listTrabajos
                  if t["id_cliente"] == id_cli and t["estado_pago"] == "Pendiente"]
    if not pendientes:
        utilidades.printPausa(cliente["nombre"], "no tiene trabajos pendientes de cobro.")
        return
    utilidades.printPausa('')
    utilidades.printPausa("--- LIQUIDACIÓN:", cliente["nombre"], "---")
    total = 0.0
    for t in pendientes:
        trabajos.mostrar_trabajo(t)
        total += t["importe"]
    utilidades.printPausa('')
    utilidades.printPausa("TOTAL A COBRAR: $", total)


def modulo_cobros():
    opcion = utilidades.pedir_opcion("=== COBROS ===",
                          ["Registrar importe de un trabajo",
                           "Registrar pago",
                           "Liquidación por empresa",
                           "Volver"])
    if opcion == "Registrar importe de un trabajo":
        registrar_importe()
        database.guardar_todo()
    elif opcion == "Registrar pago":
        registrar_pago()
        database.guardar_todo()
    elif opcion == "Liquidación por empresa":
        cobros_pendientes_por_empresa()