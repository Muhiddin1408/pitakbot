from django.shortcuts import render
from telegram import Update, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,\
    InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext

from .models import *

start_text = "Assalomu aleykum Pitakbotga xush kelibsiz😊. Botdan foydalanish uchun Boshlash tugmasini bosing"
start_button = ReplyKeyboardMarkup([[KeyboardButton('🔛Boshlash')]], resize_keyboard=True, one_time_keyboard=True)
back = ReplyKeyboardMarkup([[KeyboardButton('🔙Ortga'), KeyboardButton('🏠Bosh sahifa')]],
                             resize_keyboard=True,
                             one_time_keyboard=True)

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    username = update.effective_user.username
    name = update.effective_user.full_name


    try:
        Users.objects.create(id=user_id, username=f"@{username}", name=name[:100])
    except:
        pass
    Users.objects.filter(id=user_id).update(step=0)
    update.message.reply_text(start_text, reply_markup=start_button)
def order(update: Update, context):
    msg = update.message.text
    user_id = update.effective_user.id
    step = Users.objects.get(id=user_id)
    phone = update.message.contact
    if step.step == 0 and msg == "🔛Boshlash":
        update.message.reply_text("Qayerdan ketish joy(lar)ini kiriting!",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton('🏠Bosh sahifa')]],
                             resize_keyboard=True,
                             one_time_keyboard=True))
        Users.objects.filter(id=user_id).update(step=1)
    elif step.step == 1 and msg != '🔙Ortga' and msg != '🏠Bosh sahifa' and msg:
        update.message.reply_text("Qayerga ketish joy(lar)ini kiriting!", reply_markup=back)
        Users.objects.filter(id=user_id).update(is_from=msg)
        Users.objects.filter(id=user_id).update(step=2)
    elif step.step == 2 and msg == '🔙Ortga':
        update.message.reply_text("Qayerdan ketish joy(lar)ini kiriting!",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton('🏠Bosh sahifa')]],
                                                                   resize_keyboard=True,
                                                                   one_time_keyboard=True))
        Users.objects.filter(id=user_id).update(step=1)
    elif step.step == 2 and msg != '🔙Ortga' and msg != '🏠Bosh sahifa' and msg:
        update.message.reply_text("Qachon ketish vaqtini kiriting!", reply_markup=back)
        Users.objects.filter(id=user_id).update(is_to=msg)
        Users.objects.filter(id=user_id).update(step=3)
    elif step.step == 3 and msg == '🔙Ortga':
        update.message.reply_text("Qayerga ketish joy(lar)ini kiriting!", reply_markup=back)
        Users.objects.filter(id=user_id).update(step=2)
    elif step.step == 3 and msg != '🔙Ortga' and msg != '🏠Bosh sahifa' and msg:
        update.message.reply_text("Avtomobil turini yozing!", reply_markup=back)
        Users.objects.filter(id=user_id).update(date=msg)
        Users.objects.filter(id=user_id).update(step=4)
    elif step.step == 4 and msg == '🔙Ortga':
        update.message.reply_text("Qachon ketish vaqtini kiriting!", reply_markup=back)
        Users.objects.filter(id=user_id).update(step=3)
    elif step.step == 4 and msg != '🔙Ortga' and msg != '🏠Bosh sahifa' and msg:
        update.message.reply_text("Telefon raqamni yozing yoki pasdagi tugmani bosing!",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("☎Telefon raqamni yuborish",
                                                                                    request_contact=True)],
                                                                    [KeyboardButton('🔙Ortga'),
                                                                     KeyboardButton('🏠Bosh sahifa')]],
                             resize_keyboard=True,
                             one_time_keyboard=True))
        Users.objects.filter(id=user_id).update(car=msg)
        Users.objects.filter(id=user_id).update(step=5)
    elif step.step == 5 and msg == '🔙Ortga':
        update.message.reply_text("Avtomobil turini yozing!", reply_markup=back)
        Users.objects.filter(id=user_id).update(step=4)
    elif step.step == 5 and msg != '🔙Ortga' and msg != '🏠Bosh sahifa' and msg:
        update.message.reply_text("Qisqa izoh yozishingiz mumkin", reply_markup=back)
        Users.objects.filter(id=user_id).update(phone=msg)
        Users.objects.filter(id=user_id).update(step=6)
    elif step.step == 5 and phone:
        update.message.reply_text("Qisqa izoh yozishingiz mumkin", reply_markup=back)
        Users.objects.filter(id=user_id).update(phone=phone.phone_number)
        Users.objects.filter(id=user_id).update(step=6)
    elif step.step == 6 and msg == '🔙Ortga':
        Users.objects.filter(id=user_id).update(phone=msg)
        Users.objects.filter(id=user_id).update(step=5)
        update.message.reply_text("Telefon raqamni yozing yoki pasdagi tugmani bosing!",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("☎Telefon raqamni yuborish",
                                                                                    request_contact=True)],
                                                                    [KeyboardButton('🔙Ortga'),
                                                                     KeyboardButton('🏠Bosh sahifa')]],
                                                                   resize_keyboard=True,
                                                                   one_time_keyboard=True))
    elif step.step == 6 and msg != '🔙Ortga' and msg != '🏠Bosh sahifa' and msg:
        Users.objects.filter(id=user_id).update(comment=msg)
        obj = Users.objects.get(id=user_id)
        text = f"📍Qayerdan: {obj.is_from}\n"
        text += f"✅Qayerga: {obj.is_to}\n"
        text += f"🕐Qachon: {obj.date}\n"
        text += f"🚕Avtomobil: {obj.car}\n"
        text += f"🇺🇿Telegram: {obj.username}\n"
        text += f"📞Telefon: {obj.phone}\n"
        text += f"🔎Izoh: {obj.comment}\n"
        update.message.reply_text(text, reply_markup=ReplyKeyboardRemove())
        update.message.reply_text("Yuqoridagilarni tasdiqlang va yuborish tugmasini bosing",
                                  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✅Yuborish", callback_data="send")],
                                                                    [InlineKeyboardButton('🔙Ortga', callback_data="back"),
                                                                     InlineKeyboardButton('🏠Bosh sahifa', callback_data="home")]]))

    elif msg == "🏠Bosh sahifa":
        Users.objects.filter(id=user_id).update(step=0)
        update.message.reply_text(start_text, reply_markup=start_button)



