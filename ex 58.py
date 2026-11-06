notas = [6.0, 8.5, 7.0, 5.5, 9.0]

# Contar quantas notas são maiores ou iguais a 7
aprovados = 0

for nota in notas:
    if nota >= 7:
        aprovados += 1

# Criar função para calcular a média
def calcular_media(lista):
    soma = 0

    for nota in lista:
        soma += nota

    return soma / len(lista)

# Chamar a função
media = calcular_media(notas)

# Mostrar os resultados
print("Quantidade de notas iguais ou superiores a 7:", aprovados)
print("Média da turma:", media)