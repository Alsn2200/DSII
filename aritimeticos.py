# Questão 1

cotacao = 3.25
valor  = 65.00
result = valor / cotacao
print("O valor de R$", valor, " em dólar é $", result)

# Questão 2

celular = 299.99
chaleira = 23.87
gnomo = 66.66 
adesivos = 1.42 * 6
frete = 12.34

#a)
valorDolar = celular + chaleira + gnomo + adesivos + frete
print("A soma dos itens em dolár é de : $ %.2f" % valorDolar)

#b) 
valorReal = valorDolar * cotacao
iof =  6.38 /100
taxaIof = valorReal * iof
valorRealTotal = valorReal + taxaIof
# print(iof)
print ("O valor total dos produtos em R$ é de : %.2f"% valorReal)
print("O valor em Reais dos Produtos + taxa IOF é de : R$ %.2f" % valorRealTotal)
print("O valor da taxa IOF cobrado sobre os produtos foi de : R$ %.2f"% taxaIof)






