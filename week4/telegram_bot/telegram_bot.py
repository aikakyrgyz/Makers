import telebot
import csv
from Token import token
from telebot import types

bot = telebot.TeleBot(token)
entry = {}

inline_keyboard = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Income', callback_data='income')
button2 = types.InlineKeyboardButton('Spending', callback_data='spending')
inline_keyboard.add(button1, button2)

@bot.message_handler(commands = ['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Hello, please choose one', reply_markup=inline_keyboard)

@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    print
    if c.data == 'income':
        chat_id = c.message.chat.id
        msg = bot.send_message(chat_id,'Choose the income type', reply_markup=income_keyboard)
        bot.register_next_step_handler(msg, get_income_category)
    if c.data == 'spending':
        chat_id = c.message.chat.id
        spending_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        k1 = types.KeyboardButton('Food')
        k2 = types.KeyboardButton('Bills')
        k3 = types.KeyboardButton('Other')
        spending_keyboard.add(k1, k2, k3)
        msg = bot.send_message(chat_id, 'Choose the spending type', reply_markup=spending_keyboard)
        bot.register_next_step_handler(msg, get_spending_category)

def get_income_category(message):
    chat_id = message.chat.id
    entry.update({'category':message.text}) #or entry['category'] = message.text
    msg = bot.send_message(chat_id, 'Specify the amount')
    bot.register_next_step_handler(msg, get_sum_income)

def get_sum_income(message):
    chat_id = message.chat.id
    entry.update({'sum': message.text})
    file_name = 'income.csv'
    with open(file_name, 'a') as my_file:
        writer = csv.writer(my_file)
        writer.writerow((entry['category'], entry['sum']))
    bot.send_message(chat_id, 'Your income is saved', reply_markup=inline_keyboard )
    bot.send_sticker(chat_id, 'CAACAgIAAxkBAALlzmA6QamHE5l8U78kqpl48ShSElmtAALVAAOWn4wO2ckVovI3A30eBA')


def get_spending_category(message):
    chat_id = message.chat.id
    entry.update({'category':message.text})
    msg = bot.send_message(chat_id, 'Specify the amount')
    bot.register_next_step_handler(msg, get_sum_spending)

def get_sum_spending(message):
    chat_id = message.chat.id
    entry.update({'sum':message.text})
    file_name = 'spending.csv'
    with open(file_name, 'a') as my_file:
        writer = csv.writer(my_file)
        writer.writerow((entry['category'], entry['sum']))
    bot.send_message(chat_id, 'Your spending is saved', reply_markup=inline_keyboard )
    bot.send_sticker(chat_id, 'CAACAgIAAxkBAALlzmA6QamHE5l8U78kqpl48ShSElmtAALVAAOWn4wO2ckVovI3A30eBA')


# def start_message(message):
#     chat_id = message.chat.id
#     user_info = f'{message.from_user.first_name} {message.from_user.last_name}'
#     bot.send_message(chat_id, 'Please choose one', reply_markup=inline_keyboard)



# @bot.message_handler(content_types=['sticker', 'text'])

# def send_sticker(message):
#     chat_id = message.chat.id
#     # print(message.text) # echoes the text 
#     if message.text.lower() == 'hello':
#         bot.send_message(chat_id, "Hello from the bot")
    

#     bot.send_sticker(chat_id, 'CAACAgIAAxkBAALlzmA6QamHE5l8U78kqpl48ShSElmtAALVAAOWn4wO2ckVovI3A30eBA')


bot.polling()
