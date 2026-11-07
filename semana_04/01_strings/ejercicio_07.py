"""
Intevervención
"""
"""
Usando propiedades de string
Requisitos:
    - Ingresar su nombre y apellido por consola (variables distintas)
    - Obtener el tamaño de tu nombre completo y muéstralo en consola
    - Imprimir el resultado final, todo en mayúsculas: .upper()
    - Indicar mediante condicionales si el tamaño del nombre es mayor o no al apellido ingresado
    - Solamente ingresar el apellido paterno

"""

nombre = input("Nombre: ")
apellido = input("Apellido: ")
nombre_completo = nombre + " " + apellido

print("Tamaño del nombre completo es: {}".format(len(nombre_completo)))
print("El nombre completo del usuario es: {}".format(nombre_completo.upper()))


if len(nombre) > len(apellido):
    print("El tamaño del nombre es mayor que el del apellido.")

elif len(nombre) < len(apellido):
    print("El tamaño del apellido es mayor que el del nombre.")