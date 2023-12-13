import telebot
from telegram.constants import ParseMode
from telebot import types
import conj_funcs as cf
import keys as ks
import os

TOKEN = os.environ["JUGABOT"]
bot = telebot.TeleBot(TOKEN)
print(bot.get_me())
commands = [f"/{ele}" for ele in ks.tiempos_list()]
current_verbs = {}
conju_dicts = {}
impersonal_dicts = {}


@bot.message_handler(commands=ks.tiempos_list())
def show_tense(message):
    name = message.chat.first_name
    cid = message.chat.id
    print(message.text, name, cid)
    if message.text == "/start":
        output = f"¡Hola, {name}! \
        Escribe un verbo español en infinitivo (e.g. <b>comer</b>) para obtener sus conjugaciones"
        bot.send_message(message.chat.id, output, parse_mode=ParseMode.HTML)
        return
    if message.text == "/impersonal_forms":
        try:
            output = cf.table_impersonal(impersonal_dicts[message.chat.id])
        except KeyError:
            output = "Algo salió mal: no pude encontrar esta vez. \
            Tal vez hay que escribir un verbo"
        bot.send_message(message.chat.id, output, parse_mode=ParseMode.HTML)
        return
    if message.text == "/translation":
        try:
            output = "https://www.wordreference.com/es/en/translation.asp?spen=" + current_verbs[message.chat.id]
        except KeyError:
            output = "Algo salió mal: no pude encontrar esta vez. \
            Tal vez hay que escribir un verbo"
        bot.send_message(message.chat.id, output)
        return
    tiempo = message.text[1:]  # get rid of '/' before the command
    try:
        output = cf.get_conj(
            conju_dicts[message.chat.id], current_verbs[message.chat.id], tiempo
        )
    except KeyError:
        output = "Algo salió mal: no pude encontrar esta vez. \
            Tal vez hay que escribir un verbo"
    bot.send_message(message.chat.id, output, parse_mode=ParseMode.HTML)


@bot.message_handler(
    content_types=["text"],
)
def get_verb(message: telebot.types.Message):
    tiempo = "presente_indicativo"
    try:
        dicts = cf.get_conju_dicts(message.text)
        conju_dicts[message.chat.id] = dicts[0]
        impersonal_dicts[message.chat.id] = dicts[1]
        current_verb = impersonal_dicts[message.chat.id]['infinitivo:']
        current_verbs[message.chat.id] = current_verb
        output = cf.get_conj(conju_dicts[message.chat.id], current_verb, tiempo)
    except cf.NoResultset:
        output = "Solo se verbos españolos. No pude encontrar este verbo."

    bot.send_message(
        message.chat.id,
        output,
        parse_mode=ParseMode.HTML,
        reply_markup=create_command_buttons(),
    )


def create_command_buttons():
    commands_markup = types.ReplyKeyboardMarkup(is_persistent=True)
    for command in commands:
        commands_markup.add(types.KeyboardButton(command))
    return commands_markup


# def create_buttons():
#     tiempos = [f"{ele[1]} {ele[0]}" for ele in ks.tiempos]
#     tiempos_markups = types.ReplyKeyboardMarkup(one_time_keyboard=True)
#     buttons = []
#     for val in tiempos:
#         buttons.append(types.KeyboardButton(val))

#     tiempos_markups.add(*buttons)
#     return tiempos_markups


if __name__ == "__main__":
    bot.polling(none_stop=True)
