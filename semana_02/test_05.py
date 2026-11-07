"""
Requisitos:

1. Crear dos variables para los valores de nombre, profesión y ciudad
2. Crear dos variables para la remuneración de enero y febrero (mayor a 1500)
3. Crear 1 variables para la remuneración de enero y febrero (mayor a 1500)
4. Mostrar en pantalla el siguiente mensaje (Output)

"Hola soy 'nombres' , soy 'profesión' y mi remuneración acumulada es de ''remunera_total"

rem_1
remunera_1
rem_enero

"""
nombre = "Alejandro"
profesión = "contador"
ciudad = "Lima"
rem_enero = 1700
rem_febrero = 1800
remunera_total = rem_enero + rem_febrero

print("Hola soy {} , soy {} , vivo en {} , y mi remuneración acumulada es de {}".format(nombre, profesión, ciudad, remunera_total))