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
        return fecha_final
    except Exception as e:
        return f"Error {e}"
