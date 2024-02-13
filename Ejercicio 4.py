def ConvertirEspaciado(texto):
    # Utilizamos join con una lista de caracteres separados por un espacio adicional
    return ' '.join(texto.upper())

# Programa principal
texto = "Hola, tu"
texto_con_espacios = ConvertirEspaciado(texto)
print(texto_con_espacios)



