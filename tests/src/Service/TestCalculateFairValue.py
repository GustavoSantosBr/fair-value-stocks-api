import pytest

from src.Domain.DTO.StockDto import StockDto
from src.Service.CalculateFairValue import CalculateFairValue


class TestCalculateFairValue:

    @classmethod
    def setup_class(cls):
        cls.calculate_fair_value = CalculateFairValue()

    @pytest.fixture
    def fair_price_stock(self) -> StockDto:
        return StockDto("ITAUSA", "ITSA4", 10.78, 0.81, 6.47)

    @pytest.fixture
    def stock_without_fair_price(self) -> StockDto:
        return StockDto("ENGIE BRASIL", "EGIE3", 45.12, 2.92, -8.75)

    def test_when_the_calculation_returns_the_fair_value(self, fair_price_stock: StockDto):
        assert self.calculate_fair_value.calculate(fair_price_stock) > 0

    def test_when_the_calculation_does_not_return_the_fair_value(self, stock_without_fair_price: StockDto):
        assert self.calculate_fair_value.calculate(stock_without_fair_price) == 0
