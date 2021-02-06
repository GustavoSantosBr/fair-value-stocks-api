from datetime import datetime


class StockSpreadsheetDto:

    def __init__(self, number_of_stocks: int):
        self.created_at = datetime.now().isoformat()
        self.number_of_stocks = number_of_stocks
