import telebot
import botSet
bot = telebot.TeleBot(botSet.tokken)

@bot.message_handler(content_types=['text'])
def vkur(message):
    if message.text == "/sendmemes":
        keyboardmain = telebot.types.InlineKeyboardMarkup(row_width=2)
        fbtn = telebot.types.InlineKeyboardButton(text='https://vk.com/rash_ad')
        keyboardmain.add(fbtn)
        bot.send_message(message.from_user.id,'Ссылка на страницу Рашада',reply_markup=keyboardmain)

bot.polling(none_stop=True , interval= 0)