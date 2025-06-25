stock1 = 150
stock2 = 180
vendidas1 = 0
vendidas2 = 0
compradores = {}

while True:
    print("\nTotem autoatención CafeConLeche.")
    print("1.- Comprar entrada a Cats.")
    print("2.- Cambio de función.")
    print("3.-Mostrar stock de funciones.")
    print("4.-Salir.")
    
    opcion = (input("Seleccióne una opción: "))

    if opcion == "1":
        print("\n--Comprar entrada a cats.")
        nombre = input("Nombre del comprador: ").lower()
        if nombre in compradores:
            print("ya compraste una entrada.")
        else:
            print("1. Cats Dia Viernes.")
            print("2. Cats Día Sábado.")
            funcion = input("Cual función prefiere (1 o 2): ")
            if funcion == "1" and stock1 > 0:
                compradores[nombre] = 1
                stock1 -= 1
                vendidas1 += 1
                print("Entrada registrada en función 1!!!.","Stock disponible:")
                print("Función 1: ",stock1) 
                print("Función 2: ",stock2)
            elif funcion == "2" and stock2 > 0:
                compradores[nombre] = 2
                stock2 -= 1
                vendidas2 += 1
                print("Entrada registrada en función 2!!!.", "Stock disponible:")
                print("Función 1: ",stock1)
                print("Función 2: ",stock2)
            else:
                print("Error, función inválida o sin stock")

    elif opcion == "2":
        print("\n--Cambio de función")
        nombre = input("Nombre del comprador: ").lower()
        if nombre not in compradores:
            print("comprador no registrado/encontrado.")
        else:
            actual =compradores[nombre]
            nueva = 2 if actual == 1 else 1
            cambiar = input(f"¿Cambiara de funcion {actual} a {nueva} (S/N): ").lower()
            if cambiar == "s":
                if nueva == 1 and stock1 > 0:
                    stock1 -= 1
                    stock2 += 1
                    vendidas1 += 1
                    vendidas2 -= 1
                    compradores[nombre] = 1
                    print("Cambio realizado, su función es la 1.")
                elif nueva == 2 and stock2 > 0:
                    stock1 += 1
                    stock2 -= 1
                    vendidas1 -= 1
                    vendidas2 += 1
                    print("Cambio realizado, su función es la 2.")
                else:
                    print("No hay stock en la otra función.")
            else:
                    print("Cambio cancelado.")

    elif opcion == "3":
        print("\n-- stock de funciones--")
        print("Funcion 1 (viernes): ", stock1, "disponibles", ",totales vendidas: ", vendidas1)
        print("Funcion 2(Sábado): ", stock2, "disponibles", ",totales vendidas: ", vendidas2)
    
    elif opcion == "4":
        print("programa terminado...")
        break

    else:
        print("¡Debe ingresar una opción válida!.")

