import telebot
import time

bot_token = "989062128:AAH3AHcI4kudxRVEHkBRnvYs4uoPSYMG4xk"

bot=telebot.TeleBot(token = bot_token)

def find_at(msg):
    for text in msg:
        if '@'in text:
            return text
def find_at2(msg):
    for text in msg:
        if '*'in text:
            return text
def find_at3(msg):
    for text in msg:
        if '#'in text:
            return text
    

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message,"Hey there..I'm a bot created by san..Go ahead and type '/help' to get started")

@bot.message_handler(commands = ['help'])
def send_welcome(message):
    bot.reply_to(message,"hey this bot is used for searching people on various social media platforms like Instagram,Facebook and Twitter." + "\n" +"\n" + "To search on Instagram : Type '@' followed by username of the user you want to look for."+"\n"+"\n"+"To search on Facebook : Type '*' followed by username of the user you want to look for."+"\n"+"\n"+"To search on Twitter : Type '#' followed by username of the user you want to look for.")

@bot.message_handler(func=lambda msg:msg.text is not None and '@' in msg.text )

def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)
    bot.reply_to(message, "searching on instagram")

    bot.reply_to(message , 'https://instagram.com/{}'.format(at_text[1:]))

@bot.message_handler(func=lambda msg:msg.text is not None and '*' in msg.text )
def at_answer(message):
    texts = message.text.split()
    at_text2 = find_at2(texts)
    bot.reply_to(message, "searching on facebook")

    bot.reply_to(message , 'https://facebook.com/{}'.format(at_text2[1:]))
    
@bot.message_handler(func=lambda msg:msg.text is not None and '#' in msg.text )
def at_answer(message):
    texts = message.text.split()
    at_text3 = find_at3(texts)
    bot.reply_to(message, "searching on twitter")

    bot.reply_to(message , 'https://twitter.com/{}'.format(at_text3[1:]))

    


while True:
    try :
        bot.polling()
    except Exception:
        time.sleep(15)
