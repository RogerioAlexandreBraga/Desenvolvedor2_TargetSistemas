import json

# Carregar os dados do faturamento a partir de um arquivo JSON
with open("faturamento.json", "r") as file:
    dados = json.load(file)

# Remover dias sem faturamento (zero)
faturamento_valido = [dia["valor"] for dia in dados if dia["valor"] > 0]

# Cálculo do menor e maior faturamento
menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

# Cálculo da média mensal, considerando apenas dias com faturamento
media_mensal = sum(faturamento_valido) / len(faturamento_valido)

# Número de dias com faturamento superior à média
dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

# Exibir resultados
print(f"Menor faturamento diário: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento diário: R$ {maior_faturamento:.2f}")
print(f"Dias acima da média mensal: {dias_acima_da_media}")
