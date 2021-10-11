def conversor(tipo_pesos, valor_dolar):
    pesos = input('¿Cuantos pesos '+tipo_pesos+' tienes?: ')
    pesos = float(pesos)
    dolares = round(pesos / valor_dolar, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')

menu = """
    Bienvenido al conversor de monedas 
    
    1 - Pesos colombianos
    2 - Pesos argentinos
    3 - Pesos mexicanos
    
    Elice una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor('colombianos', 3875)
elif opcion == 2:
    conversor('argentinos', 182)
elif opcion == 3:
    conversor('mexicanos', 20.87)
else:
    print('Opción invalida')
