from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.content import ABOUT_TEXT, DELIVERY_TEXT
from app.keyboards import information_menu, main_menu


def create_dispatcher(web_app_url: str) -> Dispatcher:
    router = Router()
    home_keyboard = main_menu(web_app_url)

    @router.message(CommandStart())
    async def start(message: Message) -> None:
        await message.answer(
            "Tirikchilik do‘koniga xush kelibsiz!",
            reply_markup=home_keyboard,
        )

    @router.message(F.text == "Ma'lumot")
    async def information(message: Message) -> None:
        await message.answer(ABOUT_TEXT, reply_markup=information_menu())

    @router.message(F.text == "Bosh menyu")
    async def home(message: Message) -> None:
        await message.answer("Bosh menyu:", reply_markup=home_keyboard)

    @router.message(F.text == "Izoh qoldirish")
    async def feedback(message: Message) -> None:
        await message.answer("Izoh qoldirish funksiyasi hozircha sozlanmagan.")

    @router.message(F.text == "Yetkazib berish shartlari")
    async def delivery(message: Message) -> None:
        await message.answer(DELIVERY_TEXT, reply_markup=information_menu())

    @router.message(F.text == "Kontaktlar")
    async def contacts(message: Message) -> None:
        await message.answer("Kontakt ma'lumotlari hozircha kiritilmagan.")

    @router.message(F.text == "Savat")
    async def basket(message: Message) -> None:
        await message.answer("Savat funksiyasi hozircha sozlanmagan.")

    @router.message(F.text == "Hamkorlik")
    async def partnership(message: Message) -> None:
        await message.answer("Hamkorlik bo‘yicha ma'lumotlar hozircha kiritilmagan.")

    @router.message(F.text == "Til tanlash")
    async def language(message: Message) -> None:
        await message.answer("Qo‘llab-quvvatlanadigan tillar hali belgilanmagan.")

    @router.message(F.text == "Mahsulotlar")
    async def products(message: Message) -> None:
        await message.answer(
            "Mini App’ni ochish uchun quyidagi Mahsulotlar tugmasini bosing.",
            reply_markup=home_keyboard,
        )

    @router.message()
    async def unknown(message: Message) -> None:
        await message.answer("Menyudan bo‘limni tanlang.", reply_markup=home_keyboard)

    dispatcher = Dispatcher()
    dispatcher.include_router(router)
    return dispatcher


async def run_bot(bot: Bot, web_app_url: str) -> None:
    dispatcher = create_dispatcher(web_app_url)
    await dispatcher.start_polling(bot)

