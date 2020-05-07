import requests


def get_random_joke():
    response = requests.get("https://official-joke-api.appspot.com/jokes/programming/random")
    joke = response.json()[0]
    return f"{joke['setup']} {joke['punchline']}"
