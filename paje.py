from abc import abstractmethod
import personagem
import tala_ataque_paje

class Paje(Personagem):
    def __init__(self, nome: str, tipo: int, distancia_ataque: int, pontos_vida: int, pontos_mana: int, pontos_ataque: int, sabedoria: int, forca: int, magia: int):
        super().__init__(nome, tipo, distancia_ataque, pontos_vida, pontos_mana, pontos_ataque)
        self._sabedoria = sabedoria
        self._forca = forca
        self._magia = _magia

    def ataque_fisico(self, forca: int, sabedoria: int):
        pontos_de_ataque = (50*self._magia/100) + (50*self._forca/100)
        return pontos_de_ataque

    def fantasia(self, sabedoria: int, magia: int):
        pontos_vida = (10*self._sabedoria/100) + 40 + self._magia
        return pontos_vida

    def mira(self, sabedoria: int):
        pontos_vida = (10*self._sabedoria/100) + 80
        return pontos_vida