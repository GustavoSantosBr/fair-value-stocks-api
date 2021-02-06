from flask_restful import Api

from src.Application.Handler.GetAllFairValuesHandler import GetAllFairValuesHandler
from src.Application.Handler.PostStocksSpreadsheet import PostStocksSpreadsheet


def add_routes(application: Api):
    application.add_resource(GetAllFairValuesHandler, "/fair-prices")
    application.add_resource(PostStocksSpreadsheet, "/fair-prices/reports")
