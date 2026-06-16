from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import urllib.parse

TOKEN = "8610613439:AAGaNi2DM65tOeoJoATiMXImsORBXbQNXgE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot ishlayapti!\n/gen cat")

async def gen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Misol: /gen cat")
        return

    prompt = " ".join(context.args)
    prompt = urllib.parse.quote(prompt)

    url = f"https://image.pollinations.ai/prompt/{prompt}"

    await update.message.reply_text("🎨 Rasm tayyor...")
    await update.message.reply_photo(photo=url)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gen", gen))

    app.run_polling()

if __name__ == "__main__":
    main()
