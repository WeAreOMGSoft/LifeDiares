from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text, ContentTypeFilter
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot import requests_of_api
from bot import keyboards


class NoteCreate(StatesGroup):
    one_step_name = State()
    two_step_date = State()
    three_step_note = State()

 
class NoteGet(StatesGroup):
    one_step_choice = State()
    two_step_get_note = State()
    three_step_note = State()


api_list = ['1147186426']

async def start(message: types.Message):
    try:
        # if requests_of_api.API().register(user_id=message.from_user.id):
        if message.from_user.id in api_list:
            await message.answer(text='Привет, ты уже зарегистрирован.', reply_markup=keyboards.get_help())
        else:
            await message.answer(text='Привет, ты нажал на кнопку "\start" и запустил бота.Теперь прочитай нашу политику конфедециальности.',\
                                 reply_markup=keyboards.keyb_privace_police())
    except Exception:
        await message.answer(text='Технические неполадки')

async def police_private_yes(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='Вы согласились с условиями нашей политики конфедециальности.Мы рады предоставлять Вам наши услуги')
    api_list.append(callback.from_user.id)


async def police_private_no(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='В связи с вашим отказом принять политику конфедециальности,\nмы не можем предоставить Вам свои услуги, всего доброго!')
    if callback.from_user.id in api_list:
        api_list.remove(callback.from_user.id)
    else:
        pass

async def new_post(message: types.Message, state: FSMContext):
    if message.from_user.id in api_list:
        await NoteCreate.one_step_name.set()
        await message.answer(text='Введите имя записи:')
    else:
        await message.answer(text='Увы, мы не можем помогать вам...')


async def enter_name(message: types.Message):
    await message.answer(text=message.text)
    # connect with DB
    await message.answer(text='Отлично, теперь введите дату (дд.мм.гггг): ')
    await NoteCreate.next()


async def enter_date(message: types.Message):
    await message.answer(text=message.text)
    await NoteCreate.next()

async def enter_note(data: types.Message, state: FSMContext):
    await data.answer(text=data.text)
    await state.finish()


async def my_posts(message: types.Message):
    if message.from_user.id in api_list:
        await NoteGet.one_step_choice.set()
        await message.answer(text='Выберите запись:')
        # send list
        await message.answer(text='list')
    else:
        await message.answer(text='Вы не зарегистированы')


async def get_post(message: types.Message):
    # get note
    await message.answer(text=message.text)
    await NoteGet.next()





# async def del_post(message: types.Message):
#     await state.set_state()



def client_register_message_handler(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(start, Text(equals='Начать', ignore_case=True))
    dp.register_callback_query_handler(police_private_yes, Text(equals='agree'))
    dp.register_callback_query_handler(police_private_no, Text(equals='disagree'))
    dp.register_message_handler(new_post, commands=['new_post'], state=None)
    dp.register_message_handler(new_post, Text(equals='Новая запись', ignore_case=True), state=None)
    dp.register_message_handler(enter_name, content_types='text', state=NoteCreate.one_step_name)
    dp.register_message_handler(enter_date, content_types='text', state=NoteCreate.two_step_date)
    dp.register_message_handler(enter_note, content_types=['text', 'audio', 'photo'], state=NoteCreate.three_step_note)
    dp.register_message_handler(my_posts, commands=['my_post'], state=None)
    dp.register_message_handler(my_posts, Text(equals='Мои записи', ignore_case=True), state=None)
    dp.register_message_handler()
    # dp.register_message_handler(del_post, commands=['del_post'])
    # dp.register_message_handler(del_post, Text(equals='Удалить запись', ignore_case=True))


