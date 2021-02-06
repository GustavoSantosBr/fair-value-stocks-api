from typing import List

import requests

from src.Domain.DTO.StockDto import StockDto
from src.Domain.Exception.StocksHttpException import StocksHttpException
from src.Infrastructure.CrossCutting.StatusInvestApi.Uri import Uri


class GetAllStocksHttp:

    def __init__(self):
        pass

    def get_all_stocks(self) -> List[StockDto]:
        try:
            response = requests.get(Uri.URI_GET_ALL)
            response_data = response.json()
            stocks = []

            for stock_data in response_data:
                stocks.append(StockDto(stock_data.get("companyName"), stock_data.get("ticker"),
                                       stock_data.get("price"), stock_data.get("vpa"), stock_data.get("lpa")))
            return stocks

        except Exception as e:
            raise StocksHttpException(e.args[0])
