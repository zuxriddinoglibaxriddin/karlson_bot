from aiogram.dispatcher import FSMContext


from app.config import dp, bot
from aiogram import types
import app.database.db as db
import app.keyboards as kb
from app.database.db import select_telegram_id, commit, cursor, connection, select_all_users
from app.state import Complain, Order, Admin, Message


@dp.message_handler(commands=['start'])
async def bot_start_command(message: types.Message, ):
    await bot.send_message(message.chat.id,
                           f"Assalomu Alaykum {message.from_user.first_name}", reply_markup=kb.keyboards_menu)
    # async with state.proxy() as data:
    #     data['telegram_id'] = message.from_user.id
    #     data['username'] = message.from_user.username


@dp.message_handler(commands=['stop'])
async def bot_stop_command(message: types.Message):
    await bot.send_message(message.chat.id, "Ha mayli botdan foydalanganingiz uchun rahmat ☺")


@dp.message_handler(regexp="💬 Biz haqimizda")
async def process_about_as(message: types.Message):
    await bot.send_message(message.chat.id, "Yuridik nomi: X/K AKROMJON SHIRINLIKLARI\n"
                                            "Brend nomi: KARLSON\n"
                                            "Manzil: Olmazor tumani\n"
                                            "massiv Qora Qamish 2/4, 37-45\n"
                                            "15 - Yillik tajribaga ega", reply_markup=kb.keyboards_menu)


@dp.message_handler(regexp="📍 Bizning manzilimiz")
async def process_our_address(message: types.Message):
    await bot.send_location(message.chat.id, latitude=41.259928, longitude=69.360453,
                            reply_markup=kb.keyboards_menu)


@dp.message_handler(regexp="🛍 Bizning Mahsulotlar")
async def process_my_orders(message: types.Message):
    await bot.send_message(message.chat.id, "Bizning mahsulotlar", reply_markup=kb.keyboards_product)


@dp.message_handler(regexp="Sgushonkali")
async def process_im(message: types.Message):
    rasm = open("app/images/sugushonka.JPEG", "rb")
    await bot.send_photo(message.chat.id, rasm, "Saqlash muddati 20 kun,\n" 
                                                "Tarkibi: Qatiq, shakar, o'simlik moyi,\n"
                                                "Osh sodasi, vanilin, un, Sugushonka", reply_markup=kb.keyboards_product)


@dp.message_handler(regexp="Kakaoli kakos")
async def process_im(message: types.Message):
    rasm = open("app/images/kakaoli_kakos.JPEG", "rb")
    await bot.send_photo(message.chat.id, rasm, "Saqlash muddati 20 kun.\n"
                                                "Tarkibi: Qatiq, shakar, o'simlik moyi,\n"
                                                "Osh sodasi, vanilin, un, kakao, kakos ", reply_markup=kb.keyboards_product)




@dp.message_handler(regexp="Kakosli")
async def process_im(message: types.Message):
    rasm = open("app/images/kakos.JPEG", "rb")
    await bot.send_photo(message.chat.id, rasm, "Saqlash muddati 20 kun.\n"
                                                "Tarkibi: Qatiq, shakar, o'simlik moyi,\n"
                                                "Osh sodasi, vanilin, un, kakos ", reply_markup=kb.keyboards_product)


@dp.message_handler(regexp="Kakaoli Sugushonka")
async def process_im(message: types.Message):
    rasm = open("app/images/kakaoli_sugushonka.JPEG", "rb")
    await bot.send_photo(message.chat.id, rasm, "Saqlash muddati 20 kun.\n"
                                                "Tarkibi: Qatiq, shakar, o'simlik moyi,\n"
                                                "Osh sodasi, vanilin, un, Sugushonka, "
                                                "Kakao ", reply_markup=kb.keyboards_product)


@dp.message_handler(regexp="Kunjutli")
async def process_im(message: types.Message):
    rasm = open("app/images/kunjut.JPEG", "rb")
    await bot.send_photo(message.chat.id, rasm, "Saqlash muddati 20 kun.\n"
                                                "Tarkibi: Qatiq, shakar, o'simlik moyi,\n"
                                                "Osh sodasi, vanilin, un, kunjut", reply_markup=kb.keyboards_product)


@dp.message_handler(regexp="Oddiy")
async def process_im(message: types.Message):
    rasm = open("app/images/oddiy.JPEG", "rb")
    await bot.send_photo(message.chat.id, rasm, "Saqlash muddati 20 kun.\n"
                                                "Tarkibi: Qatiq, shakar, o'simlik moyi,\n"
                                                "Osh sodasi, vanilin, un", reply_markup=kb.keyboards_product)

