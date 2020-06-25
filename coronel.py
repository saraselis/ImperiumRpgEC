from abc import abstractmethod
import personagem
import tela_ataque_coronel

class Coronel(Personagem):
    def __init__(self, nome: str, tipo: int, distancia_ataque: int, pontos_vida: float, pontos_mana: float, pontos_ataque: int, mandonismo: float, diplomacia: float, municao: int, poder_aquisitivo: float):
        super().__init__(nome, tipo, distancia_ataque, pontos_vida, pontos_mana, pontos_ataque)
        self._mandonismo = mandonismo
        self._diplomacia = diplomacia
        self._municao = municao
        self._poder_arquivo = poder_aquisitivo

    #gets e sets dos atributos

    @get_mandonismo.setter
    def mandonismo(self,value):
        if not instance(value, float):
            raise TypeError("...")
        self._mandonismo = value.title()

    @property
    def get_mandonismo(self):
        return self._mandonismo

    @get_diplomacia.setter
    def diplomacia(self,value):
        if not instance(value, float):
            raise TypeError("...")
        self._diplomacia = value.title()

    @property
    def get_diplomacia(self):
        return self._diplomacia

    @get_municao.setter
    def municao(self,value):
        if not instance(value, int):
            raise TypeError("...")
        self._municao = value.title()

    @property
    def get_municao(self):
        return self._municao

    @get_poder_aquisitivo.setter
    def poder_aquisitivo(self,value):
        if not instance(value, float):
            raise TypeError("...")
        self._poder_arquivo = value.title()

    @property
    def get_poder_aquisitivo(self):
        return self._poder_aquisitivo

    #     @_checa_mana
    @Personagem._checa_vida
    @Personagem._checa_mana


    def toma_bala(self, inimigo: Personagem): #ataque
        ataque = (self._pontos_ataque + self.get_mandonismo + (0,1*self.get_municao))
        self.get_municao -= 10
        inimigo._pontos_vida = (inimigo._pontos_vida - ataque)
        print(f'O inimigo {inimigo._nome.title()} está com {inimigo._pontos_vida} pontos de vida!')

        self._show_ataque('toma_bala')

        if inimigo._pontos_vida.__pos__() < 0:
            print("q o diabo o tenha")
        else:
            print("do imposto de renda vc não escapa")

        return ''

    def hj_nao_cabra(self, inimigo: Personagem): #defesa
        inimigo._pontos_ataque = (inimigo._pontos_ataque - self.get_diplomacia)
        self.get_municao += 5

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

        return f''

    def passa_merthiolate(self): #regeneraçao
        regeneracao = (20 + (0.3 * poder_aquisitivo))
        self._pontos_vida = (self._pontos_vida + regeneracao)
        self._show_ataque('passa_merthiolate')
        return 'A nova vida de {} é {}'.format(self._nome.title(), self._pontos_vida)


    def maculele(self, inimigo: Personagem): #especial
        ataque = (self._pontos_mana + self.get_mandonismo + (0,3*self._get_municao))
        municao -= 30
        inimigo._pontos_vida = (inimigo._pontos_vida - ataque)
        print(f'O inimigo {inimigo._nome.title()} está com {inimigo._pontos_vida} pontos de vida!')

        self._show_ataque('maculele')

        if inimigo._pontos_vida.__pos__() < 0:
            print("q o diabo o tenha")
        else:
            print("do imposto de renda vc não escapa")

        return ''

    def pipoco_dos_tiro(self, inimigo: Personagem):
        ataque = ((0,1*self._get_municao) + (0,7*self._get_mandonismo))
        municao -= 10
        inimigo._pontos_vida = (inimigo._pontos_vida - ataque)
        print(f'O inimigo {inimigo._nome.title()} está com {inimigo._pontos_vida} pontos de vida!')

        self._show_ataque('pipoco_dos_tiro')

        if inimigo._pontos_vida.__pos__() < 0:
            print("q o diabo o tenha")
        else:
            print("do imposto de renda vc não escapa")

        return ''

    def __str__(self):
        return 'Um Coronel de nome {} está pronto pra luta'.format(self._nome)
