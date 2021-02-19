from typing import List

import requests

from src.Domain.DTO.StockDto import StockDto
from src.Domain.Exception.StocksHttpException import StocksHttpException


class GetAllStocksHttp:
    URI_GET_ALL = "https://statusinvest.com.br/category/advancedsearchresult" \
                  "?search=%7B%0A%20%20%22Sector%22%3A%20%22%22%2C%0A%20" \
                  "%20%22SubSector%22%3A%20%22%22%2C%0A%20%20%22Segment%22%3A%20%22%22%2C%0A%20%20%22" \
                  "my_range%22%3A%20%220%3B25%22%0A%7D%0A&CategoryType=1"

    def get_all_stocks(self) -> List[StockDto]:
        try:
            response = requests.get(self.URI_GET_ALL)
            response_data = response.json()
            stocks = []

            for stock_data in response_data:
                stocks.append(StockDto(stock_data.get("companyName"), stock_data.get("ticker"),
                                       stock_data.get("price"), stock_data.get("vpa"), stock_data.get("lpa")))
            return stocks

        except Exception as e:
            raise StocksHttpException(e.args[0])
