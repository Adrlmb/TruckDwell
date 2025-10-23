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


