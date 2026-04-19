

from Validate import validate_number, validate_length

# ── INGRESO USUARIO - NÚMERO ENTERO ──────────────────────────────────────────────────────

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:

    """
    Función que solicita al usuario el ingreso de un número ENTERO y lo valida.
    mensaje: Mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
    mensaje_error: Mensaje de error en el caso de que el dato ingresado sea invalido.
    mínimo: Valor mínimo admitido (inclusive)
    máximo: Valor máximo admitido (inclusive)
    reintentos: Cantidad de veces que se volverá a pedir el dato en caso de error.
    return: Número ingresado o None

    """
    contador_intentos = 0

    while contador_intentos < reintentos:
        numero_usuario = int(input(mensaje))
        if validate_number(numero_usuario, minimo, maximo):
            print(f"USTED HA INGRESADO EL NÚMERO {numero_usuario}.")
            return numero_usuario
        else:
            print(mensaje_error)
            contador_intentos += 1
            
    print("USTED HA ALCANZADO EL LÍMITE DE INTENTOS")
    return None


# ── INGRESO USUARIO - NÚMERO DECIMAL ──────────────────────────────────────────────────────

def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float|None:

    """
    Función que solicita al usuario el ingreso de un número DECIMAL y lo valida.
    mensaje: Mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
    mensaje_error: Mensaje de error en el caso de que el dato ingresado sea invalido.
    mínimo: Valor mínimo admitido (inclusive)
    máximo: Valor máximo admitido (inclusive)
    reintentos: Cantidad de veces que se volverá a pedir el dato en caso de error.
    return: Número ingresado o None

    """
    contador_intentos = 0

    while contador_intentos < reintentos:
        numero_usuario = float(input(mensaje))
        if numero_usuario >= minimo and numero_usuario <= maximo:
            print(f"USTED HA INGRESADO EL NÚMERO {numero_usuario}.")
            return numero_usuario
        else:
            print(mensaje_error)
            contador_intentos += 1
            
    print("USTED HA ALCANZADO EL LÍMITE DE INTENTOS")
    return None

# ── INGRESO USUARIO - STRING ──────────────────────────────────────────────────────

longitud = 5

def get_string(mensaje: str, mensaje_error: str, reintentos: int, longitud_string: int) -> str|None:

    """
    Función que solicita al usuario el ingreso de un STRING, valida su cantidad de catacteres y la retorna.
    mensaje: Mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
    mensaje_error: Mensaje de error en el caso de que el dato ingresado sea invalido.
    longitud: La cantidad de catacteres que deberá tener el STRING.
    return: Número ingresado o None.

    """
    
    texto_usuario = True
    contador_intentos = 0

    while contador_intentos < reintentos:
        texto_usuario = input(mensaje)
        if validate_length(texto_usuario, longitud_string):
            print(f"LA PALABRA INGRESADA ES {texto_usuario.upper()}.")
            return texto_usuario
        else: 
            print(mensaje_error)
            contador_intentos += 1
            
    print(f"LÍMITE DE {reintentos} INTENTOS ALCANZADO.")
    return None


# ── LLAMADAS A FUNCIONES ──────────────────────────────────────────────────────

get_int(
    mensaje="INGRESE UN NÚMERO ENTERO ENTRE 1 Y 200: ",
    mensaje_error="ERROR! INGRESE UN NÚMERO VÁLIDO: ",
    minimo=1,
    maximo=200,
    reintentos=2
)

get_float(
    mensaje="INGRESE UN NÚMERO DECIMAL ENTRE 1.1 Y 199.9: ",
    mensaje_error="ERROR! INGRESE UN NÚMERO VÁLIDO: ",
    minimo=1.1,
    maximo=199.9,
    reintentos=2
)

get_string(
    mensaje="INGRESE UNA PALABRA DE AL MENOS 5 LETRAS: ",
    mensaje_error="ERROR! LA PALABRA INGRESADA NO ES VÁLIDA: ",
    longitud_string=longitud,
    reintentos=3
)
