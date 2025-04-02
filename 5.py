def inverter_string(texto):
    invertida = ""
    for i in range(len(texto) - 1, -1, -1):  # Percorre a string de trás para frente
        invertida += texto[i]
    return invertida

# Entrada da string pelo usuário
texto_original = input("Digite uma palavra ou frase para inverter: ")

# Exibe o resultado
print("String invertida:", inverter_string(texto_original))
