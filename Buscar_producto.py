def buscar_producto(nombre):
    for producto in inventario:
        if producto["nombre"] == nombre:
            return producto
    return None


inventario=[
    {"nombre": "manzana", "precio": 0.5, "cantidad": 100},
    {"nombre": "banana", "precio": 0.3, "cantidad": 150},
    {"nombre": "naranja", "precio": 0.7, "cantidad": 80},
    {"nombre": "pera", "precio": 0.4, "cantidad": 120},
    {"nombre": "uva", "precio": 0.2, "cantidad": 200}
]

print("menu")
print("1. Buscar producto")
print("2. Salir")
opcion = input("Seleccione una opción: ")
if opcion == "1":
    nombre_producto = input("Ingrese el nombre del producto: ")
    resultado = buscar_producto(nombre_producto)
    if resultado:
        print(f"Producto encontrado: {resultado["nombre"]}")
        print(f"Precio: {resultado["precio"]}")
        print(f"Cantidad: {resultado["cantidad"]}")
        print(f"Valor total en inventario: {resultado["precio"] * resultado["cantidad"]}")
    else:
        print("Producto no encontrado.")