# Función para verificar si el primer número es múltiplo del segundo
def es_multiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

# Pedir al usuario dos números enteros
num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

# Verificar si alguno de los números es múltiplo del otro
if es_multiplo(num1, num2):
    print(f"{num1} es múltiplo de {num2}.")
elif es_multiplo(num2, num1):
    print(f"{num2} es múltiplo de {num1}.")
else:
    print("Los números no son múltiplos entre sí.")

