from dotenv import load_dotenv
from os import getenv
import telebot

load_dotenv()
TOKEN = getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    start_message = (f"<b>Привет! Это бот для форматирования текста python!🐍\n"
                     f"Отправь сюда python файл (расширение .py) и бот отправит код в виде текста!\n\n"
                     f"📱 Telegram: @Djmix22\n"
                     f"💻 GitHub: <a href='https://github.com/DjMix22'>DjMix22</a></b>")
    bot.send_message(
        chat_id=message.chat.id,
        text=start_message,
        parse_mode="HTML"
    )


@bot.message_handler(content_types=['document'])
def send_file(message):
    print(message.from_user.username)

    file_name = message.document.file_name
    file_extension = file_name.split(".")[-1]

    if file_extension == "py":
        file_id = message.document.file_id
        file = bot.get_file(file_id)

        result_file = bot.download_file(file.file_path)
        code = result_file.decode("utf-8")
        result_text = f"```Python\n# Файл {file_name}:\n\n{code}\n```"

        if len(result_text) > 4096:
            result_text = "*Код слишком большой!!!*"

        bot.send_message(
            chat_id=message.chat.id,
            text=result_text,
            parse_mode="Markdown"
        )


bot.polling()
