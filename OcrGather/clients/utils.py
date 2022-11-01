import requests


def get_picture(url):
    res = requests.get(url)
    return res.content

