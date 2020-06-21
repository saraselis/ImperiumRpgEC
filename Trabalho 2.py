import PySimpleGUI as sg

class TelaAtaquePaje:
    def __init__(self, ataque):
        sg.change_look_and_feel('Purple')

        panchando_adaga_img = "/home/stefanini/Documentos/IESB/6to/05-poo/ImperiumRPG/imperiumRpg/Imagens/timo-werner-germany-world-cup_lmv4q43vvn2c1mxz4748tv7h8.png"
        fantasia_img = "/home/stefanini/Documentos/IESB/6to/05-poo/ImperiumRPG/imperiumRpg/Imagens/timo-werner-germany-world-cup_lmv4q43vvn2c1mxz4748tv7h8.png"
        mira_img = "/home/stefanini/Documentos/IESB/6to/05-poo/ImperiumRPG/imperiumRpg/Imagens/90553736_2769081596521130_6112948483344302080_o.png"
        gritos_img = "/home/stefanini/Documentos/IESB/6to/05-poo/ImperiumRPG/imperiumRpg/Imagens/Novo Projeto.png"
        desenhar_img = "/home/stefanini/Documentos/IESB/6to/05-poo/ImperiumRPG/imperiumRpg/Imagens/5c6eada5a1c015297681b5f8.png"
        tertulia_img = "/home/stefanini/Documentos/IESB/6to/05-poo/ImperiumRPG/imperiumRpg/Imagens/download.png"
        gritos_lib_img = "/home/stefanini/Documentos/IESB/6to/05-poo/ImperiumRPG/imperiumRpg/Imagens/5c6eada5a1c015297681b5f8.png"
        morte_img = "/home/stefanini/Documentos/IESB/6to/05-poo/ImperiumRPG/imperiumRpg/Imagens/Novo Projeto.png"
        pocao_img = "/home/stefanini/Documentos/IESB/6to/05-poo/ImperiumRPG/imperiumRpg/Imagens/download.png"
        
        imagens_gui = {
            "ataque_fisico": panchando_adaga_img,
            "fantasia": fantasia_img,
            "mira": mira_img,
            "grito_de_guerra": gritos_img,
            "desenhar_a_desgraca": desenhar_img,
            "tertulia": tertulia_img, 
            "gritos_de_liberdade": gritos_lib_img,
            "morte": morte_img,
            "pocao_ok": pocao_img
        }
        
        for key in imagens_gui:
            if ataque == key:
                ataque = imagens_gui[key]
                break
        
        layout = [
            [sg.Image(ataque),],
            [sg.Text('Fulano ataca Ciclano', font='Courier 12', text_color='green', background_color='black')],
            [sg.Text('sara')]
        ]
        
        self.janela = sg.Window("Dados do usuário").layout(layout)
        
    def iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            break
        self.janela.close()

tela = TelaAtaquePaje('fantasia')
tela.iniciar()


from abc import abstractmethod

class Principal:
    
    @abstractmethod
    def distancia_ataque(self):
        pass
    
    def resistencia(self):
        pass

class Personagem(Principal):
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
        
    
    def grito_de_guerra(self): 
        tela = TelaAtaquePaje('grito_de_guerra')
        tela.iniciar()
    
    def __str__(self):
        return "Personagem criado"
    
    def __del__(self):
        print(f'{self._nome.title()} bateu as bota')


class Paje(Personagem, TelaAtaquePaje):
    def __init__(self, nome:str, tipo:int, distancia_ataque:int, resistencia:int,
                  pontos_vida:float, pontos_mana:float, pontos_ataque:int, sabedoria:int,
                  forca:int, magia:int):
        super().__init__(nome, tipo, distancia_ataque, resistencia, pontos_vida, pontos_mana,
                         pontos_ataque)
        self._sabedoria = sabedoria
        self._forca = forca
        self._magia = magia
    
    @property
    def sabedoria(self) -> int:
        return self._sabedoria
    
    @sabedoria.setter
    def sabedoria(self, nova_sabedoria:int):
        self._sabedoria = sabedoria
        
    @property
    def forca(self) -> int:
        return self._forca
    
    @forca.setter
    def forca(self, novo_forca:int):
        self._forca = novo_forca
        
    @property
    def magia(self) -> int:
        return self._magia
    
    @magia.setter
    def magia(self, novo_magia:int):
        self._novo_magia = novo_magia
        
        
    def ataque_fisico(self, inimigo):
        '''
            Paje saca a adaga da sua bota para desenhar o fio em seus
            adversários.
        '''
        
        ataque = (self._pontos_ataque + (50*self._magia/100) + (50*self._forca/100))
        
        if self._forca == True:
            ataque = ataque * 0.5
            
        print(f'Seu ataque agora é {ataque}!')
        
        inimigo._pontos_vida = inimigo._pontos_vida - ataque
        print(f'O inimigo {inimigo._nome.title()} está com {inimigo._pontos_vida} pontos de vida!')
        
        tela = TelaAtaquePaje('ataque_fisico')
        tela.iniciar()
        
        if inimigo._pontos_vida.__pos__() < 0:
            print("Chuta só pra ter certeza que morreu")
        else:
            print("Da proxima nao me escapa")
        return f'Parar de atacar'
    
    
    def fantasia(self):
        '''
        Paje faz uma fogueira, senta e vai tomar um bom mate para curar
        suas dores.
        '''
        
        print('Porque tradição sempre rima com chimarrão')
        
        self._pontos_vida =  (10*self._sabedoria/100) + 40 + self._magia
        
        tela = TelaAtaquePaje('fantasia')
        tela.iniciar()
        
        return f'A nova vida de {self._nome.title()} é {self._pontos_vida}'
    

    def mira(self, inimigo):
        '''
        Gaúcho se esconde na sua mira e finge que nada está acontecendo.
        '''
        pontos_vida = (10*self._sabedoria/100) + 80
        
        print(f'O ataque do inimigo {inimigo._nome.title()} diminuiu, agora é {pontos_vida}')
        
        tela = TelaAtaquePaje('mira')
        tela.iniciar()
        
        if pontos_vida.__pos__() <= 0:
            print("Esse inimigo não tem mais forças para lutar!")
        
        else:
            print(f"A vida de {self._nome.title()} é {self._pontos_vida}")
            
            if self._pontos_vida.__pos__() <= 0:
                print("Voce desfaleceu")
            else:
                print("Essa mira te salvou vivente")
        
        return f'Ningém tem paz nessa casa'


    
        
        
    def __str__(self):
        return f'Um gauchao foi iniciado, nome: {self._nome.title()}'