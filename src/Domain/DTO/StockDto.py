class StockDto:
    ZERO = 0.0

    def __init__(self, company_name: str, ticker: str, price: float or None, lpa: float or None, vpa: float or None):
        self.__company_name = company_name
        self.__ticker = ticker
        self.__price = price
        self.__lpa = lpa
        self.__vpa = vpa

    @property
    def company_name(self):
        return self.__company_name.strip()

    @property
    def ticker(self):
        return self.__ticker.strip()

    @property
    def price(self):
        price = self.__price

        if price is None:
            return self.ZERO
        return price

    @property
    def lpa(self):
        lpa = self.__lpa

        if lpa is None:
            return self.ZERO
        return lpa

    @property
    def vpa(self):
        vpa = self.__vpa

        if vpa is None:
            return self.ZERO
        return vpa
