
from telegram import Update, ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ChatMemberHandler

TOKEN = "8047601333:AAHqlfTJlF3JTOhrN0FvuK2hLYVBuGB1yI8"

WELCOME_MESSAGE = """🎰 *SELAMAT DATANG DI GRUP SLOT GACOR – S68BET* 🎰

Halo bosku semua! 👋  
Di sini kamu bakal dapet info:
✅ Slot gacor harian  
✅ Bocoran RTP tinggi  
✅ Promo eksklusif hanya untuk member grup  
✅ Bukti WD real setiap hari  

📍 Biar gak ketinggalan info & promo, pastikan kamu udah daftar:  
👉 https://t.ly/s68bet-wer

Selamat bergabung & semoga hari ini JP BESAR! 💸"""

START_MESSAGE = """👋 Hai! Saya *S68BET Bot*.  
Saya bantu kamu dapetin info slot gacor & promo menarik hari ini.

Ketik:  
- /promo → untuk lihat bonus aktif  
- /bocoran → slot gacor hari ini"""

PROMO_MESSAGE = """🎁 *PROMO S68BET HARI INI* 🎁
✅ Bonus 100% untuk member baru  
🔁 Cashback harian sampai 15%  
🎰 Event mingguan & jackpot tambahan  

📍 Daftar sekarang juga: https://t.ly/s68bet-wer"""

BOCORAN_MESSAGE = """🔥 *SLOT GACOR HARI INI* 🔥
1. Gates of Olympus (RTP 96.4%)  
2. Starlight Princess (RTP 95.9%)  
3. Mahjong Ways 2 (RTP 96.1%)  

💸 Coba sekarang & rasakan cuannya!  
👉 https://t.ly/s68bet-wer"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_MESSAGE, parse_mode=ParseMode.MARKDOWN)

async def promo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(PROMO_MESSAGE, parse_mode=ParseMode.MARKDOWN)

async def bocoran(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(BOCORAN_MESSAGE, parse_mode=ParseMode.MARKDOWN)

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.chat_member.new_chat_members:
        for member in update.chat_member.new_chat_members:
            await context.bot.send_message(chat_id=update.chat_member.chat.id,
                                           text=WELCOME_MESSAGE,
                                           parse_mode=ParseMode.MARKDOWN)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("promo", promo))
    app.add_handler(CommandHandler("bocoran", bocoran))
    app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))

    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()
