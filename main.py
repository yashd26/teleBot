#am not deploying this so just run the code, search the bot on tele(@tempDelhiBot) and play with it:)
'''
dependencies
pip install python-telegram-bot
'''

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

user_arr = [] #using array as an alternate to database

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# writting functionality of the command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    user_arr.append([user_id, user_name])

    message = "u'Current temperature in Delhi is 12℃" #am hardcoding this part but it could be done by using a weather api
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

async def once(context: ContextTypes.DEFAULT_TYPE):
    message = "u'Current temperature in Delhi is 12℃"
    # send message to all users
    for keys in user_arr:
        id = keys[0]
        await context.bot.send_message(chat_id=id, text=message)

if __name__ == '__main__':
    application = ApplicationBuilder().token('Enter ur token').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    job_queue = application.job_queue

    job_minute = job_queue.run_repeating(once, interval=60) #interval calls function everytime after 60sec
    application.run_polling()
