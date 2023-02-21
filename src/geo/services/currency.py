from typing import Optional

from django.db.models import Q

from geo.clients.currency import CurrencyClient
from geo.clients.schemas import CountryDTO, CurrencyRatesDTO
from geo.models import Currency, CurrencyRates


# todo change comments
class CurrencyService:
    """
    Сервис для работы с данными о погоде.
    """

    def get_currency(self, currency_base: str) -> Optional[CurrencyRates]:
        """
        Получение списка стран по названию.


        :type currency_base: название валюты
        :return:
        """

        currency_rates = CurrencyRates.objects.filter(
                Q(currency__base__contains=currency_base)
            )
        if not currency_rates:
            if currency_data := CurrencyClient().get_rates(currency_base):
                currency = self.build_model(currency_data)
                Currency.objects.bulk_create(currency)
                currency_rates = CurrencyRates.objects.bulk_create(
                    [self.build_model_rates(currency, name, rate) for name, rate in currency_data.rates],
                    batch_size=1000
                )
        return currency_rates

    def build_model_rates(self, currency: Currency, name: str, rate: float) -> CurrencyRates:
        return CurrencyRates(
            currency=currency,
            currency_name=name,
            rate=rate,
        )

    def build_model(self, country: CurrencyRatesDTO) -> Currency:
        """
        Формирование объекта модели страны.

        :param CountryDTO country: Данные о стране.
        :return:
        """

        return Currency(
            base=country.base,
            date=country.date,
        )
