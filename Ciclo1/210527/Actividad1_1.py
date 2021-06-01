datos_usuarios={}
id=0
opcion=1

while opcion!=5:
    opcion=input("1. Ingrear Usuario\n2. Ver Usuario\n3. Ver Todos los Usuarios\n5. Salir\n")

    if opcion=='1':
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
        if datos_usuarios:
            for usuario in datos_usuarios:
                datos_de_usuario=datos_usuarios[usuario]
                nombre=datos_de_usuario["nombre"]
                edad=datos_de_usuario["edad"]
                print(f"id:{usuario}\nnombre:{nombre}\nedad:{edad}\n\n")
        else:
            input("No hay usuarios registrados. Presione ENTER para regresar.")
    
    elif opcion=='5':
        pass

    else:
        input("Presione una tecla para continuar")
    


