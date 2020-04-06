import telebot
import botSet
bot = telebot.TeleBot(botSet.tokken)

@bot.message_handler(commands=['start'])
def welMsg(message):
    bot.send
    bot.send_sticker(message.chat.id,"Привет"+"CAACAgIAAxkBAAI-9F6LZzJORuLw_RCmageqFRrtNvDEAAIOAAPSfWEYkBysKo8rSV0YBA")


bot.polling(none_stop=True , interval= 0)