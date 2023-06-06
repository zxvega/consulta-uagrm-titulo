from titulosuagrm import EndpointClient

PROCEDENCIAS = {
        "santa_cruz": "SCZ",
        "la_paz": "LPZ",
        "beni": "BEN",
        "pando": "PAN",
        "cochabamba": "CBA",
        "chuquisaca": "CHS",
        "tarija": "TJA",
        "oruro": "ORU",
        "potosi": "POT",
        "extranjero": "EXT"
    }

cliente = EndpointClient()
cedula = "" #Ingresar un carnet de identidad de un universitario titulado
procedencia = PROCEDENCIAS["santa_cruz"]

resultado = cliente.consultar_endpoint(cedula, procedencia)

if resultado is not None:
    # Procesar el resultado de acuerdo a tus necesidades
    # ...
    print(resultado)