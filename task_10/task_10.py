# 1. Явно объявляйте все переменные
# 2. Инициализируйте каждую переменную, и делайте это правильно
# Было:
class OniPlayer:
    def __init__(self):
        self.is_open = False
        self.is_streaming = False
        self.is_play = False
        self.num_depth_frames = 0
        self.num_color_frames = 0


# Стало:

class Player:
    def __init__(self):
        self.is_open: bool = False
        self.is_streaming: bool = False
        self.is_play: bool = False
        self.num_depth_frames: int = 0
        self.num_color_frames: int = 0


# Было:
import requests


def _get_response(url, headers, params=None):
    response = requests.get(url, params=params, headers=headers)
    return response.text


# Стало
def _get_response(url: str, headers: dict, params: dict = None) -> str:
    response = requests.get(url, params=params, headers=headers)
    return response.text

# 3. Завершение работы с переменными
# Всегда присваиваю недопустимые значения (None) переменным по завершению логического блока.

# 4. Переменные и циклы
# Всегда инициализирую переменные непосредственно перед телом цикла.
