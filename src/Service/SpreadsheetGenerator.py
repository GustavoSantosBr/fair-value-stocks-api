from os.path import expanduser

import pandas

from src.Domain.DTO.StockSpreadsheetDto import StockSpreadsheetDto
from src.Domain.Exception.GenerateSpreadsheetException import GenerateSpreadsheetException
from src.Service.GetStocks import GetStocks


class SpreadsheetGenerator:
    COLUMNS = ["Empresa", "Ticker", "Preço atual", "Preço justo", "Upside"]
    FILE_PATH = expanduser(f"~/Desktop/stock_report_with_fair_price.xlsx")

    def __init__(self):
        self.__get_stocks = GetStocks()

    def generate_spreadsheet(self) -> StockSpreadsheetDto:
        try:
            stocks = self.__get_stocks.get_fair_priced_stocks()
            stocks_to_data_frame = []

            for stock in stocks:
                stocks_to_data_frame.append({
                    self.COLUMNS[0]: stock.company_name,
                    self.COLUMNS[1]: stock.ticker,
                    self.COLUMNS[2]: stock.price,
                    self.COLUMNS[3]: stock.fair_value,
                    self.COLUMNS[4]: stock.upside,
                })

            data_frame = pandas.DataFrame(stocks_to_data_frame)
            data_frame.sort_values(by=[self.COLUMNS[0], self.COLUMNS[1]]).to_excel(self.FILE_PATH)
            return StockSpreadsheetDto(len(stocks_to_data_frame))
        except Exception as e:
            raise GenerateSpreadsheetException(e.args[0])
