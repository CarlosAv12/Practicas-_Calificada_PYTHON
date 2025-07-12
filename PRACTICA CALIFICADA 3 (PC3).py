# PROBLEMA 1 ###

def porcentaje_combustible():
    while True:
        try:
            # Solicitar entrada
            x_str, y_str = input("Ingrese una fracción (X/Y): ").split("/")

            # Convertir a enteros
            x = int(x_str)
            y = int(y_str)

            # Validaciones
            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser cero.")
            if x > y:
                raise ValueError("El numerador no puede ser mayor que el denominador.")
            if x < 0 or y < 0:
                raise ValueError("Ambos valores deben ser positivos.")

            # Calcular porcentaje
            porcentaje = round((x / y) * 100)

            # Evaluar los rangos
            if porcentaje < 1:
                print("E")
            elif porcentaje > 99:
                print("F")
            else:
                print(f"{porcentaje}%")
            break  # Salir del bucle si todo fue correcto

        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar números enteros con el formato X/Y y que se cumpla X ≤ Y.")

# Ejecutar el programa
porcentaje_combustible()

# PROBLEMA 2 ####

def solicitar_calificaciones():
    entrada = input("Ingrese calificaciones separadas por comas (ejemplo: 12,20,11,13): ")

    # Separar por comas
    calificaciones_str = entrada.split(",")
    
    calificaciones = []

    for valor in calificaciones_str:
        try:
            # Eliminar espacios y convertir a entero
            nota = int(valor.strip())
            if 0 <= nota <= 20:
                calificaciones.append(nota)
            else:
                print(f"La nota '{nota}' está fuera del rango permitido (0–20). Se omitirá.")
        except ValueError:
            print(f"Error: '{valor}' no es una calificación válida. Se omitirá.")

    # Mostrar resultado final
    print("Lista de calificaciones válidas:")
    print(calificaciones)

# Ejecutar
solicitar_calificaciones()

# Problema 3 ####

import math

# Definimos la clase Circulo
class Circulo:
    # Método inicializador (constructor)
    def __init__(self, radio):
        self.radio = radio

    # Método para calcular el área del círculo
    def calcular_area(self):
        return math.pi * self.radio ** 2

# Crear dos objetos de tipo Circulo
circulo1 = Circulo(5)
circulo2 = Circulo(10)

# Calcular y mostrar el área de cada círculo
print(f"Área del círculo 1 (radio = 5): {circulo1.calcular_area():.2f}")
print(f"Área del círculo 2 (radio = 10): {circulo2.calcular_area():.2f}")

# PROBLEMA 4 ###

# Clase Rectangulo
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

# Clase Cuadrado (hereda de Rectangulo)
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)  # Usa mismo valor para largo y ancho

# Crear un objeto de tipo Rectangulo
rect = Rectangulo(8, 4)
print("Área del rectángulo:", rect.calcular_area())

# Crear un objeto de tipo Cuadrado
cuad = Cuadrado(5)
print("Área del cuadrado:", cuad.calcular_area())

# PROBLEMA 5 ###

