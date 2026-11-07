##Requisitos
#1 Creación de listas:
usuario_1 = []
usuario_2 = []

#1.1 Agregación de datos:
usuario_1.append ("Alejandro")
usuario_1.append ("Corahua")
usuario_1.insert (2, 21)
usuario_1.append ("Contador")

usuario_2.append ("Ariadna")
usuario_2.append ("Beltrán")
usuario_2.insert (2, 19)
usuario_2.append ("Modista")

print("Usuario_1:", usuario_1)
print("Usuario_2:", usuario_2)

#2 Operaciones a realizar:

#2.1 Suma de edades:
suma_edades = usuario_1[2] + usuario_2[2]
print("1.La suma de las edades es:", suma_edades)
print("--------------------------------")

#3 Concatenar listas:
Usuarios = usuario_1 + usuario_2
print("2.La suma de las listas Usuarios es:", Usuarios)
print("--------------------------------")

Usuarios_lista_original_concatenada = Usuarios.copy()

#4 Inversión de la lista:
Usuarios.reverse()
print("3: Lista invertida de Usuarios:", Usuarios)
print("--------------------------------")

#5 Eliminación de elementos:
Usuarios.remove(21)
Usuarios.pop(2)
print("4: Lista con datos borrados:", Usuarios)
print("--------------------------------")

#6 Actualizar información:
Usuarios[0] = "Diseñadora de moda"
print("5: Lista corregida con la profesión del segundo usuario:", Usuarios)
print("--------------------------------")

#7 Conteo de la lista:
Conteo_Ariadna = Usuarios.count("Ariadna")
print("6. Número de veces que aparece Ariadna:", Conteo_Ariadna)
print("--------------------------------")

#8 Copia de la lista final:
Usuarios_lista_final = Usuarios.copy()

#9 Resultados finales:
print("-------------Resultados finales de listas -------------")
print("Lista original concatenada:", Usuarios_lista_original_concatenada)
print("Lista final:", Usuarios_lista_final)
















