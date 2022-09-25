class Agenda:
  PESSOAS = []
  
  def __init__(self):
    pass  

  def armazenaPessoa(self, nome, idade, altura):
    p = Agenda(nome, idade, altura)
    Agenda.PESSOAS.append(p)

  def removePessoa(self, nome):
    for pessoa in Agenda.PESSOAS:
      if pessoa.nome == nome:
        Agenda.PESSOAS.remove(pessoa)
        break
  
  def buscaPessoa(self, nome):
    for pessoa in Agenda.PESSOAS:
      if pessoa.nome == nome:
        return True
    return False
  
  def imprimeAgenda(self):
    for pessoa in Agenda.PESSOAS:
      print(pessoa)
    
a = Agenda()
a.armazenaPessoa("Clara", 123, 1.88)
a.armazenaPessoa("Joao", 321, 1.78)
a.armazenaPessoa("Ju", 321, 1.68)
print(a.buscaPessoa("Ju"))
print(a.buscaPessoa("Clara"))
a.removePessoa("clara")
a.imprimeAgenda()
