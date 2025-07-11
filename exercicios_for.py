# Soma dos números ímpares de 1 a 10
soma_impares = 0
for numero in range(1, 11):
    if numero % 2 != 0:
        soma_impares += numero
print(f"\n📘 Soma dos números ímpares de 1 a 10: {soma_impares}")

# Ordem decrescente
print("\n📘 Números de 10 a 1 em ordem decrescente:")
for numero in range(10, 0, -1):
    print(numero)

# Tabuada de um número com input
print("\n📘 TABUADA DE UM NÚMERO")
try:
    numero = int(input("Digite um número para ver a tabuada de 1 a 10: "))
    print(f"\nTabuada de {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
except ValueError:
    print("❌ Entrada inválida! Por favor, digite um número inteiro.")

# Soma de elementos de uma lista
print("\n📘 SOMANDO ELEMENTOS DE UMA LISTA")
numeros = [3, 5, 7, 9, 11]
try:
    soma_total = sum(numeros)
    print(f" Números na lista: {numeros}")
    print(f" Soma total: {soma_total}")
except Exception as erro:
    print("❌ Ocorreu um erro ao somar os números:", erro)

# Média de elementos de uma lista
print("\n📘 MÉDIA DOS ELEMENTOS DA LISTA")
valores = [10, 20, 30, 40, 50]  # Testa depois com lista vazia também

try:
    if len(valores) == 0:
        raise ZeroDivisionError("A lista está vazia.")
    media = sum(valores) / len(valores)
    print(f" Lista de valores: {valores}")
    print(f" Média: {media:.2f}")
except ZeroDivisionError as erro:
    print("❌ Erro:", erro)