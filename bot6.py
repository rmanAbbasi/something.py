from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw import functions

app = Client('myapp', config_file='config.ini')

user_list = []
@app.on_message(filters.text)
def test(client, m:Message):
	usertext = m.text
	user_list = []
	try:
		app.join_chat(usertext)
		print('Joined')
	except:
		print('Error joining the group')
	for i in app.iter_chat_members(usertext):
		user_list.append(i.user.id)
	app.send(
		functions.channels.InviteToChannel(
			channel = app.resolve_peer("@channel_pythontest"),
			users=[app.resolve_peer(j) for j in user_list]
		)
	)
	print('END!')
app.run()