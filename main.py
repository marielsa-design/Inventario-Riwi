# Lista de los productos en un diccionario

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


def menu():
    opcion = 0
    print("Bienvenido al sistema de inventario") # Titulo principal
    while opcion < 6: # Menú de Inventario de los producto (Estructuras)
        print("1. Agregar producto") 
        print("2. Mostrar inventario") 
        print('3. Buscar el producto') 
        print('4. Actualizar producto') 
        print('5. Eliminar el producto') 
        print("6. Calcular estadisticas") 
        print("7. Salir")
        opcion = int(input("Escoge una opcion\n"))
        match opcion:
            case 1: # Agregar productos
                nombre=input("Nombre de producto: ") 
                precio=float(input("Numero de precio: "))
                cantidad=int(input("Numero de cantidad: ")) 

                nuevo_producto= { # Agregar un nuevo producto o más
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }

                inventario.append(nuevo_producto) # el metodo de "Añadir"

                print("producto agregado")       
            case 2: # Mostrar productos
                if len(inventario) == 0:
                    print(f"El inventario esta vacio") # Si el inventario no aparece
                else:
                    print(f"Inventario: ") # Mostar el invenatario
                    for i, producto in enumerate(inventario):  # Utilizar con el metodo de String 
                        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
            case 3: # Buscar productos
                nombre = input("Nombre de producto: ")
                producto_encontrado = None

                for i, producto in enumerate(inventario):
                    if producto["nombre"].lower() == nombre.lower():
                        producto_encontrado = producto
                        break
                        # Hay 2 opciones si el producto aparece o no aparece
                if producto_encontrado is not None:
                    print(f"Producto encontrado :")
                    print(producto_encontrado)
                else:
                    print("Producto no encontrado.")
            case 4: # Acualizar productos
                def buscar_producto(nombre): # Funcion de def: "buscar_producto"
                    for producto in inventario:
                        if producto["nombre"] == nombre:
                            return producto
                    return None
                
                nombre = input("Nombre del producto: ")
                resultado = buscar_producto(nombre)
                if resultado: # Mostrar el producto con el precio y cantidad
                    print(f"producto encontrado: {resultado["nombre"]}")
                    print(f"precio: {resultado["precio"]}")
                    print(f"cantidad: {resultado["cantidad"]}")
                    print(f"valor total en inventario: {resultado["precio"] * resultado["cantidad"]}")
                else:
                    print("producto no encontrado.")
            case 5: # Eliminar productos
                for i in inventario:
                    print(i)
                nombre=input("Nombre de producto que quieres eliminar: ")
                print("Producto eliminado correctamente")
                inventario.pop(0) # Metodo de def: "delete o pop"
            case 6: # Calcular productos
                if len(inventario) == 0:
                    print("No hay productos para calcular")
                else: # Mostrar el resultado de inventario
                    total_valor = 0
                    total_producto = 0
                    for producto in inventario:
                        total_valor += producto["precio"] * producto["cantidad"]
                        total_producto += producto["cantidad"]
                print("Estadísticas:")
                print(f"Valor total del inventario: {total_valor}")
                print(f"Cantidad total de productos: {total_producto}")
            case 7: # Salir el sistema
                print("salir")
                break

menu()

# Este programa permite gestionar un inventario básico utilizando listas y diccionarios.
# Se aplican estructuras de control como condicionales y bucles para validar datos,
# Mostrar información y calcular estadísticas de los productos registrados.