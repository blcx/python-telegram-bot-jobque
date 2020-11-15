import telegram
from telegram.ext import Updater, CallbackContext

interval = 10



u = Updater('')


def callback_minute(context: telegram.ext.CallbackContext):    
    context.bot.send_message(chat_id=, text="")   


j = u.job_queue

job_minute = j.run_repeating(callback_minute, interval=interval, first=0)
job_minute.enabled = True


u.start_polling()
u.idle()