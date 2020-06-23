import PySimpleGUI as sg
class TelaAtaqueCoronel:
    def __init__(self, ataque):
        sg.change_look_and_feel('Purple')

        toma_bala_img = ""
        fantasia_img = ""
        mira_img = ""

        imagens_gui = {
            "toma_bala": toma_bala_img,
            "fantasia": fantasia_img,
            "mira": mira_img
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
