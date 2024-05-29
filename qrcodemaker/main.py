import sys, os, qrcode

import qrcode, asyncio, logging
from aiogram.types import Message, FSInputFile
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart

bot = Bot(token='6833797158:AAF-II07nAajKyHfRqcd03PYrYpLrPyFpr4')
dp = Dispatcher()
async def main() -> None:
    await dp.start_polling(bot)

@dp.message(CommandStart())
async def start_cmd(msg: Message) -> None:
    await msg.answer('Привет!Я умею создавать qr-коды.\nДля этого просто отправь мне ссылку сайта!')

@dp.message()
async def make_qr(msg: Message) -> None:
    try:
        img = qrcode.make(msg.text)
        img.save("image.png")
        await msg.reply_photo(
            photo=FSInputFile(
                path=os.path.abspath('image.png')
            )
        )
    except Exception as ex:
        print(ex)
        await msg.answer('Упс! Что-то пошло не так.\nПроверь, ссылка точно правильная?')

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        logging.error('Бот выключен!')