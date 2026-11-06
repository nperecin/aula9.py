pedidos = [18.50, 25.00, 12.00, 32.50]

# Criar função para calcular o total vendido
def calcular_total(lista):
    total = 0

    for pedido in lista:
        total += pedido

    return total

# Calcular a quantidade de pedidos
quantidade = len(pedidos)

# Calcular o total vendido
total_vendido = calcular_total(pedidos)

# Criar dicionário com o resumo
resumo = {
    "cafeteria": "Café Central",
    "quantidade_pedidos": quantidade,
    "total_vendido": total_vendido
}

# Mostrar as informações do dicionário
print("Nome:", resumo["cafeteria"])
print("Quantidade de pedidos:", resumo["quantidade_pedidos"])
print("Total vendido: R$", resumo["total_vendido"])