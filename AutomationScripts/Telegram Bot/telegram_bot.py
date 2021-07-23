
from telegram import *
from telegram.ext import *


bot= Bot("")#Api key of bot in the bracket
updater = Updater("API Key",use_context=True)
dispatcher =updater.dispatcher
#function for play_music
def test_function(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="tutorial link : https://www.youtube.com/watch?v=ugR8bY4hQ4M",
    )
start_value = CommandHandler('play_music',test_function)
dispatcher.add_handler(start_value)

#function for hello
def test_function1(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello JI,how are you??",
    )
start_value = CommandHandler('Hello',test_function1)
dispatcher.add_handler(start_value)


updater.start_polling()