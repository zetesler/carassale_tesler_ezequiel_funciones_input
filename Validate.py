

def validate_number(numero_usuario: int|float, minimo: int|float, maximo: int|float) -> bool:
    """
    Valida que un número ENTERO o DECIMAL esté dentro del rango minimo-maximo.
    numero: El número a validar.
    minimo: Valor mínimo admitido (inclusive).
    maximo: Valor máximo admitido (inclusive).
    return: True si es válido, False si no lo es.
    """
    return minimo <= numero_usuario <= maximo
    # Retorna True si el número está dentro del rango, y False si no lo está.


def validate_length(texto_usuario: str, longitud_minima: int) -> bool:
    """
    Valida que un string tenga la longitud mínima requerida y solo contenga letras.
    texto: El string a validar.
    longitud_minima: Cantidad mínima de caracteres requerida.
    return: True si es válido, False si no lo es.
    """
    return len(texto_usuario) >= longitud_minima and texto_usuario.isalpha()
    # Retorna True si se cumplen ambas condiciones y False si alguna de las dos NO se cumnple.
