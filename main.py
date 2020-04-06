import telebot
import botSet
bot = telebot.TeleBot(botSet.tokken)

@bot.message_handler(content_types=['text'])
def gmsg(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,"Как дела?)")

@bot.message_handler(commands=['sendmemes'])
def vkur(message):
    keyboardmain = telebot.types.InlineKeyboardMarkup(row_width=2)
    fbtn = telebot.types.InlineKeyboardButton(text='https://vk.com/rash_ad')
    keyboardmain.add(fbtn)
    bot.send_message(message.from_user.id,'Ссылка на страницу Рашада',reply_markup=keyboardmain)


if __name__ == "__main__":
    bot.polling(none_stop=True , interval= 0)