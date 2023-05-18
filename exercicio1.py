listaMes = []
listaTem = []
ano = {}

for i in range(4):
    mes = input('Digite o mês que você deseja adicionar a temperatura: ')
    listaMes.append(mes)
    temperatura = float(input('Digite a temperatura média: '))
    listaTem.append(temperatura)
    ano[listaMes[i]] = listaTem[i]
print(ano)