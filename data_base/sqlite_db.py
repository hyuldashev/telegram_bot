import sqlite3 as sq 
from create_bot import dp, bot


def sql_start():
	global base, cur
	base = sq.connect('list.db')
	cur = base.cursor()
	if base:
		print('data base connected OK:')
	base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY,time_ TEXT,place TEXT, description TEXT, contact TEXT )')
	base.commit()


async def sql_add_command(state):
	async with state.proxy() as data:
		cur.execute('INSERT INTO menu VALUES(?, ?, ?, ?, ?, ?)', tuple(data.values()))
		base.commit()

async def sql_read(message):
	for ret in cur.execute('SELECT * FROM menu').fetchall():
		await bot.send_photo(message.from_user.id, ret[0], f'The {ret[1]} was found at {ret[2]} in the {ret[3]}\nDescription: {ret[4]}\nContact: {ret[-1]}') 