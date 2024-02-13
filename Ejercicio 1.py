def EscribirCentrado(texto):
    # Calcula la cantidad de espacios antes del texto para centrarlo
    espacios = 40 - len(texto) // 2
    # Imprime los espacios y luego el texto centrado
    print(' ' * espacios + texto)
    # Imprime el subrayado con el caracter '='
    print('=' * 80)

# Ejemplo de uso
texto = "Hola, Me llamo Anyelis"
EscribirCentrado(texto)
