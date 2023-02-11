import PySimpleGUI as sg
import fpdf
import datetime
import random
import os




# sg.theme('DarkAmber')
# função para gerar recibo da compra
numeros = range(1,100000)
momento = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
codigo_venda= random.choice(numeros)


def gera_recibo(carrinho):
    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=5)
    pdf.cell(200, 10, txt="RECIBO DE COMPRA", ln=1, align="C")
    pdf.cell(200, 10, txt="Momento da compra {}".format(momento), ln=1, align="C")
    pdf.cell(2,1, txt="  ID Venda : {}".format(codigo_venda))
    pdf.cell(200, 10, txt="ITENS COMPRADOS:", ln=1, align="L")
    pdf.cell(0, 0, txt="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", ln=1, align="C")
    


    for item in carrinho:
        pdf.cell(200, 10, txt=f"Produto: {item[0]} | Preço: R${item[1]:.2f} | Quantidade: {item[2]} | Desconto: {item[3]}% | Valor total: R${item[4]:.2f}", ln=1, align="L")
        pdf.cell(200, 10, txt="", ln=1, align="C")
        pdf.cell(200, 10, txt=f"Total da compra: R${sum([item[4] for item in carrinho]):.2f}", ln=1, align="R")
        pdf.output("recibo.pdf")

layout = [
    [sg.Text(size=(20, 1), font=('Helvetica', 20), background_color='GREY21',justification='center', key='-OUTPUT-'),],
    [sg.Text('Código de barras:', font=('Arial', 20),background_color='GREY21',size=(20, 1)), sg.Input(key='codigo',font=('Arial', 20))],
    [sg.Text('Nome do produto:', font=('Arial', 20),background_color='GREY21',size=(20, 1)), sg.Input(key='nome',font=('Arial', 20))],
    [sg.Text('Preço unitário:', font=('Arial', 20),background_color='GREY21',size=(20, 1)), sg.Input(key='preco',font=('Arial', 20))],
    [sg.Text('Quantidade:', font=('Arial', 20),background_color='GREY21',size=(20, 1)), sg.Input(key='quantidade',font=('Arial', 20))],
    [sg.Text('Desconto:', font=('Arial', 20),background_color='GREY21',size=(20, 1)), sg.Input(key='desconto',font=('Arial', 20))],
    [sg.Text('Valor total:', font=('Arial', 20),background_color='GREY21',size=(20, 1)), sg.Text('', size=(20, 1), key='valor',background_color='GREY21',font=('Arial', 20))],
    [sg.Button('Adicionar item',font=('Arial', 20)), sg.Button('Finalizar compra',font=('Arial', 20)), sg.Button('Cancelar',font=('Arial', 20)),sg.Button('CEP',font=('Arial', 20))], 
    [sg.Text('Salvar arquivo como :', font=('Arial', 20),background_color='GREY21',size=(20, 1)), sg.Input(key='Nome do arquivo',font=('Arial', 20))],
    [sg.Image(r'D:\Projetos\workspace Python\MEU SISTEMA DE LOJA\LUXURY JHON CARVALHO transparente.png', background_color='GREY21',size=(500, 500), pad=(100, 10))],
    [sg.Text("Pasta de destino"), sg.FileSaveAs()],
    
]

    
window = sg.Window('Sistema de comércio', layout, size=(1800,800), 
resizable=True, auto_size_text=True, 
default_element_size=(40, 1),
background_color='GREY21')
carrinho = []

# loop principal do sistema
while True:
    event, values = window.read(timeout=100)
    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    window['-OUTPUT-'].update(current_time)
    # verifica se o botão Adicionar item foi clicado
    if event == 'Adicionar item':
        preco = float(values['preco'])
        quantidade = int(values['quantidade'])
        desconto = float(values['desconto'])
        valor = preco * quantidade * (1 - desconto/100)
        window['valor'].update(f"R${valor:.2f}")
        carrinho.append((values['nome'], preco, quantidade, desconto, valor))
        window.FindElement('codigo').Update('')
        window.FindElement('nome').Update('')
        window.FindElement('preco').Update('')
        window.FindElement('quantidade').Update('')
        window.FindElement('desconto').Update('')
 
        # verifica se o botão Finalizar compra foi clicado
    elif event == 'Finalizar compra':
        gera_recibo(carrinho)
        new_file_name = values["Nome do arquivo"] + ".pdf"
        os.rename("recibo.pdf", new_file_name)
        sg.popup('Compra finalizada com sucesso!', 'O recibo da compra foi gerado com sucesso e está disponível .')
        break
    if event == sg.WIN_CLOSED or event == 'Exit':  # Adiciona evento para fechamento da janela ao clicar no X ou em um botão "Exit"
        break
        # verifica se o botão Cancelar foi clicado
    elif event == 'Cancelar':
        break
    

window.close()
