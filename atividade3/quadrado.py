class Quadrado:
    def __init__(self, tamanhoLado):
        self.tamanhoLado = tamanhoLado
    
    def alterarLado(self, novoTamanho):

        self.tamanhoLado = novoTamanho
    
    def resultLado(self):
        return self.tamanhoLado
    
    def areaQuadrado(self):
        return self.tamanhoLado ** 2
quadrado1 = Quadrado(5)
print(quadrado1.resultLado())
quadrado1.alterarLado(20)
print(quadrado1.resultLado())
print(f'A area do quadrado é de: {quadrado1.areaQuadrado()}')