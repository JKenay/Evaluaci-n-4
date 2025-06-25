
#Creamos los contadores iniciales de nuestro proyecto.
stock1 = 150
stock2 = 180
vendidas1 = 0
vendidas2 = 0
compradores = {} #Creamos un diccionario para  guardar compradores con función elegida.

while True: #Creamos un menú de opciónes (bucle).
    print("\nTotem autoatención CafeConLeche.")
    print("1.- Comprar entrada a Cats.")
    print("2.- Cambio de función.")
    print("3.-Mostrar stock de funciones.")
    print("4.-Salir.")
    
    opcion = (input("Seleccióne una opción: ")) #Pedimos al usuario que escoja una opción.

    if opcion == "1":
        print("\n--Comprar entrada a cats.")
        nombre = input("Nombre del comprador: ").lower() #Evitamos fallo respecto a mayúsculas
        if nombre in compradores:
            print("ya compraste una entrada.")
        else: #Mostramos funciónes disponibles
            print("1. Cats Dia Viernes.")
            print("2. Cats Día Sábado.")
            funcion = input("Cual función prefiere (1 o 2): ")
            if funcion == "1" and stock1 > 0:
                compradores[nombre] = 1
                stock1 -= 1
                vendidas1 += 1
                print("Entrada registrada en función 1!!!.","Stock disponible:") #Registro válidado
                print("Función 1: ",stock1) 
                print("Función 2: ",stock2)
            elif funcion == "2" and stock2 > 0:
                compradores[nombre] = 2
                stock2 -= 1
                vendidas2 += 1
                print("Entrada registrada en función 2!!!.", "Stock disponible:") #Registro válidado
                print("Función 1: ",stock1)
                print("Función 2: ",stock2)
            else:
                print("Error, función inválida.") #Función inválida.

    elif opcion == "2":
        print("\n--Cambio de función") #Usuario cambia de opción.
        nombre = input("Nombre del comprador: ").lower()
        if nombre not in compradores:
            print("comprador no registrado/encontrado.")#En caso de que el usuario no se encuentre archivado.
        else:
            actual =compradores[nombre]
            nueva = 2 if actual == 1 else 1
            cambiar = input(f"¿Cambiara de funcion {actual} a {nueva} (S/N): ").lower() #Cambio de función
            if cambiar == "s":
                if nueva == 1 and stock1 > 0:
                    stock1 -= 1
                    stock2 += 1
                    vendidas1 += 1
                    vendidas2 -= 1
                    compradores[nombre] = 1
                    print("Cambio exitoso!!, su función es la 1.")
                elif nueva == 2 and stock2 > 0:
                    stock1 += 1
                    stock2 -= 1
                    vendidas1 -= 1
                    vendidas2 += 1
                    print("Cambio exitoso!!, su función es la 2.")
                else:
                    print("No hay stock en la otra función.")
            else:
                    print("Cambio cancelado.")

    elif opcion == "3": #Cantidad de stock disponible y vendido.
        print("\n-- stock de funciones--")
        print("Funcion 1 (viernes): ", stock1, "disponibles", ",totales vendidas: ", vendidas1)
        print("Funcion 2(Sábado): ", stock2, "disponibles", ",totales vendidas: ", vendidas2)
    
    elif opcion == "4":
        print("programa terminado...") #Finalización del programa.
        break

    else:
        print("¡Debe ingresar una opción válida!.") #En caso de que el usuario coloque algo inválido

