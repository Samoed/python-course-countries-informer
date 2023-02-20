"""Представления Django"""
import re
from typing import Any

from django.core.cache import caches
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.request import Request

from app.settings import CACHE_WEATHER
from geo.serializers import CountrySerializer, CitySerializer
from geo.services import city
from geo.services.city import CityService
from geo.services.country import CountryService
from geo.services.currency import CurrencyService
from geo.services.schemas import CountryCityDTO
from geo.services.weather import WeatherService
from news.serializers import NewsSerializer
from news.services.news import NewsService


@api_view(["GET"])
def get_news(request: Request, name: str) -> JsonResponse:
    """
    Получить информацию о городах по названию.

    Сначала метод ищет данные в БД. Если данные не найдены, то делается запрос к API.
    После получения данных от API они сохраняются в БД.

    :param Request request: Объект запроса
    :param str name: Название города
    :return:
    """

    cache_key = f"{name}_news"
    data = caches[CACHE_WEATHER].get(cache_key)
    if not data:
        if data := NewsService().get_news(name):
            caches[CACHE_WEATHER].set(cache_key, data)

    if data:
        serializer = NewsSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    raise NotFound
