def palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    palabraInvertida = palabra[::-1]
    if palabra == palabraInvertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


if __name__ == '__main__':
    run()