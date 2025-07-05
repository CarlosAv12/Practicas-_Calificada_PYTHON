# # PRACTICA CALIFICADA 1

# #### Problema 1

resultado = []

for numero in range(1500, 2701):
    if numero % 7 == 0 and numero % 5 == 0:
        resultado.append(numero)

print("Números divisibles por 7 y múltiplos de 5 entre 1500 y 2700:")
print(resultado)

# #### Problema 2

for i in range(1, 6):
    print("* " * i)

for i in range(4, 0, -1):
    print("* " * i)

# ### Problema 3 

numeros = []

while True:
    respuesta = input("¿Desea ingresar un número? (SI o NO): ")

    if respuesta == "NO":
        break
    elif respuesta == "SI":
            numero = int(input("Ingrese el número: "))
            numeros.append(numero)
    else:
        print("Respuesta no válida. Escriba SI o NO.")

pares = 0
impares = 0

for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\nNúmeros ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)

# #### Problema 4

alumnos = []

n = int(input("¿Cuántos alumnos desea ingresar? "))

for i in range(n):
    print(f"Ingresando datos del alumno {i + 1}")
    nombre = input("Nombre del alumno: ")

    # Lista para almacenar las 3 notas del alumno
    notas = []

    # Bucle para ingresar 3 notas
    for j in range(1, 4):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {j}: "))
                if 0 <= nota <= 20:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 20.")
            except ValueError:
                print("Error: Ingrese un número válido.")
           
    # Crear un diccionario con los datos del alumno
    alumno = {
        "Alumno": nombre,
        "Notas": notas
    }
    alumnos.append(alumno)

print("Listado de alumnos:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

# #### Problema 5

def contar_digito(numero, digito):
    numero_str = str(numero)
    digito_str = str(digito)
    
    cantidad = numero_str.count(digito_str)
    
    print(f"Cantidad de veces {digito} en el número: {cantidad}")

numero_ingresado = int(input("Ingresa un número entero: "))
digito_ingresado = input("Ingresa el dígito que deseas contar: ")

contar_digito(numero_ingresado, digito_ingresado)

# #### Problema 6

a, b = 0, 1

print("Serie de Fibonacci entre 0 y 50:")

while a <= 50:
    print(a, end=", ")
    a, b = b, a + b

# #### Problema 7

def es_primo(numero):
    if numero <= 1:
        print(f"{numero} no es primo.")
        return
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(f"{numero} no es primo.")
            return
    print(f"{numero} es primo.")

numero_usuario = int(input("Ingresa un número: "))
es_primo(numero_usuario)

# #### Problema 8

def factorial(n):
    if n < 0:
        print("El número debe ser un entero no negativo.")
        return
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    print(f"El factorial de {n} es: {resultado}")

numero = int(input("Ingresa un número entero no negativo: "))
factorial(numero)

# #### Problema 9

def eliminar_vocales(texto):
    vocales = "aeiouAEIOU"
    resultado = ""

    for caracter in texto:
        if caracter not in vocales:
            resultado += caracter

    return resultado

entrada = input("Ingresa un texto: ")
salida = eliminar_vocales(entrada)
print("Texto sin vocales:", salida)

# #### Problema 10 

def convertir_fecha(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    
    # Intentamos detectar el formato con número (ej. 9/8/1636)
    if "/" in fecha:
        partes = fecha.strip().split("/")
        mes = int(partes[0])
        dia = int(partes[1])
        anio = int(partes[2])
    else:
        # Formato tipo "Septiembre 8, 1636"
        fecha = fecha.replace(",", "").strip()  # Quitamos la coma
        partes = fecha.split()
        mes = meses.index(partes[0].capitalize()) + 1  # Convertimos nombre del mes a número
        dia = int(partes[1])
        anio = int(partes[2])

    # Devolvemos la fecha con ceros a la izquierda si es necesario
    return f"{anio}-{mes:02}-{dia:02}"

entrada = input("Ingresa una fecha (formato MM/DD/AAAA o Mes D, AAAA): ")
salida = convertir_fecha(entrada)
print("Fecha en formato AAAA-MM-DD:", salida)
