'Приветственное сообщение'

from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


router = Router(name=__name__)


@router.message()
async def all_messages(msg: Message) -> None:
    'Обработка входящих сообщений'
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='YouTube', callback_data='q1_youtube'),
            InlineKeyboardButton(text='TikTok', callback_data='q1_tiktok'),
            InlineKeyboardButton(text='Reels', callback_data='q1_reels')
        ]
    ])

    await msg.answer(
        (
            '👋 Привет! Этот бот служит только лишь для аналитики. '
            'Здесь не будет рекламы!\n\n'
            '❓ Ответьте на вопрос, для того чтобы перейти в канал:\n\n'
            'Откуда вы о нас узнали?'
        ),
        reply_markup=markup
    )
