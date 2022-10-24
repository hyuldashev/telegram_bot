from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db 



async def on_startup(_):
	print('bot is online')
	sqlite_db.sql_start()


from handlers import client, other 
from handlers import admin

client.register_handlers_client(dp)
#admin.register_handlers_admin(dp)
#other.register_handlers_other(dp)



executor.start_polling(dp, skip_updates=False, on_startup=on_startup)