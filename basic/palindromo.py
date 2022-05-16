def esPalindromo(palabra):
    palabra = str(palabra).strip().lower()
    palabra and print(palabra == palabra[::-1])

esPalindromo("luzazul")