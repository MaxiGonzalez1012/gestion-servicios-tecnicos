import utilidades, menu, admin

def main():
    while True:
        try:
            utilidades.limpiarConsola()
            admin = admin.iniciarSesion()
            utilidades.limpiarConsola()

            menu.menuInicial()
        except KeyboardInterrupt:
            utilidades.limpiarConsola()

            exit = utilidades.validarInputs(
                tipo=str, 
                prompt="¿Esta seguro que desea interrumpir el programa? (S/N): ", 
                validador=lambda s: None if s.lower() == "s" or s.lower() == "n" else "Porfavor, ingrese un valor valido (S/N): "
            ).lower()
            
            if exit == "s":
                print("Cerrando el programa...")
                break

if __name__ == "__main__":
    main()