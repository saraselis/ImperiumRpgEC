from collections import OrderedDict
import PySimpleGUI as sg

class TelaAtaqueCangaceiro:
    def __init__(self, ataque):
        sg.change_look_and_feel('Purple')

        morre_infiliz_img = ""
        se_aquiete_homi_img = ""
        cristo_jesus_me_tira_dessa_img = ""
        quero_briga_de_foice_img = ""
        gaita_curandeira_img = ""

        imagens_gui = {}
        imagens_gui = OrderedDict(imagens_gui)

        imagens_gui = {
            "morre_infiliz": morre_infiliz_img,
            "se_aquiete_homi": se_aquiete_homi_img,
            "cristo_jesus_me_tira_dessa": cristo_jesus_me_tira_dessa_img,
            "quero_briga_de_foice": quero_briga_de_foice_img,
            "gaita_curandeira": gaita_curandeira_img,
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
