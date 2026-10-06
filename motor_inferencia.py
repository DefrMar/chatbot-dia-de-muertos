

from reglas import REGLAS
from conocimiento import RESPUESTAS


def normalizar_texto(texto):
    return texto.lower().strip()


def encontrar_reglas_aplicables(mensaje):
    """
    Encuentra las reglas cuyas palabras clave aparecen
    en el mensaje del usuario.
    """
    mensaje = normalizar_texto(mensaje)

    conjunto_conflicto = []

    for regla in REGLAS:
        for palabra in regla["palabras_clave"]:
            if palabra in mensaje:
                conjunto_conflicto.append(regla)
                break

    return conjunto_conflicto


def seleccionar_regla(conjunto_conflicto):
    """
    Estrategia simple de solución de conflictos:
    elegir la primera regla encontrada.
    """
    if len(conjunto_conflicto) > 0:
        return conjunto_conflicto[0]

    return None


def disparar_regla(regla):
    """
    Ejecuta la regla seleccionada y obtiene
    la respuesta asociada a su conclusión.
    """
    if regla is None:
        return None

    conclusion = regla["conclusion"]

    return RESPUESTAS.get(conclusion)


def inferir(mensaje):
    """
    Motor principal de inferencia.
    """

    # 1. Encontrar conjunto de conflicto
    conjunto_conflicto = encontrar_reglas_aplicables(mensaje)

    # 2. Seleccionar una regla
    regla_seleccionada = seleccionar_regla(conjunto_conflicto)

    # 3. Disparar regla
    respuesta = disparar_regla(regla_seleccionada)

    if respuesta is None:
        return (
            "No tengo conocimiento suficiente para responder esa pregunta. "
            "Solo puedo hablar sobre el Día de Muertos."
        )

    return respuesta