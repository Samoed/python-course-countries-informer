"""Представления Django"""

from django.core.cache import caches
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.request import Request

from app.settings import CACHE_WEATHER
from news.serializers import NewsSerializer
from news.services.news import NewsService


@api_view(["GET"])
def get_news(request: Request, alpha2code: str) -> JsonResponse:
    """
    Получение новостной ленты для указанной страны.


    :param Request request: Объект запроса
    :param str alpha2code: Название страны
    :return:
    """

    cache_key = f"{alpha2code}_news"
    data = caches[CACHE_WEATHER].get(cache_key)
    if not data:
        if data := NewsService().get_news(alpha2code):
            caches[CACHE_WEATHER].set(cache_key, data)

    if data:
        serializer = NewsSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    raise NotFound
