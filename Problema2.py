"""
En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
dejar como propina. 

"""

#1 Ingresar dato del monto consumido
consumo = float(input("Ingrese el monto total de su consumo "))

#2 Ingresar dato del porcentaje de propina
porcentaje = float(input("Ingrese el porcentaje de propina "))

#3 Establecer restrición para que el porcentaje de propina sea como mínimo del 15%
if porcentaje < 15:
    print("El porcentaje de propina debe ser al menos del 15%")

#4 Mostrar resultados
else:
    propina = consumo*(porcentaje/100)
    print(f"La cantidad de propina a dejar es {propina}")
