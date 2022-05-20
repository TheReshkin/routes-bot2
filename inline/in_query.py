from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
from routes import  avia
from telegram import InlineKeyboardMarkup
from telegram import InlineKeyboardButton
from telegram import InlineQueryResult


def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    print(query)
    results = list()

    results.append(
        InlineQueryResultArticle(
            id="Avia",
            title="Поиск авиа билетов",
            input_message_content=InputTextMessageContent(avia.avia_search(query))
        )
    )
    print(update.inline_query.id)
    context.bot.answer_inline_query(update.inline_query.id, results)


inline_caps_handler = InlineQueryHandler(inline_caps)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Что-то пошло не так, такого функционала пока нет")
