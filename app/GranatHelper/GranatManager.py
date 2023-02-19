#from fastapi import WebSocket
import json

from fuzzywuzzy import fuzz


СOMMANDS = []


with open('rules.json', 'r') as f:
    СOMMANDS = json.load(f)


class GranatManager:
    def __init__(self) -> None:
        pass

    def handle(string: str) -> None:

        q = string.replace(',','').replace('.','')\
        .replace('?','').replace("!",'')\
            .lower().strip()

        for command in СOMMANDS:

            rez = fuzz.partial_ratio(command['title'].lower(), q)
            if rez >= 80:
                return command['result']
    
        return "Похоже, что мне ничего не удалось найти :("