"""
Ejercicio 03
Participación

Requisitos:
- Crear una función que multiplicará 4 valores (int y floats)
- La función tendrá un parámetro que contendrá un valor por defecto
- Mostrar 2 casos donde se ingresó los valores donde uno no afectará el valor del parámetro
  que ya contiene un valor y otro donde si lo estará afectando
- Ingresar los valores por consola
"""

#
def multiplicar_valores(val1, val2, val3, val4 = 2.0):
    return val1 * val2 * val3 * val4

print("--- Ingreso de valores ---")


v1 = float(input("Ingrese el primer valor: "))
v2 = float(input("Ingrese el segundo valor: "))
v3 = float(input("Ingrese el tercer valor: "))
#1
print("\n--- Caso 1: No se afecta el valor por defecto ---")
resultado_1 = multiplicar_valores(v1, v2, v3)
print("Resultado (usando valor por defecto = 2.0):", resultado_1)

#
print("\n--- Caso 2: Se afecta el valor por defecto ---")
v4 = float(input("Ingrese el cuarto valor (modificará el valor por defecto): "))
resultado_2 = multiplicar_valores(v1, v2, v3, v4)
print("Resultado (con el nuevo valor ingresado):", resultado_2)