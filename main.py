import telebot
from youtube_dl import YoutubeDL
import os.path


bot = telebot.TeleBot('')
t = ''
tu = ''


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Введи ссылку на ролик')


@bot.message_handler(content_types=['text'])
def URL(message):
    global t
    global tu

    if message.text.lower() == 'mp3' or message.text.lower() == 'mp4':
        t = message.text.lower()

    if 'you' in message.text or 'you' in tu:
        tu = message.text if 'you' in message.text else tu
        if t == '':
            bot.send_message(message.chat.id, 'Ведите тип: mp3\mp4 ')

            return

        if t == 'mp3':
            bot.send_message(message.chat.id, 'Подождите, идет загрузка')
            mp3(message.chat.id, tu)
            bot.send_audio(message.chat.id, open(str(message.chat.id) + '.' + t, 'rb'))

        elif t == 'mp4':
            bot.send_message(message.chat.id, 'Подождите, идет загрузка')
            mp4(message.chat.id, tu)
            bot.send_video(message.chat.id, open(str(message.chat.id) + '.' + t, 'rb'))

        tu = ''
        t = ''


def mp3(id, url):
    if os.path.exists(str(id) + '.' + t):
        os.remove(str(id) + '.' + t)

    audio_downloader = YoutubeDL({'format': 'bestaudio', 'outtmpl': str(id) + '.' + t})
    audio_downloader.extract_info(url)


def mp4(id, url):
    if os.path.exists(str(id) + '.' + t):
        os.remove(str(id) + '.' + t)

    audio_downloader = YoutubeDL({'format': 'bestvideo', 'outtmpl': str(id) + '.' + t})
    audio_downloader.extract_info(url)


bot.polling()
