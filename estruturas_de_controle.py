# 1) Escreva um programa que, dados 2 numeros diferentes (a e b), encontre o menor deles:
 
num1  =input("Insira um numero: ")
num2 = input("Insira outo numero: ")

if num1 > num2:
    print(f'O número {num1} é maior que o número {num2}' )
elif num2 > num1:
    print(f'O número {num2} é maior que o número {num1}' )

else:
    print('Os números são iguais.')

# 2) doação de sangue -> ter entre 16 e 69, pesar 59+kg , ter dormido 6hrs no ultimo dia

nome =input('Insira seu nome: ')
idade =int(input('Insira sua idade: '))
peso =input('Insira seu peso: ')
horas_dormidas =input('Quanto tempo voçê dormiu nas ultimas 24h? ')

if idade >=16 or idade <= 69 and peso >= 50 and horas_dormidas >= 6:
    print(f'Parabéns {nome} você pode doar sangue :D')
else: 
    print(f'Infelizmente {nome} você não cumpre os requisitos para a doação de sangue.')  

# 3) adição de numeros:

num3 = int(input('Insira um numero: '))
num4 = int(input('Insira outro numero: '))
result = num3 + num4
print(f'O valor da soma foi = {result}')
if result > 20:
    result += 8
    print(f'O valor da soma + 8 foi = {result}')
else:
    print(f'O valor da soma - 5 foi = {result}')