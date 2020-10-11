import os
import random
import string

import click
import pyperclip
import requests

MONZO_AUTH_API = os.environ["MONZO_AUTH_API"]
MONZO_CLIENT_ID = os.environ["MONZO_CLIENT_ID"]
MONZO_CLIENT_SECRET = os.environ["MONZO_CLIENT_SECRET"]
MONZO_APP_REDIRECT_AUTH_URI = "http://localhost/"
MONZO_APP_REDIRECT_START_URI = "http://localhost/"


def get_random_string(*, length):
    letters = string.ascii_lowercase
    random_str = "".join(random.choice(letters) for i in range(length))
    return random_str


def get_authorization_code(url: str) -> str:
    if not url.startswith(MONZO_APP_REDIRECT_AUTH_URI):
        raise ValueError(
            f"The provided URL doesn't start with {MONZO_APP_REDIRECT_AUTH_URI}"
        )

    params = {
        key: value
        for key, value in [param.split("=") for param in url.split("?")[1].split("&")]
    }

    if authorization_code := params.get("code"):
        return authorization_code

    raise KeyError("Provided URL must have a 'code' parameter")


@click.command(name="refresh-token")
def refresh_token_command():
    # https://docs.monzo.com/#acquire-an-access-token

    # Redirect the user to Monzo
    request = requests.Request(
        "GET",
        url=f"{MONZO_AUTH_API}",
        params={
            "client_id": MONZO_CLIENT_ID,
            # This redirect URL needs to be in the added to the client
            # login into https://developers.monzo.com/ and go to Clients
            "redirect_uri": MONZO_APP_REDIRECT_AUTH_URI,
            "response_type": "code",
            "state": get_random_string(length=8),
        },
    ).prepare()
    print("Navigate in your browser to:", request.url, sep="\n")
    pyperclip.copy(request.url)
    print("URL above copied to the clipboard!")

    _ = input("Press enter to copy user email to clipboard")
    pyperclip.copy("david.torralba.goitia@gmail.com")
    print("done!")

    # from urllib.request import urlopen

    # web_url = urlopen(request.url)
    # breakpoint()

    print("Follow the steps to log in.")
    print("")
    print("Get the URL and paste it here:")
    url = input("and paste it here:").strip()
    authorization_code = get_authorization_code(url=url)

    print("")
    print("Authorization code found:", authorization_code, sep="\n")
    print("")

    # Exchange the authorization code
    response = requests.post(
        # url=f"{MONZO_API}/oauth2/token",
        url="https://api.monzo.com/oauth2/token",
        params={
            "grant_type": "authorization_code",
            "client_id": MONZO_CLIENT_ID,
            "client_secret": MONZO_CLIENT_SECRET,
            "redirect_uri": MONZO_APP_REDIRECT_START_URI,
            "code": authorization_code,
        },
    )

    if not response.ok:
        breakpoint()

    print("Refresh token:", response.json()["refresh_token"], sep="\n")
