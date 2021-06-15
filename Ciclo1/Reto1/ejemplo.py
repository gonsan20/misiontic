def comienza_digito_impar(n):
    """Esta función retorna True si n comienza por un dígito impar, ejemplo de números que
    comienzan por dígito impar: 1234, 76555, 92228
    Retorna False si n NO comienza por dígito impar
    
    Complete la siguiente línea, que sirve para guardar el primer dígito de n en una variable llamada d"""
    d = str(n)[0] #Completar -> #->[AN]Completado
    
    """d guarda un valor de tipo texto, completa la siguiente línea para cambiar el tipo de la variable d a entero"""
    d = int(d) #Completar #->[AN]Completado
    
    """Un número d es impar si d % 2 == 1
    Complete cuál es la condición que se debe cumplir para que un número SÍ sea impar"""
    if  d%2>0: #->[AN]Completado
    
        """Si entra a este condicional, es porque n empieza por un dígito impar"""
        return True
        
    """Si NO entra al condicional anterior, es porque n NO empieza por un dígito impar"""
    #Vamos a seguir completando la función solución, (línea 34)
    return False

n=23
print (n, " ", comienza_digito_impar(n))