import tkinter as tk
from tkinter import *
from tkinter import ttk

from truckdwell.core.utils import emitir_estadia
from truckdwell.core.utils import limparDados, importar_pdf

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cálculo de Estadia")

        janela_largura = 700
        janela_altura = 285

        tela_largura = self.winfo_screenwidth()
        tela_altura = self.winfo_screenheight()

        pos_x = (tela_largura // 2) - (janela_largura // 2)
        pos_y = (tela_altura // 2 ) - (janela_altura // 2 + 200)
        self.geometry(f"{janela_largura}x{janela_altura}+{pos_x}+{pos_y}")
        self.resizable(False, False)

        # Variáveis
        self.produto = tk.StringVar()
        self.transportadora = tk.StringVar()
        self.fornecedor = tk.StringVar()
        self.motorista = tk.StringVar()
        self.nf = tk.StringVar()
        self.cte = tk.StringVar()
        self.peso = tk.StringVar()
        self.dataHoraSaida = tk.StringVar()
        self.dataHoraChegada = tk.StringVar()
        self.motivo = tk.StringVar()

        self.criar_widgets()

    def criar_campo(self, container, texto, var, width = 30, tipo ="entry", opcoes =None):
        label = Label(container, text=texto, font=self.fontePadrao)
        label.pack(side=LEFT)

        if tipo == "combobox" and opcoes:
            input_widget = ttk.Combobox(container, textvariable = var, values = sorted(opcoes),
                                        width = width, font = self.fontePadrao)
        else:
            input_widget = Entry(container, textvariable = var, width = width, font = self.fontePadrao)

        input_widget.pack(side = LEFT)
        return input_widget


    def criar_widgets(self):
        self.fontePadrao = ("Arial", "10")

        # Containers

        self.container1 = Frame(self, pady = 10)
        self.container1.pack()

        self.container2 = Frame(self, padx=20, pady=5)
        self.container2.pack()

        self.container3 = Frame(self, padx=20, pady=5)
        self.container3.pack()

        self.container4 = Frame(self, padx=20, pady=5)
        self.container4.pack()

        self.container5 = Frame(self, padx=20, pady=5)
        self.container5.pack()

        self.container6 = Frame(self, padx=20, pady=5)
        self.container6.pack()

        self.container7 = Frame(self, padx=20, pady=5)
        self.container7.pack()

        self.labels()
        self.buttons()


    def labels(self):
        # Titulo
        Label(self.container1, text="Cálculo de Estadia", font=("Calibri", 20, "bold")).pack()

        # Campos
        # Nome do Fornecedor
        self.inputFornecedor = self.criar_campo(self.container2, "Fornecedor ", self.fornecedor)
        self.inputFornecedor.focus()


        # Transportadora
        transportadorasCadastradas = ['MINERACAO BELOCAL', 'CARVALHO TRANSPORTES', 'FRIBON TRANSPORTES',
                                      'FUTURO LOGISTICA',
                                      'SIMOES BEBEDOURO', 'TRANSLOPES TRANSPORTES']
        transportadorasCadastradas.sort()

        self.inputTransportadora = self.criar_campo(self.container2, "Transportadora", self.transportadora,
                                                    tipo= "combobox", opcoes = transportadorasCadastradas)

        # Motorista
        self.inputMotorista = self.criar_campo(self.container3, "Nome do Motorista ", self.motorista)


        # Produtos
        produtosCadastrados = ['ROCHA UMA', 'ROCHA CMISS', 'KCL 00-00-58 GR', 'CAL DOLO HIDRATADA', 'SSP 00-19-00',
                               'KCL 00-00-60 GR IMP', 'MAP 11-52-00 GR', 'MICRO HMoNi', 'ENXOFRE F IMP.']
        produtosCadastrados.sort()
        self.inputProduto = self.criar_campo(self.container3, "Produto ", self.produto, tipo = "combobox", opcoes = produtosCadastrados)


        # Data e Hora de Chegada
        self.inputDataHoraChegada = self.criar_campo(self.container4, "Data/Hora de Chegada ", self.dataHoraChegada, width = 20)


        # Data e Hora de Saída
        self.inputDataHoraSaida = self.criar_campo(self.container4, "Data/Hora de Saída ", self.dataHoraSaida, width = 20)

        # Número do CT-e
        self.inputCte = self.criar_campo(self.container5, "CT-e ", self.cte, width=10)


        # Número da NF
        self.inputNF = self.criar_campo(self.container5, "NF-e ", self.nf, width =10)

        # Peso da NF
        self.inputPeso = self.criar_campo(self.container5, "Peso ", self.peso, width= 10)


        # Motivo da Estadia
        self.inputMotivo = self.criar_campo(self.container6, "Motivo da Estadia", self.motivo, width = 60)


    def buttons(self):

        # Botão "Novo" - Chama a função que limpa todos os campos
        Button(self.container7, text= "Novo", font= self.fontePadrao, width = 20, command= lambda: limparDados(self)).pack(side= LEFT)

        # Botão "Importar PDF" - Chama a função que extrai os campos do PDF
        Button(self.container7, text= "Importar PDF", font= self.fontePadrao, width=20, command= lambda: importar_pdf(self)).pack(side= LEFT)

        # Botão "Emitir Estadia" - Chama a função que salva dados do input
        Button(self.container7, text= "Emitir Estadia", font= self.fontePadrao, width=20, command= lambda: emitir_estadia(self)).pack(side= LEFT)


