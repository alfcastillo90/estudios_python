import random


def run():
    numero_aletorio = random.randint(1, 100)
    numero_eledigo = int(input('Elige un número del 1 al 100: '))
    while numero_eledigo != numero_aletorio:
        if numero_eledigo < numero_aletorio:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero_eledigo = int(input('Elige otro número: '))
    print('¡Ganaste!')


if __name__ == '__main__':
    run()

