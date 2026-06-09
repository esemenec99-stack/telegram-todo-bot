from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"

tasks = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Напиши будь-яку справу, і я додам її до списку."
    )

async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not tasks:
        await update.message.reply_text("Список справ порожній.")
    else:
        text = "Ваші справи:\n"
        for i, task in enumerate(tasks, start=1):
            text += f"{i}. {task}\n"
        await update.message.reply_text(text)

async def clear_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tasks.clear()
    await update.message.reply_text("Список справ очищено.")

async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    task = update.message.text
    tasks.append(task)
    await update.message.reply_text(f"Додано: {task}")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("list", list_tasks))
app.add_handler(CommandHandler("clear", clear_tasks))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, add_task))

app.run_polling()