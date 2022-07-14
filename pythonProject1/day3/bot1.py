#텔레그램 봇 라이브러리
#pip install python-telegram-bot
Token = '5511741657:AAHHqUZrKABTgiGOe_ovSR8QrXA7wQ2KXuU'
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters

updater= Updater(token=Token, use_context=True)

def fn_write_txt(text):
    f = open('chat_info.txt', 'a')
    f.write(text)
    f.writelines('\n')
    f.close()

def fn_echo(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    # 메세지 온 거 그대로 리턴
    context.bot.send_message(chat_id = user_id, text = user_text)
    print(user_text)

def fn_command_diary(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    context.bot.send_message(chat_id = user_id, text = user_text)
    user_text = user_text[7:]
    print("다이어리 : ", user_text)
    fn_write_txt()

echo_handler = MessageHandler(Filters.text & (~Filters.command), fn_echo)
updater.dispatcher.add_handler(echo_handler)
diary_handler = CommandHandler('diary', fn_command_diary)
updater.dispatcher.add_handler(diary_handler)
updater.start_polling(timeout=1, clean=True)
updater.idle()
