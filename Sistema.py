import PySimpleGUI as sg
import fpdf
import random
import os
import urllib
import pyodbc
import pywhatkit as kit
from datetime import datetime, timedelta
import time


dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-BPKKSVH\SQLEXPRESS;"
    "Database=Fornecedores_jcstore;"
)

agora = datetime.now()  # Obtém a data e hora atual

conexao = pyodbc.connect(dados_conexao)
print("Conexao bem sucedida !")

cursor = conexao.cursor()
current_time_atual = datetime.now().strftime("%d/%m/%Y")
# FUNÇÃO PARA BUSCAR ESTOQUE ATUAL
def consulta_estoque(codigo):
    cursor.execute(f"SELECT TOP 1 Saldo FROM tbl_Vendas WHERE Cod_produto = '{codigo}' ORDER BY ID_movimentacao DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# FUNÇÃO PARA BUSCAR FORNECEDOR DO ID
def consulta_fornecedor(codigo):
    cursor.execute(f"SELECT TOP 1 Fornecedor FROM tbl_Vendas WHERE Cod_produto = '{codigo}' ORDER BY ID_movimentacao DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# FUNÇÃO PARA BUSCAR Preco_compra DO ID
def consulta_Preco_compra(codigo):
    cursor.execute(f"SELECT TOP 1 Preco_compra FROM tbl_Vendas WHERE Cod_produto = '{codigo}' ORDER BY ID_movimentacao DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# FUNÇÃO PARA BUSCAR Data_cadastro DO ID
def consulta_Data_cadastro(codigo):
    cursor.execute(f"SELECT TOP 1 Data_cadastro FROM tbl_Vendas WHERE Cod_produto = '{codigo}' ORDER BY ID_movimentacao DESC")
    result = cursor.fetchone()
    if result:
        data_cadastro = datetime.strptime(result[0], '%Y-%m-%d').strftime('%d/%m/%Y')
        return data_cadastro
    else:
        return 0


# FUNÇÃO PARA BUSCAR Tipo_Produto DO ID
def consulta_Tipo_Produto(codigo):
    cursor.execute(f"SELECT TOP 1 Tipo_Produto FROM tbl_Vendas WHERE Cod_produto = '{codigo}' ORDER BY ID_movimentacao DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# FUNÇÃO PARA BUSCAR Qualidade DO ID
def consulta_Qualidade(codigo):
    cursor.execute(f"SELECT TOP 1 Qualidade FROM tbl_Vendas WHERE Cod_produto = '{codigo}' ORDER BY ID_movimentacao DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# FUNÇÃO PARA BUSCAR Modelo_produto DO ID
def consulta_Modelo_produto(codigo):
    cursor.execute(f"SELECT TOP 1 Modelo_produto FROM tbl_Vendas WHERE Cod_produto = '{codigo}' ORDER BY ID_movimentacao DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# FUNÇÃO PARA BUSCAR Marca DO ID
def consulta_Marca(codigo):
    cursor.execute(f"SELECT TOP 1 Marca FROM tbl_Vendas WHERE Cod_produto = '{codigo}' ORDER BY ID_movimentacao DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# FUNÇÃO PARA BUSCAR Cor DO ID
def consulta_Cor(codigo):
    cursor.execute(f"SELECT TOP 1 Cor FROM tbl_Vendas WHERE Cod_produto = '{codigo}' ORDER BY ID_movimentacao DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# FUNÇÃO PARA BUSCAR Dias_em_estoque DO ID
# def consulta_Dias_em_estoque(codigo):
#     cursor.execute(f"SELECT TOP 1 Dias_em_estoque FROM tbl_Vendas WHERE Cod_produto = '{codigo}' ORDER BY Data_movimentacao DESC")
#     result = cursor.fetchone()
#     if result:
#         return result[0]
#     else:
#         return 0

# FUNÇÃO PARA BUSCAR Tamanho DO ID
def consulta_Tamanho(codigo):
    cursor.execute(f"SELECT TOP 1 Tamanho FROM tbl_Vendas WHERE Cod_produto = '{codigo}' ORDER BY Data_movimentacao DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0


# sg.theme('DarkAmber')
# função para gerar recibo da compra
numeros = range(1,100000)
momento = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
codigo_venda= random.choice(numeros)


def gera_recibo(carrinho):
    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=9)  # Aumenta o tamanho da fonte

    pdf.cell(200, 10, txt="RECIBO DE COMPRA", ln=1, align="C")
    pdf.cell(200, 10, txt="Momento da compra {}".format(momento), ln=1, align="C")
    pdf.cell(2, 10, txt="ID Venda: {}".format(codigo_venda), ln=1)
    pdf.cell(200, 10, txt="ITENS COMPRADOS:", ln=1, align="L")

    for item in carrinho:
        # Inclui tamanho, cor e marca no comprovante
       # Criar uma única célula para cada item de compra
        linha = f"Produto: {item[0]} | Marca: {item[5]} | Cor: {item[6]} | Tamanho: {item[7]} | Preço: R${item[1]:.2f} | Quantidade: {item[2]} | Desconto: {item[3]}% | Valor total: R${item[4]:.2f}"
        pdf.cell(200, 10, txt=linha, ln=1, align="L")
        pdf.cell(0, 5, txt="----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", ln=1, align="C")



        # pdf.cell(200, 10, txt=f"  - Marca: {item[5]}", ln=1, align="L")
        # pdf.cell(200, 10, txt=f"  - Cor: {item[6]}", ln=1, align="L")
        # pdf.cell(200, 10, txt=f"  - Tamanho: {item[7]}", ln=1, align="L")
        # pdf.cell(200, 10, txt=f"  - Preço: R${item[1]:.2f}", ln=1, align="L")
        # pdf.cell(200, 10, txt=f"  - Quantidade: {item[2]}", ln=1, align="L")
        # pdf.cell(200, 10, txt=f"  - Desconto: {item[3]}%", ln=1, align="L")
        # pdf.cell(200, 10, txt=f"  - Valor total: R${item[4]:.2f}", ln=1, align="L")
        

    total_compra = sum([item[4] for item in carrinho])
    pdf.cell(200, 10, txt=f"Total da compra: R${total_compra:.2f}", ln=1, align="R")
    pdf.cell(200, 10, txt=f"Cliente: {Nome_cliente}", ln=1, align="R")

    # Aumenta o espaço entre as células
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.output("recibo.pdf")
    print("Recibo gerado com sucesso!")



col1 = [
    [sg.Text(size=(40, 1), font=('Helvetica', 20),justification='center', key='-OUTPUT-'),],
    [sg.Text('JOHN CARVALHO STORE',pad=(0, 0), font=('Arial', 20), size=(25, 1),text_color='BLACK' )],
    [sg.Text('Id do produto:', font=('Arial', 20), size=(20, 1)), sg.Input(key='codigo', font=('Arial', 20))],
    [sg.Text('Fornecedor:', font=('Arial', 20),size=(20, 1)), sg.Input(key='fornecedor',font=('Arial', 20))],
    [sg.Text('Tipo de Movimentação:', font=('Arial', 20), size=(20, 1)),
    sg.InputCombo(['entrada', 'saída'], key='tipo_movimentacao', font=('Arial', 20))],
    [sg.Text('Quantidade comprada:', font=('Arial', 20), size=(20, 1)), sg.Input(key='Qtde_comprada', font=('Arial', 20))],
    [sg.Text('Preco compra:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Preco_compra',font=('Arial', 20))],
    [sg.Text('Data cadastro:', font=('Arial', 20),size=(20, 1)), sg.Input(key='data_cadastro',font=('Arial', 20))],
    [sg.Text('Data movimentacao:', font=('Arial', 20),size=(20, 1)), sg.Input(key='data_movimentacao',font=('Arial', 20),default_text = current_time_atual)],
    [sg.Text('Tipo Produto:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Tipo_Produto',font=('Arial', 20))],
    [sg.Text('Qualidade:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Qualidade',font=('Arial', 20))],
    [sg.Text('Modelo produto:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Modelo_produto',font=('Arial', 20))],
    [sg.Text('Marca:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Marca',font=('Arial', 20))],
    [sg.Text('Cor:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Cor',font=('Arial', 20))],
    [sg.Text('Tamanho:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Tamanho',font=('Arial', 20))],
    [sg.Text('Nome cliente:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Nome_cliente',font=('Arial', 20))],
    [sg.Text('Telefone cliente:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Telefone_cliente',font=('Arial', 20))],
    [sg.Text('Sexo Cliente:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Sexo_cliente',font=('Arial', 20))],
    [sg.Text('Estado:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Estado',font=('Arial', 20))],
    [sg.Text('Cidade:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Cidade',font=('Arial', 20))],
    
]
col3 = [
    [sg.Text('Bairro:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Bairro',font=('Arial', 20))],
    [sg.Text('Rua:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Rua',font=('Arial', 20))],
    [sg.Text('Complemento:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Complemento',font=('Arial', 20))],
    [sg.Text('Numero:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Numero',font=('Arial', 20))],
    [sg.Text('Preço unitário:', font=('Arial', 20),size=(20, 1)), sg.Input(key='preco',font=('Arial', 20))],
    [sg.Text('Quantidade Entrada:', font=('Arial', 20), size=(20, 1)),
     sg.Input(key='quantidade_entrada', font=('Arial', 20), disabled=True)],

    [sg.Text('Quantidade Venda:', font=('Arial', 20), size=(20, 1)),
     sg.Input(key='quantidade_venda', font=('Arial', 20), disabled=True)],
    [sg.Text('Desconto:', font=('Arial', 20),size=(20, 1)), sg.Input(key='desconto',font=('Arial', 20))],
    [sg.Text('Valor total:', font=('Arial', 20),size=(20, 1)), sg.Text('', size=(20, 1), key='valor',font=('Arial', 20))],
    [sg.Button('Adicionar item',font=('Arial', 20)), sg.Button('Finalizar compra',font=('Arial', 20)), sg.Button('Cancelar',font=('Arial', 20)),sg.Button('CEP',font=('Arial', 20))], 
    [sg.Button('Consultar Estoque',font=('Arial', 20))],
    [sg.Text('Salvar arquivo como :', font=('Arial', 20),size=(20, 1)), sg.Input(key='Nome do arquivo',font=('Arial', 20))],
    [sg.Image(r'D:\Projetos\workspace Python\Sistema_Loja\LOGO.png',size=(500, 500), pad=(100, 10))],
    [sg.Text("Pasta de destino"), sg.FileSaveAs()],
]

layout = [    [sg.Column(col1, vertical_alignment='top'), sg.Column(col3)],
  ]

window = sg.Window('Sistema de comércio', layout, size=(1800,800), 
resizable=True, auto_size_text=True, 
default_element_size=(20, 1),)
carrinho = []



# loop principal do sistema
while True:
    event, values = window.read(timeout=100)
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    window['-OUTPUT-'].update(current_time)

    if values['tipo_movimentacao'] == 'entrada':
            window['quantidade_entrada'].update(disabled=False)
            window['quantidade_venda'].update(disabled=True)
        # Verifica se a opção selecionada em 'Tipo de Movimentação' é 'saída'
    elif values['tipo_movimentacao'] == 'saída':
        window['quantidade_entrada'].update(disabled=True)
        window['quantidade_venda'].update(disabled=False)
   # verifica se o botão Consultar estoque foi clicado
    if event == 'Consultar Estoque':
            
            
            codigo_produto = values['codigo']
    

            qtde_comprada = consulta_estoque(codigo_produto)
            window['Qtde_comprada'].update(qtde_comprada)


            fornecedor = consulta_fornecedor(codigo_produto)
            window['fornecedor'].update(fornecedor)

            preco_compra = consulta_Preco_compra(codigo_produto)
            window['Preco_compra'].update(preco_compra)

            data_cadastro = consulta_Data_cadastro(codigo_produto)
            window['data_cadastro'].update(data_cadastro)

            tipo_produto = consulta_Tipo_Produto(codigo_produto)
            window['Tipo_Produto'].update(tipo_produto)

            qualidade = consulta_Qualidade(codigo_produto)
            window['Qualidade'].update(qualidade)

            modelo_produto = consulta_Modelo_produto(codigo_produto)
            window['Modelo_produto'].update(modelo_produto)
            
            marca = consulta_Marca(codigo_produto)
            window['Marca'].update(marca)

            cor = consulta_Cor(codigo_produto)
            window['Cor'].update(cor)
            

            # dias_em_estoque = consulta_Dias_em_estoque(codigo_produto)
            # window['Qtde_comprada'].update(dias_em_estoque)


            tamanho = consulta_Tamanho(codigo_produto)
            window['Tamanho'].update(tamanho)

    
   
# verifica se o botão Adicionar item foi clicado
   # Restante do seu código ...

    if event == 'Adicionar item':
        Tipo_movimentacao = values['tipo_movimentacao']
        preco = float(values['preco'])
        desconto = float(values['desconto'])

        quantidade_venda = int(values['quantidade_venda']) if Tipo_movimentacao == 'saída' and values['quantidade_venda'] else 0
        quantidade_entrada = int(values['quantidade_entrada']) if Tipo_movimentacao == 'entrada' and values['quantidade_entrada'] else 0

        quantidade_movimentada = quantidade_venda or quantidade_entrada

        valor = preco * quantidade_movimentada * (1 - desconto/100)

        window['valor'].update(f"R${valor:.2f}")

        carrinho.append((values['Tipo_Produto'], preco, quantidade_movimentada, desconto, valor,marca,cor,tamanho))

        Cod_produto = values['codigo']
        Fornecedor = values['fornecedor']
        Qtde_comprada = int(values['Qtde_comprada'])
        Preco_compra = float(values['Preco_compra'])
        Data_cadastro = values['data_cadastro']
        Data_movimentacao = values['data_movimentacao']
        Tipo_Produto = values['Tipo_Produto']
        Qualidade = values['Qualidade']
        Modelo_produto = values['Modelo_produto']
        Marca = values['Marca']
        Cor = values['Cor']
        Tamanho = values['Tamanho']
        Nome_cliente = values['Nome_cliente']
        Telefone_cliente = values['Telefone_cliente']
        Sexo_cliente = values['Sexo_cliente']
        Estado = values['Estado']
        Cidade = values['Cidade']
        Bairro = values['Bairro']
        Rua = values['Rua']
        Complemento = values['Complemento']
        Numero = values['Numero']
        Preco_venda = float(values['preco'])
        

        Qtde_vendida = quantidade_venda if Tipo_movimentacao == 'saída' else 0


        Qtde_entrada = quantidade_entrada if Tipo_movimentacao == 'entrada' else 0

       
        comando = f"""INSERT INTO tbl_Vendas(Cod_produto,Fornecedor,Tipo_movimentacao,Qtde_comprada,Preco_compra,Data_cadastro,Data_movimentacao,Tipo_Produto,Qualidade,Modelo_produto,Marca,Cor,Tamanho,Nome_cliente,Telefone_cliente,Sexo_cliente,Estado,Cidade,Bairro,Rua,Complemento,Numero,Preco_venda,Qtde_entrada,Qtde_vendida)
                    VALUES 
                    ('{Cod_produto}','{Fornecedor}','{Tipo_movimentacao}',{Qtde_comprada},{Preco_compra},'{Data_cadastro}','{Data_movimentacao}','{Tipo_Produto}','{Qualidade}','{Modelo_produto}','{Marca}','{Cor}','{Tamanho}', '{Nome_cliente}', '{Telefone_cliente}','{Sexo_cliente}','{Estado}','{Cidade}','{Bairro}','{Rua}','{Complemento}','{Numero}',{Preco_venda},{Qtde_entrada},{Qtde_vendida})"""

        cursor.execute(comando)
        cursor.commit()

    # Restante do seu código para limpar os campos após a inserção



        window.FindElement('codigo').Update('')
        window.FindElement('fornecedor').Update('')
        window.FindElement('Qtde_comprada').Update('')
        window.FindElement('Preco_compra').Update('')
        # window.FindElement('data_cadastro').Update('')
        # window.FindElement('data_movimentacao').Update('')
        window.FindElement('Tipo_Produto').Update('')
        window.FindElement('Qualidade').Update('')
        window.FindElement('Modelo_produto').Update('')
        window.FindElement('Marca').Update('')
        window.FindElement('Cor').Update('')
        window.FindElement('Tamanho').Update('')
        # window.FindElement('Nome_cliente').Update('')
        # window.FindElement('Telefone_cliente').Update('')
        # window.FindElement('Sexo_cliente').Update('')
        # window.FindElement('Estado').Update('')
        # window.FindElement('Cidade').Update('')
        # window.FindElement('Bairro').Update('')
        # window.FindElement('Rua').Update('')
        # window.FindElement('Complemento').Update('')
        # window.FindElement('Numero').Update('')
        window.FindElement('preco').Update('')
        window.FindElement('quantidade_venda').Update('')
        window.FindElement('quantidade_entrada').Update('')
        window.FindElement('desconto').Update('')
        window.FindElement('tipo_movimentacao').Update('')
     

        
 
        # verifica se o botão Finalizar compra foi clicado
    elif event == 'Finalizar compra':
        gera_recibo(carrinho)
        new_file_name = values["Nome do arquivo"]+ ".pdf"
        os.rename("recibo.pdf", new_file_name)
        sg.popup('Compra finalizada com sucesso!', 'O recibo da compra foi gerado com sucesso e está disponível .')
        window.FindElement('Nome do arquivo').Update('')
        window.FindElement('valor').Update('')

        window.FindElement('data_cadastro').Update('')
        window.FindElement('data_movimentacao').Update('')
        window.FindElement('Nome_cliente').Update('')
        window.FindElement('Telefone_cliente').Update('')
        window.FindElement('Sexo_cliente').Update('')
        window.FindElement('Estado').Update('')
        window.FindElement('Cidade').Update('')
        window.FindElement('Bairro').Update('')
        window.FindElement('Rua').Update('')
        window.FindElement('Complemento').Update('')
        window.FindElement('Numero').Update('')

                # Crie a mensagem com base nas informações dos itens
        mensagem_itens = ""
        valor_total_sem_desconto = 0
        valor_total_com_desconto = 0
        for item in carrinho:
            valor_total_sem_desconto += item[1] * item[2]  # Preço * Quantidade
            valor_desconto = (item[1] * item[2] * item[3] / 100)  # Preço * Quantidade * Desconto
            valor_total_com_desconto += item[4]  # Valor total do item após desconto

            mensagem_itens += f"""- Produto: *{item[0]}*
                - Marca : *{item[5]}*
                - Cor : *{item [6]}*
                - Tamanho: *{item[7]}*
                - Preço de compra: *R${item[1]:.2f}*
                - Quantidade comprada: *{item[2]}*
                - Desconto aplicado: *{item[3]}%*
                - Valor antes do desconto: *R${item[1] * item[2]:.2f}*
                - Valor total com *DESCONTO*: *R${item[4]:.2f}*\n\n"""

        mensagem = f"""*Obrigado* por comprar conosco, *{Nome_cliente}!*\n\n
               *JOHN CARVALHO STORE* agradece a preferência. Abaixo está os dados da sua compra:\n\n
               Detalhes da compra:\n
               {mensagem_itens}
               - Data da compra: *{Data_movimentacao}*\n
               - Horário da compra: *{current_time}*\n\n
               - Valor total sem desconto: *R${valor_total_sem_desconto:.2f}*
               - Valor total com desconto: *R${valor_total_com_desconto:.2f}*\n\n
               O link para o comprovante da compra está disponível \n
               Agradecemos novamente pela sua compra!\n
               Equipe *JOHN CARVALHO STORE*"""

        codigo_pais = "+55"
        numero_telefone = Telefone_cliente
        telefone_completo = codigo_pais + numero_telefone

        agora = datetime.now()
        horario_envio = agora + timedelta(minutes=2)

        hora_envio = horario_envio.hour
        minuto_envio = horario_envio.minute

        if Tipo_movimentacao == 'entrada':
            break
        else:
            kit.sendwhatmsg(telefone_completo, mensagem, hora_envio, minuto_envio)
    if event == sg.WIN_CLOSED or event == 'Exit':  # Adiciona evento para fechamento da janela ao clicar no X ou em um botão "Exit"
        break
    # verifica se o botão Cancelar foi clicado
    elif event == 'Cancelar':
        break
    

window.close()