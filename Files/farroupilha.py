from abc import abstractmethod
from collections import OrderedDict
import PySimpleGUI as sg
from pilha import Stack
from personagem import Principal
from personagem import GritoEx
from personagem import PocaoMixin
from personagem import Personagem
from tela_ataque_farroupilha import TelaAtaqueFarroupilha

class Farroupilha(Personagem, Stack, TelaAtaqueFarroupilha):
    def __init__(self, nome:str, tipo:int, distancia_ataque:int, resistencia:int,
                  pontos_vida:float, pontos_mana:float, pontos_ataque:int, diplomacia:int,
                  cavaleiro:bool, mateador:float, guapo:int):
        super().__init__(nome, tipo, distancia_ataque, resistencia, pontos_vida, pontos_mana,
                         pontos_ataque)
        self._diplomacia = diplomacia
        self._cavaleiro = cavaleiro
        self._mateador = mateador
        self._guapo = guapo
        self._fila = Stack()

    @property
    def diplomacia(self) -> int:
        return self._diplomacia

    @diplomacia.setter
    def diplomacia(self, nova_diplomacia:int):
        self._diplomacia = diplomacia

    @property
    def cavaleiro(self) -> bool:
        return self._cavaleiro

    @cavaleiro.setter
    def cavaleiro(self, novo_cavaleiro:bool):
        self._cavaleiro = novo_cavaleiro

    @property
    def mateador(self) -> float:
        return self._mateador

    @mateador.setter
    def mateador(self, novo_mateador:float):
        self._novo_mateador = novo_mateador

    @property
    def guapo(self) -> int:
        return self._guapo

    @guapo.setter
    def guapo(self, novo_guapo:int):
        self._guapo = novo_guapo

    @Personagem._checa_vida
    @Personagem._checa_mana
    def pranchando_adaga(self, inimigo) -> str:
        '''
            Farroupilha saca a adaga da sua bota para desenhar o fio em seus
            adversários.
        '''

        ataque = (self._pontos_ataque + self._guapo)

        if self._cavaleiro == True:
            ataque = ataque * 0.5

        print(f'Seu ataque agora é {ataque}!')

        inimigo._pontos_vida = inimigo._pontos_vida - ataque
        print(f'O inimigo {inimigo._nome.title()} está com {inimigo._pontos_vida} pontos de vida!')

        self._show_ataque('pranchando_adaga')

        if inimigo._pontos_vida.__pos__() < 0:
            self._fila.push(inimigo._nome.title())
            print("Chuta só pra ter certeza que morreu")
        else:
            print("Da proxima nao me escapa")
        return f'Guarda a adaga'

    @Personagem._checa_mana
    def mateando(self) -> str:
        '''
        Farroupilha faz uma fogueira, senta e vai tomar um bom mate para curar
        suas dores.
        '''

        print('Porque tradição sempre rima com chimarrão')

        regeneracao = 20 + (0.30*self._mateador)

        self._pontos_vida = self._pontos_vida + regeneracao

        self._show_ataque('mateando')

        return f'A nova vida de {self._nome.title()} é {self._pontos_vida}'

    @Personagem._checa_vida
    @Personagem._checa_mana
    def pala(self, inimigo) -> str:
        '''
        Gaúcho se esconde na sua pala e finge que nada está acontecendo.
        '''
        defesa = 0
        print(f'A defesa de {self._nome.title()} é {defesa}')

        inimigo._pontos_ataque = inimigo._pontos_ataque - defesa

        print(f'O ataque do inimigo {inimigo._nome.title()} diminuiu, agora é {inimigo._pontos_ataque}')

        self._show_ataque('pala')

        if inimigo._pontos_ataque.__pos__() <= 0:
            self._fila.push(inimigo._nome.title())
            print("Esse inimigo não tem mais forças para lutar!")

        else:
            self._pontos_vida = self._pontos_vida - inimigo._pontos_ataque
            print(f"A vida de {self._nome.title()} é {self._pontos_vida}")

            if self._pontos_vida.__pos__() <= 0:
                print("Voce desfaleceu")
            else:
                print("Essa pala te salvou vivente")

        return f'Ningém tem paz nessa casa'

    @Personagem._checa_vida
    @Personagem._checa_mana
    def desenhar_a_desgraca(self, inimigo) -> str:
        '''
        Farroupilha desenha a desgraça no corpo dos seus inimigos
        '''

        ataque = self._pontos_ataque + self._guapo + (0.5 * self._pontos_ataque)
        print(f'Seu ataque agora é {ataque}!')

        inimigo._pontos_vida = inimigo._pontos_vida - ataque
        print(f'A vida de {inimigo._nome.title()} é {inimigo._pontos_vida}')

        self._show_ataque('desenhar_a_desgraca')

        if inimigo._pontos_vida.__pos__() <= 0:
            print("Esse inimigo não tem mais vida para lutar!")
            self._fila.push(inimigo._nome.title())

        else:
            print("Na proxima ele não escapa!")

        return 'Chega de chutar os cuscos morto'

    @Personagem._checa_mana
    def tertulia(self) -> str:
        '''
        Farroupilha convence seu inimigo a se
            aprochegar para uma boa tertúlia. O inimigo desiste de atacar.
        '''

        self._show_ataque('tertulia')

        if self._diplomacia > 50 and self._guapo > 0:
            print("Chega de treta, vamos matear")

        else:
            print("Se lascamo, vamo degladiar")

    @Personagem._checa_vida
    @Personagem._checa_mana
    def gritos_de_liberdade(self, inimigo) -> str:
        '''
        Gaúcho perde a noção de seus ideais de humanidade e parte para cima de
            seus inimigos, é vida ou morte.
        '''
        ataque = self._pontos_ataque * self._guapo

        if self._cavaleiro is True:
            ataque = ataque + (0.9 * self._pontos_ataque)

        print(f'Seu ataque agora é {ataque}!')

        inimigo._pontos_vida = inimigo._pontos_vida - ataque
        print(f'A vida de {inimigo._nome.title()} é {inimigo._pontos_vida}')

        self._show_ataque('gritos_de_liberdade')

        if inimigo._pontos_vida.__pos__() <= 0:
            print(inimigo._nome.title())
            self._fila.push(inimigo._nome.title())
            print("Esse inimigo não tem mais vida para lutar!")

        else:
            print("Na proxima ele não escapa!")

        return 'Vento, cavalo, peão...'

    def grito_de_guerra(self) -> str:
        return f"{self._nome.title()} diz: BAhh to sem criativadE"


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

    def __str_(self):
        return f'Um gaúcho foi instanciado: {self._nome}'
