class StockFairValueDto:

    def __init__(self, company_name: str, ticker: str, price: float, fair_value: float):
        self.company_name = company_name
        self.ticker = ticker
        self.price = round(price, 2)
        self.fair_value = round(fair_value, 2)
        self.upside = round(self.__upside(), 2)

    def __upside(self) -> float:
        return ((self.fair_value - self.price) / self.fair_value) * 100
