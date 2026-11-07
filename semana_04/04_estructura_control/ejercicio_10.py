"""
Ejercicio 10
Participación #3
"""
"""
Uso de cond. if

Uso de if ternarios
Requisitos:
- Ingresar por teclado el sueldo del empleado
- Si el sueldo es mayor que 4000, imprimir "Su sueldo no tiene bonificación"
- Caso contrario indicar: "Su sueldo tiene bonificación este año y será de :
sueldo_final", sueldo_final = sueldo + 20% * sueldo

"""
#1
sueldo = float(input("Ingrese el sueldo del empleado: "))
sueldo_bono = sueldo + (0.20 * sueldo)

if sueldo > 4000:
     print("El sueldo no tiene bonificación")

else:
    print("El sueldo si tiene bonificación".format(sueldo_bono))

mensaje = "El sueldo no tiene bonificación" if sueldo > 4000 else "El sueldo si tiene bonificación este año y será de {}".format(sueldo_bono)
print(mensaje)


