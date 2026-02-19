from modulo import obtenerFechaExpiracion as ofe
from modulo import leerArchivo as la


def main():
    dominios = la("dominios.txt")
    for dominio in dominios:
        print(ofe(dominio))


if __name__ == "__main__":
    main()
