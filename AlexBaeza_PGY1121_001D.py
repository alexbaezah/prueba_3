nombre = ""
usuario = ""
rut = 0
dv = ""
edad = 0
rango = "" 
correo = ""
pago = 0
contador = 0
registro = False 
lista = []
cantidad = 0

print("----- PLATAFORMA GAME_STORE ----")
opcion = 0

while opcion < 4:
    print("1) Registrarse\n2)Conectarse\n3)Registro de accesos\n4)Salir")

    opcion = int(input("Ingrese qué opción "))
    if opcion == 1:
        rut = int(input("ingrese rut, sin puntos ni dígito verificador "))
        if rut < 5000000 or rut > 99999999:
            print("el rango debe ser entre estos valores 5000000 y 99999999 ")
        else:
            lista.append(rut)
            edad = int(input("ingresa tu edad "))
            if edad < 18 or edad > 110:
                print("Debes ser mayor de 18 y menor de 111 ")
            
            else:
                lista.append(edad)
                dv = input("ingrese dígito verificador ")
                lista.append(dv)            
                nombre = input("ingrese su nombre ")
                lista.append(nombre)            
                usuario = input("ingrese nombre de usuario ")
                lista.append(usuario)
                correo = input("ingrese correo ")
                for elemento in correo: 
                    if elemento == "@":
                        lista.append(correo)   
                cantidad = len(lista)
                if cantidad == 6: 
                    registro == True 
                elif cantidad < 6:
                    registro == False
                print(cantidad)
    elif opcion == 2:
        comparar = input("ingrese su usuario ")
        if (comparar == lista[4]) and cantidad == 6:
            print("Usuario bien ingresado ")
            email = input("ingrese correo ")
        elif (comparar == lista[4]) and cantidad < 6:
            print("Faltaron datos")
        else:
            print("No te has registado!!!")                     

    elif opcion == 3: 
        ingrese_rut = int(input("ingrese su rut para realizar búsqueda: "))
        largo = len(lista)
        if ingrese_rut == lista[0]:
            for indice, nombre in enumerate(lista):
                if indice == 0:
                    print(f"rut: {rut}-{dv}")
                elif indice == 1:
                    print(f"edad: {nombre}")
                elif indice == 3:
                    print(f"nombre: {nombre}")
                elif indice == 4:
                    print(f"usuario: {nombre}")
                elif indice == 5:
                    print(f"mail: {nombre}")

            

    

             
    