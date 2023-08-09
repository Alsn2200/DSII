import random
# 01)Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista
numeros = [1,2,3,4,5]
item = 0 
n = 0
for item in numeros:
    n += 1
    print(f'Numero {item} na posição {numeros.index(n)}')
    
# 2 Ler uma lista de 10 números reais e mostre-os na ordem inversa. 

numeros10 = [1.0, 2.0, 3.0, 4.0, 5.7, 6.5, 8.9, 9.5, 10.0]
numeros10.reverse()
print(numeros10)

# 3 Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média. 
notas = [4.7, 6.9, 8.9,9.9]
soma = 0
for num in notas:
    soma  += num
   
media = soma / 4
print(f"A media do aluno foi: {media}, referente as suas notas: {notas}")

# Ler um vetor com 20 idades e exibir a maior e menor.
listaIdades = []
for idades in range(1, 21):
    idades = random.randint(1,20)
    listaIdades.append(idades)
print('Todas as idades: ',listaIdades)
print('A maior idade é: ', max(listaIdades))
print('A menor idade é: ', min(listaIdades))
