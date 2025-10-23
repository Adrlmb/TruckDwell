from openpyxl import load_workbook

def preencher_planilha(caminho_modelo, dados, caminho_saida):
    wb = load_workbook(caminho_modelo)
    planilha = wb.active

    planilha['F3'] = dados['transportadora']
    planilha['C4'] = int(dados['nf'])
    planilha['C5'] = dados['produto']
    planilha['F12'] = dados['peso']
    planilha['B15'] = dados['dataHoraSaida']

    planilha['B9'] = dados['dataHoraChegada']
    planilha['C3'] = dados['fornecedor']
    planilha['F4'] = dados['cte']
    planilha['F5'] = dados['motorista']
    planilha['E16'] = dados['motivo']

    wb.save(caminho_saida)
    wb.close()

