#PRUEBA CRISTIAN

print("----- BIENVENIDO A PLATAFORMA GAME_STORE ----")
print(" --------------------------------------------")
print("-----> Por Favor Seleccione una opción <-----")
print(" --------------------------------------------")
opcion = 0
rut = 0
dv =0
nombre=0
edad=0
correo=0
varcorreo=0
alias=0
aliasingreso=0
lista=[]
error_edad = False
##rut.nombre.edad

while opcion != 4:
    print("1) Registrarse\n2) Conectarse\n3) Registro de accesos\n4) Salir De Sistema")
    
    opcion = int(input( " Por favor ingrese opción "))

    if opcion == 1:
            print( " Usted ha seleccionado la opción Registrarse")
            try:
                rut = int(input( " Por favor ingrese su rut sin digito verificador: "))
                lista.append(rut)
                
            except ValueError:
                    print("Solo debe ingresar numeros")
                    respuesta=input("Desea ingresar nuevamente los valores?[s/n]")
                    if respuesta=="n":
                        break
            dv = str(input( " Por favor ingrese su digito verificador: "))
            lista.append(dv)            

            while len(dv) != 1:
                try:
                   dv = str(input( " Por favor ingrese su digito verificador correctamente: "))
                   lista.append(dv)
                except:
                    print('ingrese correctamente el digito validador')
           
            nombre = str(input( " Por favor ingrese su Nombre: "))
            lista.append(nombre)

            while len(nombre) == 0:
                try:
                   nombre = str(input( " Por favor ingrese su nombre correctamente: "))
                   lista.append(nombre)
                   
                except:
                    print('ingrese correctamente el Nombre')

            edad = int(input( " Por favor Edad: "))
                         
            if edad < 18 or edad > 100:
                print("Debes ser mayor de edad")
            else:
                lista.append(edad)
              
                        
            
            alias = str(input( " Por favor ingrese su alias: "))
            lista.append(alias)
            while len(alias) ==0:
                try:
                   alias = str(input( " Por favor ingrese su alias correctamente: "))
                   lista.append(alias)

                except:
                    print('ingrese correctamente el alias')
            
            correo = str(input( " Por favor ingrese su Correo: "))
            for letra in correo: 
                if letra == "@":
                    lista.append(correo)
            print(lista)
            for i in lista:
                print(i)
            


    elif opcion == 2:
        print (" Conectarse ")

        aliaaliasingresos = str(input( " Por favor ingrese su alias: "))
        if (aliaaliasingresos == alias):
          print(' USTED SE HA REGISTRADO CON LOS SIGUIENTES DATOS ' ) 
          print(correo+ ' ' + nombre +' '+ alias  ) 
          print(' AHORA ESTA CONECTADO ' ) 
        else:
            print('Usted No posee una cuenta registrada, registrese')

    elif opcion == 3:
        try: 
            ingrese_rut = int(input("ingrese su rut para realizar búsqueda: "))
            largo = len(lista)
            if ingrese_rut == lista[0]:
                for indice, nombre in enumerate(lista):
                    if indice == 0:
                        print(f"rut: {rut}-{dv}")
                    elif indice == 3:
                        print(f"edad: {nombre}")
                    elif indice == 2:
                        print(f"nombre: {nombre}")
                    elif indice == 4:
                        print(f"usuario: {nombre}")
                    elif indice == 5:
                        print(f"mail: {nombre}")
        except:
            print("no te has registrado, elige opción 1 por favor ")
    elif opcion == 4:
        print("Ha salido del sistema")
        break