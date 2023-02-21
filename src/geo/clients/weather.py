"""
Функции для взаимодействия с внешним сервисом-провайдером данных о погоде.
"""
from typing import Optional

from app.settings import API_KEY_OPENWEATHER
from base.clients.base import BaseClient
from geo.clients.schemas import WeatherInfoDTO


class WeatherClient(BaseClient):
    """
    Реализация функций для взаимодействия с внешним сервисом-провайдером данных о погоде.
    """

    def get_base_url(self) -> str:
        return "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, location: str) -> Optional[WeatherInfoDTO]:
        """
        Получение данных о погоде.

        :param location: Город и страна
        :return:
        """
        data = self._request(
            f"{self.get_base_url()}?units=metric&q={location}&appid={API_KEY_OPENWEATHER}"
        )
        return WeatherInfoDTO(
            temp=data["main"]["temp"],
            pressure=data["main"]["pressure"],
            humidity=data["main"]["humidity"],
            wind_speed=data["wind"]["speed"],
            description=data["weather"][0]["description"],
            visibility=data["visibility"],
            dt=data["dt"],
            timezone=data["timezone"] // 3600,
        ) if data else None
