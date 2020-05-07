from urllib.parse import urljoin

import requests
from django.conf import settings

from ..constants.finance_constants import FINANCE_SERVICE_URL, FINANCE_STOCK_PRICE_ENDPOINT, \
    FINANCE_CURRENCY_CONVERTER_ENDPOINT


# actual communication towards finance api category service
def get_stock_price_for_company(company_symbol):
    """
    :param String company_symbol: target name of company
    """
    url = f"{FINANCE_SERVICE_URL}{FINANCE_STOCK_PRICE_ENDPOINT}"

    post_data = {
        'company_symbol': company_symbol,
        'region': 'US'  # default US, might think of another way to get this information
    }

    auth_token = {'token': settings.CATEGORY_API_AUTH_TOKEN}

    try:
        response = requests.post(url=url, json=post_data, params=auth_token)
    except Exception:
        response = False

    # create response object based on returned status code
    if response and response.ok:
        response_obj = response.json()
    else:
        response_obj = {'stock_price': 'error occurred calling Finance API'}

    return response_obj.get('stock_price')


def currency_converter(**kwargs):
    url = f"{FINANCE_SERVICE_URL}{FINANCE_CURRENCY_CONVERTER_ENDPOINT}"
    auth_token = {'token': settings.CATEGORY_API_AUTH_TOKEN}
    response = requests.post(url=url, json=kwargs, params=auth_token)
    return response.json().get("converted_value")
