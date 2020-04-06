import telebot
import botSet
bot = telebot.TeleBot(botSet.tokken)

@bot.message_handler(commands=['sendmemes'])
def vkur(message):
    bot.send_message(message.from_user.id,"vk.com")

bot.polling(none_stop=True , interval= 0)