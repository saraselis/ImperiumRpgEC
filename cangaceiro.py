from abc import abstractmethod
import personagem
import tela_ataque_cangaceiro

class Cangaceiro(Personagem):
    def __init__(self, nome: str, tipo:int, resistencia: int, pontos_vida: float, pontos_mana: float, pontos_ataque: int, devocao: float, temor: float, insanidade: float, rapadura: int):
        super().__init__(nome, tipo, resistencia, pontos_vida, pontos_mana, pontos_ataque)
        self._devocao = devocao
        self._temor = temor
        self._insanidade = insanidade
        self._rapadura = rapadura

    # gets e sets dos atributos

    @get_devocao.setter
    def devocao(self,value):
        if not instance(value, float):
            raise "..."
        self._devocao = value.title()

    @property
    def get_devocao(self):
        return self._devocao

    @get_temor.setter
    def temor(self,value):
        if not instance(value, float):
            raise TypeError("...")
        self._temor = value.title()

    @property
    def get_temor(self):
        return self._temor

    @get_insanidade.setter
    def insanidade(self,value):
        if not instance(value, float):
            raise TypeError("...")
        self._insanidade = value.title()

    @property
    def get_insanidade(self):
        return self._insanidade

    @get_rapadura.setter
    def rapadura(self,value):
        if not instance(value, int):
            raise TypeError("...")
        self._rapadura = value.title()

    @property
    def get_rapadura(self):
        return self._rapadura

    #     @_checa_mana
    @Personagem._checa_vida
    @Personagem._checa_mana


    def morre_infiliz(self, inimigo: Personagem): #ataque
        ataque = (self._pontos_ataque + self.get_temor - (0,3*self.get_resistencia))

        inimigo._pontos_vida = (inimigo._pontos_vida - ataque)
        print(f'O inimigo {inimigo._nome.title()} está com {inimigo._pontos_vida} pontos de vida!')

        self._show_ataque('morre_infiliz')

        if inimigo._pontos_vida.__pos__() < 0:
            print("vá tirar um dedo de prosa com o capeta")
        else:
            print("dessa foice oce não escapa")

        return ''

    @Personagem._checa_vida
    @Personagem._checa_mana

    def se_aquiete_homi(self, inimigo: Personagem): #defesa
        inimigo._pontos_ataque = (inimigo._pontos_ataque - self.get_devocao)
        print(f'O ataque do inimigo {inimigo._nome.title()} diminuiu, agora é {inimigo._pontos_ataque}')

        self._show_ataque('se_aquiete_homi')

        if inimigo._pontos_ataque.__pos__() <= 0:
            print("Esse inimigo não tem mais forças para lutar!")

        else:
            self._pontos_vida = self._pontos_vida - inimigo._pontos_ataque
            print(f"A vida de {self._nome.title()} é {self._pontos_vida}")

            if self._pontos_vida.__pos__() <= 0:
                print("Deus me leva pro céu")
            else:
                print("Este Cangaceiro está na proteção de Jesus")

        return f''

    @Personagem._checa_vida
    @Personagem._checa_mana

    def cristo_jesus_me_tira_dessa(self): #regeneracao
        regeneracao = (0,6 * self.get_rapadura)
        self._pontos_vida = (self._pontos_vida + regeneracao)
        self._show_ataque('cristo_jesus_me_tira_dessa')
        return 'A nova vida de {} é {}'.format(self._nome.title(), self._pontos_vida)

    @Personagem._checa_vida
    @Personagem._checa_mana

    def quero_briga_de_foice(self, inimigo: Personagem): #especial
        ataque = (self._pontos_mana + self.get_insanidade)

        inimigo._pontos_vida = (inimigo._pontos_vida - ataque)
        print(f'O inimigo {inimigo._nome.title()} está com {inimigo._pontos_vida} pontos de vida!')

        self._show_ataque('quero_briga_de_foice')

        if inimigo._pontos_vida.__pos__() < 0:
            print("vá tirar um dedo de prosa com o capeta")
        else:
            print("dessa foice oce não escapa")

        return ''

    @Personagem._checa_vida
    @Personagem._checa_mana

    def gaita_curandeira(self, inimigo: Personagem): #defesa
        inimigo._pontos_ataque = (inimigo._pontos_ataque - (0,3*self.get_devocao))
        print(f'O ataque do inimigo {inimigo._nome.title()} diminuiu, agora é {inimigo._pontos_ataque}')
        self._show_ataque('gaita_curandeira')

        if inimigo._pontos_ataque.__pos__() <= 0:
            print("Esse inimigo não tem mais forças para lutar!")

        else:
            self._pontos_vida = self._pontos_vida - inimigo._pontos_ataque
            print(f"A vida de {self._nome.title()} é {self._pontos_vida}")

            if self._pontos_vida.__pos__() <= 0:
                print("Deus me leva pro céu")
            else:
                print("Este Cangaceiro está na proteção de Jesus")

        return f''

    def __str__(self):
        return 'Um Cangaceiro de nome {} está pronto pra luta'.format(self._nome)
