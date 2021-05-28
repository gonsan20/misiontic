datos_usuarios={}
id=0

while True:
    opcion=input("1. Ingrear Usuario\n2. Ver Usuario\n3. Ver Todos los Usuarios\n5. Salir\n")
    if opcion=='5':
        break
    elif opcion=='1':
        nombre=input("\n\nIngresar Nombre: ")
        edad=input("\nIngresar Edad: ")
        datos_usuarios[id]={"nombre":nombre, "edad":edad}
        id+=1
        print(datos_usuarios)
    elif opcion=='2':
        id_a_buscar=int(input("\nIngresar id de usuario a buscar: "))
        
        #Valida si el id a buscar está en el directorio
        if id_a_buscar in datos_usuarios:
            usuario_buscado=datos_usuarios[id_a_buscar]
            input("Nombre: " + usuario_buscado['nombre'] + " y su edad es " + usuario_buscado['edad'] + "\n\nPresione ENTER paracontinuar")
        else:
            input("\nid no encontrado presione una tecla para regresar al menu principal")
    elif opcion=='3':
        for nombreB in datos_usuarios: 
            print("B - El nombre es %s"%(nombreB['nombre']))
    else:
        input("Presione una tecla para continuar")
        





