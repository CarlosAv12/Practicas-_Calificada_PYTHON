# PROBLEMA 1 ####

import os
os.makedirs('./CarpetaTemperaturas', exist_ok=True)

# Ruta donde se guardará el archivo
ruta_archivo = './CarpetaTemperaturas/temperaturas.txt'

contenido = """2024-01-01,15.5
2024-01-02,17.0
2024-01-03,16.2
2024-01-04,14.8
2024-01-05,18.1
2024-01-06,13.9
2024-01-07,19.3
2024-01-08,20.1
2024-01-09,21.4
2024-01-10,22.0"""

with open(ruta_archivo, 'w', encoding='utf-8') as f:
    f.write(contenido)

print("El Archivo 'temperaturas.txt' fue creado con éxito.")

# Paso 1: Leer el archivo y extraer temperaturas
ruta_entrada = './CarpetaTemperaturas/temperaturas.txt'
temperaturas = []

with open(ruta_entrada, 'r', encoding='utf-8') as file:
    for linea in file:
        fecha, temp = linea.strip().split(',')  
        temperaturas.append(float(temp))        

# Paso 2: Calculamos el promedio, máximo y mínimo
promedio = sum(temperaturas) / len(temperaturas)
maxima = max(temperaturas)
minima = min(temperaturas)

# Paso 3: Escribimos resultados en nuevo archivo
ruta_salida = './CarpetaTemperaturas/resumen_temperaturas.txt'

with open(ruta_salida, 'w', encoding='utf-8') as resumen:
    resumen.write(f'Temperatura promedio: {promedio:.2f}°C\n')
    resumen.write(f'Temperatura máxima: {maxima:.2f}°C\n')
    resumen.write(f'Temperatura mínima: {minima:.2f}°C\n')

print("El Resumen de las temperaturas en 'resumen_temperaturas' fue creado con éxito.")

# Problema 2 ###

import os

def crear_tabla(numero):
    # Crea y guarda la tabla de multiplicar del número en un archivo.
    nombre_archivo = f'tabla-{numero}.txt'
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        for i in range(1, 11):
            f.write(f"{numero} x {i} = {numero * i}\n")
    print(f"El Archivo '{nombre_archivo}' creado con la tabla del {numero}.")

def leer_tabla(numero):
    # Lee y muestra la tabla de multiplicar desde el archivo correspondiente.
    nombre_archivo = f'tabla-{numero}.txt'
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
        print(f"Contenido de '{nombre_archivo}':\n")
        print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

def mostrar_linea_tabla(numero, linea):
    # Muestra la línea m de la tabla n desde el archivo."""
    nombre_archivo = f'tabla-{numero}.txt'
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
            if 1 <= linea <= len(lineas):
                print(f"Línea {linea}: {lineas[linea - 1].strip()}")
            else:
                print(f"El número de línea está fuera del rango (1-10).")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

def pedir_entero(mensaje, minimo=1, maximo=10):
    # Solicitamos un número entero entre 1 y 10 con validación
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

def menu():
    # Muestra el menú principal.
    while True:
        print("Menú de opciones")
        print("1. Crear tabla de multiplicar y guardarla")
        print("2. Leer tabla de multiplicar desde archivo")
        print("3. Mostrar línea específica de una tabla")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            n = pedir_entero("Ingrese un número entre 1 y 10 para crear su tabla: ")
            crear_tabla(n)
        elif opcion == '2':
            n = pedir_entero("Ingrese un número entre 1 y 10 para leer su tabla: ")
            leer_tabla(n)
        elif opcion == '3':
            n = pedir_entero("Ingrese el número de la tabla (1 a 10): ")
            m = pedir_entero("Ingrese el número de línea a mostrar (1 a 10): ")
            mostrar_linea_tabla(n, m)
        elif opcion == '4':
            print("Programa finalizado.")
            break
        else:
            print("La opción es inválida. Elija entre 1 y 4.")

# Ejecutamos el menú
menu()

# Problema 3 ###

def contar_lineas_codigo(ruta):
    if not ruta.endswith('.py'):
        return

    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            lineas = [l for l in f if l.strip() and not l.strip().startswith('#')]
        print(len(lineas))
    except FileNotFoundError:
        pass  # No mostrar nada si el archivo no existe

ruta = input("Ingrese la ruta del archivo .py (nombre y ruta): ").strip()
contar_lineas_codigo(ruta)

# Problema 4 ###

import requests
import time
import sqlite3
from pymongo import MongoClient

# Definimos la función para obtener datos del tipo de cambio por mes
def obtener_tipo_cambio_mes(mes, anio):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year={anio}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error al conectar con la API para el mes {mes}: {e}")
        return []

# Obtenemos el tipo de cambio para todo el año 2023
datos_completos = []

