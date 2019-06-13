from telegram.ext import Updater,CommandHandler,InlineQueryHandler
from telegram import InputTextMessageContent, InlineQueryResultArticle
from uuid import uuid4
import socket
import os

def ip(name):
    return ("{} >> {}".format(str(name),str(socket.gethostbyname(name))))

def host(addr):
    return ("{} >> {}".format(str(addr),socket.gethostbyaddr(addr)[0]))

updater = Updater("TOKEN")

print("robot started via this IP :")
os.system("""dig TXT +short o-o.myaddr.l.google.com @ns1.google.com | awk -F'"' '{ print $2}'""")


def start(bot,update):
    bot.sendMessage(update.message.chat_id,"""Hello Dear,\nthis robot give you ip or host name by each other!""")
    bot.sendMessage(update.message.chat_id,"""Example :\n
    @bot google.com""")

def inline(bot,update):
    q = update.inline_query.query

    items = list()
    items.append(InlineQueryResultArticle(id = uuid4(),title="IP",input_message_content=InputTextMessageContent(ip(q))))
    items.append(InlineQueryResultArticle(id = uuid4(),title="Host Name",input_message_content=InputTextMessageContent(host(q))))
    bot.answerInlineQuery(update.inline_query.id,results=items)


updater.dispatcher.add_handler(CommandHandler("start",start))
updater.dispatcher.add_handler(InlineQueryHandler(inline))
updater.start_polling()
updater.idle()
