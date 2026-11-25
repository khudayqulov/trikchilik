from app.keyboards import information_menu, main_menu


def test_main_menu_has_requested_buttons_and_mini_app_link() -> None:
    keyboard = main_menu("https://shop.example")
    buttons = [button for row in keyboard.keyboard for button in row]

    assert [button.text for button in buttons] == [
        "Mahsulotlar",
        "Savat",
        "Hamkorlik",
        "Ma'lumot",
        "Til tanlash",
    ]
    assert buttons[0].web_app.url == "https://shop.example"


def test_information_menu_has_requested_sections() -> None:
    keyboard = information_menu()

    assert [row[0].text for row in keyboard.keyboard] == [
        "Izoh qoldirish",
        "Yetkazib berish shartlari",
        "Kontaktlar",
        "Bosh menyu",
    ]

