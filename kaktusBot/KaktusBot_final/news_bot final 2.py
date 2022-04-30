from parsing import main, clear
import telebot
import csv
from Token import token
from telebot import types
from datetime import date, timedelta

bot = telebot.TeleBot(token)

today = date.today().strftime("%b-%d-%Y")
yest = (date.today()-timedelta(days=1)).strftime("%b-%d-%Y")
list_ = []
def open_csv(index, choice, num):
    print(list_)
    row = ''
    if num==True:
        with open('today.csv', 'r') as f:
            csv_reader = csv.reader(f, delimiter='|')
            line_num = 0
            for row in csv_reader:
                if index == row[0]:
                    row = row
                    print('today')
                    print(row)
                    break
    else:
        with open('yesterday.csv', 'r') as f:
            csv_reader = csv.reader(f, delimiter='|')
            line_num = 0
            for row in csv_reader:
                if index == row[0]:
                    row = row
                    print('yest')
                    print(row)
                    break

    if choice == 'Image':
        return str(row[2])
    elif choice == 'Description':
        return row[4]
    elif choice == 'Title':
        return row[1]
    else:
        return row[3]
    
def create_button(choice):
    if choice == 'today':
        inline_keyboard = types.InlineKeyboardMarkup() #news button
        with open('today.csv', 'r') as f:
            csv_reader = csv.reader(f, delimiter='|')
            index = 1
            for row in csv_reader:
                button_name = row[1]
                button = types.InlineKeyboardButton(button_name, callback_data=index)
                inline_keyboard.add(button)
                index = index+1
                if index==21:
                    break
        return inline_keyboard
    elif choice == 'yesterday':
        inline_keyboard = types.InlineKeyboardMarkup() #news button
        with open('yesterday.csv', 'r') as f:
            csv_reader = csv.reader(f, delimiter='|')
            index = 1
            for row in csv_reader:
                button_name = row[1]
                button = types.InlineKeyboardButton(button_name, callback_data=index)
                inline_keyboard.add(button)
                index = index+1
                if index==21:
                    break
        return inline_keyboard
    elif choice == 'ty':
        button = types.ReplyKeyboardMarkup()
        k1 = types.KeyboardButton('News of today\n\n\n' + today)
        k2 = types.KeyboardButton('News of yesterday\n\n\n'+yest)
        button.add(k1, k2)
        return button
    elif choice == 'back and quit':
        button = types.ReplyKeyboardMarkup(one_time_keyboard=True) #back or quit
        k1 = types.KeyboardButton('Back')
        k3 = types.KeyboardButton('Back to all news')
        k4 = types.KeyboardButton('Back to main menu')
        k2 = types.KeyboardButton('Quit')
        button.add(k1, k3,k4, k2)
        return button
    else:
        button = types.ReplyKeyboardMarkup() #photo or description
        k1 = types.KeyboardButton('Image')
        k2 = types.KeyboardButton('Description')
        k3 = types.KeyboardButton('Link')
        button.add(k1, k2, k3)
        return button

inline_keyboard_t_y = create_button('ty')
photo_or_desc_keyboard = create_button('idl')
inline_keyboard_today = create_button('today')
inline_keyboard_yesterday = create_button('yesterday')
back_or_quit = create_button('back and quit')

@bot.message_handler(commands = ['start', 'hello'])
def start(message):
    clear()
    main()
    print('finished parsing!')
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Choose your news', reply_markup=inline_keyboard_t_y)
    bot.register_next_step_handler(msg, today_yesterday)
def today_yesterday(c):
    chat_id = c.chat.id
    if c.text == 'News of today':
        list_.append(True)
        bot.send_message(chat_id, 'choose one', reply_markup=inline_keyboard_today)
    else:
        list_.append(False)
        bot.send_message(chat_id, 'choose one', reply_markup=inline_keyboard_yesterday)
@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    chat_id = c.message.chat.id
    index = c.data
    bot.send_message(chat_id, 'The article you chose: \U0001F447')
    bot.send_message(chat_id, ('\U0001F4AD' + open_csv(index, 'Title', list_[-1])))
    photo_or_desc_keyboard = create_button('pdl')
    msg = bot.send_message(chat_id, 'Would you like to see the [Image], [Description] or [Link]', reply_markup = photo_or_desc_keyboard)
    bot.register_next_step_handler(msg, get_photo_or_desc, index)
def get_photo_or_desc(message, index):
    chat_id = message.chat.id
    try:
        msg = bot.send_message(chat_id,  open_csv(index, message.text, list_[-1]), reply_markup = back_or_quit)
        bot.register_next_step_handler(msg, back_or_quit_func, index)

    except:
        description = open_csv(index, message.text, list_[-1])
        length = len(description)
        if length<8192:
            description1 = description[:int(length/2)]
            index11 = 0
            while not description1.endswith('.'):
                index11+=1
                description1 = description[:int(length/2)+index11]
            description2 = description[int(length/2)+index11:]
            bot.send_message(chat_id,  description1)
            msg = bot.send_message(chat_id, description2, reply_markup=back_or_quit)
            bot.register_next_step_handler(msg, back_or_quit_func, index)
        elif length >8192 and length < 12288:
            description1 = description[:int(length/3)]
            index22 = 0
            while not description1.endswith('.'):
                index22+=1
                description1 = description[:int(length/3)+index22]
            description2 = description[int(length/3):length - int(length/3)]
            index33 = 0
            while not description2.endswith('.'):
                index33+=1
                description2 = description[int(length/3)+index33:length - int(length/3)+index33]
            description3 = description[length - int(length/3)+index33:]   
            bot.send_message(chat_id,  description1)
            bot.send_message(chat_id,  description2)
            msg = bot.send_message(chat_id, description3, reply_markup=back_or_quit)
            bot.register_next_step_handler(msg, back_or_quit_func, index)


#need to work with description
def back_or_quit_func(message, index):
    chat_id = message.chat.id
    if message.text == 'Back':
        msg = bot.send_message(chat_id, 'Would you like to see the image, description or link' , reply_markup= photo_or_desc_keyboard)
        bot.register_next_step_handler(msg, get_photo_or_desc, index)
    elif message.text =='Back to all news' and list_[-1]==True:
        bot.send_message(chat_id, 'Choose your news', reply_markup=inline_keyboard_today)
    elif message.text == 'Back to all news' and list_[-1] == False:
        bot.send_message(chat_id, 'Choose your news', reply_markup=inline_keyboard_yesterday)
    elif message.text == 'Back to main menu':
        msg = bot.send_message(chat_id, 'Choose your news', reply_markup=inline_keyboard_t_y)
        bot.register_next_step_handler(msg, today_yesterday)
    elif message.text == 'Quit':
        bot.send_message(chat_id, 'Bye')
        bot.send_sticker(chat_id, 'CAACAgIAAxkBAALuhmBDr06JKto-4J6mjh7C9o1NQvVfAALzAgACusCVBYNYHkhJJkhgHgQ') 
bot.polling()

