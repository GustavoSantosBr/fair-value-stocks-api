from src.Infrastructure.CrossCutting.Http.StatusHttp import StatusHttp


class GenerateSpreadsheetException(Exception):

    def __init__(self, message: str):
        self.__message = message
        super().__init__(self.__message)

    @property
    def message(self) -> str:
        return f"Ocorreu um erro ao gerar a planilha de ações. Detalhamento do erro: {self.__message}"

    @property
    def code(self) -> int:
        return StatusHttp.INTERNAL_SERVER_ERROR
