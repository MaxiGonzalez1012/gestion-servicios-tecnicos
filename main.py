from data import database
import utilidades, clientes, trabajos, cobros, tecnicos, reportes

# ============================================================
#  PROGRAMA PRINCIPAL (menú)
# ============================================================

def main():
    print("=" * 50)
    print("  SISTEMA DE GESTIÓN - SERVICIOS TÉCNICOS")
    print("=" * 50)

    # Cargo los datos guardados de sesiones anteriores (si los hay).
    database.cargar_todo()

    # Contadores para generar IDs únicos. Arrancan despues del ultimo
    # ID que ya exista en los archivos, asi no se repiten.
    id_cliente_actual = database.proximo_id(database.listClientes)
    id_tecnico_actual = database.proximo_id(database.listTecnicos)
    id_trabajo_actual = database.proximo_id(database.listTrabajos)

    while True:
        try:
            opcion = utilidades.pedir_opcion("========= MENÚ PRINCIPAL =========",
                                  ["Clientes", "Trabajos", "Cobros",
                                   "Técnicos", "Reportes y Consultas", "Salir"])
            utilidades.limpiarConsola()
            if opcion == "Clientes":
                id_cliente_actual = clientes.modulo_clientes(id_cliente_actual)
                input("Presione enter para continuar...")
                utilidades.limpiarConsola()
            elif opcion == "Trabajos":
                id_trabajo_actual = trabajos.modulo_trabajos(id_trabajo_actual)
                input("Presione enter para continuar...")
                utilidades.limpiarConsola()
            elif opcion == "Cobros":
                cobros.modulo_cobros()
                input("Presione enter para continuar...")
                utilidades.limpiarConsola()
            elif opcion == "Técnicos":
                id_tecnico_actual = tecnicos.modulo_tecnicos(id_tecnico_actual)
                input("Presione enter para continuar...")
                utilidades.limpiarConsola()
            elif opcion == "Reportes y Consultas":
                reportes.modulo_reportes()
                input("Presione enter para continuar...")
                utilidades.limpiarConsola()
            elif opcion == "Salir":
                print("Cerrando el sistema. ¡Hasta luego!")
                break
        
        except Exception as error:
            print("Ocurrió un error inesperado:", error)
            print("El sistema sigue funcionando.")


if __name__ == "__main__":
    main()