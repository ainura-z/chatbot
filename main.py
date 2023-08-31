from model import get_response
import time
import telebot


token = ''
bot = telebot.TeleBot(token)
step = -1

# Processing /start command
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Начни общаться с нашим чат-ботом прямо сейчас!'
                     'Напиши любое предложение.')

# Processing text messages
@bot.message_handler(content_types=["text"])
def handle_text(m):
    global step
    step += 1
    respond = get_response(m.text, step)
    if '@' in respond:
        index = respond.find('@')
        respond = respond[:index]
    bot.send_message(m.chat.id, respond)


while (True):
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print('Connection lost! Retry in 3 sec...')
        print(e)
        time.sleep(3)
