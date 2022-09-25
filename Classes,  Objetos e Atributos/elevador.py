class Elevador:
    def __init__(self, capacidade, totalAndares, andarAtual = 0):
        self.andarAtual = 0
        self.totalAndares = 10
        self.capacidade = 8
        self.pessoas = 0

    def entra(self):
        assert self.pessoas <= self.capacidade, 'Capacidade do elevador excedida'
        self.pessoas +=1
        print(f"Entrou mais uma pessoa no elevador. Agora temos: {self.pessoas}")


    def sai(self):
        assert self.pessoas > 0, "Deve existir ao menos uma pessoa no elevador para sair"
        self.pessoas = self.pessoas - 1
        print(f"Saiu uma pessoa, agora temos {self.pessoas} pessoas no elevador")

    def sobe(self):
        assert self.andarAtual < 10, f"O prédio só possui {self.totalAndares} andares, o elevador não pode mais subir"
        self.andarAtual += 1
        print(f"O elevador subiu mais um andar, agora está no andar {self.andarAtual}")

    def desce(self):
        assert self.andarAtual > 0, "O elevador já está no térreo, não pode descer"
        self.andarAtual = self.andarAtual - 1
        print(f"O elevador desceu mais um andar, agora está no andar {self.andarAtual}")

try:
    e = Elevador(10, 5)
    e.entra()
    e.entra()
    e.entra()
    e.entra()
    e.sai()
    e.sai()
    e.entra()
    e.sobe()
    e.sobe()
    e.sobe()
    e.desce()
    e.desce()

except AssertionError as a:
    print(a)



