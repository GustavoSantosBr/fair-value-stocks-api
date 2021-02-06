import jsonpickle
from flask import make_response, jsonify, Response

from src.Infrastructure.CrossCutting.Http.StatusHttp import StatusHttp


class ResponseApi:
    MIME_TYPE = "application/json"

    def __init__(self, data, status_code: int or None = None):
        self.__data = data
        self.__status_code = status_code

    def response(self) -> Response:
        if self.__status_code is None:
            self.__status_code = StatusHttp.INTERNAL_SERVER_ERROR

        if (self.__status_code >= StatusHttp.OK) and (self.__status_code <= StatusHttp.IM_USED):
            data = make_response(jsonpickle.encode({"data": self.__data}, unpicklable=False), self.__status_code)
            data.mimetype = self.MIME_TYPE
            return data
        return make_response(jsonify(self.__format_error()), self.__status_code)

    def __format_error(self):
        label_errors = "errors"
        message = "message"

        if not isinstance(self.__data, list):
            return {label_errors: [{message: self.__data}]}

        errors = []

        for error in self.__data:
            errors.append({message: error})
        return {label_errors: errors}
