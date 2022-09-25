import datetime
import math

class Pessoa:
    def __init__(self, nome, dataNascimento, altura):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.altura = altura

    def idade(self):
        hoje = datetime.date.today()
        return math.floor((hoje - self.dataNascimento).days / 365.25)

    def __str__(self):
        return f'Nome: {self.nome} \nData de Nascimento: {self.dataNascimento}\nAltura: {self.altura}'

p = Pessoa("Clara", datetime.date(2003, 6, 9), 1.58)
print(p)
print('Idade: ', p.idade())