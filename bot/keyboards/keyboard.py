from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


def keyb_privace_police():
    return InlineKeyboardMarkup().add(InlineKeyboardButton(text='Да, соглашаюсь', callback_data='agree'), \
                                          InlineKeyboardButton(text='Нет, не соглашаюсь', callback_data='disagree'))


def get_help():
    return ReplyKeyboardMarkup().add(KeyboardButton(text='Помощь'))