for mes in range(1, 13):  
    datos_mes = obtener_tipo_cambio_mes(mes, 2023)
    datos_completos.extend(datos_mes)
    time.sleep(2)  # Esperamos para no saturar la API

if not datos_completos:
    print("No se obtuvieron datos.")
    exit()

# Nos conectamos a SQLite
conn = sqlite3.connect("base.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS sunat_info (
    fecha TEXT PRIMARY KEY,
    compra REAL,
    venta REAL
)
""")

# Nos conectamos a MongoDB Atlas
mongo_uri = "mongodb+srv://carlosaquino3501:lHu0nlmMt4zdR0g2@dev.uk2uy6b.mongodb.net/?retryWrites=true&w=majority&appName=Dev"
cliente = MongoClient(mongo_uri)
mongo_db = cliente["mi_base"]
mongo_col = mongo_db["sunat_info"]

# Insertamos los datos en SQLite y MongoDB
for item in datos_completos:
    fecha = item['fecha']
    compra = item['compra']
    venta = item['venta']

    # SQLite
    cur.execute("""
    INSERT OR IGNORE INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)
    """, (fecha, compra, venta))

    # MongoDB Atlas
    mongo_col.update_one(
        {"fecha": fecha},
        {"$set": {"compra": compra, "venta": venta}},
        upsert=True
    )

conn.commit()

# Mostramos los datos desde SQLite
print("Contenido de la tabla sunat_info (SQLite)")
for row in cur.execute("SELECT * FROM sunat_info ORDER BY fecha"):
    print(row)

conn.close()

# Problema 5 ### 

from pymongo import MongoClient
from typing import List, Dict

# Ruta del archivo de ventas
RUTA_ARCHIVO = '/workspaces/PC1-PYTHON/TipoCambioSunat/ventas.csv'
RUTA_SALIDA = '//workspaces/PC1-PYTHON/TipoCambioSunat/total_ventas_solarizado.txt'

# Conexión a MongoDB Atlas
mongo_uri = "mongodb+srv://carlosaquino3501:lHu0nlmMt4zdR0g2@dev.uk2uy6b.mongodb.net/?retryWrites=true&w=majority&appName=Dev"
cliente = MongoClient(mongo_uri)
db = cliente["mi_base"]
coleccion_tipo_cambio = db["sunat_info"]     # Datos de tipo de cambio por fecha
coleccion_resultado = db["ventas_soles"]    # Donde se guardarán los totales solarizados

# ------------------------------------------
# Función para convertir las líneas del archivo en una lista de diccionarios
# ------------------------------------------
def obtener_productos(ventas: List[str]) -> List[Dict]:
    lista = []
    for venta in ventas:
        if not venta.strip():
            continue
        datos = venta.strip().split(',')

        venta_dict = {
            'fecha': datos[0],
            'producto': datos[1],
            'cantidad': int(datos[2]),
            'precio_unitario': float(datos[3])
        }
        venta_dict['sub_total'] = venta_dict['cantidad'] * venta_dict['precio_unitario']
        lista.append(venta_dict)
    return lista
# Lectura del archivo de ventas
try:
    with open(RUTA_ARCHIVO, 'r') as f:
        ventas_txt = f.readlines()
except FileNotFoundError:
    print(f"Archivo no encontrado: {RUTA_ARCHIVO}")
    exit()

ventas = obtener_productos(ventas_txt)

# Procesamiento: solarizar ventas según tipo de cambio
productos = dict()  # {producto: total_soles}

for venta in ventas:
    fecha = venta['fecha']
    producto = venta['producto']
    cantidad = venta['cantidad']
    precio_unitario = venta['precio_unitario']

    # Buscar tipo de cambio de venta en MongoDB
    tipo_cambio_doc = coleccion_tipo_cambio.find_one({"fecha": fecha})
    if tipo_cambio_doc is None:
        print(f"Tipo de cambio no encontrado para {fecha}. Venta omitida.")
        continue

    tipo_cambio = tipo_cambio_doc['venta']
    total_soles = cantidad * precio_unitario * tipo_cambio

    # Acumular el total solarizado por producto
    if producto not in productos:
        productos[producto] = total_soles
    else:
        productos[producto] += total_soles

# Guardar resultados en archivo de texto
lineas_salida = ['{producto},{total:.2f}\n'.format(producto=producto, total=total)
                 for producto, total in productos.items()]

with open(RUTA_SALIDA, 'w') as f:
    f.writelines(lineas_salida)

print(f"Archivo generado: {RUTA_SALIDA} y en MongoDB como ventas_soles")

# Guardar resultados en MongoDB (colección: ventas_soles)
for producto, total in productos.items():
    coleccion_resultado.update_one(
        {"producto": producto},
        {"$set": {"total_solarizado": round(total, 2)}},
        upsert=True
    )

# Mostrar en la consola
print("Totales solarizados por producto")
for producto, total in productos.items():
    print(f"{producto}: S/ {round(total, 2)}")




