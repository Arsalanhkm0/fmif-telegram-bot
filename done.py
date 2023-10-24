
btn1= telebot.types.InlineKeyboardButton("youtube" , url="https://www.youtube.com/@fmif_/videos")
mark1= telebot.types.InlineKeyboardMarkup()
mark1.add(btn1)

btn2= telebot.types.InlineKeyboardButton("website" , url="https://fmif.net")
mark2= telebot.types.InlineKeyboardMarkup()
mark2.add(btn2)

btn3= telebot.types.InlineKeyboardButton("link" , url="https://zil.ink/fmif")
mark3= telebot.types.InlineKeyboardMarkup()
mark3.add(btn3)


mark = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
mark.add("سایت fmif","کانال یوتیوب","ارتباط با ما") 


# new

mark3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
mark3.add("information")

@bot.message_handler(commands=["start"])
def start2(message):
    bot.send_message(message.chat.id , "welcome , please send your information" , reply_markup=mark3)

@bot.message_handler(func=lambda m:True)
def info(message):
    if message.text=="information":
        msg = bot.send_message(message.chat.id , "name please")
        bot.register_next_step_handler(msg,age)

def age(message):
    global nnn
    nnn = message.text
    msg = bot.send_message(message.chat.id , "age please")
    bot.register_next_step_handler(msg,last)

def last(message):
    global ag
    ag = message.text
    bot2.send_message(message.chat.id , f"name:{nnn}\n age:{ag}")
    bot.send_message(message.chat.id , f"سلام {nnn} خوش امدید", reply_markup=mark)