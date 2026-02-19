import whois
from datetime import datetime


def obtenerFechaExpiracion(dominio):
    try:
        w = whois.whois(dominio)
        fecha = w.expiration_date
        if isinstance(fecha, list):
            fecha = fecha[0]
        #   Convierto la forma de la fecha
        fecha_obj = datetime.fromisoformat(str(fecha))
        fecha_final = fecha_obj.strftime("%d/%m/%Y")
        return (dominio, fecha_final)
    except Exception as e:
        return f"Error {e}"


def leerArchivo(archivo):
    lista_dominios = []
    with open(archivo, "r") as f:
        for linea in f:
            dominio = linea.strip()
            if dominio:
                lista_dominios.append(dominio)
    return lista_dominios
