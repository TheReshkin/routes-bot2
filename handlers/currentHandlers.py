from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler, CallbackQueryHandler
from telegram.ext import CommandHandler, MessageHandler, Filters
# from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
import telegram_bot_calendar

import menu_buttons
import registration.sign
import routes.avia


# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.
def echo(update, context):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    update.message.reply_text(update.message.text)


# Напишем соответствующие функции.
# Их сигнатура и поведение аналогичны обработчикам текстовых сообщений.
def start(update, context):
    update.message.reply_text(
        "Привет! Я бот для поиска и отслеживания Авиа билетов",
        reply_markup=ReplyKeyboardRemove())
    # keyboard = [
    #     [
    #         InlineKeyboardButton("Option 1", callback_data='1'),
    #         InlineKeyboardButton("Option 2", callback_data='2'),
    #     ],
    #     [InlineKeyboardButton("Option 3", callback_data='3')],
    # ]
    #
    # reply_markup = InlineKeyboardMarkup(keyboard)
    # update.message.reply_text("Text2", reply_markup=reply_markup)
    print("_старт")


def button(update, context):
    # CallbackQueries need to be answered, even if no notification to the user is needed
    try:
        update.callback_query.answer()
        update.callback_query.edit_message_text(text=f"Выбранный транспорт: {update.callback_query.data}")
        print(update.callback_query.data)
        if update.callback_query.data == 'Avia':
            print('_выбран самолет')
            return 1
        elif update.callback_query.data == 'Train':
            return 1
        else:
            update.message.reply_text(
                text="Такого транспорта я не знаю \nВыберите транспорт в сообщении",
            )
            search(update, context)
    except Exception:
        print("_error")
        update.message.reply_text(
            text="Что-то пошло не так \nЯ могу искать только авиамаршруты",
        )


def menu(update, context):
    text = update.message.text
    print(text)
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                menu_buttons.menu,
                menu_buttons.search
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text="Что нужно сделать",
        reply_markup=reply_markup,
    )


def back(update, context):
    update.message.reply_text(
        text="Возвращаюсь назад",
    )

    try:
        update.message.reply_text(
            reply_markup=ReplyKeyboardRemove()
        )
    except TypeError:
        print("_ошибка типов, клавиатуры не было")


async def one_way(update, context):
    print("_one_way")
    update.message.reply_text(
        text="Куда летим?"
    )
    first_station = update.message.text
    print("_Место отправления", first_station)
    return 2


def another_way(update, context):
    update.message.reply_text(
        text="Когда летим?"
    )
    calendar_d = telegram_bot_calendar.create_calendar()
    update.message.reply_text("Please select a date: ",
                              reply_markup=calendar_d)

    second_station = update.message.text
    print("_Место назначения", second_station)

    return ConversationHandler.END


def search(update, context):
    update.message.reply_text("Откуда полетим?")
    return 1


conv_handler = ConversationHandler(
    entry_points=[CommandHandler("search", search)],
    states={
        # Функция читает ответ на первый вопрос и задаёт второй.
        1: [MessageHandler(Filters.text, one_way)],
        # Функция читает ответ на второй вопрос и завершает диалог.
        2: [MessageHandler(Filters.text, another_way)],
        3: [MessageHandler(Filters.entity(menu_buttons.back), back)],

    },

    # Точка прерывания диалога. В данном случае — команда /stop.
    # fallbacks=[MessageHandler(Filters.regex('назад'), back)]
    fallbacks=[CommandHandler("back", back)]
)


def reg(update, context):
    mail = "resh@grail.com"
    password = "resh1"
    registration.sign.register(mail, password, update.message.from_user.id)


def auth(update, context):
    mail = "resh@grail.com"
    password = "resh1"
    registration.sign.log_in(mail, password, update.message.from_user.id)


def search_raw(update, context):
    print("_search_raw")
    update.message.reply_text(text=routes.avia.get_route("MOW", "LED", "2022-05-25", "Y"))
