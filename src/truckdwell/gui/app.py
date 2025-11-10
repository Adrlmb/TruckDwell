import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk

from core.utils import emitir_estadia
from src.truckdwell.planilha.excel import preencher_planilha
from src.truckdwell.core.utils import limparDados, importar_pdf

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

        self.container1 = Frame(self)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(self)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(self)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(self)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(self)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(self)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(self)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.labels(self.container1, self.container2, self.container3, self.container4, self.container5, self.container6,
                    self.fontePadrao)
        self.buttons(self.container7, self.fontePadrao)

    def labels(self, container1, container2, container3, container4, container5, container6, fontePadrao):
        # Titulo
        self.title = Label(container1, text="Calculo de Estadia")
        self.title["font"] = ("Calibri", "20", "bold")
        self.title.pack()

        # Nome do Fornecedor
        self.labelFornecedor = Label(container2, text="Fornecedor ", font=fontePadrao)
        self.labelFornecedor.pack(side=LEFT)

        self.inputFornecedor = Entry(container2, textvariable= self.fornecedor, width=30, font=fontePadrao)
        self.inputFornecedor.focus()
        self.inputFornecedor.pack(side=LEFT)

        # Transportadora
        self.labelTransportadora = Label(container2, text="Transportadora ", font=fontePadrao)
        self.labelTransportadora.pack(side=LEFT)

        transportadorasCadastradas = ['MINERACAO BELOCAL', 'CARVALHO TRANSPORTES', 'FRIBON TRANSPORTES',
                                      'FUTURO LOGISTICA',
                                      'SIMOES BEBEDOURO', 'TRANSLOPES TRANSPORTES']
        transportadorasCadastradas.sort()

        self.inputTransportadora = ttk.Combobox(container2, textvariable=  self.transportadora,
                                                values=transportadorasCadastradas, width=30, font=fontePadrao)
        self.inputTransportadora.pack(side=LEFT)

        # Nome do Motorista
        self.labelMotorista = Label(container3, text="Nome do Motorista ", font=fontePadrao)
        self.labelMotorista.pack(side=LEFT)

        self.inputMotorista = Entry(container3, textvariable= self.motorista, width=30, font=fontePadrao)
        self.inputMotorista.pack(side=LEFT)

        # Nome do Produto
        self.labelProduto = Label(container3, text="Produto ", font=fontePadrao)
        self.labelProduto.pack(side=LEFT)

        produtosCadastrados = ['ROCHA UMA', 'ROCHA CMISS', 'KCL 00-00-58 GR', 'CAL DOLO HIDRATADA', 'SSP 00-19-00',
                               'KCL 00-00-60 GR IMP', 'MAP 11-52-00 GR', 'MICRO HMoNi', 'ENXOFRE F IMP.']
        produtosCadastrados.sort()
        self.inputProduto = ttk.Combobox(container3, textvariable= self.produto, values=produtosCadastrados, width=30,
                                         font=fontePadrao)
        self.inputProduto.pack(side=LEFT)

        # Data e Hora de Chegada
        self.labelDataHoraChegada = Label(container4, text="Data/Hora de Chegada ", font=fontePadrao)
        self.labelDataHoraChegada.pack(side=LEFT)

        self.inputDataHoraChegada = Entry(container4, textvariable= self.dataHoraChegada, width=20, font=fontePadrao)
        self.inputDataHoraChegada.pack(side=LEFT)

        # Data e Hora de Saída
        self.labelDataHoraSaida = Label(container4, text="Data/Hora de Saída ", font=fontePadrao)
        self.labelDataHoraSaida.pack(side=LEFT)

        self.inputDataHoraSaida = Entry(container4, textvariable= self.dataHoraSaida, width=20, font=fontePadrao)
        self.inputDataHoraSaida.pack(side=LEFT)

        # Número do CT-e
        self.labelCte = Label(container5, text="Número do CT-e ", font=fontePadrao)
        self.labelCte.pack(side=LEFT)

        self.inputCte = Entry(container5, textvariable= self.cte, width=10, font=fontePadrao)
        self.inputCte.pack(side=LEFT)

        # Número da NF
        self.labelNf = Label(container5, text="Número da NF ", font=fontePadrao)
        self.labelNf.pack(side=LEFT)

        self.inputNF = Entry(container5, textvariable= self.nf, width=10, font=fontePadrao)
        self.inputNF.pack(side=LEFT)

        # Peso da NF
        self.labelPeso = Label(container5, text="Peso da NF ", font=fontePadrao)
        self.labelPeso.pack(side=LEFT)

        self.inputPeso = Entry(container5, textvariable= self.peso, width=10, font=fontePadrao)
        self.inputPeso.pack(side=LEFT)

        # Motivo da Estadia
        self.labelMotivo = Label(container6, text="Motivo da Estadia ", font=fontePadrao)
        self.labelMotivo.pack(side=LEFT)

        self.inputMotivo = Entry(container6, textvariable= self.motivo, width=60, font=fontePadrao)
        self.inputMotivo.pack(side=LEFT)

    def buttons(self, container7, fontePadrao):

        # Button - Chama a função que limpa todos os campos
        self.btnInput = Button(container7, text="Novo", font=fontePadrao, width=20,
                               command= lambda: limparDados(self))
        self.btnInput.pack(side=LEFT)

        # Button - Chama a função que extrai os campos do PDF
        self.btnBuscar = Button(container7, text="Importar PDF", font=fontePadrao, width=20,
                                command= lambda: importar_pdf(self))
        self.btnBuscar.pack(side=LEFT)

        # Button - Chama a função que salva dados do input
        self.btnInput = Button(container7, text="Emitir Estadia", font=fontePadrao, width=20,
                               command= lambda: emitir_estadia(self))
        self.btnInput.pack(side=RIGHT)
        self.btnInput.place()


