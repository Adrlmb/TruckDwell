import pdfplumber

def extrair_dados_pdf(caminho_pdf):
    with pdfplumber.open(caminho_pdf) as pdf:
        page = pdf.pages[0]
        text = page.extract_text().split('\n')

    # Exemplo de extração
    referencia_produto = text[8].split(' ')[1]
    referencia_transportadora = text[9].split(' ')[1]

    dados = {
        "produto": formatar_produto(referencia_produto),
        "transportadora": formatar_transportadora(referencia_transportadora),
        "nf": text[6].split(' ')[2],
        "peso": text[5].split(": ")[1],
        "dataHoraSaida": text[3].split(' ')[3] + ' ' + text[3].split(' ')[4]
    }
    return dados

# Funções auxiliares
def formatar_produto(codigo):
    produtos = ['ROCHA UMA', 'KCL 00-00-58 GR', 'CAL DOLO HIDRATADA', 'SSP 00-19-00',
                        'KCL 00-00-60 GR IMP', 'MAP 11-52-00 GR', 'MICRO HMoNi', 'ENXOFRE F IMP.']
    codigos = ['CF040002G1', 'MP2100005806G1', 'MA1100000432Bl', 'PA5100191231G1',
                              'MP2100006124G1', 'MP2111520001G1', 'MI200323090306B1', 'MP2200000001G1']
    for i, c in enumerate(codigos):
        if codigo == c:
            return produtos[i]
    return None

def formatar_transportadora(codigo):
    transportadoras = ['MINERACAO BELOCAL', 'CARVALHO TRANSPORTES', 'FRIBON TRANSPORTES', 'FUTURO LOGISTICA',
                               'SIMOES BEBEDOURO', 'TRANSLOPES TRANSPORTES']
    codigos = ['2000227564', '2000224719', '20123215499', '2000226886', '204005', '207147']

    for i, c in enumerate(codigos):
        if codigo == c:
            return transportadoras[i]
    return None
