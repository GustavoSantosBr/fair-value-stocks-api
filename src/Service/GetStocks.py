from typing import List

from src.Domain.DTO.StockFairValueDto import StockFairValueDto
from src.Infrastructure.CrossCutting.StatusInvestApi.GetAllStocksHttp import GetAllStocksHttp
from src.Service.CalculateFairValue import CalculateFairValue


class GetStocks:

    def __init__(self):
        self.__get_all_stocks_http = GetAllStocksHttp()
        self.__calculate_fair_value = CalculateFairValue()

    def get_fair_priced_stocks(self) -> List[StockFairValueDto]:
        all_stocks = self.__get_all_stocks_http.get_all_stocks()
        stocks = []

        for stock in all_stocks:
            price = stock.price

            if price <= 0:
                continue

            fair_value = self.__calculate_fair_value.calculate(stock)

            if fair_value == 0 or fair_value <= price:
                continue

            stocks.append(StockFairValueDto(stock.company_name, stock.ticker, price, fair_value))
        return stocks
