from flask import Response

from src.Application import blueprint_stocks
from src.Application.Handler.GetAllFairValuesHandler import GetAllFairValuesHandler


@blueprint_stocks.route("/fair-prices", methods=["GET"])
def get_fair_prices() -> Response:
    return GetAllFairValuesHandler().get()
