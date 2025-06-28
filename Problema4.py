"""
Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
puede ser calculada de la siguiente forma: 1+2+3+...+n = n(n+1)/2

"""

n = int(input("Ingrese un número entero positivo "))

if n > 0:
    suma = n * (n + 1) // 2
    print(f"La suma de los primeros {n} enteros positivos es: {suma}")
else:
    print("Por favor, ingrese un número entero positivo.")
