nombre = [5]
inventario = ['vacio'] * nombre

# Menú de Inventario de los producto
def menu():
    opcion = 0
    print("Bienvenido al sistema de inventario")
    while opcion < 4:
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print('3. Buscar el producto')
        print('4. Actualizar producto ')
        print('5. Eliminar el producto')
        print("6. Calcular estadisticas")
        print("7. Salir")
        opcion = int(input("Escoge una opcion\n"))
        match opcion:
            case 1:
                if inventario.count('vacio')> 0:
                    producto=input('Ingresar el producto\n').upper()
                    if  producto in inventario:
                        print('Este producto ya esta ingresado')
                    else:
                        ubicacion = inventario.idex('vacio')
                        inventario[ubicacion] = producto
                        print(f'producto ingresando: {producto}')
                else:
                    print('Inventario lleno!')
            case 2:



#             case 2:
#                 if inventario.count('vacio')!= cupos:
#                         nombre= input('Ingresa el nombre de producto\n').upper()
#                         if nombre in inventario:
#                             ubicación= inventario.index(nombre)
#                             inventario[ubicación]= 'vacio'
#                             print(f'producto retirado: {nombre}')
#                         else:
#                             print(f'el producto de {nombre} no esta ingresado')
#                 else:
#                     print(f'inventario vacio!!!')
#             case 3:
#                 def calcular_estadisticas(inventario):
#                     if len(inventario) == 0:
#                         print("No hay productos para calcular")
#                     else:
#                         total_valor = 0
#                         total_producto = 0
#                     for producto in inventario:
#                         total_valor += producto["precio"] * producto["cantidad"]
#                         total_producto += producto["cantidad"]

#                     print("Estadísticas:")
#                     print(f"Valor total del inventario: {total_valor}")
#                     print(f"Cantidad total de productos: {total_producto}")
#             case 4:
#                 print("Adios!!")
#                 break

            # case 3:
            #     if inventario.count('vacio')!= cupos:
            #             nombre= input('Ingresa el nombre de producto\n').upper()
            #             if nombre in inventario:
            #                 ubicación= inventario.index(nombre)
            #                 inventario[ubicación]= 'vacio'
            #                 print(f'producto retirado: {nombre}')
            #             else:
            #                 print(f'el producto de {nombre} no esta ingresado')
            #     else:
            #         print(f'inventario vacio!!!')