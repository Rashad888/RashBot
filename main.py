import telebot
import botSet
bot = telebot.TeleBot(botSet.tokken)

@bot.message_handler(commands=['start'])
def welMsg(message):
    bot.send_message(message.chat.id,"Привет! Я бот Рашида, и я буду стараться тебя радовать")
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAI-9F6LZzJORuLw_RCmageqFRrtNvDEAAIOAAPSfWEYkBysKo8rSV0YBA")

bot.polling(none_stop=True , interval= 0)