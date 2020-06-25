from abc import abstractmethod
from tela_ataque_farroupilha import TelaAtaqueFarroupilha
from tela_at4que_cangaceiro import TelaAtaqueCangaceiro
from tela_at4que_coronel import TelaAtaqueCoronel
from tela_ataque_paje import TelaAtaquePaje

class Principal:
    @abstractmethod
    def distancia_ataque(self):
        print("entrei na distancia")
        return

    @abstractmethod
    def resistencia(self):
        return

class GritoEx(NotImplementedError):
    def __init__(self):
        super().__init__('Grito de guerra é algo muito pessoal... \n Como queres generalizar?')


class PocaoMixin:
    '''
        Classe Mixin que adiciona a possibilidade
            de ganho de vida ou mana.
    '''
    def tomar_chimarrao(self, potion:str, buff=10):
        '''
            Método de regeneracao do Gaúcho
        '''
        self.logica(potion, buff)
        return 'O gaúcho se recupera com um bom mate'

    def rape(self, potion:str, buff=15):
        '''
            Método de regeneracao do Pajé
        '''
        self.logica(potion, buff)
        return 'Tupã revitaliza o Pajé'

    def cachaca(self, potion:str, buff=5):
        '''
            Método de regeneracao do Cangaceiro
        '''
        self.logica(potion, buff)
        return 'Nada como uma cachaça para recuperar um nordestino'

    def cerveja(self, potion:str, buff=10):
        '''
            Método de regeneracao do Coronel
        '''
        self.logica(potion, buff)
        return 'Uma gelada recuperadora'

    def logica(self, potion:str, buff=10):
        '''
            Implementa a lógica de decisão do que será recuperado
        '''
        if potion == 'vida' and self._pontos_vida > 0:
            self._pontos_vida = self._pontos_vida + buff

        elif potion == 'mana' and self._pontos_mana  > 0:
            self._pontos_mana = self._pontos_mana + buff

        else:
            print('Vc fez uma escolha errada de poção, acabou de desperdiçá-la')

class Personagem(Principal, PocaoMixin):
    def __init__(self, nome:str, tipo:int, distancia_ataque:int, resistencia:int,
                  pontos_vida:float, pontos_mana:float, pontos_ataque:int):
        self._nome = nome
        self._tipo = tipo
        self._distancia_ataque = distancia_ataque
        self._resistencia = resistencia
        self._pontos_vida = pontos_vida
        self._pontos_mana = pontos_mana
        self._pontos_ataque = pontos_ataque

    '''getters e setters'''
    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, novo_nome:str):
        self._nome = novo_nome

    @property
    def tipo(self) -> int:
        return self._tipo

    @tipo.setter
    def tipo(self, novo_tipo:int):
        self._tipo = novo_tipo

    @property
    def distancia_ataque(self) -> int:
        return self._distancia_ataque

    @distancia_ataque.setter
    def distancia_ataque(self, novo_ataque: int):
        self._distancia_ataque = novo_ataque

    @property
    def resistencia(self) -> int:
        return self._resistencia

    @resistencia.setter
    def resistencia(self, nova_resistencia:int):
        self._resistencia = nova_resistencia

    @property
    def pontos_vida(self) -> float:
        return self._pontos_vida

    @pontos_vida.setter
    def pontos_vida(self, novo_pts_vida:float):
        self._pontos_vida = novo_pts_vida

    @property
    def pontos_mana(self) -> float:
        return self._pontos_mana

    @pontos_mana.setter
    def pontos_mana(self, novo_pts_mana: float):
        self._pontos_mana = novo_pts_mana

    @property
    def pontos_ataque(self) -> int:
        return self._pontos_ataque

    @pontos_ataque.setter
    def pontos_ataque(self, novo_pts_ataque:int):
        self._pontos_ataque = novo_pts_ataque

    def grito_de_guerra(self):
        raise GritoEx

    def _checa_mana(foo):
        '''
            Decorator que visa verificar se o personagem possui mana o suficiente para realizar
                suas ações
        '''
        def verifica(self, *inimigo) :
            if self._pontos_mana <= 10:
                return print(f"{self._nome.title()}  não tem mana o suficiente para executar esta ação!")
            else:
                foo(self, *inimigo)
        return verifica

    def _checa_vida(foo):
        '''
            Decorator que verifica se o personagem tem vida o suficiente
        '''
        def verifica(self, *inimigo) :
            if inimigo[0]._pontos_vida <= 10:
                return print(f"{inimigo[0]._nome.title()} não tem VIDA o suficiente para executar esta ação!")
            else:
                foo(self, *inimigo)
        return verifica

    @staticmethod
    def _show_ataque(tipo_ataque:str):
        '''
            Mostra imagem de ataque do personagem
        '''
        tela = TelaAtaqueFarroupilha(tipo_ataque)
        tela.iniciar()

    def __del__(self):
        return f'{self._nome.title()} bateu as bota'

    def __repr__(self):
        return f'{self._nome.title()}'
