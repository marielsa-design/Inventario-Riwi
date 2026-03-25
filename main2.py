def menu():
    inventario = []
    cupos = 5
    inventario = ["vacio"] * cupos

producto = {
    'nombre': "nombre",
    'precio': "precio",
    'cantidad': "cantidad",
}


menu
opcion = 0
print("Bienvenido al sistema de inventario")
while opcion < 4:
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadisticas")
    print("4. Salir")
    opcion = int(input("Escoge una opcion\n"))

    match opcion:
        case 1:
            if producto.count('vacio') > 0:
                producto = input("Ingresar un producto\n").upper()
                if producto in producto:
                    print("Este producto ya esta ingresado")
                else:
                    ubicación = producto.index("vacio")
                    producto[ubicación] = producto
                    print(f"producto ingresando: {producto}")
            else:
                print("Inventario lleno!!")
            
        case 2:
            def mostrar_inventario(inventario):
                if len(inventario) == 0:
                    print(f"El inventario esta vacio")
                else:
                    print(f"Inventario: ")
                for i, producto in enumerate(inventario):
                    print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        case 3:
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
        case 4:
            print("Adios!!")
            break
menu()


# Este programa permite gestionar un inventario básico utilizando listas y diccionarios.
# Se aplican estructuras de control como condicionales y bucles para validar datos,
# mostrar información y calcular estadísticas de los productos registrados.