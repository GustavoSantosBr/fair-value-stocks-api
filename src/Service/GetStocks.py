from typing import List

from src.Domain.DTO.StockFairValueDto import StockFairValueDto
from src.Domain.DTO.StockParametersDto import StockParametersDto
from src.Infrastructure.CrossCutting.StatusInvestApi.GetAllStocksHttp import GetAllStocksHttp
from src.Service.CalculateFairValue import CalculateFairValue
from src.Service.FilterStocks import FilterStocks


class GetStocks:

    def __init__(self, get_all_stocks_http: GetAllStocksHttp, filter_stocks: FilterStocks,
                 calculate_fair_value: CalculateFairValue):
        self.__get_all_stocks_http = get_all_stocks_http
        self.__filter_stocks = filter_stocks
        self.__calculate_fair_value = calculate_fair_value

    def get_fair_priced_stocks(self, stock_parameters: StockParametersDto) -> List[StockFairValueDto]:
        all_stocks = self.__get_all_stocks_http.get_all_stocks()
        all_stocks = self.__filter_stocks.filter_stocks_by_ticker(stock_parameters.tickers, all_stocks)
        return self.__calculate_fair_value.get_stocks_with_fair_value(all_stocks)
