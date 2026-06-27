import validaciones

def convertirLineaDict(linea, nombresCampos):
    '''
        Recibe una 'linea' como string y los 'nombresCampos' en una lista. Devuelve un dict referenciando key y value.
        Parsea campos que sean int, float o bool a su tipo en python.
    '''

    registro = {}
    valores = linea.strip().split(';')

    for campoIndex in range(len(nombresCampos)):
        campo = nombresCampos[campoIndex]
        valor: str = valores[campoIndex]

        if valor.lower() == "true":
            valor = True
        elif valor.lower() == "false":
            valor = False
        elif validaciones.esNumero(valor):
            try:
                valor = int(valor)
            except:
                valor = float(valor)

        registro[campo] = valor

    return registro

def obtenerPrimeroPorUser(nombre):
    return buscarRegistro("clientes", condicionLambda=lambda reg: reg["nombre"] == nombre)

def buscarRegistro(nombreTabla, condicionLambda):
    '''
        Busca registro en el archivo usando 'idKey' como la columna que debe buscar e 'idValor' como el valor que debe encontrar.
        Devuelve un diccionario del registro encontrado o None
    '''
    try:
        with open(nombreTabla + ".csv", mode='r', encoding='utf-8') as arch:
            nombresCampos = arch.readline().strip().split(';')

            for linea in arch:
                registroDict = convertirLineaDict(linea, nombresCampos)
                
                if condicionLambda(registroDict):
                    return registroDict
    except OSError as msg:
        print(f"ERROR abriendo el archivo: {msg}")

def verificarContraseña():
    pass