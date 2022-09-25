from re import T
import tabnanny


class Televisao:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

class controleRemoto:
    def __init__(self, televisao):
        self.televisao = televisao

    def aumentarVolume(self):
        assert self.televisao.volume <= 10, f'O volume já está no máximo, não é possível aumentar mais'
        self.televisao.volume +=1
        print('Volume aumentou 1')

    def diminuirVolume(self):
        assert self.televisao.volume >= 0, f'O volume já está no mínimo, não é possível diminuir mais'
        self.televisao.volume -=1
        print('Volume diminuiu 1')

    def consultarVolume(self):
        print(self.televisao.volume)

    def trocarCanal(self, numero):
        assert self.televisao.canal >= 1, f'Não existem canais anteriores a este'
        self.televisao.canal = numero

    def consultarCanal(self):
        print(self.televisao.canal)


try:
    t = Televisao(7, 4)
    c = controleRemoto(t)
    print(f'Valores inicais: \nCanal: {t.canal} \nVolume: {t.volume}')
    c.aumentarVolume()
    c.aumentarVolume()
    c.aumentarVolume()
    c.aumentarVolume()
    print("O volume da televisão é:", t.volume)
    c.diminuirVolume()
    print("O volume da televisão é:", t.volume)
    c.trocarCanal(40)
    print(f'O canal atual é: {t.canal}')
    


except AssertionError as e:
    print(e)