@dp.message_handler(regexp="Kakaoli Oddiy")
async def process_im(message: types.Message):
    rasm = open("app/images/Prjaniki.jpg", "rb")
    await bot.send_photo(message.chat.id, rasm, "Saqlash muddati 20 kun.\n"
                                                "Tarkibi: Qatiq, shakar, o'simlik moyi,\n"
                                                "Osh sodasi, vanilin, un, kakao", reply_markup=kb.keyboards_product)


@dp.message_handler(regexp="🔙 Ortga")
async def process_b(message: types.Message):
    await bot.send_message(message.chat.id, "Quyidagilardan birini tanlang 🔽", reply_markup=kb.keyboards_menu)


@dp.message_handler(regexp="✍ Izoh qoldirish")
async def complain(message: types.Message, ):
    await bot.send_message(message.chat.id, "Taklif yoki Shikoyatlaringizni kiriting",
                           reply_markup=kb.keyboard_back_complain)
    await Complain.next()


@dp.message_handler(state=Complain.complaint)
async def complain_process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['complain'] = message.text
    if message.text == '🔙 Orqaga':
        await state.finish()
        await bot.send_message(message.chat.id, "Quyidagilardan birini tanlang 🔽", reply_markup=kb.keyboards_menu)
    else:
        await bot.send_message(-565667241,
                               f'Takliflar va shikoyatdan\n'
                               f'Taklifi yoki shikoyati: {data.get("complain")}\n'
                               f'Ismi: {message.from_user.first_name}\n'
                               f'Username: @{message.from_user.username}\n')
        await bot.send_message(message.chat.id, "Taklifingiz yokida Shikoyatingiz qabul qilindi☺",
                               reply_markup=kb.keyboards_menu)

        await state.finish()


products = {
    '1': 'Sgushonkali ',
    '2': 'Kakaoli sugushonka',
    '3': 'Kakosli ',
    '4': 'Kunjutli',
    '5': 'Oddiy',
    '6': 'Kakaoli oddiy',
    '7': 'Kakaoli kakos'
}


@dp.message_handler(regexp="≡ Menu")
async def menu_process(message: types.Message):
    rasm = open("app/images/karlson.JPEG", "rb")
    await bot.send_photo(message.chat.id, rasm, "Menumizga xush-kelibsiz 🤗\n"
                                                "Narxlar bilan tanishish uchun\n"
                                                "👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻\n"
                                                "https://t.me/karlson_praynik", reply_markup=kb.keyboards_of_biscuit)
    await Order.next()


