from tkinter import END, filedialog, messagebox
from src.truckdwell.pdf.extrator import extrair_dados_pdf
from src.truckdwell.planilha.excel import preencher_planilha

def limparDados(self):
    campos = [
        self.inputTransportadora,
        self.inputNF,
        self.inputProduto,
        self.inputPeso,
        self.inputDataHoraSaida,
        self.inputDataHoraChegada,
        self.inputFornecedor,
        self.inputCte,
        self.inputMotorista,
        self.inputMotivo
    ]

    for campo in campos:
        campo.delete(0,END)

    self.inputFornecedor.focus()  # Puxa o foco para o campo Fornecedor


def importar_pdf(self):
    caminho = filedialog.askopenfilename(initialdir="truckdwell/assets/tickets_de_balanca/",
                                         title= "Selecione um arquivo",
                                         filetypes=[("PDF", "*.pdf")])
    if caminho:
        dados = extrair_dados_pdf(caminho)
        self.produto.set(dados['produto'])
        self.transportadora.set(dados['transportadora'])
        self.nf.set(dados['nf'])
        self.peso.set(dados['peso'])
        self.dataHoraSaida.set(dados['dataHoraSaida'])

def emitir_estadia(self):
    caminho_modelo = "truckdwell/assets/planilha_estadia.xlsx"
    caminho_saida = filedialog.asksaveasfilename(initialdir= "../estadias_calculadas/",
                                                 defaultextension=".xlsx",
                                                 filetypes=[("Excel", "*.xlsx")])
    dados = {
        'produto': self.produto.get().upper(),
        'transportadora': self.transportadora.get().upper(),
        'nf': self.nf.get().upper(),
        'peso': self.peso.get().upper(),
        'dataHoraSaida': self.dataHoraSaida.get().upper(),
        'fornecedor': self.fornecedor.get().upper(),
        'motorista': self.motorista.get().upper(),
        'cte': self.cte.get().upper(),
        'dataHoraChegada': self.dataHoraChegada.get().upper(),
        'motivo': self.motivo.get().upper()

    }
    preencher_planilha(caminho_modelo, dados, caminho_saida)
    messagebox.showinfo("Sucesso", "Planilha gerada com sucesso!")
