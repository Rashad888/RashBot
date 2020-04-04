import telebot
import botSet
bot = telebot.TeleBot(botSet.tokken)

@bot.message_handler(content_types=['text'])

def gmsg(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,"Как дела?)")

bot.polling(none_stop=True , interval= 0)