from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
 
b1 = KeyboardButton('/found🤷‍')
b2 = KeyboardButton('/help⚙')
b3 = KeyboardButton('/lost')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True , one_time_keyboard=True)

kb_client.add(b1).add(b2).add(b3)