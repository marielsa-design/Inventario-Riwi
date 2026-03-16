# Ejercicio 1 — Fácil
# Determinar si un número es positivo, negativo o cero

# Crea una función llamada:

# analizar_numero(numero)

# La función debe:

# Recibir un número

# Determinar si el número es:

# positivo

# negativo

# cero

# Retornar un mensaje con el resultado.

# El programa principal debe:

# Pedir al usuario que ingrese un número.

# Llamar a la función analizar_numero.

# Mostrar el resultado con primer




def analizar_numero():
    
    numero = int(input("Ingresar un numero: "))
    if numero < 0:
        print(f"Negativo") 

    if numero > 0:
        print(f"Positvo")

    if numero == 0:
        print(f"Cero")

analizar_numero()