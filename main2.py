inventario = []

def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    
    # Validar el precio
    while True:
        try:
            precio = float(input("Ingrese el precio de precio: "))
            break
        except ValueError:
            print("Error. Ingrese un numero valido")

    #Validar la cantidad de precio
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de precio: "))
            break
        except ValueError:
            print("Error. Ingresar un numero enterio valido")

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print(f"Producto agregado correctamente")

# Agregar a la lista de producto

def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print(f"El inventario esta vacio")
    else:
        print(f"Inventario: ")
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

# Calcular de estadisticas de producto

def calcular_estadisticas(inventario):
    if len(inventario) == 0:
        print("No hay productos para calcular")
    else:
        total_valor = 0
        total_producto = 0
        for producto in inventario:
            total_valor += producto["precio"] * producto["cantidad"]
            total_producto += producto["cantidad"]
        
        print("Estadísticas:")
        print(f"Valor total del inventario: {total_valor}")
        print(f"Cantidad total de productos: {total_producto}")

def menu():
    cupos = 5
    inventario = ['vacio'] * cupos

    opcion = 1
    print("Bienvenido al sistema de inventario")
    while opcion < 4:
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadisticas")
        print("4. Salir")
        opcion = int(input("Escoge una opcion\n"))

        match opcion:
            case 1:
                if inventario.count('vacio') > 0:
                    producto = input("Ingresar un producto\n").upper()
                    if producto in inventario:
                        print("Este producto ya esta ingresado")
                    else:
                        ubicación = inventario.index("vacio")
                        inventario[ubicación] = producto
                        print(f"producto ingresando: {producto}")
                else:
                    print("Inventario lleno!!")
            case 2:
                def mostrar_inventario():
                    for i, carro in enumerate(inventario, start=1):
                        print(f"{i}. {producto}")
                if len(inventario) > 0:
                    producto = input("Ingresa el producto\n").upper()
                    if producto in inventario:
                        inventario.remove(producto)
                        print(f"producto retirado: {producto}")
                    else:
                        print(f"{producto} no esta ingresado")
                else:
                    print("Inventario lleno!!")
            case 3:
                print(inventario)
            case _:
                print("Adios!!")
                break

        # opcion = input("Seleccione una opción: ")
        # if opcion == "1":
        #     agregar_producto(inventario)

        # elif opcion == "2":
        #     mostrar_inventario(inventario)

        # elif opcion == "3":
        #     calcular_estadisticas(inventario)

        # elif opcion == "4":
        #     print("Adios!")
        #     break

        # else:
        #     print("Opcion invalida, intente de nuevo")

menu()

# Este programa permite gestionar un inventario básico utilizando listas y diccionarios.
# Se aplican estructuras de control como condicionales y bucles para validar datos,
# mostrar información y calcular estadísticas de los productos registrados.4