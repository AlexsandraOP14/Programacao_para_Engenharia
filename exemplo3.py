# O objetivo é pedir a nota de 3 alunos e depois mostrar a nota mais alta, a mais baixa,
# a média geral das notas e depois ordenar em ordem crescente

lista = []

for i in range(3):
    nota = float(input('Digite a nota do Aluno {} :'.format(i+1)))
    lista.append(nota)
print('A maior nota foi: ', max(lista))
print('A menor nota foi: ', min(lista))
lista.sort(reverse = False)
print('A ordem crescente: ', lista)