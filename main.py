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

dev = types.InlineKeyboardButton(text="- ᴅᴇᴠ ",url="https://t.me/uufffuu")
ss = types.InlineKeyboardButton(text="- ʀᴀɴᴅᴏᴍ 🎲",callback_data="s")
pr = types.InlineKeyboardButton(text="- ᴘʀɪᴠᴀᴛᴇ 🔒",callback_data="ss")
@bot.message_handler(commands=["start"])
def start_welcome(message):
	name = message.chat.first_name
	u = "https://t.me/pydroi_d_3/31"
	key = types.InlineKeyboardMarkup()
	key.row_width=1
	key.add(ss,pr,dev)
	bot.send_photo(message.chat.id,u,f"""
< =============== >
- ʜɪ {name}
- ᴡᴇʟᴄᴏᴍᴇ ʙᴏᴛ ᴄʀᴇᴀᴛᴇ 
- ᴇᴍᴀɪʟ ᴘʏᴛʜᴏɴᴀɴʏᴡʜᴇʀᴇ 
< =============== >
- ᴅᴇᴠ -@uufffuu""",reply_markup=key)
@bot.callback_query_handler(func=lambda call :True)
def f(call):
	if call.data=="s":
		st(call.message)
	if call.data=="ss":
		de(call.message)
def de(message):
	bot.send_message(message.chat.id,f"- sᴇɴᴅ ʏᴏᴜʀ ɴᴀᴍᴇ ? ")
@bot.message_handler(func=lambda m:True)
def ms(message):
	name = message.text
	us = "0987654321asdfghjklpoiuytrewqzxcvbnmZXCVBNMLKJHGFDSAQWERTYUIOP0987654321"
	u = ''.join(random.choice(us)for i in range(4))
	email = name+u+f"@7amody.com"
	user = name+u
	password = u+name
	url = 'https://www.pythonanywhere.com/registration/register/beginner/'
	headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'ar,en-US;q=0.9,en;q=0.8',
'Cache-Control':'max-age=0', 
'Connection':'keep-alive', 
'Content-Length':'204',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'cookie_warning_seen=True; _ga=GA1.1.9823633.1642061837; _gid=GA1.1.1147915189.1642061837; csrftoken=sufjNFCDOqA0xy3LiA6GR94raYWbTfiHrbdnwTTRUpC0DRHiIL2P7XWeWdZFr8rI; sessionid=e42falh0airkxirkbo04473ne1xindkf',
'Host':'www.pythonanywhere.com',
'Origin':'https://www.pythonanywhere.com', 
'Referer':'https://www.pythonanywhere.com/registration/register/beginner/',
'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"', 
'Sec-Fetch-Dest':'document', 
'Sec-Fetch-Mode':'navigate', 
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-User':'?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent':generate_user_agent(),
}
	data = {
'csrfmiddlewaretoken':'T3fVafK0liWb0oVMO90Uwz81NmOOJQQ9SKdZTt1erhYb6HzjekW3Mn0OzBRihJZa',
'username':user,
'email':email,
'password1':password,
'password2':password,
'tos':'on',
'recaptcha_response_token_v3':'',
	}
	re = requests.post(url,headers=headers,data=data).text
	bot.send_message(message.chat.id,f"""
‹ ᴅᴏɴᴇ ᴄʀᴇᴀᴛᴇ ᴀᴄᴏᴜɴᴛ ❤️‍🔥
────── • ✧✧ • ──────
‹ ᴜsᴇʀɴᴀᴍᴇ : <code>{user}</code>
‹ ᴇᴍᴀɪʟ : {email}
‹ ᴘᴀssᴡᴏʀᴅ : <code>{password}</code>
────── • ✧✧ • ──────
‹ ᴅᴇᴠ : @uufffuu""",parse_mode="html")
def st(message):
	us = "0987654321asdfghjklpoiuytrewqzxcvbnmZXCVBNMLKJHGFDSAQWERTYUIOP0987654321"
	u = ''.join(random.choice(us)for i in range(6))
	S = ''.join(random.choice(us)for i in range(8))
	email = u+"@7amody.com"
	url = 'https://www.pythonanywhere.com/registration/register/beginner/'
	headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'ar,en-US;q=0.9,en;q=0.8',
'Cache-Control':'max-age=0', 
'Connection':'keep-alive', 
'Content-Length':'204',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'cookie_warning_seen=True; _ga=GA1.1.9823633.1642061837; _gid=GA1.1.1147915189.1642061837; csrftoken=sufjNFCDOqA0xy3LiA6GR94raYWbTfiHrbdnwTTRUpC0DRHiIL2P7XWeWdZFr8rI; sessionid=e42falh0airkxirkbo04473ne1xindkf',
'Host':'www.pythonanywhere.com',
'Origin':'https://www.pythonanywhere.com', 
'Referer':'https://www.pythonanywhere.com/registration/register/beginner/',
'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"', 
'Sec-Fetch-Dest':'document', 
'Sec-Fetch-Mode':'navigate', 
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-User':'?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent':generate_user_agent(),
}
	data = {
	'csrfmiddlewaretoken':'T3fVafK0liWb0oVMO90Uwz81NmOOJQQ9SKdZTt1erhYb6HzjekW3Mn0OzBRihJZa',
'username':u,
'email':email,
'password1':S,
'password2':S,
'tos':'on',
'recaptcha_response_token_v3':'',
	}
	re = requests.post(url,headers=headers,data=data).text
	bot.send_message(message.chat.id,f"""
‹ ᴅᴏɴᴇ ᴄʀᴇᴀᴛᴇ ᴀᴄᴏᴜɴᴛ ❤️‍🔥
────── • ✧✧ • ──────
‹ ᴜsᴇʀɴᴀᴍᴇ : <code>{u}</code>
‹ ᴇᴍᴀɪʟ : {email}
‹ ᴘᴀssᴡᴏʀᴅ : <code>{S}</code>
────── • ✧✧ • ──────
‹ ᴅᴇᴠ : @uufffuu""",parse_mode='html')
		

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://bot-voyyy.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))