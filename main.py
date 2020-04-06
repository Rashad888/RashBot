import telebot
import botSet
bot = telebot.TeleBot(botSet.tokken)

@bot.message_handler(commands=['start'])
def welMsg(message):
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAI-9F6LZzJORuLw_RCmageqFRrtNvDEAAIOAAPSfWEYkBysKo8rSV0YBA")
    bot.send_message(message.chat.id,'Привет! Я бот Рашада, и я буду делать все что ты скажешь!')

bot.polling(none_stop=True , interval= 0)