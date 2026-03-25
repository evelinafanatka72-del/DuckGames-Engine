import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, MenuButtonWebApp

# --- CONFIGURATION ---
# Здесь хакер увидит твой "подарок"
TOKEN = "FUCK_YOU_HACKER_GET_YOUR_OWN_TOKEN_0x666"

# Настоящий токен бот возьмет из Secrets твоего репозитория
# (Если запустишь просто так - он выдаст ошибку, что токен неверный)
REAL_TOKEN = os.getenv("BOT_TOKEN", TOKEN)

# Твоя ссылка на 3D движок
WEB_APP_URL = "https://evelinafanatka72-del.github.io/DuckGames-Engine/"

# Инициализация
logging.basicConfig(level=logging.INFO)
bot = Bot(token=REAL_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    """
    Главная команда запуска Duck Engine
    """
    text = (
        "💠 **DUCK ENGINE CLOUD V4**\n\n"
        "Система авторизации: **SUCCESS**\n"
        "Доступ к 3D ядру открыт."
    )
    
    # Кнопка для открытия твоего сайта прямо в ТГ
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="🚀 ЗАПУСТИТЬ ДВИЖОК", web_app=WebAppInfo(url=WEB_APP_URL))]
    ])
    
    await message.answer(text, reply_markup=markup, parse_mode="Markdown")

async def on_startup():
    # Ставим кнопку меню (слева от поля ввода)
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="DuckEngine 💠",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )
    )

async def main():
    await on_startup()
    print("🦆 Duck Engine Bot is UP and RUNNING!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"CRITICAL: {e}")
