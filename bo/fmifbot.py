import telebot
bot = telebot.TeleBot("6393124287:AAE9CleODokf1hMgGCqmd9TQI0dWCco_YoE")

btn1= telebot.types.InlineKeyboardButton("youtube" , url="https://www.youtube.com/@fmif_/videos")
mark1= telebot.types.InlineKeyboardMarkup()
mark1.add(btn1)

btn2= telebot.types.InlineKeyboardButton("website" , url="https://fmif.net")
mark2= telebot.types.InlineKeyboardMarkup()
mark2.add(btn2)

btn3= telebot.types.InlineKeyboardButton("link" , url="https://zil.ink/fmif")
mark4= telebot.types.InlineKeyboardMarkup()
mark4.add(btn3)

btn5= telebot.types.InlineKeyboardButton("instagram" , url="https://www.instagram.com/financialmarketsinvestmentfund/")
mark5= telebot.types.InlineKeyboardMarkup()
mark5.add(btn5)


mark = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
mark.add("سایت fmif","کانال یوتیوب","اینستاگرام","سایر شبکه های اجتماعی") 


@bot.message_handler(commands=["start"])
def start2(message):

        msg = bot.send_message(message.chat.id , "خوش امدید لطفا نام و نام خانوادگی خود رو وارد کنید " )
        bot.register_next_step_handler(msg,email)

def email(message):
    global eee
    eee = message.text
    msg =  bot.send_message(message.chat.id , "لطفا ایمیل خود رو وارد کنید" )
    bot.register_next_step_handler(msg,age)


def age(message):
    global nnn
    nnn = message.text
    msg =  bot.send_message(message.chat.id , "لطفا شماره تلفن همراه خود رو وارد کنید" )
    bot.register_next_step_handler(msg,last)
     

def last(message):
    global ag
    ag = message.text
    ch = "@fmifbotuser"
    bot.send_message( chat_id=ch , text=f"name:{eee}\n number:{ag} \n email:{nnn}")
    msg =  bot.send_message(message.chat.id , f"سلام {eee} خوش امدید" , reply_markup=mark)
    bot.register_next_step_handler(msg,btn11)
    
def btn11(message):
    if message.text=="کانال یوتیوب":
        msg= bot.send_message(message.chat.id,"لینک youtube" , reply_markup=mark1)
    elif message.text=="سایت fmif":
        msg= bot.send_message(message.chat.id , "لینک سایت fmif" , reply_markup=mark2)
    elif message.text=="سایر شبکه های اجتماعی":
        msg= bot.send_message(message.chat.id , "راه های ارتباطی با ما"  ,reply_markup=mark4)
    elif message.text=="اینستاگرام":
        msg=bot.send_message(message.chat.id , "لینک اینستاگرام"  ,reply_markup=mark5)
    elif message.text=="/start":
        msg2 = bot.send_message(message.chat.id , "خوش امدید لطفا نام و نام خانوادگی خود رو وارد کنید ")
        bot.register_next_step_handler(msg2,age)
    bot.register_next_step_handler(msg,btn11)



bot.infinity_polling()