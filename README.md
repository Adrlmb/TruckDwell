# 🚛 TruckDwell

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Em%20Refatoração-yellow)
![License](https://img.shields.io/badge/Licença-MIT-green)
![Contribuições](https://img.shields.io/badge/Contribuições-Bem--vindas-brightgreen)

**TruckDwell** é uma aplicação desenvolvida em **Python** voltada ao controle, análise e visualização do **tempo de permanência de caminhões** em áreas de carga e descarga.  
O objetivo é auxiliar equipes logísticas a monitorar o fluxo de caminhões, otimizar tempos de operação e gerar relatórios analíticos de desempenho.

![apresentacao_truckdwell](https://github.com/user-attachments/assets/9d12f18a-5578-4f38-9070-6c38351d7148)
---

## 🧭 Sumário

01. [Arquitetura do Projeto](#-arquitetura-do-projeto)
02. [Instalação](#-instalação)
03. [Como Executar](#-como-executar)
04. [Funcionalidades](#-funcionalidades)
05. [Tecnologias](#-tecnologias)
06. [Contribuição](#-contribuição)
07. [Licença](#-licença)

---

## 🧩 Arquitetura do Projeto

```
TruckDwell/
├── src/ # Código principal e módulos da aplicação
│ ├── main.py # Ponto de entrada principal
│ ├── models/ # Modelos e classes de domínio
│ ├── services/ # Regras de negócio e processamento
│ └── utils/ # Funções auxiliares e tratamento de dados
├── tickets-de-pesagem/ # Dados brutos ou scripts de integração
├── dist/ # Distribuições / builds geradas
├── display.py # Interface de visualização / execução alternativa
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo 
└── .idea/ # Metadados da IDE (pode ser ignorado)
```

## ⚙️ Instalação

1. Clone o repositório:
```
   git clone https://github.com/Adrlmb/TruckDwell.git
   cd TruckDwell
```
2. Crie e ative um ambiente virtual:

```
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Instale as dependências:
```
pip install -r requirements.txt
```

## 🚀 Como Executar
* Execute o módulo principal:
```
python src/main.py
```

## 📊 Funcionalidades
* ✅ Registro e controle de tempo de permanência de caminhões

* ✅ Leitura e processamento de tickets de pesagem

* ✅ Visualização de dados de operação (texto e gráfico)

* ✅ Exportação de relatórios

* ✅ Base modular, fácil de refatorar e expandir


## 🧱 Tecnologias

| Camada          | Ferramentas / Tecnologias      |
|-----------------|--------------------------------|
| Linguagem       | Python 3.10+                   |
| Bibliotecas     | tkinter, pdfplumber, openpyxl  |
| IDE Recomendada | PyCharm ou VSCode              |
| Armazenamento   | Local (arquivos .xlsx)         |


## 🤝 Contribuição
Contribuições são muito bem-vindas! 💡

1. Faça um fork do projeto

2. Crie uma branch para sua modificação
```
git checkout -b minha-feature
```

3. Faça commit das mudanças
```
git commit -m "Adiciona nova funcionalidade"
```

4. Envie um Pull Request 🚀

>Para sugestões ou bugs, abra uma issue descrevendo claramente o problema.

## 📜 Licença

Este projeto é licenciado sob a [MIT License](./LICENSE).  
Sinta-se livre para usar, modificar e contribuir.
