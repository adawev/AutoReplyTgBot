import asyncio
import json
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "7858891892:AAF1buSZKi8zu9epNqdDe3yiVfJ931Bvi38"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    text = 'Salom, meni guruhga qoshing va guruhni zeriktirmang. Guruhga qoshgandan keyin adminlik huquqini bering.'
    await message.answer(text)

@dp.message()
async def message_handler(msg: Message) -> None:
    question_text = msg.reply_to_message
    answer_text = msg.text
    with open('messages.json', 'r') as f:
        messages = json.load(f)
    if question_text:
        question_text = question_text.text
        if not question_text in messages.keys():
            messages[question_text] = answer_text
            with open('messages.json', 'w') as f:
                json.dump(messages, f, indent=3)

    if answer_text in messages.keys():
        await msg.answer(messages.get(answer_text))

async def main() -> None:
    P = "http://proxy.server:3128"
    session = AiohttpSession(proxy=P)
    bot = Bot(token=TOKEN, session=session,default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())