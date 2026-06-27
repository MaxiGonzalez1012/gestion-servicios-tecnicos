from data import database
import utilidades, clientes, trabajos, cobros, tecnicos, reportes, color

# ============================================================
#  PROGRAMA PRINCIPAL (menú)
# ============================================================

def main():
    utilidades.limpiarConsola()

    print(color.azul("=" * 50))
    print(color.azul("  SISTEMA DE GESTIÓN - SERVICIOS TÉCNICOS"))
    print(color.azul("=" * 50))
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
                utilidades.printPausa("Cerrando el sistema. ¡Hasta luego!")
                break
        
        except Exception as error:
            utilidades.printPausa("Ocurrió un error inesperado:", error)
            utilidades.printPausa("El sistema sigue funcionando.")

        except KeyboardInterrupt:
            utilidades.limpiarConsola()
            while True:
                salir = input("¿Está seguro que desea interrumpir el programa? (S/N): ").strip().lower()
                if salir in ("s", "n"):
                    break
                print("Por favor, ingrese un valor válido (S/N).")
            if salir == "s":
                utilidades.printPausa("Cerrando el programa...")
                break


if __name__ == "__main__":
    main()