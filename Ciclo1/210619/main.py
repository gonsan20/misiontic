from util import palabras, grafico


"""
Tareas
1. obtener palabra para adivinar
2. mostrar con __ las letras que conforman la palabra
3. preguntar por una letra al usuario
4. validar si la letra está en la palabra
5. mostrar las letras del palabra
6. preguntar por la palabra
7. validar si ha ganado o no
"""

def codificar_palabra(palabra):
    print(type(palabra))
    longitud = len(palabra) - 1
    caracter = '__'

    for i in range(longitud):
        print(caracter, end='  ')

    print()

def validar_letra(letra, palabra):
    longitud = list(palabra)

    if letra in palabra:
        return True
    else:
        return False








"""
MAIN
"""
obj_palabras= palabras()

palabra_secreta = obj_palabras.get_palabra()

codificar_palabra(palabra=palabra_secreta)

print(palabra_secreta)

letra = input("Ingrese una letra: ")

esta_en_la_palabra = validar_letra(letra=letra, palabra=palabra_secreta)

dibujo = grafico()
print()
