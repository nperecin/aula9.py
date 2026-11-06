vendas = [150.0, 230.0, 90.0, 310.0]

# Criar a função para calcular o total
def calcular_total(lista):
    total = 0

    for venda in lista:
        total += venda

    return total

# Chamar a função
faturamento = calcular_total(vendas)

# Calcular a quantidade de vendas
quantidade = len(vendas)

# Exibir os resultados
print("Faturamento total: R$", faturamento)
print("Quantidade de vendas:", quantidade)