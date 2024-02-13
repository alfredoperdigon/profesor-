def calcular_temperatura_media(temp_max, temp_min):
    return (temp_max + temp_min) / 2

def main():
    try:
        num_dias = int(input("Ingrese el número de días para los que desea calcular la temperatura media: "))
        for i in range(1, num_dias + 1):
            temp_max = float(input(f"Ingrese la temperatura máxima para el día {i}: "))
            temp_min = float(input(f"Ingrese la temperatura mínima para el día {i}: "))
            temp_media = calcular_temperatura_media(temp_max, temp_min)
            print(f"La temperatura media para el día {i} es: {temp_media}")
    except ValueError:
        print("Error: Por favor ingrese un número válido para el número de días y temperaturas.")

if __name__ == "__main__":
    main()


