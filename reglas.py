# reglas.py

REGLAS = [
    {
        "nombre": "R1",
        "patrones": [
            "que es un altar",
            "para que sirve un altar",
            "que significa el altar",
            "ofrenda",
            "altar de muertos"
        ],
        "conclusion": "altar"
    },

    {
        "nombre": "R2",
        "patrones": [
            "para que sirven las velas",
            "para que son las velas",
            "que significan las velas",
            "velas en el altar",
            "velas en la ofrenda"
        ],
        "conclusion": "velas"
    },

    {
        "nombre": "R3",
        "patrones": [
            "que significa el cempasuchil",
            "para que sirve el cempasuchil",
            "flor de cempasuchil",
            "cempasuchil en la ofrenda"
        ],
        "conclusion": "cempasuchil"
    },

    {
        "nombre": "R4",
        "patrones": [
            "que es el pan de muerto",
            "que significa el pan de muerto",
            "pan de muerto"
        ],
        "conclusion": "pan_de_muerto"
    },

    {
        "nombre": "R5",
        "patrones": [
            "que son las calaveritas",
            "que significan las calaveritas",
            "calaveritas de azucar",
            "calaveritas"
        ],
        "conclusion": "calaveritas"
    },

    {
        "nombre": "R6",
        "patrones": [
            "cuando es dia de muertos",
            "cuando se celebra dia de muertos",
            "fecha del dia de muertos",
            "1 de noviembre",
            "2 de noviembre"
        ],
        "conclusion": "fecha"
    }
]