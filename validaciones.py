def esNumero(cadena):
    #eliminamos todos los '-' y '.' para preguntar si es un digito.
    return cadena.replace("-", "", 1).replace(".", "", 1).isdigit()