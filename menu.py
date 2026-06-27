import utilidades

def menuBasico(opciones, obtenerTexto: lambda: "Bienvenido!"):
    opcion = 0

    while True:
        opcion = utilidades.elegirOpcion(
            "Elegí una opción: ", 
            list(map(lambda elemento: elemento["opcion"], opciones)),
            obtenerTexto()
        )

        utilidades.limpiarConsola()
        opciones[opcion]["funcion"]()   
        utilidades.limpiarConsola()

        if opcion == 6:
            break
        elif opcion == 7:
            return -1

def menuInicial():
    opciones = [
        { "opcion": "Clientes", "funcion": lambda: menuClientes()}, # 1
        { "opcion": "Técnicos",}, # 2
        { "opcion": "Trabajos",}, # 3
        { "opcion": "Cobros",}, # 4
        { "opcion": "Reportes y consultas",}, # 5
        { "opcion": "Salir", "funcion": lambda: utilidades.saludoFin()} # 6
    ]

    return menuBasico(
        opciones, 
        lambda: f"Bienvenido/a"
    )

def menuClientes():
    opciones = [
        { "opcion": "Registrar cliente", }, # 1
        { "opcion": "Listar clientes",}, # 2
        { "opcion": "Buscar cliente",}, # 3
        { "opcion": "Modificar cliente",}, # 4
        { "opcion": "Volver", } # 5
    ]

    return menuBasico(
        opciones, 
        lambda: f"Bienvenido/a"
    )