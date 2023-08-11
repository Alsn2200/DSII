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

# 04) Ler um vetor com 20 idades e exibir a maior e menor.
listaIdades = []
for idades in range(1, 21):
    idades = random.randint(1,20)
    listaIdades.append(idades)
print('Todas as idades: ',listaIdades)
print('A maior idade é: ', max(listaIdades))
print('A menor idade é: ', min(listaIdades))

# 05 ) Utilizando o del, remova todos os elementos da lista criada anteriormente até a lista ficar vazia.
while len(listaIdades) > 0:
    del listaIdades[0]
    print(listaIdades)
# 06) Faça uma lista de compras do mês, não se esqueça de comprar produtos de limpeza e sorvete!
produtosLimpeza = ['Sabão', 'Detergente', 'Papel-Higienico']
produtosSorveteria = ['Sorvete de Chocolate', 'Sorvete de Morango']
listaDeCompras =[ produtosLimpeza, produtosSorveteria, 'Bolacha', 'Uva', 'Aveia']
print(listaDeCompras)
# Agora «vá ao mercado» e delete apenas os produtos de limpeza da lista.
while produtosLimpeza in listaDeCompras:
        listaDeCompras.remove(produtosLimpeza)
        print(listaDeCompras)
# Agora «vá à sorveteria» e se empanturre e sorvete e tire o sorvete da lista.
while produtosSorveteria in listaDeCompras:
     listaDeCompras.remove(produtosSorveteria)
     print(listaDeCompras)

# 07: Faça uma função que determina se um número é par ou ímpar. Use o % para determinar o resto de uma divisão.Por exemplo: 3 % 2 = 1 e 4 % 2 = 0
def impar_par(number):
     if number % 2 == 0:
          print( f'Numero {number} é par')
     else:
          print( f'Numero {number} é impar')
escolha = 0
while escolha != '*':
    escolha = input('Insira um numero \n Para cancelar digite "*"') 
    print(impar_par(escolha))
# Duas palavras são um “par inverso” se uma for o contrário da outra. Escreva uma função que dado duas palavras,retorne True caso sejam.
def inverso (palavraA , palavraB):
     return palavraA == palavraB[::-1]
palavraA = input('Insira a primeira palavra')
palavraB = input('Insira a segunda palavra')

if inverso(palavraA, palavraB):
     print('Palavras iguais invertidas')
else: 
     print('As palavras não sao iguais invertidas')
     
# Escreva uma função que imprime todos os números primos entre 1 e 50 
# Dica: um número é primo se ele for divisível apenas por 1 e ele mesmo, use o operador % (resto da divisão) para isso.
def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def imprimir_primos_ate_50():
    for numero in range(1, 51):
        if primo(numero):
             print(numero)