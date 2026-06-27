import utilidades
from data import database

def iniciarSesion():
    banner = """
          Sistema de gestion de servicios tecnivos
    """

    print(utilidades.azul(banner))

    while True:
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        usuarioEncontrado = database.obtenerPrimeroPorUser(usuario)
        contraseñaValida = database.verificarContraseña(usuarioEncontrado, contraseña)

        if usuarioEncontrado and contraseñaValida:
            return usuarioEncontrado

        print("Usuario o Contraseña incorrecta. Intentelo nuevamente...")
