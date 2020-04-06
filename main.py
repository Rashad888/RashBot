import telebot
import botSet
bot = telebot.TeleBot(botSet.tokken)

@bot.message_handler(content_types=['text'])
def vkur(message):
    if message.text == "Что делаешь":
        bot.send_message(message.from_user.id,"vk.com")

bot.polling(none_stop=True , interval= 0)