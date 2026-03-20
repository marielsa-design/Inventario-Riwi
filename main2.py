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
    inventario = []

    while True:
        print("Menú")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadisticas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto(inventario)

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "3":
            calcular_estadisticas(inventario)

        elif opcion == "4":
            print("Adios!")
            break

        else:
            print("Opcion invalida, intente de nuevo")

menu()

# Este programa permite gestionar un inventario básico utilizando listas y diccionarios.
# Se aplican estructuras de control como condicionales y bucles para validar datos,
# mostrar información y calcular estadísticas de los productos registrados.4