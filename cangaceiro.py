from abc import abstractmethod
import personagem
import tela_ataque_cangaceiro

class Cangaceiro(Personagem, Stack, TelaAtaqueCangaceiro):
    def __init__(self, nome: str, tipo:int, resistencia: int, pontos_vida: float, pontos_mana: float, pontos_ataque: int, devocao: float, temor: float, insanidade: float, rapadura: int):
        super().__init__(nome, tipo, resistencia, pontos_vida, pontos_mana, pontos_ataque)
        self._devocao = devocao
        self._temor = temor
        self._insanidade = insanidade
        self._rapadura = rapadura
        self._fila = Stack()

    # gets e sets dos atributos

     @property
    def devocao(self) -> float:
        return self._devocao

    @devocao.setter
    def devocao(self, nova_devocao:float):
        self._devocao = nova_devocao

    @property
    def temor(self) -> float:
        return self._temor

    @temor.setter
    def temor(self, novo_temor:float):
        self._temor = novo_temor


    @property
    def insanidade(self) -> float:
        return self._insanidade

    @insanidade.setter
    def insanidade(self, nova_insanidade:float):
        self._insanidade = nova_insanidade

    @property
    def rapadura(self) -> int:
        return self._rapadura

    @rapadura.setter
    def rapadura(self, nova_rapadura:int):
        self._rapadura = nova_rapadura

    #     @_checa_mana
    @Personagem._checa_vida
    @Personagem._checa_mana


    def morre_infiliz(self, inimigo: Personagem): #ataque
        ataque = (self._pontos_ataque + self._temor - (0,3*self._resistencia))

        inimigo._pontos_vida = (inimigo._pontos_vida - ataque)
        print(f'O inimigo {inimigo._nome.title()} está com {inimigo._pontos_vida} pontos de vida!')

        self._show_ataque('morre_infiliz')

        if inimigo._pontos_vida.__pos__() < 0:
            print("vá tirar um dedo de prosa com o capeta")
        else:
            print("dessa foice oce não escapa")

        return 'hj eu estou louco pra dar uns bufete'

    @Personagem._checa_vida
    @Personagem._checa_mana

    def se_aquiete_homi(self, inimigo: Personagem): #defesa
        inimigo._pontos_ataque = (inimigo._pontos_ataque - self._devocao)
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

        return 'Até os homens mais brabos precisam de um descanso'

    @Personagem._checa_vida
    @Personagem._checa_mana

    def cristo_jesus_me_tira_dessa(self): #regeneracao
        regeneracao = (0,6 * self._rapadura)
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

        return 'NINGUEM ESTA LIVRE DO PECADO!!'

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

        return 'É sexta-feira santa. Nada de briga'

    def grito_de_guerra(self) -> str:
        return f"{self._nome.title()} diz: CABRA SAFADO!!"


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
        return 'Um Cangaceiro de nome {} está pronto pra luta'.format(self._nome)
