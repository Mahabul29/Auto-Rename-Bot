import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "15810007")
    API_HASH  = os.environ.get("API_HASH", "6d860c95ed52acc0641537796a40215d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7914442526:AAHtEiO2Znfpthg1kn2-H3Tv7tHuuixnLio") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Mahabul201")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://www.google.com/search?client=ms-android-realme-terr1-rso2&sca_esv=9ff2464d0a2b6d7c&sxsrf=ADLYWIJ0s4DL26aukJpEm9mGWWJX1kLQfA:1733686369016&q=photo&udm=2&fbs=AEQNm0Aa4sjWe7Rqy32pFwRj0UkWd8nbOJfsBGGB5IQQO6L3J603JUkR9Y5suk8yuy50qOYMMWTNCTu57lKPsZpPcfqPQwPMMD4P0WXn1oc4jxGqgrnGDQAHv6uVcupsPqs5yVAB-aeUFpuUGeYGyC-ZDd7DXpAVydQy474RdyTxQZK3uuQVTcYM611AhWiy_lKUTPZuNTzkchQWI5ouX37zUmoRXBjdMA&sa=X&ved=2ahUKEwjaiLWB9ZiKAxURyzQHHT4cOjcQtKgLegQIFBAB&biw=360&bih=692&dpr=3#vhid=biHuGsdCb7QpzM&vssid=mosaic")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    # -- FORCE_SUB_CHANNELS = ["Hindi_Dub_Netflix_Movies"] -- # 
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'Hindi_Dub_Netflix_Movies').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    PORT = int(os.environ.get("PORT", ""))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "False"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 
    
➻ This Is An Advanced And Yet Powerful Rename Bot.
    
➻ Using This Bot You Can Auto Rename Of Your Files.
    
➻ This Bot Also Supports Custom Thumbnail And Custom Caption.
    
➻ Use /tutorial Command To Know How To Use Me.

<b>Bot Is Made By @Hindi_Dub_Animes_Official</b>

<b><a href='https://github.com/Mahabul201/Auto-Rename-Bot'>Mahabul29/Auto-Rename-Bot.git</a></b>
"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ `[episode]` :- To Replace Episode Number
✓ `[quality]` :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S01[episode] [quality][Dual Audio] @Hindi_Dub_Animes_Official</code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 My Name :</b>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>🧑‍💻 Developer :</b> <a href='https://t.me/Hindi_Dub_Animes_Official'>PandaWep</a>
    
<b>♻️ Bot Made By :</b> @Hindi_Dub_Animes_Official"""

    
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼ 🥺 joine Plz: @Hindi_Dub_Animes_Official
╰━━━━━━━━━━━━━━━➣ </b>"""
    
    
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>My UPI - PandaWep@ybl</b> """
    
    HELP_TXT = """<b>Hey</b> {}
    
Joine @Hindi_Dub_Animes_Official To Help """





