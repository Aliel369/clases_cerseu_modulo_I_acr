def modificar_elemento(lista, indice):
    try:
        lista[indice] = 0
        print("¡Éxito! Se modificó el elemento en el índice a 0.")
    except IndexError:
        print("¡Error! El índice no existe en la lista.")
        print("El índice buscado no está dentro del rango, se le agregará un 0 al final.")
        lista.append(0)



if __name__ == "__main__":

    lista = [10, 20, 30, 40]

    print("=" * 50)
    print("Control de listas")
    print("=" * 50)
    print("Lista inicial: {}".format(lista))
    print("Regla: Índices válidos: 0 al 3. Índices invalidos de rango: > 4 o < 0")

    try:

        valor_ingresado= input("Ingresa el número de índice que deseas modificar: ")
        indice = int(valor_ingresado)

        modificar_elemento(lista, indice)

        print("Lista final resultante: {}".format(lista))

    except ValueError:
        print("Error: Debes ingresar obligatoriamente un número válido.")