class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.nota = None

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")
        print(f"Edad: {self.edad if self.edad is not None else 'No asignada'}")
        print(f"Nota: {self.nota if self.nota is not None else 'No asignada'}")

    def setAge(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print(" Edad no válida. Debe ser un número positivo.")

    def setNota(self, nota):
        if 0 <= nota <= 20:
            self.nota = nota
        else:
            print(" Nota no válida. Debe estar entre 0 y 20.")

# Como se podría usar
alumno1 = Alumno("Carlos Aquino", "2025A001")

# Asignar edad y nota
alumno1.setAge(24)
alumno1.setNota(17.2)

# Mostrar la información del estudiante
alumno1.display()

# PROBLEMA 6 ###

import requests

# Función para obtener datos del tipo de cambio por mes
def obtener_tipo_cambio_mes(mes, anio):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year={anio}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza excepción si falla la solicitud
        return response.json()
    except requests.RequestException as e:
        print(f"Error al conectar con la API para el mes {mes}: {e}")
        return []

# Obtener datos para todo el año 2025
datos_completos = []
import time 

for mes in range(1, 13):  
    datos_mes = obtener_tipo_cambio_mes(mes, 2025)
    datos_completos.extend(datos_mes)
    time.sleep(2) 

# Si no hay datos, salimos
if not datos_completos:
    print("No se obtuvieron datos.")
    exit()

min_compra = float('inf')
max_venta = float('-inf')
max_diferencia = float('-inf')

fechas_min_compra = []
fechas_max_venta = []
fechas_max_dif = []

# Analizar los datos
for item in datos_completos:
    compra = item['compra']
    venta = item['venta']
    fecha = item['fecha']
    diferencia = venta - compra

    # Mínimo valor de compra
    if compra < min_compra:
        min_compra = compra
        fechas_min_compra = [fecha]
    elif compra == min_compra:
        fechas_min_compra.append(fecha)

    # Máximo valor de venta
    if venta > max_venta:
        max_venta = venta
        fechas_max_venta = [fecha]
    elif venta == max_venta:
        fechas_max_venta.append(fecha)

    # Máxima diferencia
    if diferencia > max_diferencia:
        max_diferencia = diferencia
        fechas_max_dif = [fecha]
    elif diferencia == max_diferencia:
        fechas_max_dif.append(fecha)

# Resultados
print(f"Fechas con el valor de COMPRA mínimo ({min_compra}):")
print(fechas_min_compra)

print(f"Fechas con el valor de VENTA máximo ({max_venta}):")
print(fechas_max_venta)

print(f"Fechas con la DIFERENCIA compra-venta máxima ({max_diferencia:.3f}):")
print(fechas_max_dif)

# PROBLEMA 7 ###

from pyfiglet import Figlet
import random

# Crear objeto Figlet
figlet = Figlet()

# Obtener lista de fuentes disponibles
fuentes_disponibles = figlet.getFonts()

# Solicitar fuente al usuario
fuente_usuario = input("Ingrese una fuente (ENTER para fuente aleatoria): ").strip()

# Si no se ingresa una fuente, elegir una aleatoria
if fuente_usuario == "":
    fuente_seleccionada = random.choice(fuentes_disponibles)
    print(f"Fuente seleccionada aleatoriamente: {fuente_seleccionada}")
else:
    if fuente_usuario in fuentes_disponibles:
        fuente_seleccionada = fuente_usuario
    else:
        print("Fuente no encontrada. Se usará una aleatoria.")
        fuente_seleccionada = random.choice(fuentes_disponibles)

# Configurar la fuente seleccionada
figlet.setFont(font=fuente_seleccionada)

# Solicitar el texto
texto = input("Ingrese el texto a imprimir: ")

# Imprimir el texto en arte ASCII
print(figlet.renderText(texto))


# PROBLEMA 8 ###

import os
import zipfile
import requests

# Paso 1: Descargar la imagen y guardarla en una carpeta descargas
url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

# Crear carpeta si no existe
carpeta_descarga = 'descargas'
os.makedirs(carpeta_descarga, exist_ok=True)

# Ruta de guardado
nombre_imagen = 'perrito.jpg'
ruta_imagen = os.path.join(carpeta_descarga, nombre_imagen)

# Descargar la imagen
response = requests.get(url, headers=headers)

if response.status_code == 200:
    with open(ruta_imagen, 'wb') as f:
        f.write(response.content)
    print("Imagen descargada y guardada en:", ruta_imagen)
else:
    print("Error al descargar la imagen.")
    exit()

# Paso 2: Comprimir archivos de la carpeta en un ZIP
# Crear carpeta para guardar el zip
carpeta_zip = 'comprimido'
os.makedirs(carpeta_zip, exist_ok=True)

zip_filename = os.path.join(carpeta_zip, 'perrito_txt.zip')

print(f"Comprimiendo archivos en: {zip_filename}")

with zipfile.ZipFile(zip_filename, 'w') as zip:
    archivos = os.listdir(carpeta_descarga)
    for archivo in archivos:
        ruta_completa = os.path.join(carpeta_descarga, archivo)
        if os.path.isfile(ruta_completa):
            zip.write(ruta_completa, os.path.basename(ruta_completa))

print("Archivos comprimidos exitosamente.")

# Paso 3: Descomprimir el archivo ZIP
carpeta_destino = 'Descomprimido'
os.makedirs(carpeta_destino, exist_ok=True)

with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall(path=carpeta_destino)
    print(f"Archivos descomprimidos en la carpeta: {carpeta_destino}")



