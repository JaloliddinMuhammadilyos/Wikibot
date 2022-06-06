from telegram.bot import Bot
from telegram.user import User
from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext, MessageHandler
from telegram.update import Update
import settings
import requests
from telegram.ext.filters import Filters

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
    if len(args)== 0:
        update.message.\
            reply_text("Searchdan so'ng qidirmoqchi bo'lgan narsangizni yozing")
    else:

        search_text = ' '.join(args)
        response = requests.get('https://uz.wikipedia.org/w/api.php', {
            'action': 'opensearch',
            'search': search_text,
            'limit': 1,
            'namespace': 0,
            'format': 'json',
        })
        result = response.json()
        link = result[3]

    if len(link):
        update.message\
            .reply_text('Sizning so\'rovingiz bo\'yicha havola: ' + link[0])
    else:
        update.message.reply_text('Sizning so\'rovingiz bo\'yicha hech nima yo\'q')

    # print(result)

    #print(search_text)



    # context.bot.send_message(chat_id=update.message.chat_id, text = "Salom yana bir bor!")
        # message classga o'rab berdi



dispatcher = updater.dispatcher                            # Updater dispatcherni ichida keladi
dispatcher.add_handler(CommandHandler("start", start))     # Va dispatcherga Handler qo'shamiz. masalan commandalarni handler qiladi
dispatcher.add_handler(CommandHandler("search", search))
dispatcher.add_handler(MessageHandler(Filters.all, start))


updater.start_polling()
updater.idle()