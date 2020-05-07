import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


# This variable holds all category API services as an endpoint
available_functions_endpoint = f"{settings.SERVICE_PROVIDER_URL}/manage_functions/"


def scan_category_service():
    auth_token = {'token': settings.CATEGORY_API_AUTH_TOKEN}

    # scan every category services endpoint
    response = requests.get(url=available_functions_endpoint, params=auth_token)

    # if response is ok return the json
    if response and response.ok:
        return response.json()

    return {}
