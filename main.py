import telebot
import botSet
bot = telebot.TeleBot(botSet.tokken)

@bot.message_handler(commands=['start'])
def welMsg(message):
    s = bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAI-9F6LZzJORuLw_RCmageqFRrtNvDEAAIOAAPSfWEYkBysKo8rSV0YBA")
    bot.reply_to(message,"Привет"+str(s))



bot.polling(none_stop=True , interval= 0)