def inline(update: Update, context: CallbackContext):
    data = update.callback_query.data
    user_id = update.callback_query.from_user.id
    if data == "send":
        order = Order()
        obj = Users.objects.get(id=user_id)
        order.telegram_id = obj.id
        order.username = obj.username
        order.is_from = obj.is_from
        order.is_to = obj.is_to
        order.date = obj.date
        order.car = obj.car
        order.phone = obj.phone
        order.comment = obj.comment
        order.save()
        obj = order
        update.callback_query.message.delete()
        text = f"📍Qayerdan: {obj.is_from}\n"
        text += f"✅Qayerga: {obj.is_to}\n"
        text += f"🕐Qachon: {obj.date}\n"
        text += f"🚕Avtomobil: {obj.car}\n"
        text += f"🇺🇿Telegram: {obj.username}\n"
        text += f"📞Telefon: {obj.phone}\n"
        text += f"🔎Izoh: {obj.comment}\n"
        tg = Telegram_group.objects.all()
        for i in tg:
            try:
                context.bot.send_message(chat_id=i.telegram_id, text=text)
            except:
                pass
        Users.objects.filter(id=user_id).update(step=0)
        context.bot.send_message(chat_id=update.callback_query.from_user.id,
                                 text="✅Buyurma gruxga yuborildi!, Yangi buyurtma qilishingiz mumkin",
                                 reply_markup=start_button)
        update.callback_query.answer("✅Buyurma gruxga yuborildi!", show_alert=True)
    elif data == "home":
        update.callback_query.message.delete()
        context.bot.delete_message(chat_id=update.callback_query.from_user.id,
                                   message_id=update.callback_query.message.message_id-1)
        context.bot.send_message(chat_id=update.callback_query.from_user.id, text=start_text, reply_markup=start_button)
        Users.objects.filter(id=user_id).update(step=0)
    elif data == "back":
        update.callback_query.message.delete()
        context.bot.delete_message(chat_id=update.callback_query.from_user.id,
                                   message_id=update.callback_query.message.message_id - 1)
        context.bot.send_message(chat_id=update.callback_query.from_user.id, text="Qisqa izoh yozishingiz mumkin",
                                 reply_markup=back)


































