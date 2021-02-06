import math

from src.Domain.DTO.StockDto import StockDto


class CalculateFairValue:
    ZERO = 0.0

    def __init__(self):
        pass

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
