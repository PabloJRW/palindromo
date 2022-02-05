def palindromo(palabra):
    """Programa que toma como entrada una palabra o frase y que 
    tiene como salida la respuesta a si es o no palíndromo."""
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escirbe una palabra o frase: ")
    es_palindromo =  palindromo(palabra)
    if es_palindromo == True:
        print("ES PALÍNDROMO")
    else:
        print("NO ES PALÍNDROMO")


if __name__ == '__main__':
    run()