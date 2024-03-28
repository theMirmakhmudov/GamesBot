from aiogram import Dispatcher, Bot
from aiogram import types
from aiogram.enums import ParseMode
from config import TOKEN
import asyncio
import logging
from aiogram.filters import Command
from aiogram.enums.dice_emoji import DiceEmoji

dp = Dispatcher()
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"<b>Assalomu Aleykum, {message.from_user.mention_html()}!</b>")
    await message.answer("<b>O'ynashni boshlash uchun commandalarni bosing ❗️</b>")


@dp.message(Command("basketball"))
async def cmd_dice1(message: types.Message, bot: Bot):
    await bot.send_dice(chat_id=message.from_user.id, emoji=DiceEmoji.BASKETBALL)


@dp.message(Command("bowling"))
async def cmd_dice2(message: types.Message, bot: Bot):
    await bot.send_dice(chat_id=message.from_user.id, emoji=DiceEmoji.BOWLING)


@dp.message(Command("dart"))
async def cmd_dice2(message: types.Message, bot: Bot):
    await bot.send_dice(chat_id=message.from_user.id, emoji=DiceEmoji.DART)


@dp.message(Command("football"))
async def cmd_dice2(message: types.Message, bot: Bot):
    await bot.send_dice(chat_id=message.from_user.id, emoji=DiceEmoji.FOOTBALL)


@dp.message(Command("dice"))
async def cmd_dice2(message: types.Message, bot: Bot):
    await bot.send_dice(chat_id=message.from_user.id, emoji=DiceEmoji.DICE)


async def main() -> None:
    await dp.start_polling(bot, polling_timeout=1)
    await bot.set_my_commands([
        types.BotCommand(command="start", description="♻️ Botni qayta ishga tushurish"),
        types.BotCommand(command="basketball", description="basketball yuborish"),
        types.BotCommand(command="bowling", description="bowling yuborish"),
        types.BotCommand(command="dart", description="dart yuborish"),
        types.BotCommand(command="football", description="football yuborish"),
        types.BotCommand(command="dice", description="dice yuborish"),
    ])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
