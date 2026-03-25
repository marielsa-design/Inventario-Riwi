inventario = [
     {
        "nombre": "Laptop",
        "precio": 2500,
        "cantidad": 25
    },
    {
        "nombre": "Audiofono",
        "precio": 1200,
        "cantidad": 15
    },
    {
        "nombre": "Mouse",
        "precio": 500,
        "cantidad": 15
    }
] 

# Menú de Inventario de los producto
def menu():
    opcion = 0
    print("Bienvenido al sistema de inventario")
    while opcion < 6:
        print("1. Agregar producto") #listo
        print("2. Mostrar inventario") #listo
        print('3. Buscar el producto') #progreso #No se olvide el "buscar_producto" de diccionario
        print('4. Actualizar producto') #progreso
        print('5. Eliminar el producto') #progreso
        print("6. Calcular estadisticas") #listo
        print("7. Salir") #listo
        opcion = int(input("Escoge una opcion\n"))
        match opcion:
            case 1:
                nombre=input("Nombre de producto: ") 
                precio=float(input("Numero de precio: "))
                cantidad=int(input("Numero de cantidad: ")) 

                nuevo_producto= {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }

                inventario.append(nuevo_producto)

                print("producto agregado")       
            case 2:
                if len(inventario) == 0:
                    print(f"El inventario esta vacio")
                else:
                    print(f"Inventario: ")
                    for i, producto in enumerate(inventario):
                        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
            # case 3:
            # case 4:
            case 5:
                for i in inventario:
                    print(i)
                nombre=input("Nombre de producto que quieres eliminar: ")
                print("Producto eliminado correctamente")
                inventario.remove(nombre)
            

            case 6:
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
            case 7:
                print("salir")
                break

menu()