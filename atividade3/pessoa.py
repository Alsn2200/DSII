class Pessoa:
    def __init__(self,nome, idade, peso, altura) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def resultPessoa(self):
        return f'Nome: {self.nome}, idade: {self.idade}, peso: {self.peso} , altura: {self.altura}'
    
    def envelhecer(self):
        return self.idade +1
    
    def engordar(self, novoPeso):
        self.peso = novoPeso
    def emagrecer (self, novoPeso):
        self.peso = novoPeso
    def crescer(self):
        if self.idade >= 21:
            self.altura + 0.5
        return self.altura
    
Pessoa1 = Pessoa('Alisson', 19, 71, 1.80)
print(Pessoa1.resultPessoa())
print(Pessoa1.envelhecer())
print(Pessoa1.resultPessoa())
