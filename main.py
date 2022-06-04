from telegram.bot import Bot
from telegram.user import User
from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext
from telegram.update import Update
import settings


'''

bot = Bot(token="")
# print(bot.get_me())
user: User = bot.get_me()
# print(user.link)
'''

updater = Updater(token=settings.TELEGRAM_TOKEN)
"""python telegram bot update qilishi uchun updateni qo'ydik"""




def start(update: Update, context: CallbackContext):
    update.message\
        .reply_text("Assalomu alaykum! Wikipediada ma'lumot qidiruvchi"
                    " botga hush kelibsiz! Biron nima izlash uchun "
                    "/search va so'rovingizni yozing. /search Amir Temur")


def search(update: Update, context: CallbackContext):
    args = context.args
    search_text = ' '.join(args)


    #print(search_text)



    # context.bot.send_message(chat_id=update.message.chat_id, text = "Salom yana bir bor!")
        # message classga o'rab berdi



dispatcher = updater.dispatcher                            # Updater dispatcherni ichida keladi
dispatcher.add_handler(CommandHandler("start", start))     # Va dispatcherga Handler qo'shamiz. masalan commandalarni handler qiladi
dispatcher.add_handler(CommandHandler("search", search))



updater.start_polling()
updater.idle()