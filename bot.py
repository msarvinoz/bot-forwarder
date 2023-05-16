import requests
import telebot
import datetime
from telegram import Bot, Voice
from telegram.error import TelegramError
bot_token = "6163091703:AAEniig-IQCi6fOfsFAeu1LsQiUB9GKp3LU"
bot = telebot.TeleBot("6163091703:AAEniig-IQCi6fOfsFAeu1LsQiUB9GKp3LU")
group_id = 'python_practice_bot_for_wester'
chat_id = '@python_practice_bot_for_wester'

button = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
button.add(telebot.types.KeyboardButton('Biz haqimizda'), telebot.types.KeyboardButton('Savol va taklif uchun'))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Assalomu aleykum, wester school botiga hush kelibsiz, davom ettirish uchun quyidagilardan birini tanlang👇', reply_markup=button)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    if message.text == 'Biz haqimizda':
        about_us(message)
    elif message.text == 'Savol va taklif uchun':
        write_questions(message)
    else:
        bot.send_message(message.from_user.id, 'Sorovingiz qabul qilinmadi', reply_markup=button)


def about_us(message):
    info = f"O'quv markaz: <b>Wester school</b>\nJoylashuv: <b>Andijon</b>\nFilliallarimiz: Hozirda 4 ta fillialimiz mavjud\n<b>Qo'shimcha:</b> Siz uchun mos keladigon o'quv kurslarini taqdim etamiz. Darslar malakali ustozlar tomonidan olib boriladi(<b>teachers 7.5-9 ielts</b>)\nIsh vaqtimiz: <b>8:00-18:00</b>\nTelefon raqamimiz: <b>+999-55-500-09-10</b>\nBiz ijtimoiy tarmoqlarda:\n<b>Telegram:</b> https://t.me/wester_uz\n<b>Instagram:</b> https://www.instagram.com/wester_school/\nAloqa uchun: https://t.me/wester_reception"
    bot.send_photo(message.from_user.id, 'https://logos.telegram-plus.com/channels/wester-uz/telegram_logo.jpg', info, parse_mode='HTML')


def write_questions(message):
    question = message.text
    question1 = bot.send_message(message.from_user.id, 'Savol yoki taklifingizni yozib qoldiring.', reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(question1, question_mes, question)


def question_mes(message, question):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    if message.content_type == 'text':
        if message.from_user.username:
            group_mesg = f"Yangi murojaat:\nQachon: {formatted_time}\nSorov: {message.text}\nKimdan: t.me/{message.from_user.username}"
            bot_api_url = f"https://api.telegram.org/bot{bot_token}/sendmessage?chat_id=@{group_id}&text={group_mesg}"
            resp = requests.get(bot_api_url)
        else:
            group_mesg = f"Yangi murojaat:\nQachon: {formatted_time}\nSorov: {message.text}\nKimdan: {message.from_user.first_name}| {message.from_user.id}"
            bot_api_url = f"https://api.telegram.org/bot{bot_token}/sendmessage?chat_id=@{group_id}&text={group_mesg}"
            resp = requests.get(bot_api_url)
        bot.send_message(message.from_user.id, 'muroajatingiz uchun rahmat, jamoamiz bilan tez oraqa korib chiqamz.', reply_markup=button)
    elif message.content_type == 'photo':
        if message.from_user.username:
            group_mesg = f"Yangi murojaat:\nQachon: {formatted_time}\nSorov: Rasm shakilda👇\nKimdan: t.me/{message.from_user.username}"
            bot_api_url = f"https://api.telegram.org/bot{bot_token}/sendmessage?chat_id=@{group_id}&text={group_mesg}"
            resp = requests.get(bot_api_url)
        else:
            group_mesg = f"Yangi murojaat:\nQachon: {formatted_time}\nSorov: Rasm shakilda👇\nKimdan: {message.from_user.first_name}| {message.from_user.id}"
            bot_api_url = f"https://api.telegram.org/bot{bot_token}/sendmessage?chat_id=@{group_id}&text={group_mesg}"
            resp = requests.get(bot_api_url)
        bot.send_photo(chat_id=chat_id, photo=message.photo[-1].file_id)
        bot.send_message(message.from_user.id, 'muroajatingiz uchun rahmat, jamoamiz bilan tez oraqa korib chiqamz.', reply_markup=button)
    elif message.content_type == 'voice':
        if message.from_user.username:
            group_mesg = f"Yangi murojaat:\nQachon: {formatted_time}\nSorov: Ovoz shakilda👇\nKimdan: t.me/{message.from_user.username}"
            bot_api_url = f"https://api.telegram.org/bot{bot_token}/sendmessage?chat_id=@{group_id}&text={group_mesg}"
            resp = requests.get(bot_api_url)
        else:
            group_mesg = f"Yangi murojaat:\nQachon: {formatted_time}\nSorov: Ovoz shakilda👇\nKimdan: {message.from_user.first_name}| {message.from_user.id}"
            bot_api_url = f"https://api.telegram.org/bot{bot_token}/sendmessage?chat_id=@{group_id}&text={group_mesg}"
            resp = requests.get(bot_api_url)
        bot.send_voice(chat_id=chat_id, voice=message.voice.file_id)
        bot.send_message(message.from_user.id, 'muroajatingiz uchun rahmat, jamoamiz bilan tez oraqa korib chiqamz.', reply_markup=button)
    elif message.content_type == 'video':
        if message.from_user.username:
            group_mesg = f"Yangi murojaat:\nQachon: {formatted_time}\nSorov: Video shakilda👇\nKimdan: t.me/{message.from_user.username}"
            bot_api_url = f"https://api.telegram.org/bot{bot_token}/sendmessage?chat_id=@{group_id}&text={group_mesg}"
            resp = requests.get(bot_api_url)
        else:
            group_mesg = f"Yangi murojaat:\nQachon: {formatted_time}\nSorov: Video shakilda👇\nKimdan: {message.from_user.first_name}| {message.from_user.id}"
            bot_api_url = f"https://api.telegram.org/bot{bot_token}/sendmessage?chat_id=@{group_id}&text={group_mesg}"
            resp = requests.get(bot_api_url)
        bot.send_video(chat_id=chat_id, video=message.video.file_id)
        bot.send_message(message.from_user.id, 'muroajatingiz uchun rahmat, jamoamiz bilan tez oraqa korib chiqamz.', reply_markup=button)


bot.infinity_polling()
