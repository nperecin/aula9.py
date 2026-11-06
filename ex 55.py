despesas = [45.0, 120.0, 35.5, 80.0]

total = 0

# Percorrer a lista e calcular o total
for despesa in despesas:
    total += despesa

# Calcular a média
media = total / len(despesas)

# Encontrar a maior e a menor despesa
maior = max(despesas)
menor = min(despesas)

# Exibir os resultados
print("Total gasto: R$", total)
print("Média por despesa: R$", media)
print("Maior despesa: R$", maior)
print("Menor despesa: R$", menor)