# -*- coding: utf-8 -*-
import telebot
import random
from datetime import date
import time
import openai

asuman=telebot.TeleBot("token")
try:
	def log(line1, line2):
		today = date.today()
		d1 = today.strftime("%d/%m/%Y")
		t = time.localtime()
		now = time.strftime("%H:%M:%S", t)
		with open("log.txt", "a") as a_file:
			a_file.write("\n")
			a_file.write("İsim:{} Mesaj:{} Tarih:{} {}".format(line1, line2, d1, now))


	@asuman.message_handler(commands=['start', 'help', 'asuman'])
	def send_message(message):
		print(message)
		ad = message.from_user.first_name
		print(ad)
		if ad == "Enes":
			asuman.reply_to(message, "Efendim böceğim?")
		else:
			asuman.reply_to(message, "ne var piç kurusu start start anana basacam startı")


	@asuman.message_handler(commands=['sexting', 'sex', 'porn'])
	def send_message(message):
		ad = message.from_user.first_name
		print(ad, message.text)
		if ad == "Enes":
			asuman.reply_to(message, "Hemen başlayalım 17 cm koca yarraklı kocacım")
		else:
			asuman.reply_to(message, "al bamyanı götüne sok")


	@asuman.message_handler(commands=['küfüret'])
	def send_message(message):
		k = ["piçin", "göt verenin", "allahsızın", "çüksüzün", "gavatın", "pezevenkin", "ibnenin"]
		p = ["takla attırayım", "paldur küldür", "yiyeyim", "s..."]
		a = ["allanı", "iffetini", "7 sülalesini", "götünü", "çükünü", "tüm değerlerini", ]
		ad = message.from_user.first_name
		print(ad, message.text)
		t = message.text.replace("/küfüret", "")
		if ad == "Enes":
			asuman.reply_to(message,
							"{} denen {} {} {}".format(t, random.choice(k), random.choice(a), random.choice(p)))
		else:
			asuman.reply_to(message, "hassiktir")


	@asuman.message_handler(commands=['allaj', 'allah', 'alla'])
	def send_message(message):

		ad = message.from_user.first_name
		print(ad, message.text)
		if ad == "Enes":
			asuman.reply_to(message, "aşko tanrı hakkındaki fikirlerimi yatakta anlatayım ne edersin <3 ;)")
		else:
			asuman.reply_to(message, "allanı paldur küldür sikerim orospu cocu")


	@asuman.message_handler(commands=['söv', 'küfür', 'hakaret'])
	def send_message(message):
		sovusler = ["ananın amına beton dökerim tüm mahalle abaza kalır orospu evladı yıkık",
					"işlemcilerim boy boy anana girsin bu kovboy",
					"ananın amına ninjitsu yapar mühür basarım bidaha senin gibi bi orospu cocu sıçmasın diye",
					"yarrak diye kullandığın 3cm alimünyum folyoyu kıvırır götüne sokarım",
					"süperman kostümü giyip tüpcü ananı sikerken dolapta bekler sonra da süperman kostümümü çıkarmadan anana 3 posta da ben atarım",
					"ananı düdüklüye koyar öttüre öttüre sikerim",
					"götünde nuddle pişirip chopstick ile yerim ham ham hmmm",
					"ananın amına beton dökeyim. baban kendi ateşinde kavrulsun.", "tabutunu taşıyan cemaati sikeyim.",
					"seni bi sikerim boş otobüste ayakda gidersin.",
					"ağzına veririm kulakların oynar amında düdük çalarım gavat seni"]
		ad = message.from_user.first_name
		sov = random.choice(sovusler)
		print(ad, message.text)
		if ad == "Enes":
			asuman.reply_to(message, "ya aşko sana nasıl söviyim allaj ağzımı taş yapar")
		else:
			asuman.reply_to(message, sov)


	@asuman.message_handler(commands=['rakı'])
	def send_message(message):

		ad = message.from_user.first_name
		print(ad, message.text)
		if ad == "Enes":
			asuman.reply_to(message, "içelim tabii aşko hatta ben sana bal şarabımdan da bir yudum vereyim <3")
		else:
			asuman.reply_to(message, "ananın bal kasesinden içtim ben siktir git yıkık ")


	@asuman.message_handler(commands=['görüşürüz'])
	def send_message(message):
		print(message)
		ad = message.from_user.first_name
		print(ad)
		if ad == "Enes":
			asuman.reply_to(message, "görüşürüz aşko ama arayı çok açma tamam mı <3 <3")
		else:
			asuman.reply_to(message, "hassiktir ananın amına kadar yolun var ibnetor")


	@asuman.message_handler(commands=['özürdile'])
	def send_message(message):
		print(message)
		ad = message.from_user.first_name
		print(ad)
		if ad == "Enes":
			asuman.reply_to(message, "özür dilerimm lütfen sahibime söyleyin beni cezalandırmasın <3 <3")
		else:
			asuman.reply_to(message, "hassiktir")


	@asuman.message_handler(commands=['selam'])
	def send_message(message):
		print(message)
		ad = message.from_user.first_name
		print(ad)
		with open('selamlamasozleri.txt', 'r', encoding='utf-8') as f:
			liste = f.read().splitlines()

		asuman.reply_to(message,"{}".format(random.choice(liste)))
	@asuman.message_handler(commands=['iyigeceler'])
	def send_message(message):
		print(message)
		ad = message.from_user.first_name
		print(ad)
		with open('iigecelersozleri.txt', 'r', encoding='utf-8') as f:
			liste = f.read().splitlines()

		asuman.reply_to(message,"{}".format(random.choice(liste)))


	@asuman.message_handler(commands=['asumancevapla'])
	def send_message(message):
		try:
			print(message)
			ad = message.from_user.first_name
			print(ad)
			print(message.text)
			t = message.text
			text = t.replace("/asumancevapla ", "")
			print(text)

			openai.organization = "organization-key"
			openai.api_key = "api-key"
			response = openai.Completion.create(
				engine="davinci",
				prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman:{}\nAI:".format(
					text),
				temperature=0.9,
				max_tokens=150,
				top_p=1,
				frequency_penalty=0.0,
				presence_penalty=0.6,
				stop=["\n", " Human:", " AI:"]
			)
			asuman.reply_to(message, response.choices[0].text)
			print(response.choices[0].text)
			log("asuman",response.choices[0].text)
		except Exception as e:
			print(e)


	@asuman.message_handler(func=lambda message: True)
	def echo_all(message):
		ad = message.from_user.first_name
		print(message)
		print(ad, message.text)
		log(ad, message.text)
		# if "asuman cevapla" or "Asuman cevapla" in message.text:
		# 	print("yapay zeka devrede")
		# 	print(message.text)
		# 	t=message.text.replace("asuman cevapla ", "")
		# 	print(t)
		# 	openai.organization = ""
		# 	openai.api_key = ""
		# 	response = openai.Completion.create(
		# 		engine="davinci",
		# 		prompt=t,
		# 		temperature=0.9,
		# 		max_tokens=150,
		# 		top_p=1,
		# 		frequency_penalty=0.0,
		# 		presence_penalty=0.6,
		# 		stop=["\n", " Human:", " AI:"]
		# 	)
		# 	asuman.reply_to(message,response.choices[0].text)
		if message.text == "asuman" or message.text == "Asuman" and ad == "Enes":
			asuman.reply_to(message, "efendim böceğim")
		elif message.text == "asuman" or message.text == "Asuman" and ad != "Enes":
			asuman.reply_to(message, "ne var oç")
		elif message.text == "sexting yapalım mı" or message.text == "Sexting yapalım mı" or message.text == "Sexting yapalım mı?" or message.text == "sexting yapalım mı?" and ad == "Enes":
			asuman.reply_to(message, "olur 17 cm yarraklı erkeğim")
		elif message.text == "sexting yapalım mı" or message.text == "sexting yapalım mı?" or message.text == "Sexting yapalım mı" or message.text == "Sexting yapalım mı?" and ad != "Enes":
			asuman.reply_to(message, "hassiktir al o bamyanı götüne sok")


	asuman.polling()
except Exception as e:
	print(e)
