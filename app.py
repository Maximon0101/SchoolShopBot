from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton
from aiogram.filters import Command
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards import kb

router = Router()


@router.message(Command("start"))
async def start_app(msg: Message):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text='Перейти в канал',
        url='https://t.me/MONmain')
    )
    builder.add(InlineKeyboardButton(
        text="Список товаров",
        callback_data="price_list")
    )
    await msg.answer(
        "Привет! Подписывайтесь на @MONmain!",
        reply_markup=builder.as_markup()
    )


@router.message(Command("price_list"))
async def show_list(msg: Message):
    await msg.answer("H2O - <i>144р</i>\nNaCl - <i>256p</i>")

@router.callback_query(F.data == "price_list")
async def show_price_list(callback: types.CallbackQuery):
    await callback.message.answer("H2O - <i>144р</i>\nNaCl - <i>256p</i>")
    await callback.answer()
