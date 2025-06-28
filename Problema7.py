"""
Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.

"""
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print("Elija una opción:")
print("1. Sumar los dos números")
print("2. Restar el segundo al primero")
print("3. Multiplicar los dos números")
opcion = input("Ingrese el número de la opción: ")

if opcion == "1":
    print(f"La suma es: {numero1 + numero2}")
elif opcion == "2":
    print(f"La resta es: {numero1 - numero2}")
elif opcion == "3":
    print(f"La multiplicación es: {numero1 * numero2}")
else:
    print("Opción inválida, vuelva a intentarlo")