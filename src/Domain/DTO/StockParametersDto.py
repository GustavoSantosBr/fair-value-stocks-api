from flask import Request


class StockParametersDto:

    def __init__(self, request: Request):
        request_data = request.args
        self.__tickers = request_data.getlist("tickers")

    @property
    def tickers(self) -> list:
        if self.__tickers is None:
            return []
        return self.__tickers
