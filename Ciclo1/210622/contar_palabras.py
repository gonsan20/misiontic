"""
split() ->
join()
"""


def contar_palabras(frase):
    #una palabra está separada por espacios
    frase_dividida = frase.split(" ")
    print(frase_dividida)
    return len(frase_dividida),  frase_dividida



frase=input("Ingrese una frase de su gusto:")

n_palabras, cadena = contar_palabras(frase=frase)

print(f"el núemro de palabras es: {n_palabras}")
print (cadena)
print (" ".join(cadena))


