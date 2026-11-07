notas = [14, 8, 17, 10, 12, 5, 19, 13, 11, 16]

i = 0

for nota in notas:
    print("Nota original:", notas[i])
    notas[i] = nota / 2
    print("Nota actualizada: {}".format(notas[i]))
    i += 1

print("Lista actualizada:", notas)

#
nota_maxima = max(notas)
print("La nota más alta actualizada es:", nota_maxima)

#
notas.append(nota_maxima + 2)
notas.append(nota_maxima + 3)

print("Lista final con las nuevas notas:", notas)