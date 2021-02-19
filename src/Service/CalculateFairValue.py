import math
from typing import List

from src.Domain.DTO.StockDto import StockDto
from src.Domain.DTO.StockFairValueDto import StockFairValueDto


class CalculateFairValue:
    ZERO = 0.0

    def calculate(self, stock: StockDto) -> float:
        """
        :param stock: Receives an stock.
        :return: Returns the fair value of the stock

        The calculation is done using Benjamin Graham's formula: VI = √ 22.5 * LPA * VPA
        """
        lpa = stock.lpa
        vpa = stock.vpa

        if lpa <= self.ZERO or vpa <= self.ZERO:
            return self.ZERO
        return math.sqrt(22.5 * lpa * vpa)

    def get_stocks_with_fair_value(self, stocks: List[StockDto]) -> List[StockFairValueDto]:
        """
        :param stocks: Receives a list of stocks.
        :return: Returns a list of stocks that have fair value.
        """
        stocks_with_fair_value = []

        for stock in stocks:
            price = stock.price

            if price <= self.ZERO:
                continue

            fair_value = self.calculate(stock)

            if fair_value == self.ZERO or fair_value <= price:
                continue

            stocks_with_fair_value.append(StockFairValueDto(stock.company_name, stock.ticker, price, fair_value))
        return stocks_with_fair_value
