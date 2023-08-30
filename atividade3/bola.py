class Bola:
    def __init__(self, cor, circunferenciaEmCm,material):
        self.cor = cor 
        self.circunferenciaEmCm = circunferenciaEmCm
        self.material = material
    def trocarCor(self, novaCor):
        self.cor = novaCor
    def mostrarCor(self):
        return self.cor
itemBola = Bola('Verde', 70 , 'plastico')
print(itemBola.mostrarCor())
itemBola.trocarCor('amarela')
print(itemBola.mostrarCor())