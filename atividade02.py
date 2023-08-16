
# # Questão 01) Crie um dicionário d e coloque nele seus dados: nome, idade, telefone,endereço. Usando o dicionário d criado anteriormente, imprima seu nome.
# dados = {'nome' : 'Alisson', 'idade': 19, 'telefone': 75932452323, 'endereco': 'Santo Estevão-Ba'}
# print(dados['nome'])


# # Questão 02) Crie um dicionário d e coloque nele os dados fornecidos pelo usuário:nome, idade, telefone,endereço. Também usando d, imprima todos os itens do dicionário no formato chave : valor, ordenado pela chave

# dados02 = {}

# dados02['nome'] = input('Insira seu nome: ')
# dados02['idade'] = input('Insira sua idade: ')
# dados02['telefone'] = input('Insira seu telefone: ')
# dados02['endereco'] = input('Insira seu enderço: ')
# print('Seus dados são: \n', dados02)

# #Questão03)  Crie um dicionário que é uma agenda e coloque nele os seguintes dados:chave (cpf), nome, idade, telefone. O programa deve ler um númeroindeterminado de dados, criar a agenda e imprimir todos os itens do dicionário no formato chave: nome-idadefone.

# agenda = {}

# agenda['cpf'] = input('Digite seu cpf: ')
# agenda['nome'] = input('Digite seu nome: ')
# agenda['idade'] = input('Digite sua idade: ')
# agenda['telefone'] = input('Digite seu telefone: ')

# busca = input('Insira o cpf para buscar seus dados: ')
# if busca == agenda['cpf']:
#     print('Nome: ', agenda['nome'])
#     print('idade: ', agenda['idade'])
#     print('Telefone: ', agenda['telefone'])

# Quetão 04) Crie um programa que cadastre informações de várias pessoas (nome,idade e cpf) e depois coloque em um dicionário. Depois remova todas aspessoas menores de 18 anos do dicionário e coloque em outro dicionário.

cadastro01 = {}
opc = 0

while opc != 1:
    cadastro01['nome'] = input('Insira seu nome: ')
    cadastro01['idadae'] = input('Insira sua idade: ')
    cadastro01['cpf'] = input('Insira seu cpf: ')
    opc = input('Tecle 1 para finalizar. \n Tecle Enter para cadastrar outra pessoa')
    