# Fair Value Stocks API

[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/GustavoSantosBr/)
[![Minimum Python Version](https://img.shields.io/badge/python-%5E3.9.1-blue)](https://www.python.org)

* [Introdução](#Introdução)
    * [Preço](#Preço)
    * [Margem](#Margem)
    * [Observações](#Observações)
* [Requisitos](#Requisitos)
* [Instalação](#Instalação)
* [Endpoints](#Endpoints)

## Introdução

Benjamin Graham é considerado um dos pioneiros em investimentos a longo prazo (value investing), o investidor que foi
mentor de Warren Buffett apresentou a ideia de que o preço justo/valor intrínseco de uma ação poderia ser calculado
através de uma fórmula.

### Preço

`VI = √ (22,5 x LPA x VPA)`

`VI` = **V**alor **I**ntrínseco (preço justo)

`LPA` = **L**ucro **P**or **A**ção

`VPA` = **V**alor **P**atrimonial da **A**ção

### Margem

A Margem de Segurança é o percentual de desconto que o valor intrínseco tem em relação à cotação atual. Quanto maior o
desconto, maior o potencial de valorização da ação (upside).

`MS` = **M**argem de **S**egurança

`VI` = **V**alor **I**ntrínseco (preço justo)

`CT` = **C**otação **A**tual

`MS = ((VI - CT) / VI) * 100`

### Observações

- A fórmula não funciona com empresas que apresentaram prejuízos;
- O principal critério de Benjamin Graham é o lucro, então, empresas com `LPA` ou `VPA` negativos não serão
  consideradas;
- Isso não é uma recomendação de compra ou venda.

## Requisitos

Para a instalação e execução do projeto, sera necessário:

- [Python](https://www.python.org/downloads)
- [pip](https://pip.pypa.io/en/stable/installing)

## Instalação

Para este exemplo, estarei utilizando o powershell. Use um terminal conforme seu sistema operacional. No terminal,
navegue até o diretório de sua preferência, e execute:

```bash
> git clone https://github.com/GustavoSantosBr/fair-value-stocks-api.git
```

Navegue até a pasta {seudiretorio} utilizando:

```bash
> cd {seudiretorio} 
```

Para criar um ambiente isolado para trabalhar o projeto:

```bash
> cd python -m venv env
```

Para ativar o ambiente virtual:

```bash
> cd ./env/Scripts/activate.bat
```

Instale as depêndencias do projeto com o seguinte comando:

```bash
> pip install -r requirements.txt
```

## Endpoints

**GET** `/fair-prices`

Busca as ações que possuem uma cotação atual menor ou igual ao preço justo calculado.

- **Exemplos:**

    - Request `/fair-prices`
    - Response
       ```json
          {
              "data": [        
                  {
                      "company_name": "COELCE",
                      "ticker": "COCE5",
                      "price": 55.87,
                      "fair_value": 65.47,
                      "upside": 14.66
                  },       
                  {
                      "company_name": "CELESC",
                      "ticker": "CLSC4",
                      "price": 52.28,
                      "fair_value": 94.69,
                      "upside": 44.79
                  },
                  {
                      "company_name": "CEMIG",
                      "ticker": "CMIG3",
                      "price": 16.54,
                      "fair_value": 18.5,
                      "upside": 10.59
                  },
                  {
                      "company_name": "COPEL",
                      "ticker": "CPLE6",
                      "price": 67.93,
                      "fair_value": 152.8,
                      "upside": 55.54
                  }
              ]
          }
      ```

**POST** `/fair-prices/reports`

Gerar uma planilha/relatório com as ações que possuem uma cotação atual menor ou igual ao preço justo calculado.
O arquivo XLSX será gerado dentro do diretório `Desktop`.

- **Exemplos:**

    - Request `/fair-prices/reports`
    - Response
       ```json
          {
              "data": {
                   "created_at": "2021-02-06T10:24:21.638064",
                   "number_of_stocks": 134
              }
          }
       ```