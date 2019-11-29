import telebot
import parse
TOKEN = '908930548:AAGafUxDQbhGUbe7-J1i_8MK94_cRBLrf4k'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Этот бот сможет помочь вам в поисках любых книг. Он сделан для того ,чтобы люди быстро и удобно могли находить оригинал книги БЕСПЛАТНО!!!')


last = {}


@bot.message_handler(content_types=['text'])
def start_message(message):
	global last
	try:
		a = int(message.text)
		f = last['download'+str(a)]
		bot.send_message(message.chat.id,f)
	except Exception as e:
		try:
		
			a = parse.main_parse(message.text)
			a1 = ''
			a2 = a.values()
			for i in a:
				if 'download' in i:
					continue
				else:
					a1 += a[i] + '\n'
			last = parse.main_parse(message.text)
			bot.send_message(message.chat.id, a1)
			print(last)
		except:
			bot.send_message(message.chat.id, 'Такой книги не найдено (')


bot.polling()

