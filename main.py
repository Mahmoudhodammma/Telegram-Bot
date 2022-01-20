import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


eg = "🇪🇬"
si = "🇮🇱"
su = "🇸🇦"
dev = types.InlineKeyboardButton(text="- 7🅰︎🅼︎🅾︎🅳︎🆈︎ -",url='https://t.me/uufffuu')
ge = types.InlineKeyboardButton(text=f"- EGYPT "+str(eg),callback_data="egy")
sui = types.InlineKeyboardButton(text=f"- ISRAEL "+str(si),callback_data="sii")
siu = types.InlineKeyboardButton(text=f"- SAUDI ARABIA "+str(su),callback_data="suu")
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)
@bot.message_handler(commands=["start"])
def me(message):
	name = message.chat.first_name
	u = "https://t.me/pydroi_d_3/35"
	key = types.InlineKeyboardMarkup()
	key.row_width=1
	key.add(ge,sui,siu,dev)
	bot.send_photo((message.chat.id),u,f"""
- Hi {name}
- Surveillance Camera 🤳
- Please Choice Country 
- Dev •@uufffuu""",reply_to_message_id=(message.message_id),reply_markup=key)
@bot.callback_query_handler(func=lambda call :True)
def f(call):
	if call.data=="egy":
		p(call.message)
	if call.data=="sii":
		o(call.message)
	if call.data=="suu":
		i(call.message)
def i(message):
	x=0
	bot.send_message(message.chat.id,f"Wait Get Ip Cam "+str(su))
	headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
	url = requests.get("https://www.insecam.org/en/bycountry/SA",headers=headers)
	last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', url.text)[0]
	for page in range(int(last_page)):
		res = requests.get(f"https://www.insecam.org/en/bycountry/SA/?page={page}",headers=headers)
		find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
		for ip in find_ip:
			print(ip)
			x+=1
			with open("IP.txt","a") as mode:
				mode.write(f"{ip}\n")
	file = open("IP.txt")
	bot.send_document((message.chat.id),file,caption=f"""
- - - - - - - - - - - - - - - - - -
- Done Get Ip Cam ✔️
- Ip : {x}
- ᴄᴏᴜɴᴛʀʏ : {su}
- - - - - - - - - - - - - - - - - -
""",reply_to_message_id=(message.message_id))
	os.remove("IP.txt")
def o(message):
	x=0
	bot.send_message(message.chat.id,f"Wait Get Ip Cam "+str(si))
	headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
	url = requests.get("https://www.insecam.org/en/bycountry/SI",headers=headers)
	last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', url.text)[0]
	for page in range(int(last_page)):
		res = requests.get(f"https://www.insecam.org/en/bycountry/SI/?page={page}",headers=headers)
		find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
		for ip in find_ip:
			print(ip)
			x+=1
			with open("IP.txt","a") as mode:
				mode.write(f"{ip}\n")
	file = open("IP.txt")
	bot.send_document((message.chat.id),file,caption=f"""
- - - - - - - - - - - - - - - - - -
- Done Get Ip Cam ✔️
- Ip : {x}
- ᴄᴏᴜɴᴛʀʏ : {si}
- - - - - - - - - - - - - - - - - -
""",reply_to_message_id=(message.message_id))
	os.remove("IP.txt")	
def p(message):
	x=0
	bot.send_message(message.chat.id,f"Wait Get Ip Cam "+str(eg))
	headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
	url = requests.get("https://www.insecam.org/en/bycountry/EG",headers=headers)
	last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', url.text)[0]
	for page in range(int(last_page)):
		res = requests.get(f"https://www.insecam.org/en/bycountry/EG/?page={page}",headers=headers)
		find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
		for ip in find_ip:
			print(ip)
			x+=1
			with open("IP.txt","a") as mode:
				mode.write(f"{ip}\n")
	file = open("IP.txt")
	bot.send_document((message.chat.id),file,caption=f"""
- - - - - - - - - - - - - - - - - -
- Done Get Ip Cam ✔️
- Ip : {x}
- ᴄᴏᴜɴᴛʀʏ : {eg}
- - - - - - - - - - - - - - - - - -
""",reply_to_message_id=(message.message_id))
	os.remove("IP.txt")
		

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://mahmoudbot.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))