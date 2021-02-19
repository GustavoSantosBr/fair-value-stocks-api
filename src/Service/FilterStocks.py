from typing import List

from src.Domain.DTO.StockDto import StockDto


class FilterStocks:

    def filter_stocks_by_ticker(self, tickers: List[str], stocks: List[StockDto]) -> List[StockDto]:
        filtered_stocks = []

        if len(tickers) == 0:
            return stocks

        for stock in stocks:
            if stock.ticker.upper() in tickers:
                filtered_stocks.append(stock)
        return filtered_stocks
