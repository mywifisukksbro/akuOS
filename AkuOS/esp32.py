import requests
from config import ESP32_IP


def command(path):

    try:

        requests.get(f"http://{ESP32_IP}/{path}", timeout=2)

    except:

        print("Aku body offline.")


def happy():

    command("happy")


def alert():

    command("alert")


def sleep():

    command("sleep")


def light_on():

    command("light/on")


def light_off():

    command("light/off")


def normal():

    command("normal")