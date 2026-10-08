from reglas import REGLAS
from conocimiento import RESPUESTAS


def normalizar_texto(texto):
    texto = texto.lower().strip()

    reemplazos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "ü": "u"
    }

    for original, nuevo in reemplazos.items():
        texto = texto.replace(original, nuevo)

    return texto


def encontrar_reglas_aplicables(mensaje):
    mensaje = normalizar_texto(mensaje)

    conjunto_conflicto = []

    for regla in REGLAS:

        coincidencias = 0

        for patron in regla["patrones"]:
            patron = normalizar_texto(patron)

            if patron in mensaje:
                coincidencias += len(patron.split())

        if coincidencias > 0:
            conjunto_conflicto.append({
                "regla": regla,
                "puntuacion": coincidencias
            })

    return conjunto_conflicto


def seleccionar_regla(conjunto_conflicto):

    if not conjunto_conflicto:
        return None

    conjunto_conflicto.sort(
        key=lambda x: x["puntuacion"],
        reverse=True
    )

    return conjunto_conflicto[0]["regla"]


def disparar_regla(regla):

    if regla is None:
        return None

    return RESPUESTAS.get(regla["conclusion"])


def inferir(mensaje):

    conjunto_conflicto = encontrar_reglas_aplicables(mensaje)

    regla = seleccionar_regla(conjunto_conflicto)

    respuesta = disparar_regla(regla)

    if respuesta is None:
        return (
            "No tengo conocimiento suficiente para responder esa pregunta. "
            "Solo puedo hablar sobre el Día de Muertos."
        )

    return respuesta