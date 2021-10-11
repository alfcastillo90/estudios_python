def conversacion(mensaje):
    print('Hola')
    print('¿Como estás?')
    print(mensaje)
    print('Adiós')

def imprimir_mensaje():
    print('Mensaje especial: ')
    print('¡Estoy aprendiendo a usar funciones!')

def suma(a, b):
    print('Se suman dos números')
    resultado = a + b
    return resultado

imprimir_mensaje()

opcion = int(input('Elige una opción (1, 2, 3): '))

if opcion == 1:
    conversacion('Elegiste la opción 1')
elif opcion == 2:
    conversacion('Elegiste la opción 2')
elif opcion == 3:
    conversacion('Elegiste la opción 3')
else:
    conversacion('Opción incorrecta')

sumatoria = suma(1, 4)
print(sumatoria)



