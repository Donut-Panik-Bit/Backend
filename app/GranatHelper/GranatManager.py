from fastapi import WebSocket

hellos_exml = [
    "Привет", "Здравствуйте",
    "Добрый день", "Добрый вечер",
    "Здарова", "Приветствую",
    "День добрый", "Вечер добрый",
    "Привет", "Ку", "Хей"
]


class GranatManager:
    def __init__(self) -> None:
        pass

    def handle(msg: str) -> None:
        msg = msg.capitalize()
        if msg in hellos_exml:
            return "Привет, меня зовут Гранат!"
        else:
            return "Извини, я ничего не понял. Попробуй еще раз"