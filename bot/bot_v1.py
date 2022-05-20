# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext import CommandHandler
from handlers import currentHandlers
import inline.in_query
import settings
import menu_buttons
import logging


# создать дерево сценариев
def main():
    # logs
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    updater = Updater(settings.TOKEN, use_context=True)
    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher
    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере
    # эта функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    # /text_handler = MessageHandler(Filters.text, currentHandlers.echo)
    # сценарий поиска
    dp.add_handler(currentHandlers.conv_handler)
    # Filters.regex('^(Age|Favourite colour|Number of siblings)$'
    dp.add_handler(CommandHandler("start", currentHandlers.start))
    dp.add_handler(CommandHandler("back", currentHandlers.back))
    dp.add_handler(CommandHandler("reg", currentHandlers.reg))
    dp.add_handler(CommandHandler("auth", currentHandlers.auth))
    dp.add_handler(CommandHandler("search_raw", currentHandlers.search_raw))
    # инлайн запросы вне чата
    dp.add_handler(inline.in_query.inline_caps_handler)

    # обработчик нажатия кнопки внутри сообщения
    dp.add_handler(CallbackQueryHandler(currentHandlers.button))

    # обработчик непонятных инлайн команд
    dp.add_handler(MessageHandler(Filters.command, inline.in_query.unknown))

    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()
    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()
    # Запускаем функцию main() в случае запуска скрипта.


if __name__ == '__main__':
    main()
