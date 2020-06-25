from abc import abstractmethod
from collections import OrderedDict
import PySimpleGUI as sg
from pilha import Stack
from personagem import Principal
from personagem import GritoEx
from personagem import PocaoMixin
from personagem import Personagem
from tela_at4que_cangaceiro import TelaAtaqueCangaceiro
from tela_at4que_coronel import TelaAtaqueCoronel
from tela_ataque_farroupilha import TelaAtaqueFarroupilha
from tela_ataque_paje import TelaAtaquePaje
from farroupilha import Farroupilha
from c4ngaceiro import Cangaceiro
from cor0nel import Coronel
from paje import Paje

def main():

    germano = Farroupilha('Germano', 1, 10, 20, 40, 40.0, 50, 60, True, 70.0, 80)
    print(germano)

    germano.nome, germano.tipo, germano.distancia_ataque, germano.resistencia, germano.pontos_vida
    germano.pontos_mana, germano.pontos_ataque, germano.diplomacia, germano.cavaleiro, germano.mateador, germano.guapo
    germano.grito_de_guerra()
    germano.album_figurinhas()
    germano.buff_tipe()
    germano.pontos_vida
    germano.tomar_chimarrao('vida', 20)
    germano.pontos_vida
    bento = Farroupilha('Bento', 1, 10, 20, 60, 40.0, 50, 60, True, 70.0, 80)
    giuseppe = Farroupilha('Giuseppe', 0, 10, 20, 60, 40.0, 50, 60, True, 70.0, 80)
    garibaldi = Farroupilha('garibaldi', 0, 10, 20, 30.0, 50.0, 50, 60, True, 70.0, 80)
    print(garibaldi)
    garibaldi.grito_de_guerra()
    garibaldi.pranchando_adaga(germano)
    garibaldi.album_figurinhas()
    garibaldi.mateando()
    garibaldi.pala(bento)
    garibaldi.desenhar_a_desgraca(bento)
    garibaldi.tertulia()
    garibaldi.gritos_de_liberdade(giuseppe)
    garibaldi.gritos_de_liberdade(giuseppe)
    garibaldi.album_figurinhas()

if __name__ == '__main__':
    main()
