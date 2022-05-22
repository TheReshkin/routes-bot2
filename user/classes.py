from enum import Enum, auto
from datetime import datetime, date, time
import registration.sign


class User:
    routes = []  # будет в базе данных
    # станции, которые искал пользователь (добавить в базу данных)
    station_history = []
    mail = ''
    password = ''

    # на буд. добавь историю станций
    def __init__(self, chat_id, mail, password):
        self.chat_id = chat_id
        self.mail = mail
        self.password = password
        self.token = self.get_token()

    @staticmethod
    def get_token(self):
        # прописать обработчик ошибки
        try:
            token = registration.sign.log_in(self.mail, self.password)
            if token is not None:
                return token
            else:
                token = registration.sign.register(self.mail, self.password)
                if token is not None:
                    return token
                else:
                    raise Exception("There aren't any token. Something wrong with API :(")
        except Exception as exp:
            print("Error", exp)




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
