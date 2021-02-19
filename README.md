# Fair Value Stocks API

[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/GustavoSantosBr/)
[![Minimum Python Version](https://img.shields.io/badge/python-%5E3.9.1-blue)](https://www.python.org)

* [Introdução](#Introdução)
    * [Preço](#Preço)
    * [Margem](#Margem)
    * [Observações](#Observações)
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
- **Isso não é uma recomendação de compra ou venda**.

## Instalação

- Abra seu terminal, navegue até o diretório de sua preferência, e em seguida execute:
  ```bash
  > git clone https://github.com/GustavoSantosBr/fair-value-stocks-api.git
  ```

- Navegue até a pasta do projeto utilizando:
  ```bash
  > cd {seudiretorio}
  ```

- Em seguida, execute o comando abaixo para dar início ao contêiner do projeto:
  ```bash
  > docker-compose up -d
  ```

- Se necessário entrar no bash do contêiner, execute:
  ```bash
  > docker exec -it stocks_api bash
  ```

## Endpoints

**GET** `/stocks/fair-prices`

Busca as ações que possuem uma cotação atual menor ou igual ao preço justo calculado.

- **Exemplos:**

    - Request `/stocks/fair-prices?tickers=ITSA4&tickers=MDIA3&tickers=CPLE6`
      
       |  Propriedade  |    Obrigatório    |  Descrição                    |
       |     :---      |       :---        |  :---                         |
       |  `tickers`    |        Não        |  Uma lista/array de tickers   |

    - Response
       ```json
          {
              "data": [
                  {
                      "company_name": "COPEL",
                      "ticker": "CPLE6",
                      "price": 63.26,
                      "fair_value": 152.8,
                      "upside": 58.6
                  },
                  {
                      "company_name": "ITAUSA",
                      "ticker": "ITSA4",
                      "price": 10.25,
                      "fair_value": 10.89,
                      "upside": 5.88
                  },
                  {
                      "company_name": "M.DIAS BRANCO",
                      "ticker": "MDIA3",
                      "price": 30.69,
                      "fair_value": 32.3,
                      "upside": 4.98
                  }
              ]
          }
       ```
  
    - Response (quando não houver ações com preço justo)
       ```json
          {
              "data": []
          }
       ```
       
       |  Propriedade      |       Tipo        |  Descrição                   |
       |     :---          |       :---        |  :---                        |
       |  `company_name`   |        texto      |  Nome da empresa             |
       |  `ticker`         |        texto      |  Ticker da ação              |
       |  `price`          |        numérico   |  Preço atual da cotação      |
       |  `fair_value`     |        numérico   |  Preço justo                 |
       |  `upside`         |        numérico   |  Potencial de alta do ativo  |

      
    