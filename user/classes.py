from enum import Enum, auto
from datetime import datetime, date, time


class User:
    routes = []
    # станции, которые искал пользователь
    station_history = []

    # на буд. добавь историю станций
    def __init__(self, chat_id, user_name):
        self.chat_id = chat_id
        self.token = self.gen_token(chat_id)
        self.user_name = user_name

    @staticmethod
    def gen_token(chat_id):
        # спросить как будет выдаваться токен, запрос к Rest сервису
        return "qwerty123"

    def update_routes(self):
        # добавление изменений в маршрутах, формировать запрос
        pass


class Transport(Enum):
    Avia = auto()
    Train = auto()
    NotSelected = auto()


class Route:
    # флаг для вида транспорта
    r_type = Transport.NotSelected
    f_station = ""
    s_station = ""
    # ГГГГ, ММ, ДД, Часы, Минуты
    r_datetime = datetime(2000, 1, 1, 0, 0)
    code = ""

    # добавить коды станций
    # стоимость добавлять не нужно, будет храниться на другом ресурсе
    def __init__(self, r_type, f_station, s_station, r_date):
        self.r_type = r_type
        self.f_station = f_station
        self.s_station = s_station
        self.r_datetime = r_date

    def gen_r_code(self):
        return
