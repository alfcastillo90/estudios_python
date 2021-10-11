pesos = input('¿Cuantos pesos colombianos tienes?: ')
pesos = float(pesos)
valor_dolar = 3875
dolares = round(pesos/valor_dolar, 2)
dolares = str(dolares)
print('Tienes $'+dolares+' dólares')
