import telebot
from telebot import types
import random
from os import getenv

SECRET_KEY = str(getenv("SECRET")) # Берет значение ключа из файла .env (В docker-compose прокидывается отдельно)
game_vars = ["Камень", "Ножницы", "Бумага", "Счет"]

bot = telebot.TeleBot(SECRET_KEY, parse_mode=None)
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id, "Привет, ты парень или девушка ?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши 'Привет'")
#     elif message.text == "Девушка":
#         bot.send_message(message.from_user.id, "Ты самая красивая девушка на свете ❤️")
#     elif message.text == "Парень":
#         bot.send_message(message.from_user.id, "Ты самый лучший парень на планете")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# inMurkup = types.InlineKeyboardMarkup(row_width=1)
# but4 = types.InlineKeyboardButton("Камень", callback_data='rock')
# but5 = types.InlineKeyboardButton("Ножницы", callback_data='scissors')
# but6 = types.InlineKeyboardButton("Бумага", callback_data='paper')
# inMurkup.add(but4, but5, but6)
# user_action = input

# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):

@bot.message_handler(commands=['info'])
def get_bot_info(message):
    bot.send_message(message.from_user.id, "Привет, это первый проект моего создателя! В данный момент я в разработке.")

@bot.message_handler(commands=['start'])
def get_start_chat(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    but1 = types.KeyboardButton("Команды")
    markup.add(but1)
    bot.send_message(message.chat.id, text=f"Привет, {message.from_user.first_name}!", reply_markup=markup)
@bot.message_handler(commands=['game'])
def get_bot_info(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [types.KeyboardButton(i) for i in game_vars]
    # but2 = types.KeyboardButton("Камень")
    # but3 = types.KeyboardButton("Ножницы")
    # but4 = types.KeyboardButton("Бумага")
    # but5 = types.KeyboardButton("Счет")
    markup.add(buttons)
    bot.send_message(message.from_user.id, "Отлично, давай повеселимся!\nВыбирай - камень, ножницы или бумага:"
                     .format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    computer_counts = 0
    user_counts = 0
    draw = 0
    possible_actions = ["Камень", "Ножницы", "Бумага"]
    computer_actions = random.choice(possible_actions)
    if message.text == "Команды":
        bot.send_message(message.chat.id, text="1)/info - немного про меня\n2)/game - Играть в  камень, ножницы, бумага\n")
    elif message.text == "Крым":
        bot.send_message(message.chat.id, "🇷🇺 НАШ! 🇷🇺")
    elif message.text == computer_actions:
        draw += 1
        bot.send_message(message.chat.id, f"Оба игрока выбрали: {message.text}.\nНичья!\nДля начала новой игры пишите /game")

    elif message.text == "Камень":
        if computer_actions == "Ножницы":
            user_counts += 1
            bot.send_message(message.chat.id, text="Камень бьет ножницы.\nВы победили!\nДля начала новой игры пишите /game")
        else:
            computer_counts += 1
            bot.send_message(message.chat.id, text="Бумага оборачивает камень.\nВы проиграли!\nДля начала новой игры пишите /game")
    elif message.text == "Ножницы":
        if computer_actions == "Бумага":
            user_counts += 1
            bot.send_message(message.chat.id, text="Ножницы режут бумагу.\nВы победили!\nДля начала новой игры пишите /game")
        else:
            computer_counts += 1
            bot.send_message(message.chat.id, text="Ножницы ломаются об камень.\nВы проиграли!\nДля начала новой игры пишите /game")
    elif message.text == "Бумага":
        if computer_actions == "Камень":
            user_counts += 1
            bot.send_message(message.chat.id, text="Бумага оборачивает камень.\nВы победили!\nДля начала новой игры пишите /game")
        else:
            computer_counts += 1
            bot.send_message(message.chat.id, text="Ножницы режут бумагу.\nВы проиграли!\nДля начала новой игры пишите /game")
    elif message.text == "Счет":
        bot.send_message(message.chat.id, text=f"Победы = {user_counts}\n"
                                               f"Поражения = {computer_counts}\n"
                                               f"Ничьи = {draw}")
    else:
        bot.send_message(message.chat.id, text="Я тебя не понимаю, напиши /start")

    # markup_inline = types.InLineKeyBoardMarkup()
    # item_yes = types.InLineKeyBoardButton(text = 'Да', callback_data = 'yes')
    # item_no = types.InLineKeyBoardButton(text = 'Нет', callback_data = 'no')
    #
    # markup_inline.add(item_yes, item_no)
    # bot.send_message(message.chat.id, 'Желаете узнать небольшую информацию о вас',
    #     reply_markup = markup_inline
    # )
# @bot.callback_query_handler(func = lambda call : True)
# def answer(call):
#         if call.data == 'yes':
#             markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
#             item_female = types.KeyboardButton('Девушка')
#             item_male = types.KeyboardButton('Парень')
#
#             markup_reply.add(item_female, item_male)
#             bot.send_message(call.message.chat.id, 'Нажмите на одну из кнопок',
#                     reply_markup = markup_reply
#             )
#         elif call.data == 'no':
#             pass
bot.polling(none_stop=True, interval=0)
