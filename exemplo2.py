# O objetivo é pedir ao usuário 5 valores inteiros e inserir em uma lista
# Aseguir mostre na tela os valores em ordem crescente e decrescente

lista = []

for i in range(5):
    num = int(input('Digite um número inteiro: '))
    lista.append(num)
lista.sort(reverse = False)
print('A ordem crescente dos números é: ', lista)
lista.sort(reverse = True)
print('A ordem decrescente dos números é: ', lista)