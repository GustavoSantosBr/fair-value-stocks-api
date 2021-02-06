from flask import Response
from flask_restful import Resource

from src.Domain.Exception.StocksHttpException import StocksHttpException
from src.Infrastructure.CrossCutting.Http.StatusHttp import StatusHttp
from src.Infrastructure.CrossCutting.Response.ResponseApi import ResponseApi
from src.Service.GetStocks import GetStocks


class GetAllFairValuesHandler(Resource):

    def __init__(self):
        self.__get_stocks = GetStocks()

    def get(self) -> Response:
        try:
            result = self.__get_stocks.get_fair_priced_stocks()
            return ResponseApi(result, StatusHttp.OK).response()
        except StocksHttpException as e:
            return ResponseApi(e.message, e.code).response()
        except Exception as e:
            return ResponseApi(e.args).response()
