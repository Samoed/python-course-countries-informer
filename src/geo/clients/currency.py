"""
Функции для взаимодействия с внешним сервисом-провайдером данных о курсах валют.
"""

from app.settings import API_KEY_APILAYER
from base.clients.base import BaseClient


class CurrencyClient(BaseClient):
    """
    Реализация функций для взаимодействия с внешним сервисом-провайдером данных о курсах валют.
    """

    headers = {"apikey": API_KEY_APILAYER}

    def get_base_url(self) -> str:
        return "https://api.apilayer.com/fixer/latest"

    def get_rates(self, base: str = "rub") -> dict | None:
        """
        Получение данных о курсах валют.
        :param base: Базовая валюта
        :return:
        """
        self.params["base"] = base
        return self._request(self.get_base_url())
