
from flask import Response, request
from flask_restful import Resource

from src.Domain.DTO.StockParametersDto import StockParametersDto
from src.Domain.Exception.StocksHttpException import StocksHttpException
from src.Infrastructure.CrossCutting.Http.StatusHttp import StatusHttp
from src.Infrastructure.CrossCutting.Response.ResponseApi import ResponseApi
from src.Infrastructure.CrossCutting.StatusInvestApi.GetAllStocksHttp import GetAllStocksHttp
from src.Service.CalculateFairValue import CalculateFairValue
from src.Service.FilterStocks import FilterStocks
from src.Service.GetStocks import GetStocks


class GetAllFairValuesHandler(Resource):

    def __init__(self):
        self.__get_stocks = GetStocks(GetAllStocksHttp(), FilterStocks(), CalculateFairValue())

    def get(self) -> Response:
        try:
            stock_parameters = StockParametersDto(request)
            result = self.__get_stocks.get_fair_priced_stocks(stock_parameters)
            return ResponseApi(result, StatusHttp.OK).response()
        except StocksHttpException as e:
            return ResponseApi(e.message, e.code).response()
        except Exception as e:
            return ResponseApi(e.args).response()
