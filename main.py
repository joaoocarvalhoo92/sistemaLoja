import PySimpleGUI as sg
import fpdf
import random
import os
import pyodbc
from datetime import datetime








dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-5A10GBO;"
    "Database=Fornecedores_jcstore;"
)


conexao = pyodbc.connect(dados_conexao)
print("Conexao bem sucedida !")

cursor = conexao.cursor()

# FUNÇÃO PARA BUSCAR ESTOQUE ATUAL
def consulta_estoque(codigo):
    cursor.execute(f"SELECT TOP 1 Estoque FROM tbl_Vendas WHERE id_produto = '{codigo}' ORDER BY ID_Venda DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# FUNÇÃO PARA BUSCAR FORNECEDOR DO ID
def consulta_fornecedor(codigo):
    cursor.execute(f"SELECT TOP 1 Fornecedor FROM tbl_Vendas WHERE id_produto = '{codigo}' ORDER BY ID_Venda DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# FUNÇÃO PARA BUSCAR Preco_compra DO ID
def consulta_Preco_compra(codigo):
    cursor.execute(f"SELECT TOP 1 Preco_compra FROM tbl_Vendas WHERE id_produto = '{codigo}' ORDER BY ID_Venda DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# FUNÇÃO PARA BUSCAR Data_cadastro DO ID
def consulta_Data_cadastro(codigo):
    cursor.execute(f"SELECT TOP 1 Data_cadastro FROM tbl_Vendas WHERE id_produto = '{codigo}' ORDER BY ID_Venda DESC")
    result = cursor.fetchone()
    if result:
        data_cadastro = datetime.strptime(result[0], '%Y-%m-%d').strftime('%d/%m/%Y')
        return data_cadastro
    else:
        return 0


# FUNÇÃO PARA BUSCAR Tipo_Produto DO ID
def consulta_Tipo_Produto(codigo):
    cursor.execute(f"SELECT TOP 1 Tipo_Produto FROM tbl_Vendas WHERE id_produto = '{codigo}' ORDER BY ID_Venda DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# FUNÇÃO PARA BUSCAR Qualidade DO ID
def consulta_Qualidade(codigo):
    cursor.execute(f"SELECT TOP 1 Qualidade FROM tbl_Vendas WHERE id_produto = '{codigo}' ORDER BY ID_Venda DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# FUNÇÃO PARA BUSCAR Modelo_produto DO ID
def consulta_Modelo_produto(codigo):
    cursor.execute(f"SELECT TOP 1 Modelo_produto FROM tbl_Vendas WHERE id_produto = '{codigo}' ORDER BY ID_Venda DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# FUNÇÃO PARA BUSCAR Marca DO ID
def consulta_Marca(codigo):
    cursor.execute(f"SELECT TOP 1 Marca FROM tbl_Vendas WHERE id_produto = '{codigo}' ORDER BY ID_Venda DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# FUNÇÃO PARA BUSCAR Cor DO ID
def consulta_Cor(codigo):
    cursor.execute(f"SELECT TOP 1 Cor FROM tbl_Vendas WHERE id_produto = '{codigo}' ORDER BY ID_Venda DESC")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# FUNÇÃO PARA BUSCAR Dias_em_estoque DO ID
# def consulta_Dias_em_estoque(codigo):
#     cursor.execute(f"SELECT TOP 1 Dias_em_estoque FROM tbl_Vendas WHERE id_produto = '{codigo}' ORDER BY Data_venda DESC")
#     result = cursor.fetchone()
#     if result:
#         return result[0]
#     else:
#         return 0

# FUNÇÃO PARA BUSCAR Tamanho DO ID
def consulta_Tamanho(codigo):
    cursor.execute(f"SELECT TOP 1 Tamanho FROM tbl_Vendas WHERE id_produto = '{codigo}' ORDER BY Data_venda DESC")
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
    pdf.set_font("Arial", size=5)
    pdf.cell(200, 10, txt="RECIBO DE COMPRA", ln=1, align="C")
    pdf.cell(200, 10, txt="Momento da compra {}".format(momento), ln=1, align="C")
    pdf.cell(2,1, txt="  ID Venda : {}".format(codigo_venda))
    pdf.cell(200, 10, txt="ITENS COMPRADOS:", ln=1, align="L")
    pdf.cell(0, 0, txt="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", ln=1, align="C")

    for item in carrinho:
        pdf.cell(200, 2, txt=f"Produto: {item[0]} | Preço: R${item[1]:.2f} | Quantidade: {item[2]} | Desconto: {item[3]}% | Valor total: R${item[4]:.2f}", ln=1, align="L")
        pdf.cell(200, 2, txt="", ln=1, align="C")
    
    total_compra = sum([item[4] for item in carrinho])
    pdf.cell(200, 2, txt=f"Total da compra: R${total_compra:.2f}", ln=1, align="R")
    pdf.output("recibo.pdf")
    print("Recibo gerado com sucesso!")


col1 = [
    [sg.Text(size=(40, 1), font=('Helvetica', 20),justification='center', key='-OUTPUT-'),],
    [sg.Text('JOHN CARVALHO STORE',pad=(0, 0), font=('Arial', 20), size=(25, 1),text_color='BLACK' )],
    [sg.Text('Id do produto:', font=('Arial', 20), size=(20, 1)), sg.Input(key='codigo', font=('Arial', 20))],
    [sg.Text('Fornecedor:', font=('Arial', 20),size=(20, 1)), sg.Input(key='fornecedor',font=('Arial', 20))],
    [sg.Text('Estoque atual:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Estoque_inicial',font=('Arial', 20))],
    [sg.Text('Preco compra:', font=('Arial', 20),size=(20, 1)), sg.Input(key='Preco_compra',font=('Arial', 20))],
    [sg.Text('Data cadastro:', font=('Arial', 20),size=(20, 1)), sg.Input(key='data_cadastro',font=('Arial', 20))],
    [sg.Text('Data venda:', font=('Arial', 20),size=(20, 1)), sg.Input(key='data_venda',font=('Arial', 20))],
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
    [sg.Text('Quantidade:', font=('Arial', 20),size=(20, 1)), sg.Input(key='quantidade',font=('Arial', 20))],
    [sg.Text('Desconto:', font=('Arial', 20),size=(20, 1)), sg.Input(key='desconto',font=('Arial', 20))],
    [sg.Text('Valor total:', font=('Arial', 20),size=(20, 1)), sg.Text('', size=(20, 1), key='valor',font=('Arial', 20))],
    [sg.Button('Adicionar item',font=('Arial', 20)), sg.Button('Finalizar compra',font=('Arial', 20)), sg.Button('Cancelar',font=('Arial', 20)),sg.Button('CEP',font=('Arial', 20))], 
    [sg.Button('Consultar Estoque',font=('Arial', 20))],
    [sg.Text('Salvar arquivo como :', font=('Arial', 20),size=(20, 1)), sg.Input(key='Nome do arquivo',font=('Arial', 20))],
    [sg.Image(r'D:\Projetos\workspace Python\MEU SISTEMA DE LOJA\LUXURY JHON CARVALHO transparente.png',size=(500, 500), pad=(100, 10))],
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

   # verifica se o botão Consultar estoque foi clicado
    if event == 'Consultar Estoque':
            codigo_produto = values['codigo']

            qtde_comprada = consulta_estoque(codigo_produto)
            window['Estoque_inicial'].update(qtde_comprada)


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
            # window['Estoque_inicial'].update(dias_em_estoque)


            tamanho = consulta_Tamanho(codigo_produto)
            window['Tamanho'].update(tamanho)

    # verifica se o botão Adicionar item foi clicado


    if event == 'Adicionar item':

        
        preco = float(values['preco'])
        quantidade = int(values['quantidade'])
        desconto = float(values['desconto'])
        valor = preco * quantidade * (1 - desconto/100)
        window['valor'].update(f"R${valor:.2f}")
        carrinho.append((values['Tipo_Produto'], preco, quantidade, desconto, valor))
        Id_produto = int(values['codigo'])
        Fornecedor = values['fornecedor']
        Estoque_inicial = values['Estoque_inicial']
        Preco_compra = float(values['Preco_compra'])
        Data_cadastro = values['data_cadastro']
        Data_venda = values['data_venda']
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
        Qtde_vendida = int(values['quantidade'])

        comando = f"""INSERT INTO tbl_Vendas(Id_produto,Fornecedor,Estoque_inicial,Preco_compra,Data_cadastro,Data_venda,Tipo_Produto,Qualidade,Modelo_produto,Marca,Cor,Tamanho,Nome_cliente,Telefone_cliente,Sexo_cliente,Estado,Cidade,Bairro,Rua,Complemento,Numero,Preco_venda,Qtde_vendida)
        VALUES 
            ({Id_produto},'{Fornecedor}',{Estoque_inicial},{Preco_compra},'{Data_cadastro}','{Data_venda}','{Tipo_Produto}','{Qualidade}','{Modelo_produto}','{Marca}','{Cor}','{Tamanho}', '{Nome_cliente}', '{Telefone_cliente}','{Sexo_cliente}','{Estado}','{Cidade}','{Bairro}','{Rua}','{Complemento}','{Numero}',{Preco_venda},{Qtde_vendida})"""

        cursor.execute(comando)
        cursor.commit()
        window.FindElement('codigo').Update('')
        window.FindElement('fornecedor').Update('')
        window.FindElement('Estoque_inicial').Update('')
        window.FindElement('Preco_compra').Update('')
        window.FindElement('data_cadastro').Update('')
        window.FindElement('data_venda').Update('')
        window.FindElement('Tipo_Produto').Update('')
        window.FindElement('Qualidade').Update('')
        window.FindElement('Modelo_produto').Update('')
        window.FindElement('Marca').Update('')
        window.FindElement('Cor').Update('')
        window.FindElement('Tamanho').Update('')
        window.FindElement('Nome_cliente').Update('')
        window.FindElement('Telefone_cliente').Update('')
        window.FindElement('Sexo_cliente').Update('')
        window.FindElement('Estado').Update('')
        window.FindElement('Cidade').Update('')
        window.FindElement('Bairro').Update('')
        window.FindElement('Rua').Update('')
        window.FindElement('Complemento').Update('')
        window.FindElement('Numero').Update('')
        window.FindElement('preco').Update('')
        window.FindElement('quantidade').Update('')
        window.FindElement('desconto').Update('')
 
        # verifica se o botão Finalizar compra foi clicado
    elif event == 'Finalizar compra':
        gera_recibo(carrinho)
        new_file_name = values["Nome do arquivo"] + ".pdf"
        os.rename("recibo.pdf", new_file_name)
        sg.popup('Compra finalizada com sucesso!', 'O recibo da compra foi gerado com sucesso e está disponível .')
        window.FindElement('Nome do arquivo').Update('')
        window.FindElement('valor').Update('')
    if event == sg.WIN_CLOSED or event == 'Exit':  # Adiciona evento para fechamento da janela ao clicar no X ou em um botão "Exit"
        break
    # verifica se o botão Cancelar foi clicado
    elif event == 'Cancelar':
        break
    

window.close()
