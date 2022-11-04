from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

keyboards_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='💬 Biz haqimizda'), KeyboardButton("📍 Bizning manzilimiz")],
        [KeyboardButton(text='≡ Menu'), KeyboardButton(text="✍ Izoh qoldirish")],
        [KeyboardButton(text='🛍 Bizning Mahsulotlar')]
    ],
    resize_keyboard=True, one_time_keyboard=True
)

keyboards_product = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sgushonkali"), KeyboardButton(text="Kakosli")
        ],
        [
            KeyboardButton(text="Kakaoli sugushonka"), KeyboardButton(text="Kunjutli"), KeyboardButton(text="Oddiy")
        ],
        [
            KeyboardButton(text="Kakaoli oddiy"),  KeyboardButton(text="Kakaoli kakos")

        ],
        [
            KeyboardButton(text="🔙 Ortga")
        ]
    ], resize_keyboard=True
)

keyboards_kilogram = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='0.5kg'), KeyboardButton(text='3kg'), KeyboardButton(text='5kg')]
    ], resize_keyboard=True, one_time_keyboard=True
)

keyboard_back_complain = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔙 Orqaga')
        ]
    ],
    resize_keyboard=True
)

keyboard_cancel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='❌ Bekor qilish')
        ]
    ], resize_keyboard=True
)

keyboards_of_biscuit = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Sgushonkali ", callback_data='1')],
        [InlineKeyboardButton(text="Kakaoli Sugushonka", callback_data='2')],
        [InlineKeyboardButton(text="Kakosli ", callback_data='3')],
        [InlineKeyboardButton(text="Kunjutli ", callback_data='4')],
        [InlineKeyboardButton(text="Oddiy ", callback_data='5')],
        [InlineKeyboardButton(text='Kakaoli Oddiy',callback_data='6')],
        [InlineKeyboardButton(text='Kakaoli Kakos',callback_data='6')]
    ], resize_keyboard=True
)

keyboard_phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Telefon raqamni jonatish", request_contact=True)
        ]
    ], resize_keyboard=True, one_time_keyboard=True,
)

keyboard_adress = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Adresni jonatish", request_location=True)
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

keyboard_t_f = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Ha"), KeyboardButton(text="❌ Yoq")
        ]
    ], resize_keyboard=True
)

admin_panel_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Habar Yuborish ✍"),
            KeyboardButton(text="Hammani korish 👤"),
            KeyboardButton(text="Bosh menuga qaytish 🔙")
        ]
    ], resize_keyboard=True
)