@dp.callback_query_handler(state=Order.proudct_title)
async def callback_peoduct_handler(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
        data['product_title'] = products[callback.data]
    await callback.message.answer(text=products[callback.data], reply_markup=kb.keyboards_kilogram)
    await Order.next()


@dp.message_handler(state=Order.product_kilo)
async def order_process(message: types.Message, state=FSMContext):
    if message.text == '0.5' or '3' or '5k':
        async with state.proxy() as data:
            data['product_kilo'] = message.text
            data['telegram_id'] = message.from_user.id
            data['username'] = message.from_user.username
        await bot.send_message(message.chat.id, 'Nechta xoxlaysiz', reply_markup=kb.keyboard_cancel)
        await Order.next()
    else:
        await bot.send_message(message.chat.id, "Iltimos togri vazni jonating", reply_markup=kb.keyboards_kilogram)


@dp.message_handler(state=Order.product_count)
async def order_process_count(message: types.Message, state=FSMContext):
    if message.text.isalpha():
        await bot.send_message(message.chat.id, "Iltimos togri son yuboring")
        return Order.product_count
    if message.text == '❌ Bekor qilish':
        await state.finish()
        await bot.send_message(message.chat.id, "Quyidagilardan birini tanlang 🔽", reply_markup=kb.keyboards_menu)
    else:
        async with state.proxy() as data:
            data['product_count'] = message.text
        await bot.send_message(message.chat.id, "Nomeringizni jonating", reply_markup=kb.keyboard_phone)
        await Order.next()


@dp.message_handler(state=Order.phone_number, content_types=['contact'])
async def order_process_number(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.contact.phone_number
    await bot.send_message(message.chat.id, "Adressingizni yuboring", reply_markup=kb.keyboard_adress)
    await Order.next()


@dp.message_handler(content_types=types.ContentType.LOCATION, state=Order.address)
async def order_process_adres(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['latitude'] = message.location['latitude']
        data['longitude'] = message.location['longitude']
        data['address'] = f"{message.location['latitude']} {message.location['longitude']}"

        await state.finish()
        await bot.send_message(message.chat.id, "Shu malumotlaringizni tasdiqlaysizmi? ")
        await bot.send_message(message.chat.id, f'Pryanik Turi: {data.get("product_title")}\n'
                                                f'Pryanik Kilosi: {data.get("product_kilo")}\n'
                                                f'Pryanik Soni: {data.get("product_count")}\n'
                                                f'TelNomer: {data.get("phone_number")}', reply_markup=kb.keyboard_t_f)


@dp.message_handler(regexp="✅ Ha")
async def order_t_process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        db.new_order(
            data.get("phone_number"), data.get("product_title"), data.get("product_kilo"),
            data.get("product_count"), data.get("telegram_id"), data.get("username")
        )
        await bot.send_message(-565667241, f'Pryanik Turi: {data.get("product_title")}\n'
                                           f'Pryanik Kilosi: {data.get("product_kilo")}\n'
                                           f'Pryanik Soni: {data.get("product_count")}\n'
                                           f'Telefon: {data.get("phone_number")}\n'
                                           f'Username: @{data.get("username")}')
        await bot.send_location(-565667241, latitude=data.get('latitude'), longitude=data.get('longitude'))
        await bot.send_message(message.chat.id, "Siz muvaffaqiyatli buyurtma qildiz", reply_markup=kb.keyboards_menu)


@dp.message_handler(regexp="❌ Yoq")
async def order_t_process(message: types.Message):
    await bot.send_message(message.chat.id, "Quyidagilardan birini tanlang 🔽", reply_markup=kb.keyboards_menu)


# @dp.message_handler(commands=['yuborish'])
# async def send_all_users(message: types.Message):
#     message = "Bugun buyurtma berasizmi? 😊"
#     chats = select_telegram_id()
#     for chat in set(chats):
#         await bot.send_message(chat_id=chat[0], text=message)


@dp.message_handler(commands=['admin'])
async def admin_panel(message: types.Message):
    await bot.send_message(message.chat.id, "Usernameni kiriting")
    await Admin.next()


@dp.message_handler(state=Admin.username)
async def admin_user(message: types.Message):
    if message.text == 'admin' or 'baxa':
        await bot.send_message(message.chat.id, "Parolni kiriting")
        await Admin.next()
    else:
        await bot.send_message(message.chat.id, "Siz kiritgan username xato,Qaytatan kiriting !")
        return Admin.username


@dp.message_handler(state=Admin.password)
async def admin_password(message: types.Message, state: FSMContext):
    if message.text == '0020':
        await bot.send_message(message.chat.id, "Admin Paneliga hush kelibsiz", reply_markup=kb.admin_panel_keyboards)
        await state.finish()
    else:
        await bot.send_message(message.chat.id, "Siz kiritgan parol xato,Qaytatan kiriting !")
        return Admin.password


@dp.message_handler(regexp="Habar Yuborish ✍")
async def send_message(message: types.Message):
    await bot.send_message(message.chat.id, "Habarni yozing")
    await Message.next()


@dp.message_handler(state=Message.message)
async def send_message(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, "Siz muvaffaqiyatli yubordingiz", reply_markup=kb.admin_panel_keyboards)
    await state.finish()
    message = message.text
    chats = select_telegram_id()
    for chat in set(chats):
        await bot.send_message(chat_id=chat[0], text=message)


@dp.message_handler(regexp="Bosh menuga qaytish 🔙")
async def back_to_main_menu(message: types.Message):
    await bot.send_message(message.chat.id, "Quyidagilardan birini tanlang 🔽", reply_markup=kb.keyboards_menu)


@dp.message_handler(regexp="Hammani korish 👤")
async def all_users(message: types.Message):
    users = select_all_users()
    for user in users:
        await bot.send_message(message.chat.id, f"ID: {user[0]}\n"
                                                f"B/Q/V: {user[1]}\n"
                                                f"Telefon Raqami: {user[2]}\n"
                                                f"Mahsuloti: {user[3]}\n"
                                                f"Kilo: {user[4]}\n"
                                                f"Soni: {user[5]}\n"
                                                f"TelegramID: {user[6]}\n"
                                                f"Username: {user[7]}")


