lista = [4,5,8,9,2,4,32,70]
print(lista[-4])

# tamanho da lista -> len 
print("tamanho da lista: ",len(lista))
# deletar um item da lista -> del
del lista[-1]
print("deletar item: ", lista)

#  Concatenar listas
lista02 = [10, 20, 30]
print("Lista 1 + lista 2: ",lista + lista02)

# adicionar item a lista -> .append
lista02.append(50)
print('Adicionando mais um item: ', lista02)

# adicionar item em uma posição desejada: -> .insert(posição, valor)
lista02.insert(2,100)
print('Adicionando item  100 na posiçao desejada: ', lista02)

# adcionar elementos de uma lista em outra -> .extend

carros = ['uno', 'Hilux', 'bmw']
motos = ['fan160', 'Bross', 'pop110']
veiculos = ['caminhao']

veiculos.extend(carros)
veiculos.extend(motos)
print('Veiculos: ', veiculos)

# Ordenar a lista de maneira ascendente

alfabetica = ['d', 'w', 'a', 'c', 'h', 'b', 'd', 'o', 'y', 'k']

# inverter uma lista -> reverse: 
alfabetica.reverse()
print('Ordem inversa: ', alfabetica)
# remover item ->

alfabetica.remove('a')
print(alfabetica)

# delimitar a criação de uma lista ate determinado valor: 
lista = []
lista = (list(range(1,200)))
print(lista)
# Permitir criação de listas com  numeros espaçados: 
lista = (list(range(0,200, 5)))
print('De 5 em 5: ', lista)


