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


def configurar_cadena(palabra):
    cadena = list(palabra)
    dict_cadena={0:{"TotalCar":len(cadena), "adivinadas":0, "castigo":False, "letraRepetida":False, "chances":0, "ahorcado":False, "gano":False}}
    for i in range(len(cadena)):
        dict_cadena[i+1]=[cadena[i],0]
    return dict_cadena


def codificar_palabra(dict_palabra):
    caracter = '__'

    for i in range(1, len(dict_palabra)):
        if dict_palabra[i][1] == 0:
            print(caracter, end='  ')
        else:
            print(dict_palabra[i][0], end='  ')
    print()



def validar_letra(letra, dict_palabra):
    dict_palabra[0]["castigo"] = True
    dict_palabra[0]["letraRepetida"] = False

    for i in range(1, len(dict_palabra)):
        if dict_palabra[i][0] == letra:
            dict_palabra[0]["castigo"] = False
            if dict_palabra[i][1] == 1:
                dict_palabra[0]["letraRepetida"] = True
            else:
                dict_palabra[i][1] = 1
                dict_palabra[0]["adivinadas"] += 1
        if dict_palabra[0]["TotalCar"] == dict_palabra[0]["adivinadas"]:
            dict_palabra[0]["gano"] = True
    return dict_palabra




def analizar_resultado(dict_palabra):
    if dict_palabra[0]["letraRepetida"] == True:
        dict_palabra = aplicar_castigo(dict_palabra)
        dict_palabra[0]["letraRepetida"] = False
    if dict_palabra[0]["castigo"] == True:
        dict_palabra = aplicar_castigo(dict_palabra)
        dict_palabra[0]["castigo"] = False
    if dict_palabra[0]["gano"] == True:
        print("FELICITACIONES!!!! GANASTE!!!")
    return dict_palabra



def aplicar_castigo(dict_palabra):
    dibujo = grafico()
    if dict_palabra[0]["chances"] < 6:
        print(dibujo.get_grafico(dict_palabra[0]["chances"]))
        dict_palabra[0]["chances"]+=1
        if dict_palabra[0]["chances"] == 6:
            print("\nTe queda solo una oportunidad")
        else:
            print(f"\nTe quedan {7-dict_palabra[0]['chances']} oportunidades")
    else:
        print(dibujo.get_grafico(dict_palabra[0]["chances"]))
        print("\nPerdiste")
        dict_palabra[0]["ahorcado"] = True
    return dict_palabra







"""
--------------------------------
              MAIN
--------------------------------
"""
palabra_secreta = llamar_palabra_secreta()
print(palabra_secreta)

dict_palabra = configurar_cadena(palabra=palabra_secreta)
print(dict_palabra)

codificar_palabra(dict_palabra=dict_palabra)
#print(cadena_palabra)

opcion=0
while opcion<=2:
    try:
        opcion=int(input("1. Ingresar Letra\n2. Adivinar Palabra\n3. Rendirse\n-->\t"))
    except:
        print("")

    if opcion == 1:
        letra = input("Ingrese una letra: ")
        dict_palabra = validar_letra(letra=letra, dict_palabra=dict_palabra)
        dict_palabra = analizar_resultado(dict_palabra=dict_palabra)
        codificar_palabra(dict_palabra=dict_palabra)
        print(dict_palabra)
        if dict_palabra[0]["ahorcado"] is True:
            opcion = 5
        if dict_palabra[0]["gano"] == True:
            opcion = 5

    if opcion == 2:
        palabra_candidata = input("Ingrese la palabra: ")
        if palabra_candidata == palabra_secreta:
            dict_palabra[0]["gano"] == True
            dict_palabra = analizar_resultado(dict_palabra=dict_palabra)
            opcion = 5
        else:
            dict_palabra[0]["castigo"]=True
            dict_palabra = analizar_resultado(dict_palabra=dict_palabra)
            codificar_palabra(dict_palabra=dict_palabra)
            print(dict_palabra)
            if dict_palabra[0]["ahorcado"] is True:
                opcion = 5

    if opcion == 3:
        dict_palabra[0]["castigo"]=True
        dict_palabra[0]["chances"] = 6
        dict_palabra = analizar_resultado(dict_palabra=dict_palabra)

    else:
        print("Ingrese una opción válida entre 1 y 3")
        opcion = 0