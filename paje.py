from abc import abstractmethod
import personagem
import tala_ataque_paje

class Paje(Personagem):
    def __init__(self, nome: str, tipo: int, distancia_ataque: int, pontos_vida: int, pontos_mana: int, pontos_ataque: int, sabedoria: int, forca: int, magia: int):
        super().__init__(nome, tipo, distancia_ataque, pontos_vida, pontos_mana, pontos_ataque)
        self._sabedoria = sabedoria
        self._forca = forca
        self._magia = magia

    @get_sabedoria.setter
    def sabedoria(self,value):
        if not instance(value, int):
            raise TypeError("Erro")
        self._sabedoria = value.title()

    @property
    def get_sabedoria(self):
        return self._sabedoria
    self.get_sabedoria

    @get_forca.setter
    def forca(self,value):
        if not instance(value, int):
            raise TypeError("Erro")
        self._forca = value.title()

    @property
    def get_forca(self):
        return self._forca
    self.get_forca

    @get_magia.setter
    def magia(self,value):
        if not instance(value, int):
            raise TypeError("Erro")
        self._magia = value.title()

    @property
    def get_magia(self):
        return self._magia
    self.get_magia


    def ataque_fisico(self, inimigo)
        pontos_de_ataque = (50*self._magia/100) + (50*self._forca/100)
        self._pontos_ataque = self._pontos_ataque + pontos_de_ataque
        self._show_ataque('ataque fisico')
        return f'Agora o ataque de {self._nome.title()} é {self._pontos_ataque}'


    def fantasia(self, inimigo)
        fantasia = (0.1*self._sabedoria) + 40 + self._magia
        self._pontos_vida = self._pontos_vida + fantasia
        self._show_ataque('fantasia')    
        return f'A fantasia de {self._nome.title()}, agora é {self._pontos_vida}'

    def mira(self, inimigo):
        mira = (0.1*self._sabedoria) + 80
        self._pontos_vida = self._pontos_vida + mira
        self._show_ataque('mira')    
        return f'A mira de {self._nome.title()}, agora é {self._pontos_vida}'

    def grito_de_guerra(self): 
        return f"{self._nome.title()} diz: UH! UH! UH! UH!"
    
    def  __str__ ( próprio ):
        return  'Um nome de usuário {} está pronto para luta'.formato(próprio._nome )





