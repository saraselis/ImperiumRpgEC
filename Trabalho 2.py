class Paje:   
    def __init__(self, sabedoria: int, forca: int, magia: int):
        self._sabedoria = sabedoria
        self._forca = forca
        self._magia = magia
        
    def __str__(self) -> str:
        return "O paje foi instanciado!"
        
    @property
    def sabedoria(self) -> int:
        return self._sabedoria

    @sabedoria.setter
    def sabedoria(self, value: int):
        self._sabedoria = value

    @property
    def forca(self) -> int:
        return self._forca

    @forca.setter
    def forca(self, value: int):
        self._forca = value
    
    @property
    def magia(self) -> int:
        return self._magia

    @magia.setter
    def magia(self, value: int):
        self._magia = value

    def _ataque_fisico(foo):
        def mostra(self) :
            foo(self)
        return mostra
        
    @_ataque_fisico
    def ataque_fisico(self):
        pontos_de_ataque = (50*self._magia/100) + (50*self._forca/100)
        return pontos_de_ataque

    def _fantasia(foo):
        def mostra(self) :
            foo(self)
        return mostra
        
    @_fantasia
    def fantasia(self):
        pontos_vida = (10*self._sabedoria/100) + 40 + self._magia
        return pontos_vida

    def _mira(foo):
        def mostra(self) :
            foo(self)
        return mostra
        
    @_mira
    def mira(self):
        pontos_vida = (10*self._sabedoria/100) + 80
        return pontos_vida


page = Paje(2000, 1000, 5000)
print(page.sabedoria)
print(page.forca)
print(page.magia)
page.ataque_fisico()
page.fantasia()
page.mira()
