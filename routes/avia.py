import requests


# установить библиотеку для поиска аэропортов по ИАТО
# import airportsdata

def avia_search(f_station, s_station, date):
    print("Avia")
    return edit_answer()


def avia_search(inline_query, num=5):
    print("Avia")
    return edit_answer_query(num)


def edit_answer_query(num):
    f_station = "Москва"
    s_station = "Санкт-Петербург"
    t_num = "1"
    # departure
    dep_date = "01.01.2022"
    dep_time = "09:00"
    # arrival
    arr_date = "01.01.2022"
    arr_time = "14:00"
    travel_time = "7:00"
    company = "Победа"
    link = "aviasales.ru"
    num_seats = "10"
    min_price = "2400"

    if num > 0:
        answer = f"""🛫 {num}
        {f_station}➡️{s_station}
        🕐 Отправление: {dep_time}  {dep_date}
        🕗 Прибытие: {arr_time}  {arr_date}
        ⏰ Время в пути: {travel_time}
        {num_seats} мест от {min_price} ₽
        Перевозчик: {company}
        Ссылка: {link}""" + \
                 "\n" + \
                 edit_answer_query(num - 1) if num > 0 else """ """
    else:
        return ""
    return answer


def edit_answer():
    f_station = "Москва1"
    s_station = "Санкт-Петербург"
    t_num = "1"
    # departure
    dep_date = "01.01.2022"
    dep_time = "09:00"
    # arrival
    arr_date = "01.01.2022"
    arr_time = "14:00"
    travel_time = "7:00"
    company = "Победа"
    link = "aviasales.ru"
    num_seats = "10"
    min_price = "2400"

    answer = f"""🛫 {1}
    {f_station}➡️{s_station}
    🕐 Отправление: {dep_time}  {dep_date}
    🕗 Прибытие: {arr_time}  {arr_date}
    ⏰ Время в пути: {travel_time}
    {num_seats} мест от {min_price} ₽
    Перевозчик: {company}
    Ссылка: {link}"""

    return answer


def get_route(dep_code, arrival_code, dep_date, service_class, adult=1, child=0, infant=0, count=5):
    import requests

    url = "https://best-routes.herokuapp.com//routes/avia?departureCode=MOW&arrivalCode=LED&departureDate=2022-04-27&adult=1&child=0&infant=0&serviceClass=Y&count=-1"

    payload = {}
    headers = {
        'Token': '1:HzvFemBUQt56BVuGwJKAeJMktshMsNcCahy7fjVT97Oam7hT8LeNrTci8K0tzt1T6J0kyCuPVGZVqLjPqudQ4a78tnfOK3e16klB'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
