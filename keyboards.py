from calendar import c
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

subs_menu = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text='🎁Все 6 со скидкой🎁',callback_data='six_buy'),
    InlineKeyboardButton(text='🎀Тариф "Школьницы"(1-11 кл)💦',callback_data='school_buy'),
    InlineKeyboardButton(text='🍭Тариф "Cтуденткu"(1-4 курс)🌺',callback_data='students_buy'),
    InlineKeyboardButton(text='👩‍❤️‍💋‍👨Тариф "Инцест"(родственники)💔',callback_data='incest_buy'),
    InlineKeyboardButton(text='😈Тариф "И3Н0С"🩸',callback_data='iznoc_buy'),
    InlineKeyboardButton(text='💣Тариф "Впuскu и Тусовкu"🔥',callback_data='vpiska_buy'),
    InlineKeyboardButton(text='📹Тариф "З00ПАРК"💌',callback_data='zoo_buy'),
    InlineKeyboardButton(text='👀Тариф "Пробнuк"💟',callback_data='trial_buy')
)

six_menu = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Оплатить',callback_data='buy-699'),
    InlineKeyboardButton(text='Назад',callback_data='back'),
)

skodnics_menu = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Оплатить',callback_data='buy-349'),
    InlineKeyboardButton(text='Назад',callback_data='back'),
)

students_menu = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Оплатить',callback_data='buy-299'),
    InlineKeyboardButton(text='Назад',callback_data='back')
)
incest_menu = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Оплатить',callback_data='buy-299'),
    InlineKeyboardButton(text='Назад',callback_data='back')
)

iznoc_menu = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Оплатить',callback_data='buy-309'),
    InlineKeyboardButton(text='Назад',callback_data='back')
)

vpiski_menu = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Оплатить',callback_data='buy-249'),
    InlineKeyboardButton(text='Назад',callback_data='back')
)

zoo_menu = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Оплатить',callback_data='buy-349'),
    InlineKeyboardButton(text='Назад',callback_data='back')
)

trial_menu = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Оплатить',callback_data='buy-145'),
    InlineKeyboardButton(text='Назад',callback_data='back')
)

buying_menu = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Проверить',callback_data='prover04ka'),
    InlineKeyboardButton(text='Назад',callback_data='back')
)