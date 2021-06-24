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


def llamar_palabra_secreta():
    obj_palabras = palabras()
    palabra_secreta = obj_palabras.get_palabra()
    palabra_secreta = palabra_secreta[0:len(palabra_secreta) - 1]
    return (palabra_secreta)


def codificar_palabra(cadena):
    caracter = '__'

    for i in range(2, len(cadena)):
        if i % 2 == 0:
            if cadena[i] == 0:
                print(caracter, end='  ')
            else:
                print(cadena[i - 1], end='  ')
    print()


def configurar_cadena(palabra):
    cadena = list(palabra)
    longitud = len(palabra) * 2 + 1
    for i in range(longitud):
        if i % 2 == 0:
            cadena.insert(i, 0)
    return cadena


def validar_letra(letra, cadena):
    adivinadas = cadena[0]

    for i in range(1, len(cadena)):
        if i % 2 == 1:
            if letra == cadena[i]:
                cadena[i + 1] = 1
                cadena[0] += 2

    if adivinadas==cadena[0]:
        castigo=True
    else:
        castigo=False

    if len(cadena)-1 == cadena[0]:
        gano=True
        print("FELICITACIONES!!!! GANASTE!!!")
    else:
        gano=False

    return cadena, castigo, gano



def validar_repetidos(letra, letras):
    count=0
    letras.append(letra)
    for i in range(len(letras)):
        if letra == letras[i]:
            count+=1
    if count>1:
        print(f"\nLa letra {letra} ya ha sido ingresada")
        return True, letras, True
    else:
        return False, letras, False


def aplicar_castigo(oportunidades):
    dibujo = grafico()
    if oportunidades < 6:
        print(dibujo.get_grafico(oportunidades))
        oportunidades+=1
        if oportunidades == 6:
            print("\nTe queda solo una oportunidad")
        else:
            print(f"\nTe quedan {7-oportunidades} oportunidades")
        return False, oportunidades
    else:
        print(dibujo.get_grafico(oportunidades))
        print("\nPerdiste")
        return  True, oportunidades





"""
--------------------------------
              MAIN
--------------------------------
"""
palabra_secreta = llamar_palabra_secreta()
print(palabra_secreta)

cadena_palabra = configurar_cadena(palabra=palabra_secreta)

codificar_palabra(cadena=cadena_palabra)
#print(cadena_palabra)

castigo=False
gano = False
ahorcado = False
oportunidades=0
opcion=0
letras=[]
repetido= False

while opcion<=2:
    try:
        opcion=int(input("1. Ingresar Letra\n2. Adivinar Palabra\n3. Rendirse\n-->\t"))
    except:
        print("")

    if opcion == 1:
        letra = input("Ingrese una letra: ")
        repetido, letras, castigo = validar_repetidos(letra=letra, letras=letras)
        if repetido is False:
            cadena_palabra, castigo, gano = validar_letra(letra=letra, cadena=cadena_palabra)

        codificar_palabra(cadena=cadena_palabra)

        if castigo is True:
            ahorcado, oportunidades = aplicar_castigo(oportunidades=oportunidades)

        if gano is True:
            opcion=3

        if ahorcado is True:
            opcion=3

        #print(cadena_palabra)
        #print(castigo)
        #print(gano)

    elif opcion == 2:
        palabra_candidata = input("Ingrese la palabra: ")

        if palabra_candidata == palabra_secreta:
            print("FELICITACIONES!!!! GANASTE!!!")
            gano = True
        else:
            codificar_palabra(cadena=cadena_palabra)
            ahorcado, oportunidades = aplicar_castigo(oportunidades=oportunidades)

        if gano is True:
            opcion = 3

        if ahorcado is True:
            opcion = 3

    elif  opcion == 3:
        ahorcado, oportunidades = aplicar_castigo(oportunidades=6)

    else:
        input("Ingrese una opción válida entre 1 y 3")
        opcion = 0

