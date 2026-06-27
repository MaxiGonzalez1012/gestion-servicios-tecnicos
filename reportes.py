import trabajos, utilidades
from data import database

# ============================================================
#  MÓDULO 5: REPORTES Y CONSULTAS
# ============================================================

def reporte_por_estado(estado):
    filtrados = [t for t in database.listTrabajos if t["estado"] == estado]
    utilidades.printPausa('')
    utilidades.printPausa("--- TRABAJOS:", estado.upper(), "---")
    if not filtrados:
        utilidades.printPausa("No hay trabajos en este estado.")
        return
    for t in filtrados:
        trabajos.mostrar_trabajo(t)


def reporte_cobros_pendientes():
    pendientes = [t for t in database.listTrabajos if t["estado_pago"] == "Pendiente"]
    utilidades.printPausa('')
    utilidades.printPausa('--- COBROS PENDIENTES ---')
    if not pendientes:
        utilidades.printPausa("No hay cobros pendientes. ¡Todo cobrado!")
        return
    total = 0.0
    for t in pendientes:
        trabajos.mostrar_trabajo(t)
        total += t["importe"]
    utilidades.printPausa('')
    utilidades.printPausa("TOTAL PENDIENTE DE COBRO: $", total)


def modulo_reportes():
    opcion = utilidades.pedir_opcion("=== REPORTES Y CONSULTAS ===",
                          ["Trabajos pendientes",
                           "Trabajos realizados",
                           "Trabajos incompletos",
                           "Trabajos reprogramados",
                           "Cobros pendientes",
                           "Volver"])
    if opcion == "Trabajos pendientes":
        reporte_por_estado("Pendiente")
    elif opcion == "Trabajos realizados":
        reporte_por_estado("Realizado")
    elif opcion == "Trabajos incompletos":
        reporte_por_estado("Incompleto")
    elif opcion == "Trabajos reprogramados":
        reporte_por_estado("Reprogramado")
    elif opcion == "Cobros pendientes":
        reporte_cobros_pendientes()