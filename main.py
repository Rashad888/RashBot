import telebot
import botSet
bot = telebot.TeleBot(botSet.tokken)

@bot.message_handler(commands=['start'])
def welMsg(message):
    bot.reply_to(message.from_user.id,"Привет")
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAI-9F6LZzJORuLw_RCmageqFRrtNvDEAAIOAAPSfWEYkBysKo8rSV0YBA")


bot.polling(none_stop=True , interval= 0)