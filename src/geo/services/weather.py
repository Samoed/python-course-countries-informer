from typing import Optional

from django.db.models import Q

from geo.clients.schemas import CountryDTO, WeatherInfoDTO
from geo.clients.weather import WeatherClient
from geo.models import City, Country, Weather


class WeatherService:
    """
    Сервис для работы с данными о погоде.
    """

    def get_weather(self, alpha2code: str, city: str) -> Optional[dict]:
        """
        Получение погоды по стране и городу.

        :param alpha2code: ISO Alpha2 код страны
        :param city: Город
        :return:
        """

        weather = Weather.objects.filter(
            Q(city__name__contains=city) | Q(city__country__alpha2code__contains=alpha2code)
        )
        if not weather:
            if weather_data := WeatherClient().get_weather(f"{city},{alpha2code}"):
                weather = Weather.objects.create(
                    self.build_model(weather_data, city, alpha2code)
                )

        return weather

    def build_model(self, weather: WeatherInfoDTO, city_name: str, alpha2code: str) -> Weather:
        """
        Формирование объекта модели погоды.


        :param WeatherInfoDTO weather: Данные о погоде.
        :param str city_name: Город
        :param str alpha2code: ISO Alpha2 код страны
        :return:
        """
        city = City.objects.filter(
            Q(name__contains=city_name) | Q(country__alpha2code__contains=alpha2code)
        )
        return Weather(
            city=city,
            temp=weather.temp,
            pressure=weather.pressure,
            humidity=weather.humidity,
            wind_speed=weather.wind_speed,
            description=weather.description,
            visibility=weather.visibility,
            dt=weather.dt,
            timezone=weather.timezone,
        )
