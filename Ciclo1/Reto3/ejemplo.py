"""

Alphabeto=["a",".-","b","-...","c","-.-.","d","-..","e",".","f","..-.",
"g","--.","h","....","i","..","j",".---","k","-.-","l",".-..",
"m","--","n","-.","o","---","p",".--.","q","--.-","r",".-.",
"s","...","t","-","u","..-","v","...-","w",".--","x","-..-",
"y","-.--","z","--.."]

"""

def traducir_mensaje(frase_dividida):
    alphabeto=["a",".-","b","-...","c","-.-.","d","-..","e",".","f","..-.",
    "g","--.","h","....","i","..","j",".---","k","-.-","l",".-..",
    "m","--","n","-.","o","---","p",".--.","q","--.-","r",".-.",
    "s","...","t","-","u","..-","v","...-","w",".--","x","-..-",
    "y","-.--","z","--.."," ","/"]

    for i in range(len(frase_dividida)):
        for j in range(len(alphabeto)):
            if j%2 == 1:
                if frase_dividida[i] == alphabeto[j]:
                    frase_dividida[i]=alphabeto[j-1]

    return frase_dividida



#mensaje_a_traducir="p a l a b r a / d i f e r e n t e"
#mensaje_a_traducir=".... . -- --- ... / . -. -.-. --- -. - .-. .- -.. --- / ..- -. .- / .--. .-.. .- -. - .- / -. ..- -. -.-. .- / .- -. - . ... / ...- .. ... - .-"
#mensaje_a_traducir="-. --- ... / .... .- -. / .--. .. -.-. .- -.. --- / -.. --- ... / -- --- ... --.- ..- .. - --- ..."
mensaje_a_traducir="- . -. . -- --- ... / -.-. --- -- .. -.. .- / .--. .- .-. .- / - .-. . ... / -.. .. .- ... / -- .- ..."

frase_dividida = []
frase_dividida = mensaje_a_traducir.split(" ")
print(frase_dividida)
print(frase_dividida[4])

cadena_traducida = traducir_mensaje(frase_dividida)
mensaje_traducido=""
mensaje_traducido=mensaje_traducido.join(cadena_traducida)
print(mensaje_traducido)
mensaje_traducido=mensaje_traducido.upper()
print(mensaje_traducido)


