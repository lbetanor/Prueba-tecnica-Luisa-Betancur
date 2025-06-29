from logger import log

def limpiar_saldo(num:str) -> float:
    """
    Limpia el saldo de una cuenta eliminando caracteres no numéricos y convirtiéndolo a float.

    Args:
        num (str): El saldo de la cuenta como cadena, que puede contener símbolos como "$", ",", o espacios.

    Returns:
        float: El saldo limpio convertido a tipo float.
    """
    try:
        saldo_limpio = str(num).strip().replace("$", "").replace(",", "").replace(" ", "")
        return float(saldo_limpio)
    except Exception as e:
        log.error(f"No se pudo convertir el saldo: '{num}' → {e}")
        raise ValueError(f"No se pudo convertir el saldo: '{num}' → {e}")
    

