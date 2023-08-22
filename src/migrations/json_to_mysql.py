import json
from utils import add_joke


def get_json():
    with open('dataset/jokes.json', encoding="utf8") as f:
        doc = json.load(f)
        return doc


def json_to_mysql():
    resp = get_json()
    for item in resp:
        category = item.get("type")
        body = f'{item.get("setup")}\n \n{item.get("punchline")}'
        add_joke(category=category, joke=body)