from fuzzywuzzy import fuzz
import json

СOMMANDS = []


with open('rules.json', 'r') as f:
    СOMMANDS = json.load(f)


def hear(string: str) -> str:

    q = string.replace(',','').replace('.','')\
        .replace('?','').replace("!",'')\
            .lower().strip()

    for command in СOMMANDS:

        rez = fuzz.partial_ratio(command['title'].lower(), q)
        if rez >= 80: return command['result']
    
    return "Похоже, что мне ничего не удалось найти :("
