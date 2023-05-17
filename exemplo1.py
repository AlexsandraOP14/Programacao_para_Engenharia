# O objetivo é pedir para usuário o nome de 5 amigos e salvar em uma lista
# A seguir exibir o nome de cada amigo com uma mensagem

lista = []
traco = ('_')

for i in range (5):
    nomes = input('Digite o nome de um amigo: ')
    lista.append(nomes)
for i in range (5):
    print(traco * 50)
    print('Obrigada por fazer parte da minha vida: ',lista[i])