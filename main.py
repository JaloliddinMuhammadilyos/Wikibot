from telegram.bot import Bot
from telegram.user import User


bot = Bot(token="5573637035:AAHdNMvfB0MvfnJMuyWjTmEFLLoG8cX_H7U")
# print(bot.get_me())
user: User = bot.get_me()
print(user.link)