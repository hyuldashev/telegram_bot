from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State , StatesGroup
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db

async def command_start(message : types.Message):
	await message.answer('Welcome to lost and found bot.' , reply_markup=kb_client)
#async def command_echo(message : types.Message):
#	await message.reply(message.text)
async def command_help(message : types.Message):
	await message.answer('This bot helps to find the lost, or find the owner of the found. Click to found')

class FSMAdmin(StatesGroup):
	photo = State()
	name = State()
	time = State()
	place = State()
	describtion = State()
	contact = State()

	#start
#@dp.message_handler(commands='found' , state=None)
async def cm_start(message : types.Message):
	await FSMAdmin.photo.set()
	await message.reply('Upload photo🖼')


#state exit
#@dp.message_handler(state="*", commands='cencel❌')
#@dp.message_handler(Text(equals='cencel❌', ignore_case=True), state="*")
#async def cancel_handler(message: types.Message, state: FSMContext):
#	current_state = await state.get_state()
#	if current_state is None:
#		return
#	await state.finish()
#	await message.reply('👌')


#1 answer
@dp.message_handler(content_types=['photo'] , state=FSMAdmin.photo)
async def load_photo(message: types.Message, state:FSMContext):
	async with state.proxy() as data:
		data['photo'] = message.photo[0].file_id
	await FSMAdmin.next()
	#await message.reply('👌')
	await message.reply('What is this?(name🪪)')
#
#2 answer
#@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['name'] = message.text
	await FSMAdmin.next()
	#await message.reply('👌')
	await message.reply('When did you found?(time🕥)')
#
#
#3 answer
#@dp.message_handler(state=FSMAdmin.time)
async def load_time(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['time'] = message.text
	await FSMAdmin.next()
	#await message.reply('👌')
	await message.reply('Wher did you found it?(place📍)')

#4 answer
#@dp.message_handler(state=FSMAdmin.place)
async def load_place(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['place'] = message.text
	await FSMAdmin.next()
	#await message.reply('👌')
	await message.reply('describtion✍')


#@dp.message_handler(state=FSMAdmin.describtion)
async def load_description(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['describtion'] = message.text
	await FSMAdmin.next()
	#await message.reply('👌')
	await message.reply('contact or user id')


#@dp.message_handler(state=FSMAdmin.describtion)
async def load_contact(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['contact'] = message.text
	await message.reply('👌')
	await message.reply('New data saved successfuly')

#	async with state.proxy() as data:
#		await message.reply(str(data))
	await sqlite_db.sql_add_command(state)
	await state.finish()


@dp.message_handler(commands=['lost'])
async def lost_menu_command(message : types.Message):
	await sqlite_db.sql_read(message)






def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start'])
	#dp.register_message_handler(command_echo, comands=['echo'])
	dp.register_message_handler(command_help, commands=['help⚙']) 
	dp.register_message_handler(cm_start, commands=['found🤷‍'], state=None)
#	dp.register_message_handler(cancel_handler, state="*", commands=['cencel❌'])
#	dp.register_message_handler(cancel_handler, Text(equals='cencel❌', ignore_case=True), state="*")
	dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
	dp.register_message_handler(load_name, state=FSMAdmin.name)
	dp.register_message_handler(load_time, state=FSMAdmin.time)
	dp.register_message_handler(load_place, state=FSMAdmin.place)
	dp.register_message_handler(load_description, state=FSMAdmin.describtion)
	dp.register_message_handler(load_contact, state=FSMAdmin.contact)
	dp.register_message_handler(lost_menu_command, commands=['lost'])


