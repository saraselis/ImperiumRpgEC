from abc import abstractmethod
import personagem
import tela_ataque_cangaceiro

class Cangaceiro(Personagem):
    def __init__(self, nome: str, tipo:int, resistencia: int, pontos_vida: int, pontos_mana: int, pontos_ataque: int, devocao: int, temor: int, insanidade: int, rapadura: int):
        super().__init__(nome, tipo, resistencia, pontos_vida, pontos_mana, pontos_ataque)
        self._devocao = devocao
        self._temor = temor
        self._insanidade = insanidade
        self._rapadura = rapadura

    def morre_infiliz(self, temor: int, resistencia: int):
        ataque = self._pontos_ataque * self._temor - (0,3*self._resistencia)
        return ataque

    def se_aquiete_homi(self, devocao: int, ataque_inimigo: int):
        self._resistencia += 10
        self._ataque_inimigo = self._ataque_inimigo - self._devocao
        return ataque_inimigo

    def cristo_jesus_me_tira_dessa(self, rapadura: int, pontos_vida: int):
        regeneracao = 0,6 * self._rapadura
        return pontos_vida

    def quero_briga_de_foice(self, pontos_mana: int, insanidade: int):
        resistencia -= 15
        ataque = self._pontos_mana * self._insanidade
        return ataque

    def gaita_curandeira(self, devocao: int, ataque_inimigo: int):
        devocao += 10
        self._ataque_inimigo = self._ataque_inimigo - (0,3*self._ataque_inimigo) - (0,2*self._devocao)
        return self._ataque_inimigo

    def __str__(self):
        return 'Um Cangaceiro de nome {} está pronto pra luta'.format(self._nome)
