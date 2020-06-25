from abc import abstractmethod
from collections import OrderedDict
import PySimpleGUI as sg
from pilha import Stack
from personagem import Principal
from personagem import GritoEx
from personagem import PocaoMixin
from personagem import Personagem
from tela_at4que_coronel import TelaAtaqueCoronel

class Coronel(Personagem, Stack, TelaAtaqueCoronel):
    def __init__(self, nome: str, tipo: int, distancia_ataque: int, pontos_vida: float, pontos_mana: float, pontos_ataque: int, mandonismo: float, diplomacia: float, municao: int, poder_aquisitivo: float):
        super().__init__(nome, tipo, distancia_ataque, pontos_vida, pontos_mana, pontos_ataque)
        self._mandonismo = mandonismo
        self._diplomacia = diplomacia
        self._municao = municao
        self._poder_arquivo = poder_aquisitivo
        self._fila = Stack()

    #gets e sets dos atributos

    @property
    def mandonismo(self) -> float:
        return self._mandonismo

    @mandonismo.setter
    def mandonismo(self, nova_mandonismo:float):
        self._mandonismo = mandonismo

    @property
    def diplomacia(self) -> int:
        return self._diplomacia

    @diplomacia.setter
    def diplomacia(self, nova_diplomacia:int):
        self._diplomacia = diplomacia

    @property
    def municao(self) -> int:
        return self._municao

    @municao.setter
    def municao(self, novo_municao:int):
        self._municao = novo_municao

    @property
    def poder_aquisitivo(self) -> float:
        return self._mateador

    @poder_aquisitivo.setter
    def poder_aquisitivo(self, novo_poder_aquisitivo:float):
        self._poder_arquivo = novo_poder_aquisitivo


    #     @_checa_mana
    @Personagem._checa_vida
    @Personagem._checa_mana


    def toma_bala(self, inimigo: Personagem): #ataque
        ataque = (self._pontos_ataque + self._mandonismo + (0,1*self._municao))
        self._municao = self._municao - 10
        inimigo._pontos_vida = (inimigo._pontos_vida - ataque)
        print(f'O inimigo {inimigo._nome.title()} está com {inimigo._pontos_vida} pontos de vida!')

        self._show_ataque('toma_bala')

        if inimigo._pontos_vida.__pos__() < 0:
            print("q o diabo o tenha")
        else:
            print("do imposto de renda vc não escapa")

        return 'guarda o revolver'

    def hj_nao_cabra(self, inimigo: Personagem): #defesa
        inimigo._pontos_ataque = (inimigo._pontos_ataque - self._diplomacia)
        self._municao = self._municao + 5

        print(f'O ataque do inimigo {inimigo._nome.title()} diminuiu, agora é {inimigo._pontos_ataque}')

        self._show_ataque('hj_nao_cabra')

        if inimigo._pontos_ataque.__pos__() <= 0:
            print("Esse inimigo não tem mais forças para lutar!")

        else:
            self._pontos_vida = self._pontos_vida - inimigo._pontos_ataque
            print(f"A vida de {self._nome.title()} é {self._pontos_vida}")

            if self._pontos_vida.__pos__() <= 0:
                print("Falecestes")
            else:
                print("Hj este coronel irá viver")

        return 'eu escolho paz'

    def passa_merthiolate(self): #regeneraçao
        regeneracao = (20 + (0.3 * self._poder_aquisitivo))
        self._pontos_vida = (self._pontos_vida + regeneracao)
        self._show_ataque('passa_merthiolate')
        return 'A nova vida de {} é {}'.format(self._nome.title(), self._pontos_vida)


    def maculele(self, inimigo: Personagem): #especial
        ataque = (self._pontos_mana + self._mandonismo + (0,3*self._municao))
        self._municao = self._municao - 30
        inimigo._pontos_vida = (inimigo._pontos_vida - ataque)
        print(f'O inimigo {inimigo._nome.title()} está com {inimigo._pontos_vida} pontos de vida!')

        self._show_ataque('maculele')

        if inimigo._pontos_vida.__pos__() < 0:
            print("q o diabo o tenha")
        else:
            print("do imposto de renda vc não escapa")

        return 'ahh mas é hj q tu morre'

    def pipoco_dos_tiro(self, inimigo: Personagem): #ataque
        ataque = ((0,1*self._municao) + (0,7*self._mandonismo))
        self._municao = self._municao - 10
        inimigo._pontos_vida = (inimigo._pontos_vida - ataque)
        print(f'O inimigo {inimigo._nome.title()} está com {inimigo._pontos_vida} pontos de vida!')

        self._show_ataque('pipoco_dos_tiro')

        if inimigo._pontos_vida.__pos__() < 0:
            print("q o diabo o tenha")
        else:
            print("do imposto de renda vc não escapa")

        return 'Hj todos irão sofrer perante meu revolver'

    def grito_de_guerra(self) -> str:
        return f"{self._nome.title()} diz: É hj que irei te roubar"


    def buff_tipe(self):
        if self._tipo == 1:
            ataque = super().distancia_ataque
            self._distancia_ataque = ataque + 10
            print("Buff de Ranged")

        elif self._tipo == 0:
            ataque = super()._resistencia
            self._resistencia = ataque + 10
            print("Buff de Melee")
        else:
            pass

    def album_figurinhas(self):
        print(f"Ultimo morto: {self._fila.topo()}")
        print("Lista de mortos:")
        self._fila.show_pilha()


    def __str__(self):
        return 'Um Coronel de nome {} está pronto pra luta'.format(self._nome)
