def leer_archivo(archivo):
    with open("dominios.txt", "r", encoding="utf-8") as archivo:
        lista_contenido = [linea.strip() for linea in archivo]
    return sorted(lista_contenido)


def guardar_lista_ordenada(archivo, lista):
    with open(archivo, "w") as archivo:
        for dominio in lista:
            archivo.write(str(dominio) + "\n")


def main():
    archivo = "dominios.txt"
    lista_ordenada = leer_archivo(archivo)
    guardar_lista_ordenada(archivo, lista_ordenada)
    print(f"Ahora tenes ordenado el archivo {lista_ordenada}")


if __name__ == "__main__":
    main()
