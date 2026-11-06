notas = [7.5, 8.0, 6.5, 9.0]

soma = 0

for nota in notas:
    print("Nota:", nota)
    soma += nota

media = soma / len(notas)

print("Soma das notas:", soma)
print("Média das notas:", media)