import telebot

from settings import token, code_words
from engine import send_photo

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def get_text_message(message: telebot.types.Message):
    for words, dir_path in code_words:
        for word in words:
            if word.lower() not in message.text.lower():
                continue
            send_photo(bot=bot, address=message.from_user.id, directory=dir_path)


if __name__ == '__main__':
    bot.polling(none_stop=True)
