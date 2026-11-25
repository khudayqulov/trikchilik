from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    WebAppInfo,
)


def main_menu(web_app_url: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Mahsulotlar", web_app=WebAppInfo(url=web_app_url))],
            [KeyboardButton(text="Savat"), KeyboardButton(text="Hamkorlik")],
            [KeyboardButton(text="Ma'lumot"), KeyboardButton(text="Til tanlash")],
        ],
        resize_keyboard=True,
    )


def information_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Izoh qoldirish")],
            [KeyboardButton(text="Yetkazib berish shartlari")],
            [KeyboardButton(text="Kontaktlar")],
            [KeyboardButton(text="Bosh menyu")],
        ],
        resize_keyboard=True,
    )

