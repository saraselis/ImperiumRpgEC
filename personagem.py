class Principal:

    @abstractmethod
    def distancia_ataque(self):
        pass

    def resistencia(self):
        pass

class Personagem(Principal):
    def __init__(self, nome:str, tipo:int, distancia_ataque:int, resistencia:int, pontos_vida:float, pontos_mana:float, pontos_ataque:int):
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
    def tipo(self) -> str:
        return self._tipo

    @tipo.setter
    def tipo(self, novo_tipo:str):
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

    '''metodos da classe'''
    def perder_vida(self, loss:int):
        self._pontos_vida = self._pontos_vida - loss
        return f'A vida deste personagem agora é {self._pontos_vida}'

    def aumentar_vida(self): # precisa?
        pass

    def gastar_mana(self):  # precisa?
        pass

    def grito_de_guerra(self):
        pass

    def decepa_inimigo(inimigo):
        inimigo.__del__()
        return 'Amiguinho decepado'

    def __str__(self):
        return "Personagem criado"

    def __del__(self):
        print(f'{self._nome.title()} bateu as bota')
