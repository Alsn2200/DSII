# len -> calcular caractere ex: len("string")
string = "olá Alisson"
print(len(string))
# Indices de string ex: palavra[0]
palavra  = "Alisson"
print(palavra[2])

# Fatiamento de strings ex: frase[0:15]
frase =  "olá Alisson tudo bem?"
print(frase[0:11])

# formatação utilizando o .format
nome = input('Insira seu nome: ')
idade = input('Insira sua idade: ')
print("Olá {} você tem {}".format(nome, idade))

# formatação utilizando o printf 
print(f'Olá {nome} você tem {idade}')


#1) "Python é muito legal"
frase2 = "Python é muito legal."
print('Palavra 1', frase2[0:6])
print('Palavra 2', frase2[7:8])
print('Palavra 3', frase2[9:14])
print('Palavra 4', frase2[15:])

#2) Tamanho da frase e das palavras: 

print('O tamanho da frase é: ' , len(frase2))
print('Palavra 1', len(frase2[0:6]))
print('Palavra 2', len(frase2[7:8]))
print('Palavra 3', len(frase2[9:14]))
print('Palavra 4', len(frase2[15:]))

# 3) split ->:
print(frase2.split)



