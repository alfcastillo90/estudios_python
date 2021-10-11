menu = """
    Bienvenido al conversor de monedas 
    
    1 - Pesos colombianos
    2 - Pesos argentinos
    3 - Pesos mexicanos
    
    Elice una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input('¿Cuantos pesos colombianos tienes?: ')
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = round(pesos / valor_dolar, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')
elif opcion == 2:
    pesos = input('¿Cuantos pesos argentinos tienes?: ')
    pesos = float(pesos)
    valor_dolar = 182
    dolares = round(pesos / valor_dolar, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')
elif opcion == 3:
    pesos = input('¿Cuantos pesos mexicanos tienes?: ')
    pesos = float(pesos)
    valor_dolar = 20.87
    dolares = round(pesos / valor_dolar, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')
else:
    print('Opción invalida')
