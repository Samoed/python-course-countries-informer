"""
Функции для взаимодействия с внешним сервисом-провайдером данных о погоде.
"""
from typing import Optional

from app.settings import API_KEY_OPENWEATHER
from base.clients.base import BaseClient


class WeatherClient(BaseClient):
    """
    Реализация функций для взаимодействия с внешним сервисом-провайдером данных о погоде.
    """

    def get_base_url(self) -> str:
        return "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, location: str) -> Optional[dict]:
        """
        Получение данных о погоде.

        :param location: Город и страна
        :return:
        """

        return self._request(
            f"{self.get_base_url()}?units=metric&q={location}&appid={API_KEY_OPENWEATHER}"
        )
