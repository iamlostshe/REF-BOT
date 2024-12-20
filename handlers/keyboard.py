'Клавиатуры (обработчики нажатий на кнопки)'

from os import getenv

from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv

from utils import db

router = Router(name=__name__)

# Загружаем TOKEN из .env
load_dotenv()
CHANELL_URL = getenv('CHANELL_URL')


@router.callback_query()
async def all_inline_keyboards(call: CallbackQuery) -> None:
    'Обработка нажатий на кнопки'
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Перейти', url=CHANELL_URL)
        ]
    ])

    user_id = call.from_user.id

    await call.message.edit_text(
        (
            'Спасибо за ответ!\n\n'
            'Для перехода в канал нажмите кнопку ниже:'
        ),
        reply_markup=markup
    )

    sourse = call.data.split('_')[1]

    first_name = call.from_user.first_name
    is_premium = call.from_user.is_premium
    language_code = call.from_user.language_code
    last_name = call.from_user.last_name
    username = call.from_user.username

    await db.add_user(
        user_id,
        sourse,
        first_name,
        last_name,
        is_premium,
        language_code,
        username
    )
