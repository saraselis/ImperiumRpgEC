from collections import OrderedDict
import PySimpleGUI as sg

class TelaAtaqueFarroupilha:
    '''
        Essa classe tem a função de inicializar o PysimpleGUI e apresentar as imagens de ataque
            dos personagems do RPG. \n
    '''
    def __init__(self, ataque):
        sg.change_look_and_feel('Purple')

        panchando_adaga_img = "/home/stefanini/Documentos/IESB/6to/05-poo/ImperiumRPG/imperiumRpg/Imagens/farroupilha/pranchando_ataga.png"
        mateando_img = "/home/stefanini/Documentos/IESB/6to/05-poo/ImperiumRPG/imperiumRpg/Imagens/farroupilha/mateando.png"
        pala_img = "/home/stefanini/Documentos/IESB/6to/05-poo/ImperiumRPG/imperiumRpg/Imagens/farroupilha/pala.png"
        desenhar_img = "/home/stefanini/Documentos/IESB/6to/05-poo/ImperiumRPG/imperiumRpg/Imagens/farroupilha/desenhar_desgraca.png"
        tertulia_img = "/home/stefanini/Documentos/IESB/6to/05-poo/ImperiumRPG/imperiumRpg/Imagens/farroupilha/tertulia.png"
        gritos_lib_img = "/home/stefanini/Documentos/IESB/6to/05-poo/ImperiumRPG/imperiumRpg/Imagens/farroupilha/gritos_liberdade.png"

        imagens_gui = {}
        

        imagens_gui = {
            "pranchando_adaga": panchando_adaga_img,
            "mateando": mateando_img,
            "pala": pala_img,
            "desenhar_a_desgraca": desenhar_img,
            "tertulia": tertulia_img,
            "gritos_de_liberdade": gritos_lib_img,
        }

        imagens_gui = OrderedDict(imagens_gui)

        for key in imagens_gui:
            if ataque == key:
                ataque = imagens_gui[key]
                break

        layout = [
            [sg.Image(ataque),]
        ]

        self.janela = sg.Window("Dados do usuário").layout(layout)

    def iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            break
        self.janela.close()
