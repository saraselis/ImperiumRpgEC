from abc import abstractmethod
import personagem
import tela_ataque_coronel

class Coronel(Personagem):
    def __init__(self, nome: str, tipo: int, distancia_ataque: int, pontos_vida: int, pontos_mana: int, pontos_ataque: int, mandonismo: int, diplomacia: int, municao: int, poder_aquisitivo: int):
        super().__init__(nome, tipo, distancia_ataque, pontos_vida, pontos_mana, pontos_ataque)
        self._mandonismo = mandonismo
        self._diplomacia = diplomacia
        self._municao = municao
        self._poder_arquivo = poder_aquisitivo

    def toma_bala(self, municao: int, pontos_ataque: int, poder_aquisitivo: int):
        self._poder_aquisitivo += 20
        ataque = self._pontos_ataque * self._mandonismo
        municao -= 1
        return ataque

    def hj_nao_cabra(self, diplomacia: int, municao: int, ataque_inimigo: int):
        ataque_inimigo = ataque_inimigo - (0.2*diplomacia)
        municao += 2
        return ataque_inimigo

    def passa_merthiolate(self, poder_aquisitivo: int, pontos_vida: int):
        regeneracao = 20 + (0.3 * poder_aquisitivo)
        pontos_vida = pontos_vida + regeneracao
        return pontos_vida

    def maculele(self, pontos_mana: int, mandonismo: int, municao: int):
        ataque = self._pontos_mana * mandonismo
        municao -= 3
        return ataque

    def pipoco_dos_tiro(self, municao: int, mandonismo: int, pontos_ataque: int):
        self._mandonismo += 20
        ataque = pontos_ataque * (0,7*mandonismo)
        municao -= 2
        return ataque
