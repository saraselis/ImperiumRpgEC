# pysimplegui

import PySimpleGUI as sg 

class TelaPython:
	def __init__(self):
		# look
		sg.change_look_and_feel('Purple')


		# layout
		layout = [
			[sg.Image(r'/home/stefanini/Área de Trabalho/download.png'),],
			[sg.Text('Nome', size=(5,0)), sg.Input(size=(50,0), key='nome')],
			[sg.Text('Idade', size=(5,0)), sg.Input(size=(50,0), key='idade')],
			[sg.Text('Quais contatos você possue?')],
			[sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'),
				sg.Checkbox('Telegram', key='telegram')],

			[sg.Text('Aceita cartão', font='Courier 12', text_color='blue', background_color='gray')],
			[sg.Radio('Sim', 'cartoes', key='aceita_cartao'), sg.Radio('Nao', 'cartoes', key='nao_aceita_cartao')],

			[sg.Slider(range=(0,255), default_value=0, orientation='h', size=(15, 20), key='slider_vel')],

			[sg.Button('Enviar dados')],

			[sg.Output(size=(30,20))]
			
		]	
		# UpdateAnimation(source, time_between_frames=0)


		# Janela
		self.janela = sg.Window("Dados do usuário").layout(layout)

		# Extrair os dados da tela
		

	def iniciar(self):
		while True:
			self.button, self.values = self.janela.Read()
			move_figure(teste,
    					x_direction,
    						y_direction)

			nome = self.values['nome']		
			idade = self.values['idade']
			acc_gmail = self.values['gmail']
			acc_outlo = self.values['outlook']
			acc_teleg = self.values['telegram']
			aceita_cartao = self.values['aceita_cartao']
			nao_aceita_cartao = self.values['nao_aceita_cartao']
			velocidade_script = self.values['slider_vel']


			print(f'nome: {nome}')
			print(f'idade: {idade}')
			print(f'acc_gmail: {acc_gmail}')
			print(f'acc_outlo: {acc_outlo}')
			print(f'acc_teleg: {acc_teleg}')
			print(f'aceita_cartao: {aceita_cartao}')
			print(f'nao_aceita_cartao: {nao_aceita_cartao}')
			print(f'velocidade_script: {velocidade_script}')
			print('')


if __name__ == '__main__':
	tela = TelaPython()
	tela.iniciar()

# TypeError: 'NoneType' object is not subscriptable