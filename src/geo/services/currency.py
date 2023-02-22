from typing import Optional

from django.db.models import Q

from geo.clients.currency import CurrencyClient
from geo.clients.schemas import CountryDTO, CurrencyRatesDTO
from geo.models import Currency, CurrencyRates


class CurrencyService:
    """
    Сервис для работы с данными о валютах.
    """

    def get_currency(self, currency_base: str) -> Optional[CurrencyRates]:
        """
        Получение валюты по названию.


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
        """
        Формирование объекта модели значения отношений валют.

        :param Currency currency: Валюта
        :param str name: называние валюты
        :param float rate: отношение валют
        :return:
        """
        return CurrencyRates(
            currency=currency,
            currency_name=name,
            rate=rate,
        )

    def build_model(self, currency: CurrencyRatesDTO) -> Currency:
        """
        Формирование объекта модели валюты.

        :param CurrencyRatesDTO currency: Данные о валюте.
        :return:
        """

        return Currency(
            base=currency.base,
            date=currency.date,
        )
