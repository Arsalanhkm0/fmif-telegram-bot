import telebot
import time

bot = telebot.TeleBot("6484966305:AAE_EyuZimOaJoxxbyT5k2bbFhIzzUMQTTU")
bot2 = telebot.TeleBot("6111193996:AAHzbVroaXeSCiyOtcQ7IG2K_eOyeriIBVg")

# 1

# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(message.chat.id , "سلام خوش امدید")

# @bot.message_handler(commands=["help"])
# def help(message):
#     bot.reply_to(message , "سلام میتونم کمکتون کنم؟")

# 2

# btn1= telebot.types.InlineKeyboardButton("سایت fmif" , url= "https://fmif.net")
# btn2= telebot.types.InlineKeyboardButton("کانال یوتیوب" , url= "https://www.youtube.com/@fmif_/videos")

# mark1= telebot.types.InlineKeyboardMarkup()

# mark1.add(btn1,btn2)

# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(message.chat.id , "سلام خوش امدید")

# @bot.message_handler(commands=["help"] )
# def help(message):
#     bot.send_message(message.chat.id , "سلام چطور میتونم کمکتون کنم؟" , reply_markup=mark1)

# 3

# mark2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

# mark2.add("کانال یوتیوب" , " سایت ")

# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(message.chat.id , "سلام خوش امدید" , reply_markup=mark2)


# 4

# btn1= telebot.types.InlineKeyboardButton("سایت fmif" , callback_data="site")
# btn2= telebot.types.InlineKeyboardButton("کانال یوتیوب" , callback_data="youtube")
# btn3= telebot.types.InlineKeyboardButton("کانال تلگرام" , callback_data="chanel")

# mark1= telebot.types.InlineKeyboardMarkup()

# mark1.add(btn1,btn2,btn3)

# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(message.chat.id , "سلام خوش امدید" ,reply_markup=mark1)

# @bot.callback_query_handler(func=lambda call:True)
# def call(call):
#     if call.data=="site":
#         bot.send_message(call.message.chat.id, "وبسایت")
#     elif call.data=="youtube":
#         bot.answer_callback_query(call.id , "یوتیوب")
#     elif call.data == "chanel":
#         bot.answer_callback_query(call.id , "کانال" , show_alert=True)


# 5
# mark3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
# mark3.add("information")

# @bot.message_handler(commands=["start"])
# def start2(message):
#     bot.send_message(message.chat.id , "welcome , please send your information" , reply_markup=mark3)

# @bot.message_handler(func=lambda m:True)
# def info(message):
#     if message.text=="information":
#         msg = bot.send_message(message.chat.id , "name please")
#         bot.register_next_step_handler(msg,age)

# def age(message):
#     global nnn
#     nnn = message.text
#     msg = bot.send_message(message.chat.id , "age please")
#     bot.register_next_step_handler(msg,last)

# def last(message):
#     global ag
#     ag = message.text
#     msg = bot.send_message(message.chat.id , f"name:{nnn}\n age:{ag}")

# 7

# @bot.message_handler(commands=["start"])
# def start(message):
#     mark = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn = telebot.types.KeyboardButton("phone number" , request_contact=True)
#     mark.add(btn)
#     bot.send_message(message.chat.id , "سلام خوش امدید" , reply_markup=mark)
# bot.register_next_step_handler(aaa,mmm)
    
# 8

# @bot.message_handler(commands=["start"])
# def photo(p):
#     bot.send_photo(p.chat.id , open("C:/Users/lenovo/Desktop/New folder (4)/IMG_0131.JPG" , 'rb'))
#     bot.send_message(p.chat.id , "hi")

# @bot.message_handler(commands=["start"])
# def act(m):
#     bot.send_chat_action(m.chat.id , action="typing")
#     time.sleep(5)
#     bot.send_message(m.chat.id , "hi")

# 9

# @bot.message_handler(commands=["start"])
# def ed(m):
#     ms = bot.send_message(m.chat.id , "hello")
#     time.sleep(1)
#     bot.edit_message_text(chat_id=m.chat.id , message_id=ms.message_id , text="hi")
# @bot.message_handler(commands=["start"])
# def ed(m):
#     ms = bot.send_message(m.chat.id , "hello")
#     time.sleep(1)
#     bot.delete_message(chat_id=m.chat.id , message_id=ms.message_id)
#     bot.send_message(m.chat.id , "deleted")

# 10

# @bot.message_handler(commands=["start"] , content_types=["text"])
# def aaa(m):
#     a = bot.send_message(m.chat.id ,  "hi")
#     ch = "@fmifbotuser"
#     bot.send_message(
#         chat_id=ch ,
#           text="hi")

# new


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