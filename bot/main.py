from aiogram import executor
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from .settings import TOKEN
from .handlers.clien_handlers import client_register_message_handler


def _on_startup(dp: Dispatcher):
    client_register_message_handler(dp=dp)


def main():
    bot = Bot(token=TOKEN, parse_mode='HTML')
    dispatcher = Dispatcher(bot=bot, storage=MemoryStorage())
    executor.start_polling(dispatcher=dispatcher, skip_updates=True, on_startup=_on_startup(dispatcher))
