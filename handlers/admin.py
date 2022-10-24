#from aiogram.dispatcher import FSMContext
#from aiogram.dispatcher.filters.state import State , StatesGroup
#from create_bot import dp, bot 
#from aiogram import types, Dispatcher



#class FSMAdmin(StatesGroup):
#	photo = State()
#	name = State()
#	time = State()
#	place = State()
#	describtion = State()

	#start
#@dp.message_handler(commands='found' , state=None)
#async def cm_start(message : types.Message):
#	await FSMAdmin.photo.set()
#	await message.reply('Upload photo🖼')


#1 answer
#@dp.message_handler(content_types=['photo'] , state=FSMAdmin.photo)
#async def load_photo(message: types.Message, state:FSMContext):
#	async with state.proxy() as data:
#		data['photo'] = message.photo[0].file_id
#	await FSMAdmin.next()
#	await message.reply('What is this?(name🪪)')
#
#2 answer
#@dp.message_handler(state=FSMAdmin.name)
#async def load_name(message: types.Message, state: FSMContext):
#	async with state.proxy() as data:
#		data['name'] = message.text
#	await FSMAdmin.next()
#	await message.reply('When did you found?(time🕥)')
#
#
#3 answer
#@dp.message_handler(state=FSMAdmin.time)
#async def load_time(message: types.Message, state: FSMContext):
#	async with state.proxy() as data:
#		data['time'] = message.text
#	await FSMAdmin.next()
#	await message.reply('Wher did you found it?(place📍)')

#4 answer
#@dp.message_handler(state=FSMAdmin.place)
#async def load_place(message: types.Message, state: FSMContext):
#	async with state.proxy() as data:
#		data['place'] = message.text
#	await FSMAdmin.next()
#	await message.reply('describtion✍')


#@dp.message_handler(state=FSMAdmin.describtion)
#async def load_description(message: types.Message, state: FSMContext):
#	async with state.proxy() as data:
#		data['describtion'] = message.text

#	async with state.proxy() as data:
#		await message.reply(str(data))
#	await state.finish()


#def register_handlers_admin(dp : Dispatcher):
#	dp.register_message_handler(cm_start, commands=['found🤷‍'], state=None)
#	dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
#	dp.register_message_handler(load_name, state=FSMAdmin.name)
#	dp.register_message_handler(load_time, state=FSMAdmin.time)
#	dp.register_message_handler(load_place, state=FSMAdmin.place)
#	dp.register_message_handler(load_description, state=FSMAdmin.describtion)