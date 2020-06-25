import PySimpleGUI as sg
class TelaAtaqueCoronel:
    def __init__(self, ataque):
        sg.change_look_and_feel('Purple')

        toma_bala_img = ""
        hj_nao_cabra_img = ""
        passa_merthiolate_img = ""
        gritos_img = ""
        maculele_img = ""
        pipoco_dos_tiro_img = ""
        morte_img = ""
        pocao_img = ""

        imagens_gui = {
            "toma_bala": toma_bala_img,
            "hj_nao_cabra": hj_nao_cabra_img,
            "passa_merthiolate": passa_merthiolate_img,
            "grito_de_guerra": gritos_img,
            "maculele": maculele_img,
            "pipoco_dos_tiro": pipoco_dos_tiro_img,
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
