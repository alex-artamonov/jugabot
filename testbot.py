import telebot
from telegram.constants import ParseMode
from telebot import types
import conj_funcs as cf
import keys as ks


TOKEN = "6303319026:AAFpGl2CnTr8bP0J9i5iMhjRkGP35HRhAMY"

bot = telebot.TeleBot(TOKEN)
commands = [f"/{ele}" for ele in ks.tiempos_list()]
# commands.append('/start')
# print(commands)

# table = "yo\t\tpuedo\ntu\t\tpuedes\nel\t\tpuede"
# tiempos_list = ks.tiempos_list
current_verb = ""
conju_dict = {}

@bot.message_handler(commands=ks.tiempos_list())
def show_tense(message):
    # print(commands)
    
    name = message.chat.first_name
    cid = message.chat.id
    print(message.text, name, cid)
    # print(dir(message))
    # fid = message.from.id
    if message.text == '/start':
        output = f"¡Hola, {name}! \
        Escribe un verbo en español en infinitivo (e.g. <b>comer</b>) para obtener sus conjugaciones"
        bot.send_message(message.chat.id, output, parse_mode=ParseMode.HTML)
        return

    tiempo = message.text[1:] #get rid of '\' before the command
    # bot.send_message(message.chat.id, f"Hola, {message.chat.first_name}")
    try:
        output = cf.get_conj(conju_dict, current_verb, tiempo)
    except KeyError:
        output = "Algo salió mal: no pude encontrar esta vez. \
            Tal vez hay que escribir un verbo"
    bot.send_message(message.chat.id, output, \
        parse_mode=ParseMode.HTML)


@bot.message_handler(content_types=['text'], )
def get_verb(message: telebot.types.Message):
    global current_verb
    current_verb = message.text
    global conju_dict
    tiempo = 'presente_indicativo'
    try:
        conju_dict = cf.get_conju_dicts(current_verb)
        output = cf.get_conj(conju_dict, current_verb, tiempo)
        # print(conju_dict)
    except cf.NoResultset:
        output = "Solo se verbos españolos. No pude encontrar este verbo."    
    # bot.reply_to(message, get_conj(message.text), parse_mode=ParseMode.HTML)
    
    bot.send_message(message.chat.id, output, \
        parse_mode=ParseMode.HTML, reply_markup=create_command_buttons())

def create_command_buttons():
    # commands_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    commands_markup = types.ReplyKeyboardMarkup(is_persistent=True)
    for command in commands:
        commands_markup.add(types.KeyboardButton(command))
    return commands_markup

def create_buttons():
    tiempos = [f"{ele[1]} {ele[0]}" for ele in ks.tiempos]
    tiempos_markups = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    buttons = []
    for val in tiempos:
        buttons.append(types.KeyboardButton(val))

    tiempos_markups.add(*buttons)
    return tiempos_markups


bot.polling(none_stop=True)