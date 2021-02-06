from flask import Response
from flask_restful import Resource

from src.Domain.Exception.GenerateSpreadsheetException import GenerateSpreadsheetException
from src.Domain.Exception.StocksHttpException import StocksHttpException
from src.Infrastructure.CrossCutting.Http.StatusHttp import StatusHttp
from src.Infrastructure.CrossCutting.Response.ResponseApi import ResponseApi
from src.Service.SpreadsheetGenerator import SpreadsheetGenerator


class PostStocksSpreadsheet(Resource):

    def __init__(self):
        self.__spreadsheet_generator = SpreadsheetGenerator()

    def post(self) -> Response:
        try:
            result = self.__spreadsheet_generator.generate_spreadsheet()
            return ResponseApi(result, StatusHttp.CREATED).response()
        except StocksHttpException as e:
            return ResponseApi(e.message, e.code).response()
        except GenerateSpreadsheetException as e:
            return ResponseApi(e.message, e.code).response()
        except Exception as e:
            return ResponseApi(e.args).response()
