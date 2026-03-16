# Función para determinar si una persona puede votar

# Crea una función llamada:puede_votar(edad)

# La función debe:

# Recibir la edad de una persona
# Si la edad es mayor o igual a 18, RETORNAR "Puede votar"
# Si no, RETORNAR "No puede votar"

# El programa principal debe:

# a. Pedir el nombre
# b. Pedir la edad
# c. Llamar a la función
# d. Mostrar el resultado en pantalla.

cupos = 4
usuario = ["vacio"]*cupos

def puede_votar():
    
    edad = int(input("Ingresar tu edad: "))
    if edad < 17:
        print(f"No se puede votar")
    
    if edad > 18:
        print(f"Puede votar")

    if edad == 18:
        print(f"Puede votar")

puede_votar()

opcion = 1
print("Bienvenido a el centro de votación")

while True:
    print("a. Pedir el nombre")
    print("b. Pedir la edad")
    print("c. Llamar a la función")
    print("d. Mostrar el resultado en pantalla")

    try:
        opcion = int(input("Ingresar una opción: "))
    except ValueError:
        print("Ingresar una opción válido ")

    match opcion:
        case 1:
            if usuario.count("vacio") > 0:
                nuevo_usuario = input(f"Ingresa tu nombre: ").upper()
                if usuario in usuario:
                    print("Ese nombre ya existe")
                else:
                    index = nuevo_usuario.index("vacio")
                    usuario[index] = usuario
                    print(f"Nombre '{usuario}' agregado correctamente")
            else:
                print("Tu nombre ya esta aquí")

        case 2:
            if usuario.count("vacio") > 0:
                nuevo_nombre = input(f"Ingresar tu edad: ")
                if usuario in nuevo_usuario:
                    print("Este tu edad ya existe")
                else:
                    index = nuevo_usuario.index("vacio")
                    usuario[index] = nuevo_usuario
                    print(f"Edad '{nuevo_usuario}' agregado correctamente")
            else:
                print("Tu edad ya esta aqui")

        case 3:
            print("\nFuncion actual: ")
            for i, item in enumerate(usuario):
                print(f"Espacio {i+1}: {item}")
