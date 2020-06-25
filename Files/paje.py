from abc import abstractmethod
from collections import OrderedDict
import PySimpleGUI as sg
from pilha import Stack
from personagem import Principal
from personagem import GritoEx
from personagem import PocaoMixin
from personagem import Personagem
from tela_ataque_paje import TelaAtaquePaje

class Paje(Personagem):
    def __init__(self, nome: str, tipo: int, distancia_ataque: int, pontos_vida: float, pontos_mana: float, pontos_ataque: int, sabedoria: int, forca: int, magia: int):
        super().__init__(nome, tipo, distancia_ataque, pontos_vida, pontos_mana, pontos_ataque)
        self._sabedoria = sabedoria
        self._forca = forca
        self._magia = magia
        self._fila = Stack()

    @property
    def get_sabedoria(self):
        return self._sabedoria

    @get_sabedoria.setter
    def sabedoria(self,value):
        if not instance(value, int):
            raise TypeError("...")
        self._sabedoria = value.title()

    @property
    def get_forca(self):
        return self._forca

    @get_forca.setter
    def forca(self,value):
        if not instance(value, int):
            raise TypeError("...")
        self._forca = value.title()

    @property
    def get_magia(self):
        return self._magia

    @get_magia.setter
    def magia(self,value):
        if not instance(value, int):
            raise TypeError("...")
        self._magia = value.title()


    @Personagem._checa_vida
    @Personagem._checa_mana

    def ataque_fisico(self, inimigo: Personagem): #ataque
        ataque = ((0,5*self.get_magia) + (0,5*self.get_forca))
        inimigo._pontos_vida = (inimigo._pontos_vida - ataque)
        print(f'O inimigo {inimigo._nome.title()} está com {inimigo._pontos_vida} pontos de vida!')

        self._show_ataque('ataque_fisico')

        if inimigo._pontos_vida.__pos__() < 0:
            print("O inimigo foi derrotado")
        else:
            print("Cuidado! O inimigo ainda pode atacar")

        return 'Na proxima ele não escapa!'

    @Personagem._checa_vida
    @Personagem._checa_mana

    def fantasia(self, inimigo: Personagem): #defesa
        fantasia = ((0.1*self.get_sabedoria) + 40 + self.get_magia)
        inimigo._pontos_ataque = (inimigo._pontos_ataque - fantasia)
        print(f'O ataque do inimigo {inimigo._nome.title()} diminuiu, agora é {inimigo._pontos_ataque}')

        self._show_ataque('fantasia')

        if inimigo._pontos_ataque.__pos__() <= 0:
            print("Esse inimigo não tem mais forças para lutar!")

        else:
            self._pontos_vida = self._pontos_vida - inimigo._pontos_ataque
            print(f"A vida de {self._nome.title()} é {self._pontos_vida}")

            if self._pontos_vida.__pos__() <= 0:
                print("Você perdeu toda a sua vida!")
            else:
                print("Ainda há vida!")

        return f'A fantasia te salvou!'

    @Personagem._checa_vida
    @Personagem._checa_mana

    def compensacao(self):#regeneracao
        regeneracao = 10 + (0,3*self.get_sabedoria)
        self._pontos_vida = (self._pontos_vida + regeneracao)
        self._show_ataque('compensacao')
        return 'A nova vida de {} é {}'.format(self._nome.title(), self._pontos_vida)

    @Personagem._checa_vida
    @Personagem._checa_mana

    def mira(self, inimigo: Personagem): #defesa/regeneracao
        mira = ((0.1*self.get_sabedoria) + 80)
        self._pontos_vida = (self._pontos_vida + mira)
        inimigo._pontos_ataque = (inimigo._pontos_ataque - mira)
        print(f'O ataque do inimigo {inimigo._nome.title()} diminuiu, agora é {inimigo._pontos_ataque}')

        self._show_ataque('mira')

        if inimigo._pontos_ataque.__pos__() <= 0:
            print("Esse inimigo não tem mais forças para lutar!")

        else:
            self._pontos_vida = self._pontos_vida - inimigo._pontos_ataque
            print(f"A vida de {self._nome.title()} é {self._pontos_vida}")

            if self._pontos_vida.__pos__() <= 0:
                print("Você perdeu toda a sua vida!")
            else:
                print("Ainda há vida!")

        return f'Não temos um minuto de paz!'

    def grito_de_guerra(self):
        return f"{self._nome.title()} diz: UH! UH! UH! UH!"

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

    def  __str__ (self):
        return  'Um Pajé de nome {} está pronto para luta'.format(self._nome.title())
