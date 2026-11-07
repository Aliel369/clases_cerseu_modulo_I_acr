"""Intervención"""

"""
Requisitos:
- Crear una lista de notas, 10 notas
- Obtener la suma de notas, utilizando el recorrido, apoyarse de una variable auxiliar
- Obtener las notas aprobadas y desaprobadas, empezar con listas vacías
- Obtener el promedio de notas, dentro de una variable
- Mostrar la nota más baja y la más alta

"""
#1
notas = [12, 10, 19, 11, 13, 15, 14, 11, 16, 17]
print("Lista de notas:", notas)

#2
suma_notas = 0
for nota in notas:
    suma_notas += nota

print("Suma total de notas:", suma_notas)

#3
aprobadas = []
desaprobadas = []

for nota in notas:
    if nota >= 11:
        aprobadas.append(nota)

    else:
        desaprobadas.append(nota)

print("Notas aprobadas:", aprobadas)
print("Notas desaprobadas:", desaprobadas)

#4
promedio_notas = suma_notas / len(notas)
print("Promedio de notas:", promedio_notas)

#5
nota_baja = min(notas)
print("Nota más baja:", nota_baja)
nota_alta = max(notas)
print("Nota más alta:", nota_alta)
