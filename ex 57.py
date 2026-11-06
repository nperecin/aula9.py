produto = {
    "nome": "Caderno",
    "preco": 25.90,
    "quantidade": 10
}

# Calcular o valor inicial do estoque
valor_inicial = produto["preco"] * produto["quantidade"]

print("Produto:", produto["nome"])
print("Valor inicial do estoque: R$", valor_inicial)

# Acrescentar 5 unidades ao estoque
produto["quantidade"] += 5

# Calcular o novo valor do estoque
novo_valor = produto["preco"] * produto["quantidade"]

# Mostrar os dados atualizados
print("Nova quantidade:", produto["quantidade"])
print("Novo valor em estoque: R$", novo_valor)