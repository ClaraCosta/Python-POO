class Aluno:
    def __init__(self, matricula, nome, provas, notaTrabalho):
        self.matricula = matricula
        self.nome = nome
        self.provas = provas
        self.notaTrabalho = notaTrabalho

    @property
    def provas(self):
        return self.__provas

    @provas.setter
    def provas(self, provas):
        assert type(provas) == list, 'Provas deve ser do tipo list'
        assert len(provas) == 2, 'Devem existir duas notas de provas'
        self.__provas = provas

    @property
    def notaTrabalho(self):
        return self.__notaTrabalho

    @notaTrabalho.setter
    def notaTrabalho(self, notaTrabalho):
        assert type(notaTrabalho) == int or type(notaTrabalho) == float, 'Nota do trabalho trabalho deve ser numérica.'
        self.__notaTrabalho = notaTrabalho

    def calcularMedia(self):
        return (self.provas[0] + self.provas[1] + self.notaTrabalho) / 3

    def notaParaFinal(self):
        return 10 - self.calcularMedia()

try:
    a = Aluno(201819,'Clara',[10,7],10)
    a.calcularMedia()
    a.notaParaFinal()

    print(f'Nome: {a.nome} \nNota 1: {a.provas[0]}\nNota 2: {a.provas[1]}\nMédia: {a.calcularMedia()}')

except AssertionError as a:
    print(a)

