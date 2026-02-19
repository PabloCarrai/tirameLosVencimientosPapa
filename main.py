from modulo import obtenerFechaExpiracion as ofe


def main():
    fecha_vencimiento = ofe("program.gob.ar")
    print(fecha_vencimiento)


if __name__ == "__main__":
    main()
