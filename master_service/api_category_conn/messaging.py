# importing the requests library
from urllib.parse import urljoin

import requests
from django.conf import settings

from ..constants.messaging_constants import MESSAGING_SERVICE_URL, MESSAGING_EMAIL_ENDPOINT, MESSAGING_DISCORD_ENDPOINT


# Add communication to messaging api category service
def send_email(recipient, subject, content):
    """
    :param String recipient: recipient of the email
    :param String subject: subject of the email
    :param String content: content of the email
    """
    url = f"{MESSAGING_SERVICE_URL}{MESSAGING_EMAIL_ENDPOINT}"

    post_data = {
        'recipient': recipient,
        'subject': subject,
        'content': content
    }
    auth_token = {'token': settings.CATEGORY_API_AUTH_TOKEN}

    response = requests.post(url=url, json=post_data, params=auth_token)


def send_discord_message(**kwargs):
    """
    :param String username: name of the bot
    :param String content: content of the message
    """
    url = f"{MESSAGING_SERVICE_URL}{MESSAGING_DISCORD_ENDPOINT}"
    auth_token = {'token': settings.CATEGORY_API_AUTH_TOKEN}
    response = requests.post(url=url, json=kwargs, params=auth_token)
