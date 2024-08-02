import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import load_dotenv
import os
import keyboards.keyboards as kb
import random

dp = Dispatcher()


# Common
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Выберите действие:", reply_markup=kb.mainMenu)


@dp.message(F.text == "Назад")
async def back_to_main(message: Message):
    await message.answer("Выберите действие:", reply_markup=kb.mainMenu)


# Личные данные
@dp.message(F.text == "Личные данные")
async def user_properties(message: Message):
    name = "МУТАНТ РАЗРАБОТЧИК"
    gender = "МУЖИК"
    height = 198
    weight = 100
    await message.answer(
        f"Имя: {name}\nПол: {gender}\nРост: {height}\nВес (текущий): {weight}"
    )


# Телосложение


async def create_typical_answer(value, date):
    returned = f"Последняя запись: {date}\nЗначение: {value}"
    return returned


@dp.message(F.text == "Телосложение")
async def call_bodybuilder_menu(message: Message):
    await message.answer("Выберите действие:", reply_markup=kb.bodybuilderMenu)


@dp.message(F.text == "Вес")
async def call_bodybuilder_weight(message: Message):
    last_added_date = "24.03"
    value = 100
    text = await create_typical_answer(last_added_date, value)
    await message.answer(text, reply_markup=kb.common_lastMenu)


@dp.message(F.text == "Рост")
async def call_bodybuilder_height(message: Message):
    last_added_date = 24.03
    value = 198
    text = await create_typical_answer(last_added_date, value)
    await message.answer(text, reply_markup=kb.common_lastMenu)


@dp.message(F.text == "Обхваты")
async def call_bodybuilder_girth(message: Message):
    await message.answer("Выберите действие:", reply_markup=kb.bodybuilderGirthMenu)


@dp.message(F.text == "Расчеты")
async def call_bodybuilder_calculations(message: Message):
    await message.answer(
        "Выберите действие:", reply_markup=kb.bodybuilderCalculationsMenu
    )


# Тренировки
@dp.message(F.text == "Тренировки")
async def rand(message: Message):
    await message.answer(
        "Выберите действие:", reply_markup=kb.bodybuilderCalculationsMenu
    )


# Питание
@dp.message(F.text == "Питание")
async def rand(message: Message):
    await message.answer(f"Рандомное число: {random.randint(1000, 10000)}")


# Саммари
@dp.message(F.text == "Обзор")
async def rand(message: Message):
    await message.answer(f"Сайт с обзором сохраненных данных находится в стадии разработки")

# AI-помощник
@dp.message(F.text == "AI-помощник")
async def rand(message: Message):
    await message.answer(f"AI-помощник находится в стадии разработки")


@dp.message(F.text == "Bubna")
async def rand(message: Message):
    await message.answer(f"Рандомное число: {random.randint(1000, 10000)}")


@dp.message()
async def echo(message: Message):
    text = message.text
    await message.answer(message.text)  # type: ignore
