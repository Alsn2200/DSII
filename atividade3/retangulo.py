class Retangulo:
    def __init__(self, comprimento, largura) -> None:
        self.comprimento = comprimento
        self.largura = largura
    def alterarComprimentoLargura(self, nComprimento, nLargura):
        self.comprimento = nComprimento
        self.largura = nLargura
    def resultRetangulo(self):
        return self.comprimento, self.largura
    def perimetroRetangulo(self):
        return (self.comprimento + self.largura) * 2
Retangulo1 = Retangulo(10, 5)
print(Retangulo1.resultRetangulo())
Retangulo1.alterarComprimentoLargura(20, 40)
print(Retangulo1.resultRetangulo())
print(f'O perimetro do retangulo é de : {Retangulo1.perimetroRetangulo()}')