from typing import Optional

from geo.clients.currency import CurrencyClient
from geo.clients.schemas import CountryDTO, CurrencyRatesDTO
from geo.models import Country


# todo change comments
class CurrencyService:
    """
    Сервис для работы с данными о погоде.
    """

    def get_currency(self, currency_base: str) -> Optional[dict]:
        """
        Получение списка стран по названию.


        :type currency_base: название валюты
        :return:
        """

        if data := CurrencyClient().get_rates(currency_base):
            return data

        return None

    def build_model(self, country: CountryDTO) -> Country:
        """
        Формирование объекта модели страны.

        :param CountryDTO country: Данные о стране.
        :return:
        """

        return Country(
            alpha3code=country.alpha3code,
            name=country.name,
            alpha2code=country.alpha2code,
            capital=country.capital,
            region=country.region,
            subregion=country.subregion,
            population=country.population,
            latitude=country.latitude,
            longitude=country.longitude,
            demonym=country.demonym,
            area=country.area,
            numeric_code=country.numeric_code,
            flag=country.flag,
            currencies=[currency.code for currency in country.currencies],
            languages=[language.name for language in country.languages],
        )
