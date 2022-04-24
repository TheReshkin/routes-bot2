from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler, CallbackQueryHandler
from telegram.ext import CommandHandler, MessageHandler, Filters

import menu_buttons


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
        "Привет! Я бот для поиска и отслеживания ЖД и Авиа билетов",
        reply_markup=ReplyKeyboardRemove())
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2'),
        ],
        [InlineKeyboardButton("Option 3", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Text2", reply_markup=reply_markup)
    print(update.message.reply_text)


def button(update, context):
    # CallbackQueries need to be answered, even if no notification to the user is needed
    update.callback_query.answer()
    update.callback_query.edit_message_text(text=f"Выбранная кнопка: {update.callback_query.data}")


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
    try:
        update.message.reply_text(
            reply_markup=ReplyKeyboardRemove()
        )
    except TypeError:
        print("ошибка типов")


def one_way(update, context):
    transport = update.message.text
    if transport == menu_buttons.train:
        update.message.reply_text(
            text="Откуда едем?",
            reply_markup=ReplyKeyboardRemove()
        )
    elif transport == menu_buttons.plane:
        update.message.reply_text(
            text="Откуда летим?",
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        update.message.reply_text(
            text="Такого транспорта я не знаю \nВыберите транспорт на клавиатуре",
        )
        one_way()
    first_station = update.message.text
    print("Место отправления", first_station)
    return 2


def another_way(update, context):
    update.message.reply_text(
        text="Куда едем?"
    )
    second_station = update.message.text
    print("место назначения", second_station)

    return ConversationHandler.END


def search(update, context):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=menu_buttons.plane),
                KeyboardButton(text=menu_buttons.train)
            ],
            [
                KeyboardButton(text=menu_buttons.back)
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    update.message.reply_text(
        text="На поезде или самолетом?",
        reply_markup=reply_markup
    )
    user_text = update.message
    print(user_text)
    if user_text == menu_buttons.plane:
        return 1
    elif user_text == menu_buttons.train:
        return 1
    elif user_text == menu_buttons.back:
        return 3
    else:
        update.message.reply_text(
            text="Такого транспорта я не знаю \nВыберите транспорт на клавиатуре",
            reply_markup=reply_markup
        )


conv_handler = ConversationHandler(
    entry_points=[CommandHandler("search", search)],
    states={
        # Функция читает ответ на первый вопрос и задаёт второй.
        1: [MessageHandler(Filters.text, one_way)],
        # Функция читает ответ на второй вопрос и завершает диалог.
        2: [MessageHandler(Filters.text, another_way)],
        3: [MessageHandler(Filters.entity(menu_buttons.back), back)],
        4: [CallbackQueryHandler(button)]
    },

    # Точка прерывания диалога. В данном случае — команда /stop.
    fallbacks=[MessageHandler(Filters.entity(menu_buttons.back), back)]
)
