from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
)

# Common
## Меню регистрации
registerMenu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Зарегистрироваться")]],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Регистрируйся делай делай",
)
## Основное меню
mainMenu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Личные данные"), KeyboardButton(text="Телосложение")],
        [KeyboardButton(text="Тренировки"), KeyboardButton(text="Питание")],
        [KeyboardButton(text="Обзор"), KeyboardButton(text="AI-помощник")],
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Начальное меню",
)
## Меню в конце расчетов
common_lastMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Обновить значение"),
            KeyboardButton(text="История записей"),
        ],
        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="",
)
# Телосложение

## Начальное меню во вкладке телосложение
bodybuilderMenu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Вес"), KeyboardButton(text="Рост")],
        [KeyboardButton(text="Обхваты"), KeyboardButton(text="Расчеты")],
        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Меню телосложения",
)

## Меню обхватов
bodybuilderGirthMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Обхват jopi"),
            KeyboardButton(text="Обхват груди"),
            KeyboardButton(text="Обхват шеи"),
        ],
        [
            KeyboardButton(text="Обхват талии"),
            KeyboardButton(text="Обхват бедра"),
            KeyboardButton(text="Обхват предплечья"),
        ],
        [
            KeyboardButton(text="Обхват голени"),
            KeyboardButton(text="Обхват бицепса"),
            KeyboardButton(text="Обхват chлеNa"),
        ],
        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Обхваты",
)

## Меню расчетов
bodybuilderCalculationsMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Джон Вейдер"),
            KeyboardButton(text="Индекс массы тела"),
            KeyboardButton(text="Метаболический возраст"),
        ],
        [
            KeyboardButton(text="Калораж в день"),
            KeyboardButton(text="Расчет нормального веса"),
            KeyboardButton(text="Расчет идеального веса"),
        ],
        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Различные расчеты для вашего тела",
)

# Тренировки
    trainingMainMenu = ReplyKe
# Питание

# Обзор

# AI-помощник