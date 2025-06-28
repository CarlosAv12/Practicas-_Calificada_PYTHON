"""
Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
encuentran en la posición 0, 4 y 5.
lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
Resultado esperado: ['Verde', 'Blanco', 'Negro']

"""
lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
lista_muestra.remove('Rojo')
lista_muestra
lista_muestra.remove('Rosa')
lista_muestra
lista_muestra.remove('Amarillo')
lista_muestra

print(f"La lista obtenida será {lista_muestra}")